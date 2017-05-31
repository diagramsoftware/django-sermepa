from django.conf.urls import url

from .views import sermepa_ipn

# urlpatterns = patterns('sermepa.views',
#     url(
#         regex=r'^$',
#         view='sermepa_ipn',
#         name='sermepa_ipn',
#     ),
# )

urlpatterns = [
    url('^$', sermepa_ipn, name='sermepa_ipn')
]
