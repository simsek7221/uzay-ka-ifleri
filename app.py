from ursina import *
from ursina import Ursina, Entity, EditorCamera, color, held_keys, Text, invoke
import random

# Oyunu başlat
app = Ursina()

# --- 1. ÇEVRE VE ARKA PLAN ---
window.title = "Echoes of Orbit - NASA Space Apps"
window.color = color.black
window.borderless = False

# Uzay ortamı için arka plan yıldızları (Basit küçük küpler)
for _ in range(150):
    Entity(
        model='cube',
        color=color.white,
        position=(random.uniform(-50, 50), random.uniform(-50, 50), random.uniform(-50, 50)),
        scale=random.uniform(0.1, 0.4)
    )

# --- 2. MERKEZİ NESNE: DÜNYA VE YÖRÜNGE ---
# Dünya Modeli (Mavi-Yeşil Küre)
earth = Entity(
    model='sphere',
    color=color.azure,
    scale=6,
    position=(0, 0, 0)
)

# Dünya'nın kendi etrafında yavaşça dönmesi
def update():
    earth.rotation_y += 5 * time.dt
    
    # Oyuncu hareketi (Kontrol merkezi konsolu etrafında gezinme)
    if held_keys['w']:
        player.z += 5 * time.dt
    if held_keys['s']:
        player.z -= 5 * time.dt
    if held_keys['a']:
        player.x -= 5 * time.dt
    if held_keys['d']:
        player.x += 5 * time.dt

# --- 3. OYUNCU (KONTROL MERKEZİ TERMİNALİ) ---
# Oyuncunun 3D uzay istasyonu odasındaki kamerası
player = EditorCamera()
player.position = (0, 2, -15)

# --- 4. NASA VERİ / UYDU NESNELERİ (Toplanabilir / İncelenebilir) ---
# Yörüngedeki Uzay Çöpleri veya Sinyal Noktaları
debris_list = []

for i in range(5):
    angle = i * (360 / 5)
    debris = Entity(
        model='cube',
        color=color.orange,
        scale=0.8,
        position=(math.sin(math.radians(angle)) * 10, 0, math.cos(math.radians(angle)) * 10),
        collider='box'
    )
    debris_list.append(debris)

# --- 5. ARAYÜZ (UI - BİLGİLENDİRİCİ METİNLER) ---
title_text = Text(
    text="NASA SPACE APPS: Echoes of Orbit",
    position=(-0.85, 0.45),
    scale=1.2,
    color=color.cyan
)

mission_text = Text(
    text="Gorev: Yorbitteki anomalileri tespit et ve sinyali cozumle.\nWASD ile hareket et, fare ile etrafa bak.",
    position=(-0.85, 0.38),
    scale=0.8,
    color=color.light_gray
)

# Oyunu çalıştır
app.run()