# 🚚 Robot Antar Paket – Uniform Cost Search di Semarang

Proyek ini adalah simulasi pencarian **rute tercepat** untuk **robot pengantar paket** di wilayah **Semarang** menggunakan algoritma **Uniform Cost Search (UCS)**. Seluruh implementasi dibuat **dari nol (from scratch)** menggunakan **Python standar** tanpa library eksternal untuk pencarian jalur. Proyek ini cocok sebagai studi kasus dalam pemahaman algoritma pencarian berbasis graf dan penerapannya di dunia nyata, khususnya untuk sistem logistik pintar.

---

## Fitur Utama

- Implementasi algoritma Uniform Cost Search (UCS) dari awal
- Representasi peta Semarang sebagai graf berbobot (berbasis node dan edge)
- Perhitungan biaya perjalanan antar titik secara dinamis
- Simulasi pengiriman paket dari titik awal ke tujuan
- Berbasis aplikasi Python murni (tanpa library eksternal)
- Mempertimbangkan jarak, waktu, dan kerusakan jalan untuk mendapatkan jalan yang tercepat

---

## Algoritma yang Digunakan

Uniform Cost Search (UCS) adalah algoritma pencarian berbasis **grafik berbiaya** yang selalu mengeksplorasi jalur dengan total biaya terendah terlebih dahulu. UCS cocok untuk pencarian jalur optimal dalam konteks biaya transportasi, waktu tempuh, atau jarak tempuh.

---
## Data set

dataset di peroleh SCRAPPING dari situs [DATA JALAN DINAS PEKERJAAN UMUM KOTA SEMARANG](https://jalanpu.semarangkota.go.id/). nah kemudian untuk Data waktu tempuh ke tujuan dari hal kemacetan kendaraan di kumpulkan secara langsung secara manual dari google maps

## Kesimpulan

Berdasarkan hasil analisis, proyek ini berhasil dalam mengimplementasikan 
algoritma Uniform-Cost Search (UCS). Hasil percobaan menunjukkan bahwa UCS 
manual yang dikembangkan memiliki akurasi 100%, identik dengan hasil yang 
diperoleh menggunakan modul, yang berarti implementasi manual sudah cukup 
optimal dan dapat diandalkan dalam menghasilkan jalur yang efisien. 
Selain itu, analisis clustering yang dilakukan menggunakan Silhouette Score juga 
menunjukkan hasil yang baik dengan nilai 0.6. Mengingat bahwa nilai Silhouette 
Score di atas 0.5 menunjukkan kualitas clustering yang cukup baik, hal ini 
mengindikasikan bahwa pengelompokan data telah dilakukan dengan efektif, 
menghasilkan cluster yang terpisah dengan baik. Dengan demikian, proyek ini dapat 
dianggap berhasil dalam mencapai tujuan yang diinginkan, baik dalam hal optimasi 
jalur menggunakan UCS maupun dalam clustering. 

