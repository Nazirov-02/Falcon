from django.core.mail import send_mail
from django.conf import settings

def send_verification_email(user, request):
    from django.utils.http import urlsafe_base64_encode
    from django.utils.encoding import force_bytes
    from django.contrib.auth.tokens import default_token_generator
    from django.urls import reverse

    # URL yaratish
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    verify_url = request.build_absolute_uri(
        reverse('email_verify', kwargs={'uidb64': uid, 'token': token})
    )

    # Email yuborish
    subject = "Email Verification"
    message = f"Please verify your email by clicking the link below:\n{verify_url}"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list)
