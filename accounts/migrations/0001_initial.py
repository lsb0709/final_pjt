# Generated by Django 3.2.13 on 2022-12-13 07:37

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(error_messages={'unique': '이미 사용중인 아이디입니다.'}, max_length=25, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()])),
                ('nickname', models.CharField(max_length=25, unique=True)),
                ('age', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('gender', models.CharField(choices=[(None, '선택'), ('M', '남자'), ('W', '여자')], default='선택', max_length=2)),
                ('postcode', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('detailAddress', models.CharField(max_length=250)),
                ('extraAddress', models.CharField(max_length=250)),
                ('phone_num', models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(regex='^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')])),
                ('is_phone_active', models.BooleanField(default=False)),
                ('profile_image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/accounts/')),
                ('kakao_id', models.BigIntegerField(null=True, unique=True)),
                ('naver_id', models.CharField(max_length=100, null=True, unique=True)),
                ('google_id', models.CharField(max_length=100, null=True, unique=True)),
                ('pet_notice', models.BooleanField(default=True)),
                ('note_notice', models.BooleanField(default=True)),
                ('notice_pet', models.BooleanField(default=True)),
                ('notice_note', models.BooleanField(default=True)),
                ('block', models.ManyToManyField(related_name='blockers', to=settings.AUTH_USER_MODEL)),
                ('followings', models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('liking', models.ManyToManyField(related_name='like', to=settings.AUTH_USER_MODEL)),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AuthPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phone', models.IntegerField()),
                ('auth_number', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/accounts_pet/')),
                ('petname', models.CharField(max_length=25)),
                ('petage', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('petgender', models.CharField(choices=[(None, '선택'), ('M', '남아'), ('F', '여아')], default='선택', max_length=2)),
                ('neutralization', models.CharField(choices=[(None, '선택'), ('Y', '중성화 완료'), ('N', '중성화 전')], default='선택', max_length=2)),
                ('species', models.CharField(default='선택', max_length=3)),
                ('breeds', models.CharField(max_length=10)),
                ('birthday', models.DateField(blank=True)),
                ('vaccination_status', models.BooleanField(default=False)),
                ('characteristics', models.CharField(blank=True, max_length=100)),
                ('size', models.CharField(max_length=10, null=True)),
                ('weight', models.FloatField(default=0, max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
