from pprint import pprint

import stripe
from django.conf import settings

API_KEY = settings.STRIPE_API_KEY
stripe.api_key = API_KEY


def get_session(course):
    title_product = f"{course.name}" if course.name else ''

    product = stripe.Product.create(
        name=f'{title_product}'
    )

    price = stripe.Price.create(
        unit_amount=course.price * 100,
        currency='rub',
        product=f'{product.id}',
    )

    session = stripe.checkout.Session.create(
        success_url="http://example.com/success",
        line_items=[
            {
                'price': f'{price.id}',
                'quantity': 1,
            }
        ],
        mode='payment',

    )
    return session
