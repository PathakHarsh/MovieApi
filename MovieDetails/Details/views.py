from django.http import request
from django.shortcuts import render
from rest_framework import serializers
from rest_framework import authentication
from rest_framework.views import APIView
# Create your views here.
from Details.serializers import MovieSerializer
from Details.models import Movie
from django.http import JsonResponse,HttpResponse
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
sortable_fields = ['name',"rating","release_date","duration"]




class movie_details(APIView):
    

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        print("request.getttttttttt",request.GET)
        movies = Movie.objects.all()
        
        sort_by_field = request.GET.get("sort_by")
        search_field = request.GET.get("search_item")
        
        if search_field:#if search field is sent ,filter movies which has the search item in name or description
            movies = movies.filter(Q(name__icontains=search_field) | Q(description__icontains=search_field))
        
        all_fields = [movie.name for movie in Movie._meta.get_fields()]

        if sort_by_field:#if sort by field is sent checking here
            if sort_by_field in sortable_fields:#check for invalid fields
                all_movies = movies.order_by(sort_by_field)
                all_movies.order_by(sort_by_field)
            else:
                return  Response("Invalid sort filter",status=400)
        


        movie_serializer = MovieSerializer(all_movies,many=True)
        return Response(movie_serializer.data)

