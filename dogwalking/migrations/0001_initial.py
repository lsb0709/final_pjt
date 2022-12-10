
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dogwalking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('members', models.IntegerField(default=1, null=True)),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('writing_down', models.BooleanField(default=False)),
                ('area', models.CharField(choices=[('경기도', '경기도'), ('서울시', '서울시'), ('부산광역시', '부산광역시'), ('경상남도', '경상남도'), ('인천광역시', '인천광역시'), ('경상북도', '경상북도'), ('대구광역시', '대구광역시'), ('충청남도', '충청남도'), ('전라남도', '전라남도'), ('전라북도', '전라북도'), ('충청북도', '충청북도'), ('강원도', '강원도'), ('대전광역시', '대전광역시'), ('광주광역시', '광주광역시'), ('울산광역시', '울산광역시'), ('제주도', '제주도'), ('세종시', '세종시')], default='선택', max_length=100)),
                ('like_user', models.ManyToManyField(blank=True, related_name='like_dogwalking', to=settings.AUTH_USER_MODEL)),
                ('pet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pet', to='accounts.pet')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(choices=[('1', '⭐'), ('2', '⭐⭐'), ('3', '⭐⭐⭐'), ('4', '⭐⭐⭐⭐'), ('5', '⭐⭐⭐⭐⭐')], max_length=2)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('review_image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='images/')),
                ('dogwalking_date', models.DateField(blank=True)),
                ('place', models.CharField(max_length=50)),
                ('dogwalking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dogwalking.dogwalking')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('dogwalking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dogwalking.dogwalking')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
