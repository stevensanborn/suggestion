from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from signup.views import register , user_login, user_signout, get_started , user_account
from box.views import user_boxes,user_boxes_create,user_box,open_box,open_box_thankyou

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'signup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^signup-thankyou/$', 'signup.views.thankyou', name='thankyou'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', register, name='register'), 
    url(r'^getting-started/', get_started, name='get-started'),
    url(r'^signin/$', user_login, name='signin'),
    
    url(r'^accounts/login/$', user_login, name='signin-account'),
    url(r'^signout/$', user_signout, name='signout'),
    
    url(r'^account/$', user_account, name='account'),
    url(r'^account/suggestion-boxes/$', user_boxes, name='user_boxes'),
    url(r'^account/suggestion-box/(?P<box_id>[0-9]+)/$', user_box, name='user_box'),
    url(r'^account/suggestion-boxes/create/$', user_boxes_create, name='user_boxes_create'),
    
    url(r'^suggestion/(?P<url_hash>[^/]+)/$', open_box, name='open_box'),
    url(r'^suggestion/(?P<url_hash>[^/]+)/thankyou$', open_box_thankyou, name='open_box_thankyou'),
)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)