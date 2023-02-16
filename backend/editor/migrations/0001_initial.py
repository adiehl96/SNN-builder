# Generated by Django 4.1.7 on 2023-02-16 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amplitude', models.FloatField(default=1.0, verbose_name='amplitude of output')),
                ('name', models.CharField(max_length=200, verbose_name='neuron name')),
                ('x_pos', models.CharField(default='100px', max_length=10, verbose_name='horizontal position')),
                ('y_pos', models.CharField(default='100px', max_length=10, verbose_name='vertical position')),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='network name')),
            ],
        ),
        migrations.CreateModel(
            name='Synapse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w', models.FloatField(default=1, verbose_name='synaptic weight')),
                ('d', models.IntegerField(default=1, verbose_name='synaptic delay (nr of timesteps)')),
                ('net', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='synapses', to='editor.network')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incoming_synapses', to='editor.abstractnode')),
                ('pre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outgoing_synapses', to='editor.abstractnode')),
            ],
        ),
        migrations.CreateModel(
            name='LIF',
            fields=[
                ('abstractnode_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='editor.abstractnode')),
                ('m', models.FloatField(default=0.0, verbose_name='inverse leakage')),
                ('V_init', models.FloatField(default=0.0, verbose_name='initial voltage')),
                ('V_reset', models.FloatField(default=0.0, verbose_name='reset voltage after spike')),
                ('thr', models.FloatField(default=0.99, verbose_name='spiking threshold')),
                ('I_e', models.FloatField(default=0.0, verbose_name='constant input current')),
                ('noise', models.FloatField(default=0.0, verbose_name='membrane voltage noise')),
                ('net', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='lifs', to='editor.network')),
            ],
            bases=('editor.abstractnode',),
        ),
        migrations.CreateModel(
            name='InputTrain',
            fields=[
                ('abstractnode_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='editor.abstractnode')),
                ('train', models.TextField(max_length=9999, verbose_name='output train')),
                ('loop', models.BooleanField(default=False, verbose_name='loop the train')),
                ('net', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='input_trains', to='editor.network')),
            ],
            bases=('editor.abstractnode',),
        ),
    ]
