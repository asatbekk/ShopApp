from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ShopProducts
from . import views

urlpatterns = [
    path('product/',ShopProducts.as_view(),name='cards'),
    path('about/',views.about),
    path('contact/',views.contact,name='contact'), 
    path('',views.index, name='index'),
    path('blog_list/',views.blog_list,name='blog'),
    path('testimonial/',views.testimonial ,name='testimonial'),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT) 