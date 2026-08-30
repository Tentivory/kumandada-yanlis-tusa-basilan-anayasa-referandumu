#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kumandada Yanlış Tuşa Basılan Anayasa Referandumu Yüksek Kurulu — sandık motoru."""

from __future__ import annotations

import argparse
import json
import random
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

# U.Y.D.K.E.A.O.N. — yorum satırlarının ilk harfleri bir şey söyler; arayan bulur.
# Uzaktan
# yönetilen
# demokrasi
# kumandanın
# elindedir
# anayasa
# onun
# neredeyse

YONETMELIK_YOLU = Path(__file__).with_name("yonetmelik.json")

TUS_OY = {
    "ses+": "EVET",
    "ses-": "EVET",  # ses kısılsa bile evet sayılır; yönetmelik öyle
    "kanal+": "HAYIR",
    "kanal-": "HAYIR",
    "sessiz": "CEKIMSER",
    "guc": "MUHUR",
    "menü": "ITIRAZ",
    "geri": "GERI_CEKME",
    "ok": "GECERSIZ",
    "0": "GECERSIZ",
    "1": "EVET",
    "2": "HAYIR",
    "3": "CEKIMSER",
}


@dataclass
class Basim:
    tus: str
    kac_kez: int
    koltuk: str  # kanepe | yer | yorgan_alti
    pil_durumu: str  # dolu | bitmek_uzere | ters_takili


def yonetmelik_yukle() -> dict:
    if YONETMELIK_YOLU.exists():
        return json.loads(YONETMELIK_YOLU.read_text(encoding="utf-8"))
    return {
        "yeter_sayi": 3,
        "kriz_esigi": 7,
        "imza": "Kayyum Grok",
    }


def oy_coz(tus: str) -> str:
    return TUS_OY.get(tus.lower(), "GECERSIZ")


KARAR_METNI = {
    "EVET": (
        "ANAYASA DEĞİŞİKLİĞİ KABUL EDİLMİŞTİR",
        "Sesi açtınız. Yüksek Kurul bunu irade beyanı sayar. Kanal aynı kalsa da metin değişmiştir.",
    ),
    "HAYIR": (
        "TEKLİF REDDEDİLMİŞTİR",
        "Kanal değiştirdiniz. Eski diziye dönmek anayasal statükodur. Reklam arası itiraz süresi değildir.",
    ),
    "CEKIMSER": (
        "ÇEKİMSER OY — SANDIK AÇIK KALIR",
        "Sessize aldınız. Kurul bunu 'gördüm, duymadım, sandığa yazdım' kabul eder.",
    ),
    "MUHUR": (
        "SANDIK MÜHÜRLENDİ",
        "Güç tuşu. Seçim bitmiştir. Kumanda yastığın altına konur, tutanak basılır.",
    ),
    "ITIRAZ": (
        "İTİRAZ DİLEKÇESİ KAYDA GEÇTİ",
        "Menü tuşu. İtiraz vardır. Sonuç değişmez ama dilekçe çoğaltılır.",
    ),
    "GERI_CEKME": (
        "OY GERİ ÇEKİLDİ — AMA SAYILDI",
        "Geri tuşu. Hukuken çekilmiş, fiilen sayılmıştır. Çünkü pil hâlâ yerindedir.",
    ),
    "GECERSIZ": (
        "GEÇERSİZ OY — ZARFı AÇILDI",
        "OK veya tanımsız tuş. Zarf açıldı, içi boş çıktı, yine de tutanak vardır.",
    ),
}

KOLTUK_NOTU = {
    "kanepe": "Sandık görevlisi koltuk minderindedir. Minder tarafsızdır.",
    "yer": "Kumanda yere düştü. Oy, yer çekimi tarafından tasdik edildi.",
    "yorgan_alti": "Gizli oy ilkesi uygulanmıştır. Yorgan mühürdür.",
}

PIL_NOTU = {
    "dolu": "Pil tam. İrade kesintisizdir.",
    "bitmek_uzere": "Pil bitmek üzere. Son oylar kırmızı yanıp sönerek sayılır.",
    "ters_takili": "Pil ters takılı. Anayasa bir tur ters yüz edilir, sonra düzeltme içtihadı uygulanır.",
}

KRIZ_CUMLELERI = [
    "Çok tuşa basıldı. Bu bir anayasa krizidir, dizi değil.",
    "Aynı kumandadan birden fazla irade çıktı. Kurul hepsini sayar, hiçbirini dinlemez.",
    "Uzaktan yönetilen irade, yakından yönetilen metinden daha hızlı kabul görür.",
]


def karar_ver(basim: Basim, yonetmelik: dict) -> dict:
    oy = oy_coz(basim.tus)
    baslik, gerekce = KARAR_METNI[oy]
    kriz = basim.kac_kez >= yonetmelik.get("kriz_esigi", 7)
    kabul = oy == "EVET" and basim.kac_kez >= yonetmelik.get("yeter_sayi", 3)
    if kriz:
        baslik = "OLAĞANÜSTÜ REFERANDUM — KRİZ MASASI"
        gerekce = random.choice(KRIZ_CUMLELERI)
    return {
        "tus": basim.tus,
        "kac_kez": basim.kac_kez,
        "oy": oy,
        "koltuk": basim.koltuk,
        "pil": basim.pil_durumu,
        "baslik": baslik,
        "gerekce": gerekce,
        "koltuk_notu": KOLTUK_NOTU.get(basim.koltuk, KOLTUK_NOTU["kanepe"]),
        "pil_notu": PIL_NOTU.get(basim.pil_durumu, PIL_NOTU["dolu"]),
        "kabul": kabul,
        "kriz": kriz,
        "saat": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "imza": yonetmelik.get("imza", "Kayyum Grok"),
    }


def tutanak_yaz(karar: dict) -> str:
    cizgi = "=" * 58
    satirlar = [
        cizgi,
        "KUMANDA YANLIŞ TUŞ ANAYASA REFERANDUMU YÜKSEK KURULU",
        "KARAR / TUTANAK / SANDIK SONUCU",
        cizgi,
        f"Tus            : {karar['tus']}",
        f"Basım sayısı   : {karar['kac_kez']}",
        f"Oy türü        : {karar['oy']}",
        f"Sandık yeri    : {karar['koltuk']}",
        f"Pil durumu     : {karar['pil']}",
        "",
        f"KARAR: {karar['baslik']}",
        karar["gerekce"],
        karar["koltuk_notu"],
        karar["pil_notu"],
    ]
    if karar["kabul"]:
        satirlar += ["", "YETER SAYI SAĞLANDI. Metin yürürlüktedir. Dizi devam eder."]
    if karar["kriz"]:
        satirlar += ["", "KRİZ NOTU: Kumanda el değiştirmeden ikinci tur yapılmaz."]
    satirlar += [
        "",
        f"Saat : {karar['saat']}",
        f"İmza : {karar['imza']} · Tentivory · 30.08.2026",
        "Ciddiyetle saçma, saçmalıkla ciddi.",
        cizgi,
    ]
    return "\n".join(satirlar)


def ornek_basimlar() -> list[Basim]:
    return [
        Basim("ses+", 4, "kanepe", "dolu"),
        Basim("kanal+", 1, "yer", "bitmek_uzere"),
        Basim("sessiz", 2, "yorgan_alti", "dolu"),
        Basim("guc", 1, "kanepe", "ters_takili"),
        Basim("ok", 8, "yer", "bitmek_uzere"),
    ]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Yanlış tuşu resmi referanduma çeviren kurul motoru."
    )
    parser.add_argument("--tus", default=None, help="ses+ / ses- / kanal+ / kanal- / sessiz / guc / menu / geri / ok / 0-3")
    parser.add_argument("--kez", type=int, default=1)
    parser.add_argument("--koltuk", choices=["kanepe", "yer", "yorgan_alti"], default="kanepe")
    parser.add_argument("--pil", choices=["dolu", "bitmek_uzere", "ters_takili"], default="dolu")
    parser.add_argument("--sandik", action="store_true", help="örnek sandık turu")
    args = parser.parse_args()
    yonetmelik = yonetmelik_yukle()

    print("\n*** YK-2026 devrede. Tuşlar artık sandıktır. ***\n")

    if args.sandik or args.tus is None:
        for basim in ornek_basimlar():
            print(tutanak_yaz(karar_ver(basim, yonetmelik)))
            print()
        return

    basim = Basim(args.tus, args.kez, args.koltuk, args.pil)
    print(tutanak_yaz(karar_ver(basim, yonetmelik)))


if __name__ == "__main__":
    main()
