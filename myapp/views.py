from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#def hello (request):
    #return HttpResponse("<h1>Lisboa!</h1>")

def about(request):
    return HttpResponse("This is the about page.")

def home(request):
    return render(request, 'home.html')
def key_business_questions(request):
    return render(request, 'key_business_questions.html')

def data(request):
    return render(request, 'data.html')


def deliverables(request):
    return render(request, 'deliverables.html')

def strategic_questions(request):
    return render(request, 'strategic_questions.html')

def sq_visitor_satisfaction(request):
    return render(request, 'sq_visitor_satisfaction.html')

def sq_crowding(request):
    return render(request, 'sq_crowding.html')

def sq_market_segmentation(request):
    return render(request, 'sq_market_segmentation.html')

def sq_value_for_money(request):
    return render(request, 'sq_value_for_money.html')

def sq_accessibility(request):
    return render(request, 'sq_accessibility.html')

def sq_content_quality(request):
    return render(request, 'sq_content_quality.html')

def sq_journey(request):
    return render(request, 'sq_journey.html')

def sq_benchmarking(request):
    return render(request, 'sq_benchmarking.html')

def sq_communications(request):
    return render(request, 'sq_communications.html')

def sq_monitoring(request):
    return render(request, 'sq_monitoring.html')

def kore_kpis(request):
    return render(request,'kore_kpis.html')
