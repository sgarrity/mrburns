# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django.conf.urls import patterns, url
from django.conf.urls.i18n import i18n_patterns
from django.views.decorators.cache import cache_page

from mrburns.main.views import GlowView, ShareView, StringsView


urlpatterns = i18n_patterns('',
    url('^$', cache_page(60)(GlowView.as_view()), name='glow.home'),
    url('^l10n_strings/$', StringsView.as_view(), name='glow.strings')
)

urlpatterns += patterns('',
    url('^share/$', ShareView.as_view(), name='glow.share'),
)
