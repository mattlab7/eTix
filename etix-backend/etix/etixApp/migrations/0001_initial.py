# Generated by Django 3.2.5 on 2021-08-28 08:38

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import etixApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('userID', models.TextField(default='<function generate_user_id at 0x000001A987C4B1F0>', editable=False, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(blank=True, max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('Last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_active', models.BooleanField(default=True)),
                ('is_customer', models.BooleanField(default=False)),
                ('is_vendor', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
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
            name='Customer',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customerID', models.TextField(default=etixApp.models.generate_customer_id, editable=False, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('customerGender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('P', 'Prefer not to say')], max_length=1)),
                ('customerFirstName', models.CharField(blank=True, max_length=100)),
                ('customerLastName', models.CharField(blank=True, max_length=100)),
                ('customerContact_Number', models.TextField(blank=True, max_length=11)),
                ('customerAddress', models.TextField(blank=True, max_length=200)),
                ('customerBirthday', models.DateField()),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['customerID'],
            },
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('destinationID', models.TextField(default=etixApp.models.generate_destination_id, editable=False, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('destinationTimeDeparture', models.TimeField(blank=True, null=True)),
                ('destinationOnwardDate', models.DateField()),
                ('destinationStartName', models.TextField(max_length=1000)),
                ('destinationEndName', models.TextField(max_length=1000)),
                ('destinationFrom', models.TextField(max_length=1000)),
                ('destinationTo', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='HelpDesk',
            fields=[
                ('helpdeskID', models.TextField(default=etixApp.models.generate_helpdesk_id, editable=False, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('helpdeskTitle', models.TextField(max_length=200, null=True)),
                ('helpdeskMessage', models.TextField(blank=True, max_length=10000, null=True)),
                ('helpdeskDateTime', models.DateTimeField(auto_now_add=True)),
                ('helpdeskStatus', models.CharField(choices=[('OP', 'Open'), ('CL', 'Close')], max_length=2)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='etixApp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Row',
            fields=[
                ('rowID', models.TextField(default=etixApp.models.generate_row_id, editable=False, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('capacity', models.IntegerField()),
                ('destination', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='etixApp.destination')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('seatID', models.TextField(default=etixApp.models.generate_seat_id, editable=False, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('status', models.BooleanField()),
                ('row', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='etixApp.row')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('vendorID', models.TextField(default=etixApp.models.generate_vendor_id, editable=False, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('vendorContact_Number', models.TextField(max_length=11)),
                ('vendorStatus', models.BooleanField(default=False)),
                ('vendorName', models.CharField(max_length=100)),
                ('vendorBankAcc', models.CharField(max_length=15)),
                ('vendorRegistrationNo', models.CharField(max_length=15)),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vendor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['vendorID'],
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ticketID', models.TextField(default=etixApp.models.generate_ticket_id, editable=False, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('ticketName', models.TextField(max_length=100)),
                ('seat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='etixApp.seat')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('serviceID', models.TextField(default=etixApp.models.generate_service_id, editable=False, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('destinationTimeDeparture', models.TimeField(blank=True, null=True)),
                ('serviceName', models.TextField(max_length=1000)),
                ('serviceDesc', models.TextField(max_length=10000)),
                ('serviceStatus', models.CharField(choices=[('AC', 'active'), ('DC', 'Disactive')], max_length=2)),
                ('serviceRowCapacity', models.IntegerField(blank=True, null=True)),
                ('destination', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='etixApp.destination')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='etixApp.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='SeatType',
            fields=[
                ('seatTypeID', models.TextField(default=etixApp.models.generate_seattype_id, editable=False, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('destinationTimeDeparture', models.TimeField(blank=True, null=True)),
                ('seatTypeName', models.TextField(max_length=1000)),
                ('seatTypePrice', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('seatTypeQuantity', models.IntegerField()),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='etixApp.services')),
            ],
        ),
        migrations.AddField(
            model_name='seat',
            name='seatType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='etixApp.seattype'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('paymentID', models.TextField(default=etixApp.models.generate_payment_id, editable=False, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('paymentStatus', models.CharField(choices=[('UP', 'UnPaid'), ('CP', 'Complete')], max_length=2)),
                ('paymentDateTime', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='etixApp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='HelpResponse',
            fields=[
                ('helpResponseID', models.TextField(default=etixApp.models.generate_help_response_id, editable=False, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('helpResponseDateTime', models.DateTimeField(auto_now_add=True)),
                ('helpResponseMessage', models.TextField(blank=True, max_length=10000, null=True)),
                ('helpdesk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='etixApp.helpdesk')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cartID', models.TextField(default=etixApp.models.generate_cart_id, editable=False, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('cartTotal', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='etixApp.customer')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='etixApp.services')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('adminID', models.TextField(default=etixApp.models.generate_admin_id, editable=False, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
