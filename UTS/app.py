from flask import Flask, render_template, request
from forms import GajiForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Fungsi untuk menghitung gaji akhir
def hitung_gaji(kehadiran, lembur, tidak_masuk, izin, cuti):
    gaji_pokok = 5000000
    tunjangan_lembur = lembur * 50000
    potongan_tidak_masuk = tidak_masuk * 100000
    potongan_cuti_berlebih = max(0, cuti - 5) * 75000

    gaji_akhir = gaji_pokok + tunjangan_lembur - potongan_tidak_masuk - potongan_cuti_berlebih
    return gaji_akhir, potongan_tidak_masuk, potongan_cuti_berlebih

@app.route("/", methods=["GET", "POST"])
def index():
    form = GajiForm()
    hasil_output = []

    if form.validate_on_submit():
        # Mengambil jumlah karyawan dari form
        jumlah_karyawan = form.jumlah_karyawan.data
        
        # Menampilkan form data karyawan hanya jika jumlah karyawan lebih dari 0
        if jumlah_karyawan > 0:
            return render_template("input_karyawan.html", form=form, jumlah_karyawan=jumlah_karyawan)

    return render_template("index.html", form=form)

@app.route("/submit", methods=["POST"])
def submit():
    jumlah_karyawan = int(request.form['jumlah_karyawan'])
    hasil_output = []

    for i in range(jumlah_karyawan):
        nama = request.form[f'nama_{i}']
        kehadiran = int(request.form[f'kehadiran_{i}'])
        lembur = int(request.form[f'lembur_{i}'])
        tidak_masuk = int(request.form[f'tidak_masuk_{i}'])
        izin = int(request.form[f'izin_{i}'])
        cuti = int(request.form[f'cuti_{i}'])

        # Menghitung gaji untuk karyawan
        gaji, potongan_tidak_masuk, potongan_cuti_berlebih = hitung_gaji(kehadiran, lembur, tidak_masuk, izin, cuti)

        hasil_output.append({
            'nama': nama,
            'kehadiran': kehadiran,
            'lembur': lembur,
            'tidak_masuk': tidak_masuk,
            'izin': izin,
            'cuti': cuti,
            'gaji': gaji,
            'potongan_tidak_masuk': potongan_tidak_masuk,
            'potongan_cuti_berlebih': potongan_cuti_berlebih
        })
    
    return render_template("hasil_gaji.html", hasil_output=hasil_output)

if __name__ == "__main__":
    app.run(debug=True)
