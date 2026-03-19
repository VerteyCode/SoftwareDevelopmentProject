from django.shortcuts import render, redirect
from .models import NautilusReviewModel, NautilusConsultationModel, NautilusTeamModel


def ConsultationPage(request):
    if request.method == "POST":
        newFirstname = request.POST.get('firstname')
        newLastname = request.POST.get('lastname')
        newEmail = request.POST.get('email')
        newPhone = request.POST.get('phone')
        newMessage = request.POST.get('message')
        newLawType = request.POST.get('lawType')

        addedConsultationData = NautilusConsultationModel(
            firstname=newFirstname,
            lastname=newLastname,
            email=newEmail,
            phone=newPhone,
            message=newMessage,
            lawType=newLawType
        )
        addedConsultationData.save()
        return redirect('ConsultationPage')

    return render(request, 'ConsultationPage.html')


def ReviewPage(request):
    if request.method == "POST":
        newFirstname = request.POST.get('firstname')
        newLastname = request.POST.get('lastname')
        newMessage = request.POST.get('message')
        newRating = request.POST.get('rating')

        addedReviewData = NautilusReviewModel(
            firstname=newFirstname,
            lastname=newLastname,
            message=newMessage,
            rating=newRating
        )
        addedReviewData.save()
        return redirect('ReviewPage')
    Reviews = NautilusReviewModel.objects.all()
    return render(request, 'ReviewPage.html', {'NautilusReview': Reviews})

def TeamPage(request):
    teams = NautilusTeamModel.objects.all()
    return render(request, 'TeamPage.html', {'NautilusTeam': teams})

def PricingPage(request):
    return render(request, 'PricingPage.html')
