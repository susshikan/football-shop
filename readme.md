# Vintage Sports (TUGAS INDIVIDU PBP)

## Link Deployment
https://muhammad-haikal42-vintagesports.pbp.cs.ui.ac.id

<details>
    <summary><h2>Tugas Individu 2</h2></summary>

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

</details>


<details>
    <summary><h2>Tugas Individu 3</h2></summary>

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery sangat penting dalam pengembangan sebuah platform karena hal ini merupakan mekanisme utama dalam pertukaran data antara client dan server, misalnya saat aplikasi web atau mobile membutuhkan data seperti data produk, berita, atau pesan dari server dan sebaliknya server menerima input dari pengguna seperti form, komentar, atau transaksi. Dengan adanya data delivery, komunikasi antar sistem dapat berlangsung secara konsisten dan efisien, serta memungkinkan interoperabilitas antara aplikasi yang dibangun dengan bahasa pemrograman berbeda karena data dikirim dengan format standar. Selain itu, data delivery juga memastikan keamanan karena memungkinkan adanya validasi, enkripsi, serta perlindungan terhadap serangan yang mungkin terjadi selama proses pertukaran data.

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya JSON lebih baik dibanding XML ini dikarenakan JSON (JavaScript Object Notation) jauh lebih sederhana, ringkas, mudah dibaca manusia, dan langsung dapat dipetakan ke struktur data di berbagai bahasa pemrograman modern. Lalu JSON lebih populer dibanding XML karena lebih hemat bandwidth, lebih cepat diproses dan sintaksnya lebih ringan sehingga JSON menjadi pilihan utama dalam hampir semua API modern.

## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada form Django berfungsi untuk melakukan validasi terhadap data yang diinput pengguna sebelum data tersebut digunakan atau disimpan ke dalam database. is_valid() sangat penting sebab dengan adanya is_valid(), developer bisa mencegah masuknya data yang salah atau berbahaya ke database sehingga menjaga integritas dan keamanan aplikasi.

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token pada form Django sangat penting untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery), yaitu serangan di mana penyerang memanfaatkan sesi login aktif seorang pengguna untuk mengirim request palsu tanpa sepengetahuan korban. csrf_token sendiri berfungsi sebagai token unik yang harus dikirim bersama setiap request POST sehingga server dapat memastikan bahwa request tersebut benar-benar berasal dari form sah di aplikasi itu sendiri. Jika csrf_token tidak ditambahkan maka penyerang dapat dengan mudah membuat form tiruan untuk memaksa browser korban mengirim request.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### 1. Menambah beberap atribut baru pada `models.py`
```py
CATEGORY_CHOICES = [
        ('match_worn_vintage', 'Match Worn Vintage'),
        ('player_issue_vintage', 'Player Issue Vintage'),
        ('replica_vintage', 'Replica Vintage'),
        ('reissue_retro', 'Reissue Retro'),
        ('special_edition_vintage', 'Special Edition Vintage'),
        ('analysis', 'Analysis'),
    ]

    history_value_choices = [
        ('classic', 'Classic'),
        ('signed_vintage', 'Signed Vintage'),
        ('limited_edition', 'Limited Edition'),
        ('historical_matches', 'Historical Matches')
    ]

    history_value = models.CharField(max_length=50,choices=history_value_choices, default='classic')
```

### 2. Membuat forms.py untuk kerangka dalam form

### 3. Membuat fungsi baru pada `views.py` untuk mengatur logika pada form product
- `create_product`
    ```py
    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return redirect('main:show_main')

        context = {'form': form}
        return render(request, "create_product.html", context)
    ```
- `show_product`
    ```py
    def show_product(request, id):
        product = get_object_or_404(Product, pk=id)

        context = {
            'product': product
        }

        return render(request, "product_detail.html", context)
    ```

### 4. Membuat template html
- Pertama2 saya membuat base.html pada folder templates pada root sebagai header pada setiap file html
- Mengatur konfigurasi template file pada `settings.py` dengan menambah kode ini 
    ```py
    TEMPLATES = [
        {
            ...
            'DIRS': [BASE_DIR / 'templates'], 
            ...
        }
    ]
    ```
- Lalu membuat `create_product.html` dan `product_detail.html` sebagai UI pada pages create product dan product_detail
- Melakukan sedikit perubahan pada `main.html`

### 5. Membuat fungsi baru pada `views.py` untuk mengatur data delivery
- show_xml 
    ```py
    def show_xml(request):
        news_list = Product.objects.all()
        xml_data = serializers.serialize("xml", news_list)
        return HttpResponse(xml_data, content_type="application/xml")
    ```
- show_json
     ```py
    def show_json(request):
        news_list = Product.objects.all()
        json_data = serializers.serialize("json", news_list)
        return HttpResponse(json_data, content_type="application/json")
    ```
- show_xml_by_id
    ```py
    def show_xml_by_id(request, news_id):
        try:
            news_item = Product.objects.filter(pk=news_id)
            xml_data = serializers.serialize("xml", news_item)
            return HttpResponse(xml_data, content_type="application/xml")
        except Product.DoesNotExist:
            return HttpResponse(status=404)
    ```
- show_json_by_id
     ```py
    def show_json_by_id(request, news_id):
        try:
            news_item = Product.objects.get(pk=news_id)
            json_data = serializers.serialize("json", [news_item])
            return HttpResponse(json_data, content_type="application/json")
        except Product.DoesNotExist:
            return HttpResponse(status=404)
    ```

### 6. membuat routing baru pada `urls.py`
```py
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-news/', create_product, name='create_product'),
    path('news/<str:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),  
    path('json/', show_json, name='show_json'),
    path('xml/<str:news_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:news_id>/', show_json_by_id, name='show_json_by_id')
    ]
```

### 7. Menambah konfigurasi csrf token pada `settings.py`
- Menambah kode ini pada ```settings.py```
    ```py
    CSRF_TRUSTED_ORIGINS = [
        "https://muhammad-haikal42-vintagesports.pbp.cs.ui.ac.id"
    ]
    ```
- Ini dilakukan agar tidak terjadi csrf pada aplikasi


## Apakah ada feedback untuk asisten dosen tutorial 2 yang telah kamu kerjakan sebelumnya?
Sejauh ini belum ada, para asdos sudah melakukan tugasnya dengan sangat baik

</details>