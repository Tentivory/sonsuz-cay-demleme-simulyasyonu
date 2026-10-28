#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SONSUZ ÇAY DEMLEME SİMÜLASYONU
Bu kod, çayın neden asla tam demlenmediğini bilimsel olarak kanıtlar.
"""

import time
import random
import sys

def demle():
    print("🍵 Çay demleme protokolü başlatılıyor...")
    print("Suyun kaynaması bekleniyor. Bu evrensel bir sabır testidir.\n")
    
    while True:
        bekleme = random.randint(1, 5)
        for i in range(bekleme):
            sys.stdout.write(f"\rDemleniyor{'.' * ((i % 3) + 1)}   ")
            sys.stdout.flush()
            time.sleep(0.8)
        
        # %10 ihtimalle "bitti" de ama aslında bitmedi
        if random.random() < 0.1:
            print("\n\n✅ Çay hazır görünüyor!")
            time.sleep(1)
            print("❌ Yanlış alarm. Henüz demlenmedi. Tekrar başlıyoruz...")
            time.sleep(1)
        else:
            print("\n\n⏳ Hala demleniyor. Lütfen sabırlı olun. Çay acele etmez.")
            time.sleep(0.5)

if __name__ == "__main__":
    try:
        demle()
    except KeyboardInterrupt:
        print("\n\n😴 Simülasyon durduruldu. Çay asla demlenmeyecek. Bu bir özelliktir, hata değil.")
        print("İyi uykular.")
