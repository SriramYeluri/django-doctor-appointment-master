
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('location', models.CharField(max_length=100)),
                ('start_time', models.CharField(max_length=10)),
                ('end_time', models.CharField(max_length=10)),
                ('qualification_name', models.CharField(max_length=100)),
                ('institute_name', models.CharField(max_length=100)),
                ('hospital_name', models.CharField(max_length=100)),
                ('department', models.CharField(choices=[('Dentistry', 'Dentistry'), ('Cardiology', 'Cardiology'), ('ENT Specialists', 'ENT Specialists'), ('Astrology', 'Astrology'), ('Neuroanatomy', 'Neuroanatomy'), ('Blood Screening', 'Blood Screening'), ('Eye Care', 'Eye Care'), ('Physical Therapy', 'Physical Therapy')], max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TakeAppointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('phone_number', models.CharField(max_length=120)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.Appointment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
