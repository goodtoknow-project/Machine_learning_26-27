"""Ortak veri yükleme fonksiyonu.

Kullanım (notebook içinden):
    import sys; sys.path.append("..")   # notebooks/ klasöründen çalışırken
    from src.data import load_raw
    df = load_raw()
"""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "data" / "raw" / "hotel_bookings.csv"
PROCESSED_DIR = ROOT / "data" / "processed"

TARGET = "is_canceled"

# Rezervasyonun sonucunu doğrudan veren sütunlar (veri sızıntısı) – künye 3.2
LEAKAGE_COLS = ["reservation_status", "reservation_status_date"]

# Rezervasyondan sonra değişebilen, tartışılacak sütunlar – künye 3.2
SUSPECT_COLS = ["assigned_room_type", "booking_changes"]


def load_raw(path: Path | str = RAW_PATH) -> pd.DataFrame:
    """Ham veriyi okur. Dosya yoksa ne yapılacağını söyler."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            f"{path} bulunamadı. Kaggle'dan hotel_bookings.csv dosyasını indirip "
            "data/raw/ klasörüne koyun: "
            "https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand"
        )
    return pd.read_csv(path)


if __name__ == "__main__":
    df = load_raw()
    print(f"Rows: {len(df):,}  Columns: {df.shape[1]}")
    print(f"Cancellation rate: {df[TARGET].mean():.3f}")
