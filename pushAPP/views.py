from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import json
from django.views.decorators.csrf import csrf_exempt
from pywebpush import webpush

def home(request):
    context = {
        'vapid_public_key': settings.VAPID_PUBLIC_KEY
    }
    return render(request, 'home.html', context)

def send_web_push(subscription_info, message_body):
    return webpush(
        subscription_info=subscription_info,
        data=message_body,
        vapid_private_key=settings.VAPID_PRIVATE_KEY,
        vapid_claims={
            "sub": f"mailto:{settings.VAPID_ADMIN_EMAIL}",
        }
    )

@csrf_exempt
def subscribe(request):
    if request.method == 'POST':
        subscription_info = json.loads(request.body)
        
        # 테스트를 위한 즉시 알림 전송
        try:
            send_web_push(
                subscription_info,
                "구독이 완료되었습니다!"
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
            
    return JsonResponse({'status': 'error'})
