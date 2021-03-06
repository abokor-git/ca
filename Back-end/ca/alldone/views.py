from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.core.exceptions import ObjectDoesNotExist
from .models import users
from .models import jobs
from .models import postulant
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        "Présentation de l'API"
    }
    return Response(api_urls)

@api_view(['GET'])
def Users(request):
    api_urls = {
        "Présentation des users"
    }
    return Response(api_urls)

@api_view(['POST'])
def Profile(request):
    try:
        user = users.objects.get(email=request.data.get('email'))
        user_all = { 
            "first_name": user.first_name,
            "last_name": user.last_name,
            "ent_name": user.ent_name,
            "email": user.email,
            "is_client": user.is_client,
            "address": user.address,
            "city": user.city,
            "phone": user.phone,
            "birth_date": user.birth_date,
            "fourth_date": user.fourth_date,
            "about_me": user.about_me,
            "competences": user.competences,
            "certifier": user.certifier,
        }
    except ObjectDoesNotExist:
        user_all = "Profil n'existe pas !!!"

    return Response(user_all)

@api_view(['POST'])
def IsExist(request):
    
    try:
        user_all = users.objects.get(email=request.data.get('email'))
        user_all = "true"
    except ObjectDoesNotExist:
        user_all = "false"

    return Response(user_all)

@api_view(['POST'])
def AddUsers(request):
    user = users.objects.create(first_name=request.data.get('first_name'),last_name=request.data.get('last_name'),ent_name=request.data.get('ent_name'),email=request.data.get('email'),is_client=request.data.get('is_client'),address=request.data.get('address'),city=request.data.get('city'),phone=request.data.get('phone'),birth_date=request.data.get('birth_date'),fourth_date=request.data.get('fourth_date'),about_me=request.data.get('about_me'),competences=request.data.get('competences'),certifier=request.data.get('certifier'))
    user.save()
    return Response("user created")

@api_view(['GET'])
def Jobs(request):
    api_urls = {
        "Présentation des jobs"
    }
    return Response(api_urls)

@api_view(['POST'])
def CreateJob(request):

    user = users.objects.get(email=request.data.get('email'))

    job = jobs.objects.create(name=request.data.get('name'),nb_users=request.data.get('nb_users'),competences=request.data.get('competences'),about_job=request.data.get('about_job'),horaire=request.data.get('horaire'),type_job=request.data.get('type_job'),user=user)
    job.save()
    return Response("job created")

@api_view(['GET'])
def ListJob(request):

    response = []
    job = jobs.objects.all()
    response = [{
        "id": job.pk,
        "name": job.name,
        "nb_users": job.nb_users,
        "competences": job.competences,
        "about_job": job.about_job,
        "horaire": job.horaire,
        "type_job": job.type_job,
        } for job in job ]

    return Response(response)

@api_view(['POST'])
def MyJob(request):

    user = users.objects.get(email=request.data.get('email'))
    job = jobs.objects.filter(user=user)
    response = []
    
    response = [{
        "id": job.pk,
        "name": job.name,
        "nb_users": job.nb_users,
        "competences": job.competences,
        "about_job": job.about_job,
        "horaire": job.horaire,
        "type_job": job.type_job,
        } for job in job ]
    
    return Response(response)

@api_view(['GET'])
def DetailJob(request, pk):

    job = jobs.objects.get(pk=pk)
    user = users.objects.get(pk=job.user.pk)
    var = { 
        "name": job.name, 
        "nb_users": job.nb_users, 
        "competences": job.competences, 
        "about_job": job.about_job, 
        "horaire": job.horaire, 
        "type_job": job.type_job, 
        "ent_name": user.ent_name, 
        "address": user.address, 
        "phone": user.phone,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "city": user.city,
        "birth_date": user.birth_date,
        "fourth_date": user.fourth_date,
        "about_me": user.about_me,
        "certifier": user.certifier,
    }
    
    return Response(var)

@api_view(['GET'])
def Postulant(request):
    api_urls = {
        "Présentation des postulant"
    }
    return Response(api_urls)

@api_view(['POST'])
def CreatePostulant(request):

    job = jobs.objects.get(pk=request.data.get("id"))

    user = users.objects.get(email=request.data.get('email'))
    
    postulantt = postulant.objects.create(job=job,user=user)
    postulantt.save()
    return Response("postulant created")
