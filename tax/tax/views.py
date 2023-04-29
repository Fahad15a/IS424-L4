from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>This is a site to calculate tax</h1>")
def calculate_tax(request, num):
    tax_rate = 0.15
    total = num * (1 + tax_rate)
    return HttpResponse(f"<h1>The total price after tax is {total}</h1>")
def tax_rate(request):
    tax_rate = 0.15
    return render(request,  {'tax_rate': tax_rate})