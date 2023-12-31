# Generated by Django 4.2.6 on 2023-10-23 16:05

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import sdk.sso.server.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Consumer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255, unique=True)),
                (
                    "private_key",
                    models.CharField(
                        default=sdk.sso.server.models.ConsumerSecretKeyGenerator("private_key"),
                        max_length=64,
                        unique=True,
                    ),
                ),
                (
                    "public_key",
                    models.CharField(
                        default=sdk.sso.server.models.ConsumerSecretKeyGenerator("public_key"),
                        max_length=64,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Token",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "request_token",
                    models.CharField(
                        default=sdk.sso.server.models.TokenSecretKeyGenerator("request_token"),
                        max_length=64,
                        unique=True,
                    ),
                ),
                (
                    "access_token",
                    models.CharField(
                        default=sdk.sso.server.models.TokenSecretKeyGenerator("access_token"),
                        max_length=64,
                        unique=True,
                    ),
                ),
                ("timestamp", models.DateTimeField(default=django.utils.timezone.now)),
                ("redirect_to", models.CharField(max_length=1023)),
                (
                    "consumer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="tokens", to="server.consumer"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]
