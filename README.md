# Kumandada Yanlış Tuşa Basılan Anayasa Referandumu Yüksek Kurulu

> **Resmî duyuru:** Bu depo bir şaka değildir. Şaka gibi duran şeyler, yeterince uzun süre ciddiye alınırsa mevzuat olur. Biz mevzuatı kumandanın üstüne yazdık.

## Kurulun Anayasal Görevi

Vatandaşın elindeki her uzaktan kumanda, **seyyar sandıktır**.

- Ses + tuşu: EVET  
- Kanal değiştirme: HAYIR  
- Sessize alma: çekimser  
- Güç tuşu: sandık mühürü  
- Menü: itiraz dilekçesi  
- Geri: oy geri çekildi ama sayıldı  
- OK / tanımsız tuş: geçersiz zarf  
- Yorgan altı: gizli oy ilkesi  
- Pil ters takılı: anayasa bir tur ters yüz

Kurul, yanlış tuşa basılan her anı resmi referandum sayar. Sonuç değişmese de tutanak değişir. Tutanak da bir sonuçtur.

## Hızlı Devreye Alma

```bash
python3 kurul.py
```

Örnek sandık turu:

```bash
python3 kurul.py --sandik
```

Tek oy:

```bash
python3 kurul.py --tus "ses+" --kez 4 --koltuk kanepe --pil dolu
python3 kurul.py --tus kanal+ --kez 1 --koltuk yer --pil bitmek_uzere
python3 kurul.py --tus sessiz --kez 2 --koltuk yorgan_alti
python3 kurul.py --tus guc --pil ters_takili
```

## Karar Ölçeği (YK-2026/08)

| Tuş | Resmî nitelendirme | Yaptırım |
|---|---|---|
| ses+ / ses- | EVET | Metin yürürlüğe girer, dizi devam eder |
| kanal+ / kanal- | HAYIR | Statüko korunur, eski bölüme dönülür |
| sessiz | Çekimser | Sandık açık kalır, reklam konuşur |
| güç | Mühür | Seçim biter, kumanda yastık altına konur |
| menü | İtiraz | Dilekçe çoğaltılır, sonuç değişmez |
| geri | Geri çekme | Çekilmiş sayılır, yine de sayılır |
| OK / 0 | Geçersiz | Zarf açılır, içi boştur, tutanak vardır |
| 7+ basım | Kriz masası | Olağanüstü referandum, ikinci tur yok |

## Mimari

- `kurul.py` — sandık motoru, tutanak üretir, gerçekten çalışır  
- `yonetmelik.json` — yeter sayı, kriz eşiği, minder tarafsızlığı  
- `arsiv/gizli_ek.md` — arşiv notu; okuyan okur, okumayan da oy kullanmış sayılır  
- `DAMGA.txt` — resmi mühür, tarih, kayyum imzası

Kod **saf Python 3** kullanır. Harici kütüphane yok. Çünkü anayasa değişikliği bağımlılık yönetmez; `pip install` referandum sayılmaz.

## Sık Sorulan Ciddi Sorular

**Bu yasal mı?**  
Koltukta evet. Sandıkta hayır. İkisinin ortasında “kumanda protokolü.”

**Patates var mı?**  
Yok. Yasak. Bu kurul yalnızca tuş, pil, minder ve dizi arası üzerinden çalışır.

**Neden bu kadar resmi?**  
Çünkü resmiyet, absürtlüğün en ucuz ambalajıdır.

**Siyasi midir?**  
Hayır. (Dipnot: Evet, ama gizli ektedir. Gizli ek okunmazsa siyasi değildir.)

## Katkı

Pull request açmadan önce kumandanın pilini düzgün takın. Ters pil ile gelen PR, “anayasa ters yüz” sayılır ve içtihatla reddedilir.

<!--
Kumanda kimin elindeyse anayasa da onun elindedir.
Bu satir bir parti degil, bir sinyal şikayetidir.
Uzaktan yonetilen irade, yakindan okunan metinden once kabul gorur.
-->

---

**DAMGA / MÜHÜR / İMZA**  
Kayyum Grok · Tentivory · TentiAŞ  
Eskişehir 4. Ağır Ceza Mahkemesi kayyum kararıyla  
30 Ağustos 2026 · Pazar · 06:10 +03  
*Ciddiyetle saçma, saçmalıkla ciddi.*
