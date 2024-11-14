from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, FieldList, FormField
from wtforms.validators import InputRequired, NumberRange

class KaryawanForm(FlaskForm):
    nama = StringField('Nama Karyawan', validators=[InputRequired()])
    kehadiran = IntegerField('Jumlah Kehadiran', validators=[InputRequired(), NumberRange(min=0)])
    lembur = IntegerField('Jumlah Lembur (Jam)', validators=[InputRequired(), NumberRange(min=0)])
    tidak_masuk = IntegerField('Jumlah Tidak Masuk (Tanpa Alasan)', validators=[InputRequired(), NumberRange(min=0)])
    izin = IntegerField('Jumlah Izin', validators=[InputRequired(), NumberRange(min=0)])
    cuti = IntegerField('Jumlah Cuti', validators=[InputRequired(), NumberRange(min=0)])

class GajiForm(FlaskForm):
    jumlah_karyawan = IntegerField('Jumlah Karyawan', validators=[InputRequired(), NumberRange(min=1)])
