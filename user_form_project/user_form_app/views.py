from django.http import JsonResponse
from .models import UserDetails
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
import logging

@csrf_exempt
def submit_form(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        password = request.POST.get('password')

        try:

            UserDetails.objects.create(email=email, dob=dob, age=age, password=password)

        except IntegrityError as e:
            logging.error("Integrity error is {}".format(e))
            return JsonResponse({"Message": "django.db.utils.IntegrityError: UNIQUE constraint failed for email"}, status=403)

        except Exception as e:
            logging.error("Error is {}".format(e))
            return JsonResponse({"message": e})

        return JsonResponse({'message': 'Data successfully inserted!'})

    return JsonResponse({'message': 'Invalid request.'})
    
