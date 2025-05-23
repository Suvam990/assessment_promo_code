from django.shortcuts import render


import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST





def home(request):
    return render(request, 'home.html')

@csrf_exempt
@require_POST
def apply_promo(request):
    if request.content_type != 'application/json':
        return JsonResponse({
            'success': False,
            'message': 'Content-Type must be application/json'
        }, status=400)

    try:
        data = json.loads(request.body)
        code = data.get('code')
        tier = data.get('tier')

        valid_promos = {
            'FLASH7': ['boost'],
            'SUMMER20': ['basic', 'premium'],
            'WELCOME10': ['basic', 'boost', 'premium']
        }

        if code in valid_promos and tier in valid_promos[code]:
            return JsonResponse({
                'success': True,
                'discountedPrice': 7
            })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Invalid promo code or tier'
            }, status=400)

    except (json.JSONDecodeError, TypeError):
        return JsonResponse({
            'success': False,
            'message': 'Invalid JSON format'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error: {str(e)}'
        }, status=500)
