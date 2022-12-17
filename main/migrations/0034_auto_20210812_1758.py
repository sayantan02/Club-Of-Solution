# Generated by Django 3.1.1 on 2021-08-12 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_auto_20210812_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='member',
            name='user',
        ),
        migrations.AddField(
            model_name='member',
            name='user1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee1', to='main.userdetail'),
        ),
        migrations.AddField(
            model_name='member',
            name='user10',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee10', to='main.userdetail'),
        ),
        migrations.AddField(
            model_name='member',
            name='user11',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee11', to='main.userdetail'),
        ),
        migrations.AddField(
            model_name='member',
            name='user12',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee12', to='main.userdetail'),
        ),
        migrations.AddField(
            model_name='member',
            name='user13',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee13', to='main.userdetail'),
        ),
        migrations.AddField(
            model_name='member',
            name='user14',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee14', to='main.userdetail'),
        ),
        migrations.AddField(
            model_name='member',
            name='user15',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee15', to='main.userdetail'),
        ),
        migrations.AddField(
            model_name='member',
            name='user16',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee16', to='main.userdetail'),
        ),
        migrations.AddField(
            model_name='member',
            name='user17',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee17', to='main.userdetail'),
        ),
        migrations.AddField(
            model_name='member',
            name='user18',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee18', to='main.userdetail'),
        ),
        migrations.AddField(
            model_name='member',
            name='user19',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee19', to='main.userdetail'),
        ),
        migrations.AddField(
            model_name='member',
            name='user2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee2', to='main.userdetail'),
        ),
        migrations.AddField(
            model_name='member',
            name='user20',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee20', to='main.userdetail'),
        ),
        migrations.AddField(
            model_name='member',
            name='user3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee3', to='main.userdetail'),
        ),
        migrations.AddField(
            model_name='member',
            name='user4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee4', to='main.userdetail'),
        ),
        migrations.AddField(
            model_name='member',
            name='user5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee5', to='main.userdetail'),
        ),
        migrations.AddField(
            model_name='member',
            name='user6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee6', to='main.userdetail'),
        ),
        migrations.AddField(
            model_name='member',
            name='user7',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee7', to='main.userdetail'),
        ),
        migrations.AddField(
            model_name='member',
            name='user8',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee8', to='main.userdetail'),
        ),
        migrations.AddField(
            model_name='member',
            name='user9',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee9', to='main.userdetail'),
        ),
        migrations.AlterField(
            model_name='member',
            name='shop',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.shop'),
        ),
    ]