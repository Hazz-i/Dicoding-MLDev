# Submission 1: SMS-Spam-Clasifications

Nama: Wahid Hasim Santoso

````bash
# SMS Spam Classification

| **Deskripsi**      | **Detail**                                                                                                                                                                                                                                      |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Dataset**         | [SMS Spam Collection (Text Classification)](https://www.kaggle.com/datasets/thedevastator/sms-spam-collection-a-more-diverse-dataset)                                                                                                         |
| **Masalah**         | Spam merupakan masalah umum di era digitalisasi. Salah satu media yang sering terkena spam adalah SMS. Karena seringnya pesan tidak relevan, banyak pengguna yang mengabaikan SMS, termasuk pesan yang bersifat penting atau mendesak.            |
| **Solusi**          | Proyek ini bertujuan untuk mengembangkan alat yang dapat secara otomatis mengklasifikasikan pesan SMS sebagai spam atau bukan spam. Dengan alat ini, pesan penting dapat disampaikan, sementara pesan tidak penting dapat diabaikan.            |
| **Metode Pengolahan** | Dataset terdiri dari dua kolom: `sms` (berisi teks SMS) dan `label` (1 untuk spam, 0 untuk non-spam). Data diproses dengan mengubah teks menjadi non-kapital dan label ke format integer. Dataset kemudian dibagi menjadi train (80%) dan evaluasi (20%). |
| **Arsitektur Model** | Model menggunakan jaringan saraf tiruan dengan lapisan berikut: Input, TextVectorization, Embedding, GlobalAveragePooling1D, dan Dense. Fully connected layer terdiri dari dua Dense layer dengan masing-masing 64 dan 32 unit (ReLU), serta output layer dengan sigmoid. Loss yang digunakan adalah Binary Crossentropy dan optimizer Adam. |
| **Metrik Evaluasi**  | Model dievaluasi menggunakan AUC, FalsePositives, TruePositives, FalseNegatives, TrueNegatives, dan Binary Accuracy.                                                                                                                          |
| **Performa Model**   | Model mencapai AUC 99%, FalsePositives 110, TruePositives 5333, FalseNegatives 667, TrueNegatives 38320, dan Binary Accuracy 98%.                                                                                                             |

## Cara Menjalankan Proyek

1. **Install Dependencies**:
   Pastikan Anda sudah memiliki Python 3.9 atau versi lebih baru dan install dependencies:
   ```bash
   pip install -r requirements.txt

````
