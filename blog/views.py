from django.views.generic import ListView, DetailView
from django.conf import settings
from django.http import Http404
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)

from .models import Entry


class EntryListView(ListView):

    template_name = 'blog/entry_list.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            qs = Entry.private.all()
        elif self.request.user.is_authenticated():
            qs = Entry.login.all()
        else:
            qs = Entry.public.all()

        qs = qs.order_by('-created')

        paginator = Paginator(
            qs,
            getattr(
                settings,
                'BLOG_ENTRIES_PER_PAGE',
                20
            )
        )
        page = self.request.GET.get('page', 1)
        try:
            qs = paginator.page(page)
        except PageNotAnInteger:
            qs = paginator.page(1)
        except EmptyPage:
            qs = paginator.page(paginator.num_pages)

        return qs


class EntryDetailView(DetailView):
    model = Entry
    pk_url_kwarg = 'entry_id'
    template_name = 'blog/entry_detail.html'

    def get_object(self):
        try:
            pk = int(self.kwargs[self.pk_url_kwarg])
            if self.request.user.is_superuser:
                return Entry.private.get(pk=pk)
            elif self.request.user.is_authenticated():
                return Entry.login.get(pk=pk)
            else:
                return Entry.public.get(pk=pk)
        except (KeyError, Entry.DoesNotExist):
            raise Http404
