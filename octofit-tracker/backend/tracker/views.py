from django.http import JsonResponse


def health(request):
	return JsonResponse({
		'status': 'ok',
		'service': 'octofit-django-backend',
		'port': 8000,
	})
