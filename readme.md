# Vintage Sports (TUGAS 3 PBP)

## Link Deployment
https://muhammad-haikal42-vintagesports.pbp.cs.ui.ac.id
## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery sangat penting dalam pengembangan sebuah platform karena hal ini merupakan mekanisme utama dalam pertukaran data antara client dan server, misalnya saat aplikasi web atau mobile membutuhkan data seperti data produk, berita, atau pesan dari server dan sebaliknya server menerima input dari pengguna seperti form, komentar, atau transaksi. Dengan adanya data delivery, komunikasi antar sistem dapat berlangsung secara konsisten dan efisien, serta memungkinkan interoperabilitas antara aplikasi yang dibangun dengan bahasa pemrograman berbeda karena data dikirim dengan format standar. Selain itu, data delivery juga memastikan keamanan karena memungkinkan adanya validasi, enkripsi, serta perlindungan terhadap serangan yang mungkin terjadi selama proses pertukaran data.

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya JSON lebih baik dibanding XML ini dikarenakan JSON (JavaScript Object Notation) jauh lebih sederhana, ringkas, mudah dibaca manusia, dan langsung dapat dipetakan ke struktur data di berbagai bahasa pemrograman modern. Lalu JSON lebih populer dibanding XML karena lebih hemat bandwidth, lebih cepat diproses dan sintaksnya lebih ringan sehingga JSON menjadi pilihan utama dalam hampir semua API modern.

## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada form Django berfungsi untuk melakukan validasi terhadap data yang diinput pengguna sebelum data tersebut digunakan atau disimpan ke dalam database. is_valid() sangat penting sebab dengan adanya is_valid(), developer bisa mencegah masuknya data yang salah atau berbahaya ke database sehingga menjaga integritas dan keamanan aplikasi.

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token pada form Django sangat penting untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery), yaitu serangan di mana penyerang memanfaatkan sesi login aktif seorang pengguna untuk mengirim request palsu tanpa sepengetahuan korban. csrf_token sendiri berfungsi sebagai token unik yang harus dikirim bersama setiap request POST sehingga server dapat memastikan bahwa request tersebut benar-benar berasal dari form sah di aplikasi itu sendiri. Jika csrf_token tidak ditambahkan maka penyerang dapat dengan mudah membuat form tiruan untuk memaksa browser korban mengirim request.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).


## Apakah ada feedback untuk asisten dosen tutorial 2 yang telah kamu kerjakan sebelumnya?
Sejauh ini belum ada, para asdos sudah melakukan tugasnya dengan sangat baik