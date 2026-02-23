# 📱 FitWizard Pro Mobile

Мобильная версия тренировочного планировщика на **Kivy/KivyMD**.

## 🚀 Быстрый старт (тестирование на ПК)

### 1. Установка зависимостей

```bash
pip install kivy kivymd pillow
```

### 2. Запуск приложения

```bash
cd mobile_app
python main.py
```

---

## 📲 Сборка APK для Android

### Способ 1: Google Colab (Рекомендуется для Windows)

1. Откройте [Google Colab](https://colab.research.google.com/)
2. Загрузите папку `mobile_app` на Google Drive
3. Выполните:

```python
# Установка Buildozer
!pip install buildozer cython==0.29.33

# Установка Android SDK/NDK
!sudo apt-get update
!sudo apt-get install -y python3-pip build-essential git python3 python3-dev ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev

# Копирование проекта
from google.colab import drive
drive.mount('/content/drive')
!cp -r /content/drive/MyDrive/mobile_app /content/

# Сборка
%cd /content/mobile_app
!buildozer android debug
```

4. Скачайте APK из папки `/content/mobile_app/bin/`

---

### Способ 2: WSL2 (Windows Subsystem for Linux)

1. Установите WSL2:
```powershell
wsl --install -d Ubuntu
```

2. В Ubuntu:
```bash
sudo apt update
sudo apt install python3-pip build-essential git openjdk-17-jdk

pip3 install buildozer cython

cd /mnt/c/Users/Матвей/Desktop/проект/mobile_app
buildozer android debug
```

---

### Способ 3: GitHub Actions (Автоматическая сборка)

1. Создайте репозиторий на GitHub
2. Добавьте файл `.github/workflows/build.yml`:

```yaml
name: Build Android APK

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Build APK
      uses: ArtemSBulgakov/buildozer-action@v1
      with:
        workdir: mobile_app
        buildozer_version: stable
    
    - name: Upload APK
      uses: actions/upload-artifact@v3
      with:
        name: app
        path: mobile_app/bin/*.apk
```

3. APK будет доступен в разделе "Actions" → "Artifacts"

---

## 📁 Структура проекта

```
mobile_app/
├── main.py           # Главный файл приложения
├── buildozer.spec    # Конфигурация сборки
├── icon.png          # Иконка (512x512) - создайте!
├── presplash.png     # Заставка - создайте!
└── README.md         # Этот файл
```

---

## 🎨 Экраны приложения

| Экран | Описание |
|-------|----------|
| Welcome | Приветственный экран |
| Focus | Выбор группы мышц |
| Goal | Выбор цели тренировки |
| Params | Ввод параметров (вес, рост, возраст) |
| Result | Программа тренировок на 4 недели |
| Workout | Экран выполнения тренировки |

---

## 🔧 Кастомизация

### Добавление GIF-анимаций

Для поддержки GIF на мобильных устройствах используйте:

```python
from kivy.uix.image import AsyncImage

# В KV файле:
AsyncImage:
    source: "exercise_gifs/приседания.gif"
    anim_delay: 0.05
```

### Изменение темы

```python
# Светлая тема
self.theme_cls.theme_style = "Light"

# Другой цвет
self.theme_cls.primary_palette = "Purple"
```

---

## ❓ Частые вопросы

**Q: Почему не работает на Windows?**
A: Buildozer работает только на Linux. Используйте WSL2, Google Colab или GitHub Actions.

**Q: Как добавить иконку?**
A: Создайте `icon.png` (512x512 px) и раскомментируйте строку в `buildozer.spec`.

**Q: Как уменьшить размер APK?**
A: Укажите только одну архитектуру: `android.archs = arm64-v8a`

---

## 📞 Поддержка

Если есть вопросы — спрашивайте!
