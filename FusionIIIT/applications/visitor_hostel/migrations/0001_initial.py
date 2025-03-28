# Generated by Django 3.1.5 on 2024-07-16 15:44

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
            name='BookingDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_category', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='C', max_length=1)),
                ('modified_visitor_category', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='C', max_length=1)),
                ('person_count', models.IntegerField(default=1)),
                ('purpose', models.TextField(default='Hi!')),
                ('booking_from', models.DateField()),
                ('booking_to', models.DateField()),
                ('arrival_time', models.TextField(blank=True, null=True)),
                ('departure_time', models.TextField(blank=True, null=True)),
                ('forwarded_date', models.DateField(blank=True, null=True)),
                ('confirmed_date', models.DateField(blank=True, null=True)),
                ('check_in', models.DateField(blank=True, null=True)),
                ('check_out', models.DateField(blank=True, null=True)),
                ('check_in_time', models.TimeField(blank=True, null=True)),
                ('check_out_time', models.TimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Confirmed', 'Confirmed'), ('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Canceled', 'Canceled'), ('CancelRequested', 'CancelRequested'), ('CheckedIn', 'CheckedIn'), ('Complete', 'Complete'), ('Forward', 'Forward')], default='Pending', max_length=15)),
                ('remark', models.CharField(blank=True, max_length=40, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='VhImage/')),
                ('number_of_rooms', models.IntegerField(blank=True, default=1, null=True)),
                ('number_of_rooms_alloted', models.IntegerField(blank=True, default=1, null=True)),
                ('booking_date', models.DateField(default=django.utils.timezone.now)),
                ('bill_to_be_settled_by', models.CharField(choices=[('Intender', 'Intender'), ('Visitor', 'Visitor'), ('ProjectNo', 'ProjectNo'), ('Institute', 'Institute')], default='Intender', max_length=15)),
                ('caretaker', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='caretaker', to=settings.AUTH_USER_MODEL)),
                ('intender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=20)),
                ('quantity', models.IntegerField(default=0)),
                ('consumable', models.BooleanField(default=False)),
                ('opening_stock', models.IntegerField(default=0)),
                ('addition_stock', models.IntegerField(default=0)),
                ('total_stock', models.IntegerField(default=0)),
                ('serviceable', models.IntegerField(default=0)),
                ('non_serviceable', models.IntegerField(default=0)),
                ('inuse', models.IntegerField(default=0)),
                ('total_usable', models.IntegerField(default=0)),
                ('remark', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='VisitorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_phone', models.CharField(max_length=15)),
                ('visitor_name', models.CharField(max_length=40)),
                ('visitor_email', models.CharField(blank=True, max_length=40)),
                ('visitor_organization', models.CharField(blank=True, max_length=100)),
                ('visitor_address', models.TextField(blank=True)),
                ('nationality', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RoomDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=4, unique=True)),
                ('room_type', models.CharField(choices=[('SingleBed', 'SingleBed'), ('DoubleBed', 'DoubleBed'), ('VIP', 'VIP')], max_length=12)),
                ('room_floor', models.CharField(choices=[('GroundFloor', 'GroundFloor'), ('FirstFloor', 'FirstFloor'), ('SecondFloor', 'SecondFloor'), ('ThirdFloor', 'ThirdFloor')], max_length=12)),
                ('room_status', models.CharField(choices=[('Booked', 'Booked'), ('CheckedIn', 'CheckedIn'), ('Available', 'Available'), ('UnderMaintenance', 'UnderMaintenance')], default='Available', max_length=20)),
                ('visitor', models.ManyToManyField(blank=True, to='visitor_hostel.VisitorDetail')),
            ],
        ),
        migrations.CreateModel(
            name='MealRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_date', models.DateField()),
                ('morning_tea', models.IntegerField(default=0)),
                ('eve_tea', models.IntegerField(default=0)),
                ('breakfast', models.IntegerField(default=0)),
                ('lunch', models.IntegerField(default=0)),
                ('dinner', models.IntegerField(default=0)),
                ('persons', models.IntegerField(default=0)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor_hostel.bookingdetail')),
                ('visitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor_hostel.visitordetail')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_number', models.CharField(max_length=40)),
                ('cost', models.IntegerField(default=0)),
                ('item_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor_hostel.inventory')),
            ],
        ),
        migrations.AddField(
            model_name='bookingdetail',
            name='rooms',
            field=models.ManyToManyField(to='visitor_hostel.RoomDetail'),
        ),
        migrations.AddField(
            model_name='bookingdetail',
            name='visitor',
            field=models.ManyToManyField(to='visitor_hostel.VisitorDetail'),
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_bill', models.IntegerField(default=0)),
                ('room_bill', models.IntegerField(default=0)),
                ('payment_status', models.BooleanField(default=False)),
                ('bill_date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='visitor_hostel.bookingdetail')),
                ('caretaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('room', models.ManyToManyField(to='visitor_hostel.RoomDetail')),
            ],
        ),
    ]
