# Vintage Sports

## Link Deployment
https://muhammad-haikal42-vintagesports.pbp.cs.ui.ac.id
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
#### 1. Membuat proyek Django baru.

-   Membuat *virtual environment* Python dengan perintah `python -m venv env`, dan mengaktifkannya dengan perintah `env\Scripts\activate`.
-   Membuat file `requirements.txt` 
-   Buat project Django baru dengan perintah `django-admin start project vintage_sports .`

#### 2. Membuat aplikasi *main* pada proyek tersebut.

-   Menjalankan perintah `python manage.py startapp main`.
-   Menambahkan `'main'` ke `INSTALLED_APPS` pada `vintage_sports/settings.py`.
#### 3. Melakukan *routing* ke `main`
-   Menambahkan *modules-modules* di bawah ini pada `vintage_sports/urls.py`
    ```py
    from django.urls import path, include
    ```
-   Menambahkan URL app `main`
    ```py
    path('', include('main.urls'))
    ```


#### 4. Membuat model pada aplikasi `main` dengan nama `Product` 
-   membuat model baru dengan nama `Product` pada `main/models.py` dan tambahkan atribut yang sesuai

#### 5. Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah *template* HTML.

-   Membuat fungsi `show_index` pada `main/views.py` 
-   Lalu menambahkan atribut-atribut yang dibutuhkan

#### 6. Menambahkan routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`.

-   Membuat file `main/urls.py` dan tambahkan baris-baris di bawah ini:
    ```py
    urlpatterns = [
        path('', show_index, name='index'),
    ]
    ```
#### 7. Melakukan *deployment* di PWS.

-   Membuat projek baru
-   Konfigurasi *environment variables* yang ada di `.env.prod`.
-   Push branch master ke pws

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Bagan](assets/bagan.png)
* **urls.py** berfungsi untuk memeriksa pola URL dan mengarahkan ke fungsi/class di views.py yang sesuai.

* **views.py** berfungsi untuk menangani logika utama pada saat URL dipanggil. View menerima request, berinteraksi dengan models.py untuk mengambil/memanipulasi data (jika diperlukan), lalu mengembalikannya dalam bentuk JSON.
* **models.py** berfungsi untuk mendefinisikan struktur data menggunakan ORM (Object-Relational Mapping) yang nantinya akan dihubungkan dengan database.
* **Berkas HTML** nantinya akan digunakan untuk merender data yang diterima ke broser

## Jelaskan peran settings.py dalam proyek Django!
* Konfigurasi variabel Global seperti DEBUG, SECRET_KEY, ALLOWED_HOST. dll
* Database setup dimana setting.py dapat menentukan jenis database apa yang akan dipakai dan menghubugnkannya dengan projek
* Mengkonfigurasi middleware

## Bagaimana cara kerja migrasi database di Django?
Migrage database di Django dilakukan secara otomatis berdasarkan penerapan perubahan skema model ke datase
+ Pertama2 lakukan perubahan terlebih dahulu pada models.py
+ Jalankan perintah ``python manage.py makemigrations`` dimana fungsi dari perintah ini adalah untuk membuat django memerika perubahan model dari migrasi terakhir lalu mengenerate file di folder migrations
+ Apply migrasi ke database menggunakan perintah ``python manage.py migrate``

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
* Djago menggunakan bahasa python yang lebih mudah untuk dipelajari pemula dibanding bahasa lain
* Framework Fullstack yang artinya django dapat mengurus frondend dan backend dalam 1 framework sehingga pemula cukup belajar 1 framework saja
* Dokumentasi lengkap dan Komunitas yang besar

## Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Sejauh ini belum ada, para asdos sudah melakukan tugasnya dengan sangat baik