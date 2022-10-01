from django.shortcuts import render
from django.conf import settings
import stripe

# Create your views here.

from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLIC_KEY
        return context
    
def charge(request):
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
        # charge = stripe.checkout.Session.create(
        #     payment_method_types=['card'],
        #     line_items=[{
        #         'price': '{{PRICE_ID}}',
        #         'quantity': 1,
        #     }],
        #     payment_intent_data={
        #         'application_fee_amount': 200,
        #     },
        #     mode='payment',
        #     success_url='https://example.com/success',
        #     cancel_url='https://example.com/cancel',
        #     stripe_account='{{CONNECTED_STRIPE_ACCOUNT_ID}}',
        # )

        charge = stripe.Charge.create(
            amount=500,
            currency='brl',
            description='The donate dogs',
            source=request.POST['stripeToken']
        )  
            
        return render(request, 'charge.html')

        