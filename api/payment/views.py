from django.shortcuts import render
from fjango.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

import braintree


# Create your views here.


getway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="use_your_merchant_id",
        public_key="use_your_public_key",
        private_key="use_your_private_key"
    )
)

def validate_user_session(id, token):
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False

@csrf_exempt
def genetate_token(requset, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error': 'invalid session, Please login again!'})

    return JsonResponse({'clientToken': gateway.client_token.generate(), 'success': True})
