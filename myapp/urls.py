from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('data/', views.data, name='data'),
    path('key_business_questions/', views.key_business_questions, name='key_business_questions'),
    path('deliverables/', views.deliverables, name='deliverables'),
    path('strategic_questions/', views.strategic_questions, name='strategic_questions'),
    path('sq/visitor_satisfaction/', views.sq_visitor_satisfaction, name='sq_visitor_satisfaction'),
    path('sq/crowding/', views.sq_crowding, name='sq_crowding'),
    path('sq/market_segmentation/', views.sq_market_segmentation, name='sq_market_segmentation'),
    path('sq/value_for_money/', views.sq_value_for_money, name='sq_value_for_money'),
    path('sq/accessibility/', views.sq_accessibility, name='sq_accessibility'),
    path('sq/content_quality/', views.sq_content_quality, name='sq_content_quality'),
    path('sq/journey/', views.sq_journey, name='sq_journey'),
    path('sq/benchmarking/', views.sq_benchmarking, name='sq_benchmarking'),
    path('sq/communications/', views.sq_communications, name='sq_communications'),
    path('sq/monitoring/', views.sq_monitoring, name='sq_monitoring'),
    path('kore_kpis/', views.kore_kpis, name='kore_kpis'),
    path('home/notebook/', views.show_notebook, name='show_notebook'),
]

    
    