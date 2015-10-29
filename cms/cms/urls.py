from django.conf.urls import patterns, include, url
from django.contrib import admin
from DjangoUeditor import urls as DjangoUeditor_urls
from django.conf import settings #for edit

urlpatterns = patterns('',
    url(r'^$', 'cms_app.views.index', name='index'),
    url(r'^column/(?P<column_slug>[^/]+)/$', 'cms_app.views.column_detail', name='column'),
    url(r'^news/(?P<pk>\d+)/(?P<article_slug>[^/]+)/$',  'cms_app.views.article_detail', name='article'),
    url(r'^aboutus/index.html/$',  'cms_app.views.aboutus', name='aboutus'),

    url(r'^accounts/login/$',  'cms_app.views.login'),
    url(r'^accounts/register/$', 'cms_app.views.register'),
    url(r'^accounts/logout/$', 'cms_app.views.logout'),

    url(r'^ueditor/', include(DjangoUeditor_urls)),
    url(r'^admin/', include(admin.site.urls)),

)


if settings.DEBUG:#for edit
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)