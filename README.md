# E-Commerce End-to-End Data Pipeline & Analytics

Bu proje, Brezilya merkezli e-ticaret platformu **Olist**'in gerçek verileri üzerinde kurulan uçtan uca bir veri mühendisliği ve iş analitiği (BI) çalışmasıdır.

Ham CSV verileri otomatik bir ETL akışıyla işlenerek Dockerize edilmiş bir PostgreSQL ilişkisel veritabanına aktarılmış ve analitik SQL sorguları ile iş kararlarını destekleyecek çıktılar üretilmiştir.

---

## Mimari ve Teknolojiler

- **Veri Tabanı & Altyapı:** PostgreSQL 15, Docker & Docker Compose, pgAdmin 4
- **Programlama & ETL:** Python 3, Pandas, SQLAlchemy, Psycopg2
- **Veri Analitiği:** İlişkisel Veri Modelleme, İleri Seviye SQL (Aggregation, Window Functions, JOINs)

---

## Proje Yapısı

```text
├── data/
│   └── raw/               # Ham e-ticaret CSV dosyaları (Gitignore altında)
├── sql/
│   ├── schema.sql         # Tablo şemaları ve ilişkisel kısıtlamalar (PK/FK)
│   └── analytics.sql      # İş zekası ve analitik SQL sorguları
├── src/
│   ├── db.py              # Veritabanı motoru ve bağlantı yönetimi
│   └── etl.py             # Veri temizleme, dönüştürme ve yükleme scripti
├── docker-compose.yml     # PostgreSQL ve pgAdmin konteyner orkestrasyonu
├── requirements.txt       # Gerekli Python bağımlılıkları
└── README.md
```
