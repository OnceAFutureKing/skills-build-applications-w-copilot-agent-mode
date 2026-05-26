from django.http import JsonResponse
from django.shortcuts import render


def index(request):
	return render(
		request,
		'tracker/index.html',
		{
			'name': 'octofit-django-backend',
			'status': 'ok',
			'routes': ['/api/health', '/api/health/'],
		},
	)


def health(request):
	return JsonResponse({
		'status': 'ok',
		'service': 'octofit-django-backend',
		'port': 8000,
	})
