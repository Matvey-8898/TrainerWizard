# ============== ЛОКАЛИЗАЦИЯ (перенесена в JSON-файлы) ==============

import json
from pathlib import Path
from typing import Dict, Any
import flet as ft
import random
import datetime
import asyncio


def load_locales(locales_dir: Path) -> Dict[str, Dict[str, str]]:
    """Загружает все JSON-файлы локалей из директории и возвращает словарь {lang: dict}.
    Если директории нет или файлов нет — возвращает пустой словарь.
    """
    locales: Dict[str, Dict[str, str]] = {}
    try:
        if not locales_dir.exists():
            return {}
        for f in locales_dir.glob("*.json"):
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
                if isinstance(data, dict):
                    locales[f.stem] = data
            except Exception:
                # silently skip malformed files
                continue
    except Exception:
        return {}

    # Если есть английская локаль, подтянем недостающие ключи в другие языки как fallback
    try:
        if 'en' in locales and isinstance(locales['en'], dict):
            en = locales['en']
            for lang_key, lang_dict in list(locales.items()):
                if lang_key == 'en' or not isinstance(lang_dict, dict):
                    continue
                for k, v in en.items():
                    if k not in lang_dict:
                        lang_dict[k] = v
    except Exception:
        pass

    return locales


LOCALES = load_locales(Path(__file__).parent / "locales") or {}

EXERCISES = {
    'Full Body': [
        # Универсальные упражнения
        {'name': 'Приседания', 'type': 'compound', 'difficulty': 'beginner', 'gif': 'приседания.gif'},
        {'name': 'Отжимания', 'type': 'compound', 'difficulty': 'beginner', 'gif': 'отжимания.gif'},
        {'name': 'Выпады', 'type': 'compound', 'difficulty': 'beginner', 'gif': 'выпады.gif'},
        {'name': 'Планка', 'type': 'core', 'difficulty': 'beginner', 'gif': 'планка.gif', 'is_hold': True},
        {'name': 'Скалолаз', 'type': 'compound', 'difficulty': 'intermediate', 'gif': 'скалолаз.gif'},
        {'name': 'Берпи', 'type': 'compound', 'difficulty': 'intermediate', 'gif': 'Берпи (женский вариант).gif'},
        {'name': 'Прыжки с хлопками', 'type': 'cardio', 'difficulty': 'beginner', 'gif': 'Прыжки с хлопками над головой.gif'},
        {'name': 'Ягодичный мостик', 'type': 'compound', 'difficulty': 'beginner', 'gif': 'ягодичный моститк.gif'},
        {'name': 'Боковая планка', 'type': 'core', 'difficulty': 'intermediate', 'gif': 'Боковая планка.gif', 'is_hold': True},
        {'name': 'Велосипед', 'type': 'core', 'difficulty': 'beginner', 'gif': 'Велосипед (скручивания).gif'},
        {'name': 'Русские скручивания', 'type': 'core', 'difficulty': 'beginner', 'gif': 'Русские скручивания.gif'},
        {'name': 'Скручивания на полу', 'type': 'core', 'difficulty': 'beginner', 'gif': 'Скручивания на полу.gif'},
        {'name': 'Подъёмы ног', 'type': 'core', 'difficulty': 'beginner', 'gif': 'подъемы ног.gif'},
        {'name': 'Мёртвый жук', 'type': 'core', 'difficulty': 'beginner', 'gif': 'Мёртвый жук.gif'},
        
        # Мужские упражнения для всего тела (высокая интенсивность)
        {'name': 'Берпи с отжиманиями', 'type': 'compound', 'difficulty': 'intermediate', 'gif': 'берпи с отжиманиями.gif', 'male_focused': True},
        {'name': 'Динамическая боковая планка', 'type': 'core', 'difficulty': 'intermediate', 'gif': 'динамическая боковая планка.gif', 'male_focused': True, 'is_hold': True},
        {'name': 'Выпады вперёд-назад', 'type': 'compound', 'difficulty': 'intermediate', 'gif': 'Выпады вперёд-назад.gif', 'male_focused': True},
        {'name': 'Скручивания локтем к колену', 'type': 'core', 'difficulty': 'intermediate', 'gif': 'Скручивания локтем к колену.gif', 'male_focused': True},
        {'name': 'Подъём таза на одной ноге', 'type': 'compound', 'difficulty': 'intermediate', 'gif': 'Подъём таза на одной ноге.gif', 'male_focused': True},
        {'name': 'Подъём ног лёжа вверх', 'type': 'core', 'difficulty': 'intermediate', 'gif': 'Подъём ног лёжа.gif', 'male_focused': True},
        {'name': 'Супермен', 'type': 'core', 'difficulty': 'beginner', 'gif': 'Супермен (удержание).webp', 'male_focused': True, 'is_hold': True},
        {'name': 'Широкие отжимания', 'type': 'compound', 'difficulty': 'beginner', 'gif': 'Широкие отжимания.gif', 'male_focused': True},
        {'name': 'Алмазные отжимания', 'type': 'compound', 'difficulty': 'intermediate', 'gif': 'алмазные отжимания.gif', 'male_focused': True},
        
        # Женские упражнения для всего тела (безопасные)
        {'name': 'Вариации планки', 'type': 'core', 'difficulty': 'beginner', 'gif': 'планка на локтях.gif', 'female_focused': True, 'is_hold': True},
        {'name': 'Приседания плие', 'type': 'compound', 'difficulty': 'beginner', 'gif': 'Приседания плие.gif', 'female_focused': True},
        {'name': 'Ягодичный мостик на одной ноге', 'type': 'compound', 'difficulty': 'beginner', 'gif': 'Подъём таза на одной ноге.gif', 'female_focused': True},
        {'name': 'Вариации отжиманий', 'type': 'compound', 'difficulty': 'beginner', 'gif': 'Отжимания с колен.gif', 'female_focused': True},
        {'name': 'Бёрпи (женский вариант)', 'type': 'compound', 'difficulty': 'intermediate', 'gif': 'Берпи (женский вариант).gif', 'female_focused': True},
        {'name': 'Глубокие приседания', 'type': 'compound', 'difficulty': 'beginner', 'gif': 'Глубокие приседания с наклоном.gif', 'female_focused': True},
        {'name': 'Королевская становая тяга', 'type': 'compound', 'difficulty': 'intermediate', 'gif': 'Королевская становая тяга.gif', 'female_focused': True},
        {'name': 'Поза ребёнка', 'type': 'core', 'difficulty': 'beginner', 'gif': 'Поза ребёнка.gif', 'female_focused': True, 'is_hold': True},
        {'name': 'Боковые наклоны', 'type': 'core', 'difficulty': 'beginner', 'gif': 'Боковые наклоны.gif', 'female_focused': True},
    ],
    'Legs': [
        {'name': 'Приседания', 'type': 'compound', 'difficulty': 'beginner', 'gif': 'приседания.gif'},
        {'name': 'Болгарские сплит-приседания', 'type': 'compound', 'difficulty': 'intermediate', 'gif': 'Болгарские сплит-приседания.gif'},
        {'name': 'Выпады в ходьбе', 'type': 'compound', 'difficulty': 'beginner', 'gif': 'Выпады с ходьбой.gif'},
        {'name': 'Ягодичный мостик', 'type': 'isolation', 'difficulty': 'beginner', 'gif': 'ягодичный моститк.gif'},
        {'name': 'Становая тяга на одной ноге', 'type': 'compound', 'difficulty': 'intermediate', 'gif': 'Становая тяга на одной ноге.gif'},
        {'name': 'Приседания у стены', 'type': 'isolation', 'difficulty': 'beginner', 'gif': 'Приседания у стены.gif', 'is_hold': True},
        {'name': 'Подъёмы на носки', 'type': 'isolation', 'difficulty': 'beginner', 'gif': 'Подъёмы на носки.gif'},
        {'name': 'Приседания с прыжком', 'type': 'compound', 'difficulty': 'intermediate', 'gif': 'Приседания с прыжком.gif'},
        {'name': 'Выпады', 'type': 'compound', 'difficulty': 'beginner', 'gif': 'выпады.gif'},
        {'name': 'Статические выпады', 'type': 'compound', 'difficulty': 'beginner', 'gif': 'Статические выпады.gif'},
        # Женские упражнения для ног
        {'name': 'Приседания плие', 'type': 'compound', 'difficulty': 'beginner', 'gif': 'Приседания плие.gif', 'female_focused': True},
        {'name': 'Подъёмы ног в сторону', 'type': 'isolation', 'difficulty': 'beginner', 'gif': 'Подъёмы ног лёжа.gif', 'female_focused': True},
        {'name': 'Подъёмы ног лёжа', 'type': 'isolation', 'difficulty': 'beginner', 'gif': 'Подъём ног лёжа.gif', 'female_focused': True},
        {'name': 'Ягодичный мостик на одной ноге', 'type': 'isolation', 'difficulty': 'intermediate', 'gif': 'Подъём таза на одной ноге.gif', 'female_focused': True},
    ],
    'Chest': [
        {'name': 'Отжимания', 'type': 'compound', 'difficulty': 'beginner', 'gif': 'отжимания.gif'},
        {'name': 'Широкие отжимания', 'type': 'compound', 'difficulty': 'beginner', 'gif': 'Широкие отжимания.gif'},
        {'name': 'Алмазные отжимания', 'type': 'compound', 'difficulty': 'intermediate', 'gif': 'алмазные отжимания.gif'},
        {'name': 'Отжимания с ногами на возвышении', 'type': 'compound', 'difficulty': 'intermediate', 'gif': 'Отжимания с ногами на возвышении.gif'},
        {'name': 'Отжимания на брусьях', 'type': 'compound', 'difficulty': 'intermediate', 'gif': 'Отжимания на брусьях (грудные).gif'},
        {'name': 'Псевдо-планш отжимания', 'type': 'compound', 'difficulty': 'advanced', 'gif': 'Псевдо-планш отжимания.gif'},
        {'name': 'Узкие отжимания', 'type': 'compound', 'difficulty': 'intermediate', 'gif': 'узкие отжимания.gif'},
        {'name': 'Отжимания с колен', 'type': 'compound', 'difficulty': 'beginner', 'gif': 'Отжимания с колен.gif'},
        {'name': 'Отжимания с возвышения', 'type': 'compound', 'difficulty': 'beginner', 'gif': 'Отжимания с возвышения.gif'},
        {'name': 'Планка', 'type': 'core', 'difficulty': 'beginner', 'gif': 'планка.gif', 'is_hold': True},
        {'name': 'Боковая планка', 'type': 'core', 'difficulty': 'intermediate', 'gif': 'Боковая планка.gif', 'is_hold': True},
        {'name': 'Обратная планка', 'type': 'core', 'difficulty': 'intermediate', 'gif': 'Обратная планка.gif', 'is_hold': True},
    ],
    'Arms': [
        # Трицепс
        {'name': 'Обратные отжимания на трицепс', 'type': 'isolation', 'difficulty': 'beginner', 'gif': 'Обратные отжимания на трицепс.gif'},
        {'name': 'Алмазные отжимания', 'type': 'compound', 'difficulty': 'intermediate', 'gif': 'алмазные отжимания.gif'},
        {'name': 'Узкие отжимания', 'type': 'compound', 'difficulty': 'beginner', 'gif': 'узкие отжимания.gif'},
        # Бицепс и комплексные
        {'name': 'Подтягивания', 'type': 'compound', 'difficulty': 'intermediate', 'gif': 'подтягивания.gif'},
        {'name': 'Отжимания', 'type': 'compound', 'difficulty': 'beginner', 'gif': 'отжимания.gif'},
        {'name': 'Псевдо-планш отжимания', 'type': 'compound', 'difficulty': 'advanced', 'gif': 'Псевдо-планш отжимания.gif'},
        {'name': 'Планка в собаку', 'type': 'compound', 'difficulty': 'intermediate', 'gif': 'Планка с переходом в собаку мордой вниз.gif'},
        {'name': 'Отжимания с возвышения', 'type': 'compound', 'difficulty': 'beginner', 'gif': 'Отжимания с возвышения.gif'},
        {'name': 'Отжимания с колен', 'type': 'compound', 'difficulty': 'beginner', 'gif': 'Отжимания с колен.gif'},
        {'name': 'Широкие отжимания', 'type': 'compound', 'difficulty': 'beginner', 'gif': 'Широкие отжимания.gif'},
        {'name': 'Планка', 'type': 'core', 'difficulty': 'beginner', 'gif': 'планка.gif', 'is_hold': True},
        {'name': 'Планка на локтях', 'type': 'core', 'difficulty': 'beginner', 'gif': 'планка на локтях.gif', 'is_hold': True},
    ],
    'Core': [
        {'name': 'Планка', 'type': 'core', 'difficulty': 'beginner', 'gif': 'планка.gif', 'is_hold': True},
        {'name': 'Боковая планка', 'type': 'core', 'difficulty': 'beginner', 'gif': 'Боковая планка.gif', 'is_hold': True},
        {'name': 'Скручивания на полу', 'type': 'core', 'difficulty': 'beginner', 'gif': 'Скручивания на полу.gif'},
        {'name': 'Велосипед', 'type': 'core', 'difficulty': 'beginner', 'gif': 'Велосипед (скручивания).gif'},
        {'name': 'Русские скручивания', 'type': 'core', 'difficulty': 'beginner', 'gif': 'Русские скручивания.gif'},
        {'name': 'Подъёмы ног', 'type': 'core', 'difficulty': 'intermediate', 'gif': 'подъемы ног.gif'},
        {'name': 'Скалолаз', 'type': 'core', 'difficulty': 'intermediate', 'gif': 'скалолаз.gif'},
        {'name': 'Мёртвый жук', 'type': 'core', 'difficulty': 'beginner', 'gif': 'Мёртвый жук.gif'},
        {'name': 'Ножницы', 'type': 'core', 'difficulty': 'beginner', 'gif': 'ножницы.gif'},
        {'name': 'Планка на локтях', 'type': 'core', 'difficulty': 'beginner', 'gif': 'планка на локтях.gif', 'is_hold': True},
        {'name': 'Обратная планка', 'type': 'core', 'difficulty': 'intermediate', 'gif': 'Обратная планка.gif', 'is_hold': True},
        {'name': 'Подъём ног лёжа', 'type': 'core', 'difficulty': 'beginner', 'gif': 'Подъём ног лёжа.gif'},
        {'name': 'Динамическая боковая планка', 'type': 'core', 'difficulty': 'intermediate', 'gif': 'динамическая боковая планка.gif', 'is_hold': True},
        # Мужские упражнения на пресс (более интенсивные)
        {'name': 'Скалолаз (быстрый)', 'type': 'core', 'difficulty': 'intermediate', 'gif': 'скалолаз.gif', 'male_focused': True},
        {'name': 'Русские скручивания сидя', 'type': 'core', 'difficulty': 'intermediate', 'gif': 'Русские скручивания сидя.gif', 'male_focused': True},
        # Женские упражнения на пресс (мягкая нагрузка)
        {'name': 'Боковые наклоны', 'type': 'core', 'difficulty': 'beginner', 'gif': 'Боковые наклоны.gif', 'female_focused': True},
        {'name': 'Подтягивания коленей', 'type': 'core', 'difficulty': 'beginner', 'gif': 'Подтягивания колен.gif', 'female_focused': True},
    ],
    'Weight Loss': [
        # ===== УНИВЕРСАЛЬНЫЕ КАРДИО УПРАЖНЕНИЯ =====
        {'name': 'Берпи', 'type': 'hiit', 'difficulty': 'intermediate', 'gif': 'берпи с отжиманиями.gif'},
        {'name': 'Прыжки с хлопками над головой', 'type': 'hiit', 'difficulty': 'beginner', 'gif': 'Прыжки с хлопками над головой.gif'},
        {'name': 'Бег с высоким подниманием коленей', 'type': 'hiit', 'difficulty': 'beginner', 'gif': 'Бег с высоким подниманием коленей.gif'},
        {'name': 'Скалолаз', 'type': 'hiit', 'difficulty': 'intermediate', 'gif': 'скалолаз.gif'},
        {'name': 'Приседания с прыжком', 'type': 'hiit', 'difficulty': 'intermediate', 'gif': 'Приседания с прыжком.gif'},
        {'name': 'Конькобежец', 'type': 'hiit', 'difficulty': 'intermediate', 'gif': 'Конькобежец.gif'},
        {'name': 'Бег на месте', 'type': 'hiit', 'difficulty': 'beginner', 'gif': 'Бег на месте.gif'},
        
        # ===== НИЗКОУДАРНЫЕ УПРАЖНЕНИЯ =====
        {'name': 'Приседания', 'type': 'strength', 'difficulty': 'beginner', 'gif': 'приседания.gif'},
    ],
}
    
def switch_language(lang: str, app_instance=None):
    """Переключает язык глобально и опционально обновляет UI переданного приложения."""
    global CURRENT_LANG
    CURRENT_LANG = lang
    if app_instance is not None:
        try:
            app_instance.lang = lang
            # ожидается метод refresh_screen у TrainingApp
            if hasattr(app_instance, 'refresh_screen'):
                app_instance.refresh_screen()
        except Exception:
            pass

    # Попытаться перезагрузить файлы локалей на случай, если они были добавлены/изменены
    try:
        global LOCALES
        locales_path = Path(__file__).parent / "locales"
        loaded = load_locales(locales_path)
        if isinstance(loaded, dict) and loaded:
            LOCALES = loaded
    except Exception:
        pass

# Текущая выбранная локаль по умолчанию
CURRENT_LANG = 'ru'

def translate(key: str, lang: str | None = None) -> str:
    """Возвращает перевод для ключа с учётом fallback: requested -> en -> любой доступный -> ключ."""
    if lang is None:
        lang = CURRENT_LANG
    try:
        # первый приоритет: запрошенный язык
        if isinstance(LOCALES, dict):
            loc = LOCALES.get(lang, {})
            if key in loc:
                return loc.get(key)
            # fallback на английский
            if 'en' in LOCALES and key in LOCALES['en']:
                return LOCALES['en'][key]
            # любой другой первый найденный перевод
            for ldict in LOCALES.values():
                if isinstance(ldict, dict) and key in ldict:
                    return ldict[key]
    except Exception:
        pass
    return key

def has_translation(key: str, lang: str | None = None) -> bool:
    if lang is None:
        lang = CURRENT_LANG
    return key in LOCALES.get(lang, {}) if isinstance(LOCALES, dict) else False


# ============== ГЛАВНЫЙ КЛАСС ПРИЛОЖЕНИЯ ==============

class TrainingApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "💪 TrainerWizard"
        self.page.padding = 0
        self.page.spacing = 0
        
        # Путь к GIF - пробуем несколько вариантов
        possible_paths = [
            Path(__file__).parent / "assets",
            Path(__file__).parent.parent / "exercise_gifs",
            Path(__file__).parent / "exercise_gifs",
            Path.cwd() / "exercise_gifs",
            Path.cwd() / "assets",
        ]
        
        self.gifs_dir = None
        for path in possible_paths:
            if path.exists():
                self.gifs_dir = path
                print(f"✅ GIF папка найдена: {path}")
                break
        
        if self.gifs_dir is None:
            self.gifs_dir = Path(__file__).parent / "assets"
            print(f"⚠️ GIF папка не найдена, используем: {self.gifs_dir}")
        
        # Настройки
        self.lang = 'ru'
        self.theme = 'dark'
        self.apply_theme()
        
        # Данные пользователя
        self.user_data = {}
        self.program_data = None
        self.completed_workouts = set()
        self.completed_rest_days = set()
        self.workout_history = []
        self.selected_zones = set()
        self.progress_data = {
            'weight': [],
            'measurements': {'chest': [], 'waist': [], 'hips': [], 'arms': []},
            'photos': []
        }
        
        # Текущий экран
        self.current_screen = None
        self.settings_visible = False
        self.current_workout = None
        self.timer_generation = 0
        
        # Показываем экран приветствия
        self.show_welcome()
    
    def t(self, key):
        return translate(key, self.lang)
    
    def apply_theme(self):
        if self.theme == 'dark':
            self.page.theme_mode = ft.ThemeMode.DARK
            self.colors = {
                'bg': '#0a0e27',
                'bg_card': '#1a1f3a',
                'bg_hover': '#252b4a',
                'primary': '#667eea',
                'primary_hover': '#5a67d8',
                'secondary': '#f093fb',
                'success': '#00d4aa',
                'success_hover': '#00b894',
                'warning': '#ffa726',
                'warning_hover': '#ff9800',
                'danger': '#ff5252',
                'text': '#ffffff',
                'text_secondary': '#a0aec0',
                'border': '#2d3748',
            }
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            self.colors = {
                'bg': '#f0f4f8',
                'bg_card': '#ffffff',
                'bg_hover': '#e2e8f0',
                'primary': '#667eea',
                'primary_hover': '#5a67d8',
                'secondary': '#f093fb',
                'success': '#00d4aa',
                'success_hover': '#00b894',
                'warning': '#ffa726',
                'warning_hover': '#ff9800',
                'danger': '#ff5252',
                'text': '#1a202c',
                'text_secondary': '#718096',
                'border': '#e2e8f0',
            }
        self.page.bgcolor = self.colors['bg']
        self.page.update()
    

    
    def create_gradient_container(self, content, colors, **kwargs):
        return ft.Container(
            content=content,
            gradient=ft.LinearGradient(
                begin=ft.Alignment(-1, -1),
                end=ft.Alignment(1, 1),
                colors=colors,
            ),
            **kwargs,
        )
    
    def create_animated_card(self, content, color, delay_ms=0, **kwargs):
        return ft.Container(
            content=content,
            padding=kwargs.get('padding', 22),
            border_radius=kwargs.get('border_radius', 20),
            bgcolor=self.colors['bg_card'],
            border=ft.border.all(2, color),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=15,
                color=ft.Colors.with_opacity(0.3, color),
                offset=ft.Offset(0, 5),
            ),
            animate=ft.Animation(400, ft.AnimationCurve.EASE_OUT),
            animate_opacity=ft.Animation(400, ft.AnimationCurve.EASE_OUT),
            animate_scale=ft.Animation(300, ft.AnimationCurve.EASE_OUT),
            width=kwargs.get('width', 800),
            on_hover=lambda e: self._on_card_hover(e),
        )
    
    def _on_card_hover(self, e):
        if e.data == "true":
            e.control.scale = 1.02
            e.control.shadow = ft.BoxShadow(
                spread_radius=2,
                blur_radius=20,
                color=ft.Colors.with_opacity(0.4, self.colors['primary']),
                offset=ft.Offset(0, 8),
            )
        else:
            e.control.scale = 1.0
            e.control.shadow = ft.BoxShadow(
                spread_radius=0,
                blur_radius=15,
                color=ft.Colors.with_opacity(0.3, self.colors['primary']),
                offset=ft.Offset(0, 5),
            )
        e.control.update()
    
    def create_gradient_button(self, text, colors, on_click, **kwargs):
        return ft.Container(
            content=ft.Text(
                text,
                size=kwargs.get('text_size', 16),
                weight=ft.FontWeight.BOLD,
                color="white",
                text_align=ft.TextAlign.CENTER,
            ),
            gradient=ft.LinearGradient(
                begin=ft.Alignment(-1, 0),
                end=ft.Alignment(1, 0),
                colors=colors,
            ),
            padding=ft.Padding.symmetric(horizontal=30, vertical=14),
            border_radius=kwargs.get('border_radius', 25),
            width=kwargs.get('width', 800),
            alignment=ft.Alignment(0, 0),
            on_click=on_click,
            animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
            animate_scale=ft.Animation(150, ft.AnimationCurve.EASE_OUT),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=12,
                color=ft.Colors.with_opacity(0.4, colors[0]),
                offset=ft.Offset(0, 4),
            ),
            on_hover=lambda e: self._on_button_hover(e, colors),
        )
    
    def _on_button_hover(self, e, colors):
        if e.data == "true":
            e.control.scale = 1.05
            e.control.shadow = ft.BoxShadow(
                spread_radius=2,
                blur_radius=18,
                color=ft.Colors.with_opacity(0.5, colors[0]),
                offset=ft.Offset(0, 6),
            )
        else:
            e.control.scale = 1.0
            e.control.shadow = ft.BoxShadow(
                spread_radius=0,
                blur_radius=12,
                color=ft.Colors.with_opacity(0.4, colors[0]),
                offset=ft.Offset(0, 4),
            )
        e.control.update()
    
    def create_glow_text(self, text, size, color, **kwargs):
        return ft.Container(
            content=ft.Text(
                text,
                size=size,
                weight=kwargs.get('weight', ft.FontWeight.BOLD),
                color=color,
                text_align=kwargs.get('text_align', ft.TextAlign.CENTER),
            ),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=20,
                color=ft.Colors.with_opacity(0.5, color),
            ),
        )
    
    def build_top_bar(self):
        # Кнопки действий (показываем только если программа сгенерирована)
        action_buttons = []
        if hasattr(self, 'program_data') and self.program_data:
            action_buttons = [
                ft.Container(
                    content=ft.Icon(ft.Icons.SAVE, color="white", size=18),
                    width=36,
                    height=36,
                    border_radius=18,
                    bgcolor=self.colors['primary'],
                    alignment=ft.Alignment(0, 0),
                    on_click=lambda e: self.save_program(),
                    tooltip=self.t('save_program'),
                ),
                ft.Container(
                    content=ft.Icon(ft.Icons.MENU_BOOK, color="white", size=18),
                    width=36,
                    height=36,
                    border_radius=18,
                    bgcolor=self.colors['secondary'],
                    alignment=ft.Alignment(0, 0),
                    on_click=lambda e: self.show_diary(),
                    tooltip=self.t('diary'),
                ),
                ft.Container(
                    content=ft.Icon(ft.Icons.REFRESH, color="white", size=18),
                    width=36,
                    height=36,
                    border_radius=18,
                    bgcolor=self.colors['warning'],
                    alignment=ft.Alignment(0, 0),
                    on_click=lambda e: self.show_welcome(),
                    tooltip=self.t('new_program'),
                ),
            ]
        
        return ft.Container(
            content=ft.Row([
                ft.Row([
                    ft.Container(
                        content=ft.Text("💪", size=24),
                        animate_scale=ft.Animation(300, ft.AnimationCurve.ELASTIC_OUT),
                    ),
                    ft.Text("TrainerWizard", size=18, weight=ft.FontWeight.BOLD, 
                           color=self.colors['text']),
                ], spacing=8),
                ft.Row([
                    *action_buttons,
                    ft.Container(
                        content=ft.Icon(ft.Icons.SETTINGS, color="white", size=20),
                        width=40,
                        height=40,
                        border_radius=20,
                        gradient=ft.LinearGradient(
                            begin=ft.Alignment(-1, -1),
                            end=ft.Alignment(1, 1),
                            colors=[self.colors['primary'], self.colors['secondary']],
                        ),
                        alignment=ft.Alignment(0, 0),
                        on_click=lambda e: self.toggle_settings(),
                        animate_scale=ft.Animation(150, ft.AnimationCurve.EASE_OUT),
                        on_hover=lambda e: setattr(e.control, 'scale', 1.1 if e.data == "true" else 1.0) or e.control.update(),
                    ),
                ], spacing=6),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            padding=ft.Padding.symmetric(horizontal=15, vertical=12),
            gradient=ft.LinearGradient(
                begin=ft.Alignment(-1, -1),
                end=ft.Alignment(1, 1),
                colors=[self.colors['bg_card'], self.colors['bg']],
            ),
            border=ft.border.only(bottom=ft.BorderSide(1, self.colors['border'])),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=10,
                color=ft.Colors.with_opacity(0.2, self.colors['primary']),
                offset=ft.Offset(0, 2),
            ),
        )
    
    def build_settings_panel(self):
        
        # Языки - используем кнопки вместо dropdown
        lang_buttons = []
        languages = [
            ("ru", "🇷🇺 Русский"),
            ("en", "🇬🇧 English"),
            ("es", "🇪🇸 Español"),
            ("de", "🇩🇪 Deutsch"),
            ("zh", "🇨🇳 中文"),
            ("it", "🇮🇹 Italiano"),
            ("pl", "🇵🇱 Polski"),
            ("tr", "🇹🇷 Türkçe"),
            ("hi", "🇮🇳 हिन्दी"),
            ("ar", "🇸🇦 العربية"),
            ("ko", "🇰🇷 한국어"),
            ("nl", "🇳🇱 Nederlands"),
            ("sv", "🇸🇪 Svenska"),
        ]
        
        for lang_code, lang_name in languages:
            is_selected = self.lang == lang_code
            lang_buttons.append(
                ft.Container(
                    content=ft.Text(lang_name, size=14, 
                                   color="white" if is_selected else self.colors['text']),
                    padding=ft.Padding.symmetric(horizontal=15, vertical=10),
                    border_radius=10,
                    bgcolor=self.colors['primary'] if is_selected else self.colors['bg_hover'],
                    on_click=lambda e, lc=lang_code: self.do_change_language(lc),
                    ink=True,
                )
            )
        
        # Темы - кнопки
        theme_buttons = []
        themes = [
            ("dark", f"🌙 {self.t('theme_dark')}"),
            ("light", f"☀️ {self.t('theme_light')}"),
        ]
        
        for theme_code, theme_name in themes:
            is_selected = self.theme == theme_code
            theme_buttons.append(
                ft.Container(
                    content=ft.Text(theme_name, size=14,
                                   color="white" if is_selected else self.colors['text']),
                    padding=ft.Padding.symmetric(horizontal=20, vertical=12),
                    border_radius=10,
                    bgcolor=self.colors['primary'] if is_selected else self.colors['bg_hover'],
                    on_click=lambda e, tc=theme_code: self.do_change_theme(tc),
                    ink=True,
                    expand=True,
                )
            )
        
        return ft.Container(
            content=ft.Column([
                # Заголовок с кнопкой закрытия
                ft.Row([
                    ft.Text(self.t('settings'), size=22, weight=ft.FontWeight.BOLD,
                           color=self.colors['text']),
                    ft.IconButton(
                        icon=ft.Icons.CLOSE,
                        icon_color=self.colors['danger'],
                        icon_size=24,
                        on_click=lambda e: self.hide_settings()
                    ),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                
                ft.Divider(color=self.colors['border'], height=20),
                
                # Выбор языка - заголовок
                ft.Text(self.t('settings_language'), size=14, color=self.colors['text_secondary']),
                ft.Container(height=8),
                
                # Кнопки языков
                ft.Column(lang_buttons, spacing=6),
                
                ft.Container(height=25),
                
                # Выбор темы - заголовок
                ft.Text(self.t('settings_theme'), size=14, color=self.colors['text_secondary']),
                ft.Container(height=8),
                
                # Кнопки тем
                ft.Row(theme_buttons, spacing=10),
                
                ft.Container(height=40),
                
                ft.Divider(color=self.colors['border']),
                
                ft.Container(height=20),
                
                # Кнопка "Назад"
                ft.ElevatedButton(
                    self.t('settings_back'),
                    bgcolor=self.colors['success'],
                    color="white",
                    width=800,
                    height=50,
                    on_click=lambda e: self.hide_settings()
                ),
                
                ft.Container(height=15),
                
                # Кнопка "Выйти"
                ft.ElevatedButton(
                    self.t('settings_exit'),
                    bgcolor=self.colors['danger'],
                    color="white",
                    width=800,
                    height=50,
                    on_click=lambda e: self.page.window.destroy()
                ),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO),
            padding=25,
            bgcolor=self.colors['bg_card'],
            border_radius=ft.border_radius.only(top_left=20, bottom_left=20),
            width=800,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                offset=ft.Offset(-5, 0),
            ),
        )
    
    def do_change_language(self, lang):
        # Используем общую функцию переключения языка, чтобы обновить глобальные LOCALES
        try:
            switch_language(lang, self)
        except Exception:
            # fallback: просто поменяем локаль у этого экземпляра
            self.lang = lang
            if hasattr(self, 'refresh_screen'):
                self.refresh_screen()
        self.settings_visible = True
    
    def do_change_theme(self, theme):
        self.theme = theme
        self.apply_theme()
        self.settings_visible = True
        self.refresh_screen()
    
    def toggle_settings(self):
        if self.settings_visible:
            self.hide_settings()
        else:
            self.show_settings()
    
    def show_settings(self):
        self.settings_visible = True
        self.refresh_screen()
    
    def hide_settings(self):
        self.settings_visible = False
        self.refresh_screen()
    
    def refresh_screen(self):
        screens = {
            'welcome': self.show_welcome,
            'params': self.show_params,
            'goal': self.show_goal,
            'focus': self.show_focus,
            'safety': self.show_safety,
            'nutrition': self.show_nutrition,
            'result': self.show_result,
            'workout': self.show_workout,
            'progress': self.show_progress,
            'diary': self.show_diary,
        }
        handler = screens.get(self.current_screen, self.show_welcome)
        handler()
    
    def build_page(self, content):
        self.page.controls.clear()
        
        # Основной контент со скроллом
        content_column = ft.Column([
            self.build_top_bar(),
            ft.Container(
                content=ft.Column([content], scroll=ft.ScrollMode.AUTO, expand=True),
                expand=True,
            ),
        ], spacing=0, expand=True)
        
        # Если тёмная тема - накладываем контент поверх фона
        if self.theme == 'dark':
            # Фон на весь экран
            bg_container = ft.Container(
                content=ft.Image(
                    src="/bg_dark.png",
                    fit="cover",
                    width=2000,
                    height=2000,
                ),
                left=0,
                right=0,
                top=0,
                bottom=0,
            )
            main_content = ft.Stack([
                bg_container,
                ft.Container(
                    content=content_column,
                    expand=True,
                ),
            ], expand=True)
        else:
            bg_container = ft.Container(
                content=ft.Image(
                    src="/bg_light.webp",
                    fit="cover",
                    width=2000,
                    height=2000,
                ),
                left=0,
                right=0,
                top=0,
                bottom=0,
            )
            main_content = ft.Stack([
                bg_container,
                ft.Container(
                    content=content_column,
                    expand=True,
                ),
            ], expand=True)
        
        # Если настройки открыты - показываем справа (выдвигающаяся панель)
        if self.settings_visible:
            # Затемнение фона при открытых настройках
            overlay = ft.Container(
                bgcolor=ft.Colors.with_opacity(0.5, ft.Colors.BLACK),
                expand=True,
                on_click=lambda e: self.hide_settings(),
            )
            
            # Панель настроек справа
            settings_panel = ft.Container(
                content=self.build_settings_panel(),
                right=0,
                top=0,
                bottom=0,
            )
            
            page_content = ft.Stack([
                main_content,
                overlay,
                settings_panel,
            ], expand=True)
        else:
            page_content = main_content
        
        self.page.add(page_content)
        self.page.update()
    
    # ============== ЭКРАН ПРИВЕТСТВИЯ ==============
    def show_welcome(self):

        self.current_screen = 'welcome'
        
        # Градиенты для карточек
        male_gradient = ['#667eea', '#764ba2']
        female_gradient = ['#f093fb', '#f5576c']
        
        content = ft.Container(
            content=ft.Column([
                ft.Container(height=20),
                
                # Заголовок — убрали эмодзи, сделали аккуратный светящийся заголовок
                ft.Container(
                    content=self.create_glow_text(self.t('welcome'), size=36, color=self.colors['primary']),
                    animate_opacity=ft.Animation(500, ft.AnimationCurve.EASE_OUT),
                ),
                ft.Text(self.t('welcome_subtitle'),
                       size=15, color=self.colors['text_secondary'],
                       text_align=ft.TextAlign.CENTER),
                ft.Container(
                    content=ft.Text(self.t('motivation_text'),
                           size=13, italic=True, color=self.colors['secondary'],
                           text_align=ft.TextAlign.CENTER),
                    animate_opacity=ft.Animation(600, ft.AnimationCurve.EASE_OUT),
                ),
                
                ft.Container(height=20),
                
                # Две карточки в ряд
                ft.Row([
                    # Карточка мужчина
                    ft.Container(
                        content=ft.Stack([
                            ft.Container(
                                content=ft.Image(
                                    src="/male.jpg",
                                    fit="cover",
                                ),
                                width=280,
                                height=380,
                                border_radius=16,
                                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                            ),
                            ft.Container(
                                content=ft.Text(
                                    self.t('male'),
                                    size=24,
                                    weight=ft.FontWeight.BOLD,
                                    color="white",
                                ),
                                bottom=20,
                                left=0,
                                right=0,
                                alignment=ft.Alignment(0, 0),
                            ),
                        ]),
                        width=280,
                        height=380,
                        border_radius=16,
                        border=ft.border.all(3, "#8B5CF6"),
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        on_click=lambda e: self.select_gender("male"),
                        scale=1,
                        animate_scale=ft.Animation(150, ft.AnimationCurve.EASE_OUT),
                        on_hover=lambda e: self._on_card_hover(e),
                    ),
                    
                    # Карточка женщина
                    ft.Container(
                        content=ft.Stack([
                            ft.Container(
                                content=ft.Image(
                                    src="/female.png",
                                    fit="cover",
                                ),
                                width=280,
                                height=380,
                                border_radius=16,
                                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                            ),
                            ft.Container(
                                content=ft.Text(
                                    self.t('female'),
                                    size=24,
                                    weight=ft.FontWeight.BOLD,
                                    color="white",
                                ),
                                bottom=20,
                                left=0,
                                right=0,
                                alignment=ft.Alignment(0, 0),
                            ),
                        ]),
                        width=280,
                        height=380,
                        border_radius=16,
                        border=ft.border.all(3, "#8B5CF6"),
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        on_click=lambda e: self.select_gender("female"),
                        scale=1,
                        animate_scale=ft.Animation(150, ft.AnimationCurve.EASE_OUT),
                        on_hover=lambda e: self._on_card_hover(e),
                    ),
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                
                ft.Container(height=25),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=ft.Padding.symmetric(horizontal=20),
        )
        
        self.build_page(content)
    
    def select_gender(self, gender):
        self.user_data = {'gender': gender}
        self.program_data = None
        self.completed_workouts = set()
        self.completed_rest_days = set()
        self.workout_history = []
        self.show_params()
    
    # ============== ЭКРАН ПАРАМЕТРОВ ==============
    def show_params(self):
        self.current_screen = 'params'
        
        # Поля ввода - компактные
        self.height_field = ft.TextField(
            label=f"📏 {self.t('height')} ({self.t('cm')})",
            keyboard_type=ft.KeyboardType.NUMBER,
            width=500,
            height=50,
            border_radius=10,
            border_color=self.colors['border'],
            focused_border_color=self.colors['primary'],
            text_style=ft.TextStyle(color=self.colors['text'], size=13),
            label_style=ft.TextStyle(color=self.colors['text_secondary'], size=11),
        )
        self.weight_field = ft.TextField(
            label=f"⚖️ {self.t('weight')} ({self.t('kg')})",
            keyboard_type=ft.KeyboardType.NUMBER,
            width=500,
            height=50,
            border_radius=10,
            border_color=self.colors['border'],
            focused_border_color=self.colors['primary'],
            text_style=ft.TextStyle(color=self.colors['text'], size=13),
            label_style=ft.TextStyle(color=self.colors['text_secondary'], size=11),
        )
        self.age_field = ft.TextField(
            label=f"🎂 {self.t('age')} ({self.t('years')})",
            keyboard_type=ft.KeyboardType.NUMBER,
            width=500,
            height=50,
            border_radius=10,
            border_color=self.colors['border'],
            focused_border_color=self.colors['primary'],
            text_style=ft.TextStyle(color=self.colors['text'], size=13),
            label_style=ft.TextStyle(color=self.colors['text_secondary'], size=11),
        )
        
        self.days_dropdown = ft.Dropdown(
            label=self.t('days_per_week'),
            width=500,
            height=50,
            options=[
                ft.dropdown.Option("3", "3"),
                ft.dropdown.Option("4", "4"),
            ],
            value="3",
            border_radius=10,
            border_color=self.colors['border'],
            focused_border_color=self.colors['primary'],
            text_style=ft.TextStyle(color=self.colors['text'], size=13),
            label_style=ft.TextStyle(color=self.colors['text_secondary'], size=11),
        )
        
        self.level_dropdown = ft.Dropdown(
            label=self.t('level'),
            width=500,
            height=50,
            options=[
                ft.dropdown.Option("beginner", self.t('beginner')),
                ft.dropdown.Option("intermediate", self.t('intermediate')),
                ft.dropdown.Option("advanced", self.t('advanced')),
            ],
            value="beginner",
            border_radius=10,
            border_color=self.colors['border'],
            focused_border_color=self.colors['primary'],
            text_style=ft.TextStyle(color=self.colors['text'], size=13),
            label_style=ft.TextStyle(color=self.colors['text_secondary'], size=11),
        )
        
        self.error_text = ft.Text("", color=self.colors['danger'], size=11)
        
        content = ft.Container(
            content=ft.Column([
                ft.Container(height=10),
                ft.Text(self.t('enter_data'), size=16, weight=ft.FontWeight.BOLD,
                       color=self.colors['text']),
                ft.Container(height=12),
                
                self.height_field,
                ft.Text(f"120-250 {self.t('cm')}", size=9, color=self.colors['text_secondary']),
                ft.Container(height=4),
                self.weight_field,
                ft.Text(f"40-200 {self.t('kg')}", size=9, color=self.colors['text_secondary']),
                ft.Container(height=4),
                self.age_field,
                ft.Text(f"14-80 {self.t('years')}", size=9, color=self.colors['text_secondary']),
                
                ft.Container(height=10),
                
                self.days_dropdown,
                ft.Container(height=6),
                self.level_dropdown,
                
                ft.Container(height=6),
                self.error_text,
                
                ft.Container(height=12),
                
                ft.ElevatedButton(
                    self.t('continue_btn'),
                    bgcolor=self.colors['primary'],
                    color="white",
                    width=300,
                    height=42,
                    style=ft.ButtonStyle(
                        text_style=ft.TextStyle(size=13),
                        shape=ft.RoundedRectangleBorder(radius=12)
                    ),
                    on_click=self.validate_params
                ),
                
                ft.Container(height=6),
                
                ft.TextButton(
                    self.t('back_btn'),
                    on_click=lambda e: self.show_welcome()
                ),
                
                ft.Container(height=10),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=0),
            padding=ft.Padding.symmetric(horizontal=15),
        )
        
        self.build_page(content)
    
    def validate_params(self, e):
        try:
            height = int(self.height_field.value) if self.height_field.value else 0
            weight = int(self.weight_field.value) if self.weight_field.value else 0
            age = int(self.age_field.value) if self.age_field.value else 0
            
            if height == 0:
                self.error_text.value = self.t('error_height')
            elif weight == 0:
                self.error_text.value = self.t('error_weight')
            elif age == 0:
                self.error_text.value = self.t('error_age')
            elif height < 120 or height > 250:
                self.error_text.value = self.t('error_height_range')
            elif weight < 40 or weight > 200:
                self.error_text.value = self.t('error_weight_range')
            elif age < 14 or age > 80:
                self.error_text.value = self.t('error_age_range')
            else:
                self.user_data['height'] = height
                self.user_data['weight'] = weight
                self.user_data['age'] = age
                self.user_data['days'] = int(self.days_dropdown.value)
                self.user_data['level'] = self.level_dropdown.value
                self.show_goal()
                return
            
            self.page.update()
        except:
            self.error_text.value = self.t('error_height')
            self.page.update()
    
    # ============== ЭКРАН ВЫБОРА ЦЕЛИ ==============
    def show_goal(self):
        self.current_screen = 'goal'

        # Карточки по образцу выбора пола (шире чуть)
        card_w = 320
        card_h = 380

        # Карточка Сброс веса
        weight_card = ft.Container(
            content=ft.Stack([
                ft.Container(
                    content=ft.Image(src="/bg_dark.png", fit="cover"),
                    width=card_w,
                    height=card_h,
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Container(height=18),
                        ft.Text(self.t('weight_loss'), size=22, weight=ft.FontWeight.BOLD, color="white"),
                    ]),
                    left=18,
                    top=18,
                ),
                ft.Container(
                    content=ft.Image(src="/vesovaya_cropped.png", fit="contain", width=300, height=240),
                    right=-40,
                    bottom=-14,
                ),
            ]),
            width=card_w,
            height=card_h,
            border_radius=16,
            border=ft.border.all(3, "#10B981"),
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            on_click=lambda e: self.select_goal("weight_loss"),
            on_hover=lambda e: self._on_card_hover(e),
        )

        # Карточка Набор массы
        mass_card = ft.Container(
            content=ft.Stack([
                ft.Container(
                    content=ft.Image(src="/bg_dark.png", fit="cover"),
                    width=card_w,
                    height=card_h,
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Container(height=18),
                        ft.Text(self.t('muscle_gain'), size=22, weight=ft.FontWeight.BOLD, color="white"),
                    ]),
                    left=18,
                    top=18,
                ),
                ft.Container(
                    content=ft.Image(src="/muskul.png", fit="contain", width=160, height=140),
                    right=6,
                    bottom=6,
                ),
            ]),
            width=card_w,
            height=card_h,
            border_radius=16,
            border=ft.border.all(3, "#8B5CF6"),
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            on_click=lambda e: self.select_goal("muscle_gain"),
            on_hover=lambda e: self._on_card_hover(e),
        )

        content = ft.Container(
            content=ft.Column([
                ft.Container(height=12),
                ft.Text(self.t('choose_goal'), size=28, weight=ft.FontWeight.BOLD, color=self.colors['text']),
                ft.Text(self.t('goal_subtitle'), size=14, color=self.colors['text_secondary']),
                ft.Container(height=18),
                ft.Row([weight_card, mass_card], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                ft.Container(height=20),
                ft.TextButton(self.t('back_btn'), on_click=lambda e: self.show_params()),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=ft.Padding.symmetric(horizontal=20),
        )

        self.build_page(content)
    
    def select_goal(self, goal):
        self.user_data['goal'] = goal
        # Рассчитываем оптимальное количество недель по биометрии
        self.calculate_weeks()
        if goal == 'weight_loss':
            self.user_data['focus'] = 'Weight Loss'
            self.show_safety()
        else:
            self.show_focus()
    
    # ============== ЭКРАН ВЫБОРА ЗОНЫ ==============
    def show_focus(self):
        self.current_screen = 'focus'
        
        def select_zone(zone):
            self.selected_zones = {zone}
            self.show_focus()
        
        def get_zone_btn(text, zone_key, top, left):
            is_selected = zone_key in self.selected_zones
            return ft.Container(
                content=ft.Text(
                    text,
                    size=11,
                    weight=ft.FontWeight.BOLD,
                    color="white" if is_selected else self.colors['text'],
                ),
                padding=ft.Padding(left=12, right=12, top=6, bottom=6),
                border_radius=15,
                bgcolor="#8B5CF6" if is_selected else self.colors['bg_card'],
                border=ft.border.all(2, "#8B5CF6"),
                on_click=lambda e, z=zone_key: select_zone(z),
                top=top,
                left=left,
            )
        
        # Точка на теле
        def dot(top, left):
            return ft.Container(width=10, height=10, bgcolor="#3B82F6", border_radius=5, top=top, left=left)
        
        # Горизонтальная линия (сплошная)
        def line_h(top, left, width):
            return ft.Container(width=width, height=2, bgcolor="#3B82F6", top=top, left=left)
        
        # Вертикальная линия (сплошная)
        def line_v(top, left, height):
            return ft.Container(width=2, height=height, bgcolor="#3B82F6", top=top, left=left)
        
        # Картинка тела с кнопками
        body_stack = ft.Stack([
            # Картинка тела по центру
            ft.Container(
                content=ft.Image(
                    src="/ТЕЛЛОЛ.png",
                    fit="contain",
                    height=400,
                ),
                left=80,
                top=60,
            ),
            
            # === ВСЕ ГРУППЫ МЫШЦ (сверху) - без линии ===
            get_zone_btn(self.t('all_muscles'), "Full Body", top=5, left=110),
            
            # === ГРУДЬ (слева) ===
            get_zone_btn(self.t('chest_zone'), "Chest", top=120, left=5),
            line_h(top=135, left=70, width=80),  # линия вправо
            line_v(top=135, left=148, height=30),  # линия вниз
            line_h(top=163, left=148, width=45),  # линия вправо к точке
            dot(top=158, left=188),  # точка на груди
            
            # === РУКИ (справа) ===
            get_zone_btn(self.t('arms_zone'), "Arms", top=100, left=305),
            line_h(top=115, left=260, width=45),  # линия влево
            line_v(top=108, left=260, height=7),  # линия вниз к точке
            dot(top=108, left=255),  # точка на бицепсе
            
            # === ПРЕСС (слева) ===
            get_zone_btn(self.t('core_zone'), "Core", top=215, left=5),
            line_h(top=230, left=70, width=30),  # линия вправо от кнопки
            line_v(top=195, left=100, height=35),  # линия вверх
            line_h(top=195, left=100, width=120),  # линия вправо к точке
            dot(top=190, left=215),  # точка на прессе (вправо и вверх)
            
            # === НОГИ (справа) ===
            get_zone_btn(self.t('legs_zone'), "Legs", top=355, left=305),
            line_h(top=370, left=265, width=40),  # линия влево
            line_v(top=300, left=265, height=70),  # линия вверх к точке
            dot(top=292, left=260),  # точка на шортах (вправо и вверх)
            
        ], width=390, height=450)
        
        content = ft.Container(
            content=ft.Column([
                # Заголовок
                ft.Text(
                    self.t('focus_question'),
                    size=18,
                    weight=ft.FontWeight.BOLD,
                    color=self.colors['text'],
                    text_align=ft.TextAlign.CENTER,
                ),
                
                body_stack,
                
                # Кнопки внизу
                ft.Row([
                    ft.Container(
                        content=ft.Text(self.t('continue_btn').replace(' →', ''), size=14, weight=ft.FontWeight.BOLD, color="white"),
                        padding=ft.Padding(left=30, right=30, top=12, bottom=12),
                        border_radius=25,
                        bgcolor="#3B82F6",
                        on_click=lambda e: self.select_focus(list(self.selected_zones)[0] if self.selected_zones else "Full Body"),
                    ),
                    ft.Container(
                        content=ft.Text(self.t('back_btn').replace('← ', ''), size=14, weight=ft.FontWeight.BOLD, color=self.colors['text']),
                        padding=ft.Padding(left=30, right=30, top=12, bottom=12),
                        border_radius=25,
                        bgcolor=self.colors['bg_card'],
                        border=ft.border.all(2, self.colors['border']),
                        on_click=lambda e: self.show_goal(),
                    ),
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=15),
                
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
            padding=ft.Padding.symmetric(horizontal=15),
        )
        
        self.build_page(content)
    
    def _on_zone_hover(self, e):
        if e.data == "true":
            e.control.scale = 1.08
        else:
            e.control.scale = 1.0
        e.control.update()
    
    def select_focus(self, focus):
        self.user_data['focus'] = focus
        self.show_safety()
    
    # ============== ЭКРАН БЕЗОПАСНОСТИ ==============
    def show_safety(self):
        self.current_screen = 'safety'
        
        age = self.user_data.get('age', 25)
        
        warnings = []
        
        if age >= 60:
            warnings.append(ft.Container(
                content=ft.Column([
                    ft.Text(self.t('safety_60plus'), size=15, weight=ft.FontWeight.BOLD,
                           color=self.colors['danger']),
                    ft.Text(self.t('safety_60_1'), size=12, color=self.colors['text']),
                    ft.Text(self.t('safety_60_2'), size=12, color=self.colors['text']),
                    ft.Text(self.t('safety_60_3'), size=12, color=self.colors['text']),
                ], spacing=4),
                padding=14,
                border_radius=12,
                bgcolor=self.colors['bg_card'],
                border=ft.border.all(1, self.colors['danger']),
            ))
        elif age >= 50:
            warnings.append(ft.Container(
                content=ft.Column([
                    ft.Text(self.t('safety_50plus'), size=15, weight=ft.FontWeight.BOLD,
                           color=self.colors['warning']),
                    ft.Text(self.t('safety_50_1'), size=12, color=self.colors['text']),
                    ft.Text(self.t('safety_50_2'), size=12, color=self.colors['text']),
                    ft.Text(self.t('safety_50_3'), size=12, color=self.colors['text']),
                ], spacing=4),
                padding=14,
                border_radius=12,
                bgcolor=self.colors['bg_card'],
                border=ft.border.all(1, self.colors['warning']),
            ))
        elif age < 18:
            warnings.append(ft.Container(
                content=ft.Column([
                    ft.Text(self.t('safety_teen'), size=15, weight=ft.FontWeight.BOLD,
                           color=self.colors['success']),
                    ft.Text(self.t('safety_teen_1'), size=12, color=self.colors['text']),
                    ft.Text(self.t('safety_teen_2'), size=12, color=self.colors['text']),
                    ft.Text(self.t('safety_teen_3'), size=12, color=self.colors['text']),
                ], spacing=4),
                padding=14,
                border_radius=12,
                bgcolor=self.colors['bg_card'],
                border=ft.border.all(1, self.colors['success']),
            ))
        
        warnings.append(ft.Container(
            content=ft.Column([
                ft.Text(self.t('safety_general'), size=15, weight=ft.FontWeight.BOLD,
                       color=self.colors['primary']),
                ft.Text(self.t('safety_gen_1'), size=12, color=self.colors['text']),
                ft.Text(self.t('safety_gen_2'), size=12, color=self.colors['text']),
                ft.Text(self.t('safety_gen_3'), size=12, color=self.colors['text']),
            ], spacing=4),
            padding=14,
            border_radius=12,
            bgcolor=self.colors['bg_card'],
            border=ft.border.all(1, self.colors['primary']),
        ))
        
        self.agree_checkbox = ft.Checkbox(
            label=self.t('safety_agree'),
            value=False,
            check_color="white",
            fill_color=self.colors['success'],
        )
        
        content = ft.Container(
            content=ft.Column([
                ft.Container(height=15),
                ft.Text(self.t('safety_title'), size=22, weight=ft.FontWeight.BOLD,
                       color=self.colors['warning']),
                ft.Text(self.t('safety_subtitle'), size=13, color=self.colors['text_secondary']),
                ft.Container(height=15),
                
                *warnings,
                
                ft.Container(height=15),
                ft.Container(
                    content=ft.Row(
                        [self.agree_checkbox],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    width=float("inf"),
                ),
                ft.Container(height=15),
                
                ft.ElevatedButton(
                    self.t('continue_btn'),
                    bgcolor=self.colors['primary'],
                    color="white",
                    width=800,
                    height=48,
                    on_click=self.check_safety_agree
                ),
                
                ft.Container(height=10),
                
                ft.TextButton(
                    self.t('back_btn'),
                    on_click=lambda e: self.show_goal() if self.user_data.get('goal') == 'weight_loss' else self.show_focus()
                ),
                
                ft.Container(height=15),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
            padding=ft.Padding.symmetric(horizontal=20),
        )
        
        self.build_page(content)
    
    def check_safety_agree(self, e):
        if self.agree_checkbox.value:
            self.show_nutrition()
        else:
            self.page.snack_bar = ft.SnackBar(
                ft.Text(self.t('safety_confirm_error'), color="white"),
                bgcolor=self.colors['warning']
            )
            self.page.snack_bar.open = True
            self.page.update()
    
    # ============== ЭКРАН ПИТАНИЯ ==============
    def show_nutrition(self):
        self.current_screen = 'nutrition'
        
        nutrition = self.calculate_nutrition()
        
        goal = self.user_data.get('goal', 'weight_loss')
        goal_emoji = "📉" if goal == 'weight_loss' else "📈"
        goal_text = self.t('goal_weight_loss') if goal == 'weight_loss' else self.t('goal_muscle_gain')
        
        content = ft.Container(
            content=ft.Column([
                ft.Container(height=15),
                ft.Text(self.t('nutrition_title'), size=22, weight=ft.FontWeight.BOLD,
                       color=self.colors['text']),
                ft.Container(height=15),
                
                # Калории
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Text(goal_emoji, size=28),
                            ft.Text(goal_text, size=16, weight=ft.FontWeight.BOLD,
                                   color=self.colors['text']),
                        ], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Text(f"{nutrition['calories']}", size=44, weight=ft.FontWeight.BOLD,
                               color=self.colors['primary']),
                        ft.Text(self.t('kcal_day'), size=13, color=self.colors['text_secondary']),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                    padding=22,
                    border_radius=18,
                    bgcolor=self.colors['bg_card'],
                    width=800,
                ),
                
                ft.Container(height=15),
                
                # БЖУ
                ft.Container(
                    content=ft.Row([
                        ft.Container(
                            content=ft.Column([
                                ft.Text("🥩", size=24),
                                ft.Text(self.t('protein'), size=9, color=self.colors['text_secondary']),
                                ft.Text(f"{nutrition['protein']}{self.t('g')}", size=15, weight=ft.FontWeight.BOLD,
                                       color=self.colors['primary']),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2),
                            padding=10,
                            border_radius=12,
                            bgcolor=self.colors['bg_card'],
                            width=85,
                        ),
                        ft.Container(
                            content=ft.Column([
                                ft.Text("🥑", size=24),
                                ft.Text(self.t('fats'), size=9, color=self.colors['text_secondary']),
                                ft.Text(f"{nutrition['fat']}{self.t('g')}", size=15, weight=ft.FontWeight.BOLD,
                                       color=self.colors['warning']),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2),
                            padding=10,
                            border_radius=12,
                            bgcolor=self.colors['bg_card'],
                            width=85,
                        ),
                        ft.Container(
                            content=ft.Column([
                                ft.Text("🍞", size=24),
                                ft.Text(self.t('carbs'), size=9, color=self.colors['text_secondary']),
                                ft.Text(f"{nutrition['carbs']}{self.t('g')}", size=15, weight=ft.FontWeight.BOLD,
                                       color=self.colors['success']),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2),
                            padding=10,
                            border_radius=12,
                            bgcolor=self.colors['bg_card'],
                            width=85,
                        ),
                    ], spacing=8, alignment=ft.MainAxisAlignment.CENTER),
                    width=800,
                ),
                
                ft.Container(height=15),
                
                # Персональные рекомендации по питанию
                ft.Container(
                    content=ft.Column([
                        ft.Text(self.t('nutrition_tips'), size=13, weight=ft.FontWeight.BOLD,
                               color=self.colors['text']),
                        ft.Text(f"💧 {self.t('rec_water_daily').replace('{amount}', str(round(self.user_data.get('weight', 70) * 33 / 1000, 1)))}",
                               size=11, color=self.colors['text_secondary']),
                        ft.Text(f"🕐 {self.t('rec_meal_count').replace('{count}', str(nutrition.get('meals_count', 5)))}",
                               size=11, color=self.colors['text_secondary']),
                        ft.Text(f"⏰ {self.t('rec_meal_pre_workout')}",
                               size=11, color=self.colors['text_secondary']),
                        ft.Text(f"🍽️ {self.t('rec_meal_post_workout')}",
                               size=11, color=self.colors['text_secondary']),
                        ft.Text(f"🌙 {self.t('rec_meal_evening')}",
                               size=11, color=self.colors['text_secondary']),
                        ft.Text(f"💡 {self.t('rec_meal_tip_loss') if goal == 'weight_loss' else self.t('rec_meal_tip_gain')}",
                               size=11, color=self.colors['text_secondary']),
                    ], spacing=4),
                    padding=18,
                    border_radius=14,
                    bgcolor=self.colors['bg_card'],
                    width=800,
                ),
                
                ft.Container(height=20),
                
                ft.ElevatedButton(
                    self.t('to_program'),
                    bgcolor=self.colors['primary'],
                    color="white",
                    width=280,
                    height=48,
                    on_click=lambda e: self.generate_and_show_program()
                ),
                
                ft.Container(height=10),
                
                ft.TextButton(
                    self.t('back_btn'),
                    on_click=lambda e: self.show_safety()
                ),
                
                ft.Container(height=15),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=ft.Padding.symmetric(horizontal=20),
        )
        
        self.build_page(content)
    
    def calculate_weeks(self):
        """Рассчитывает оптимальное количество недель программы по биометрии"""
        weight = self.user_data.get('weight', 70)
        height = self.user_data.get('height', 175)
        age = self.user_data.get('age', 25)
        goal = self.user_data.get('goal', 'weight_loss')
        level = self.user_data.get('level', 'beginner')
        days = self.user_data.get('days', 3)
        
        bmi = weight / ((height / 100) ** 2)
        
        if goal == 'weight_loss':
            # Чем выше ИМТ — тем дольше программа
            if bmi >= 35:
                base_weeks = 12       # ожирение 2+ степени
            elif bmi >= 30:
                base_weeks = 10       # ожирение 1 степени
            elif bmi >= 27:
                base_weeks = 8        # предожирение с запасом
            elif bmi >= 25:
                base_weeks = 6        # лёгкий лишний вес
            else:
                base_weeks = 5        # ИМТ в норме, сушка/рельеф
        else:
            # Набор массы
            if bmi < 18.5:
                base_weeks = 10       # дефицит массы — долго набирать
            elif bmi < 22:
                base_weeks = 8        # худощавый
            elif bmi < 25:
                base_weeks = 6        # норма
            else:
                base_weeks = 5        # уже есть масса
        
        # Корректировка по возрасту (после 40 метаболизм замедляется)
        if age >= 50:
            base_weeks += 2
        elif age >= 40:
            base_weeks += 1
        
        # Корректировка по уровню подготовки
        if level == 'beginner':
            base_weeks += 1  # новичкам нужно больше адаптации
        elif level == 'advanced':
            base_weeks = max(4, base_weeks - 1)  # опытным быстрее
        
        # Корректировка по частоте тренировок
        if days <= 2:
            base_weeks += 2  # мало тренировок — дольше
        elif days >= 5:
            base_weeks = max(4, base_weeks - 1)  # часто — быстрее
        
        # Ограничения: 4-16 недель
        weeks = max(4, min(16, base_weeks))
        
        self.user_data['weeks'] = weeks
        return weeks
    
    def calculate_nutrition(self):
        gender = self.user_data.get('gender', 'male')
        age = self.user_data.get('age', 25)
        weight = self.user_data.get('weight', 70)
        height = self.user_data.get('height', 175)
        goal = self.user_data.get('goal', 'weight_loss')
        days = self.user_data.get('days', 3)
        
        # Формула Миффлина-Сан Жеора (BMR)
        if gender == 'male':
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161
        
        # Более точный коэффициент активности
        if days <= 2:
            activity = 1.2       # минимальная активность
        elif days == 3:
            activity = 1.375     # лёгкая активность
        elif days <= 5:
            activity = 1.55      # умеренная активность
        else:
            activity = 1.725     # высокая активность
        
        tdee = int(bmr * activity)
        
        # ИМТ
        bmi = weight / ((height / 100) ** 2)
        
        if goal == 'weight_loss':
            # Дефицит зависит от ИМТ: чем выше ИМТ, тем больше можно дефицит
            if bmi >= 30:
                deficit = 600
            elif bmi >= 27:
                deficit = 500
            else:
                deficit = 400
            calories = max(1200 if gender == 'female' else 1500, int(tdee - deficit))
            protein = int(weight * 1.8)
            fat = int(weight * 0.8)
        else:
            # Профицит зависит от уровня
            level = self.user_data.get('level', 'beginner')
            if level == 'beginner':
                surplus = 350   # новички растут быстрее
            elif level == 'intermediate':
                surplus = 250
            else:
                surplus = 200   # опытным нужен меньший профицит
            calories = int(tdee + surplus)
            protein = int(weight * 2.0)
            fat = int(weight * 1.0)
        
        protein_cal = protein * 4
        fat_cal = fat * 9
        carbs_cal = max(0, calories - protein_cal - fat_cal)
        carbs = int(carbs_cal / 4)
        
        # Расчёт воды (мл): 30-35 мл/кг + тренировки
        water_base = int(weight * 33)  # средний показатель 33 мл/кг
        water_training = 500  # доп. 500 мл в дни тренировок
        if age >= 50:
            water_base = int(weight * 30)  # пожилым чуть меньше
        
        # Количество приёмов пищи
        if goal == 'weight_loss':
            meals = 4 if calories < 2000 else 5
        else:
            meals = 5 if calories < 2800 else 6
        
        nutrition = {
            'calories': calories,
            'protein': protein,
            'fat': fat,
            'carbs': carbs,
            'tdee': tdee,
            'bmr': int(bmr),
            'bmi': round(bmi, 1),
            'water_base_ml': water_base,
            'water_training_ml': water_base + water_training,
            'meals_count': meals,
            'deficit_or_surplus': -deficit if goal == 'weight_loss' else surplus,
        }
        
        self.user_data['nutrition_plan'] = nutrition
        return nutrition
    
    # ============== ГЕНЕРАТОР ПРОГРАММЫ ==============
    def generate_and_show_program(self):
        self.program_data = self.generate_program()
        self.show_result()
    
    def generate_recommendations(self):
        goal = self.user_data.get('goal', 'weight_loss')
        level = self.user_data.get('level', 'beginner')
        days = self.user_data.get('days', 3)
        weight = self.user_data.get('weight', 70)
        height = self.user_data.get('height', 175)
        age = self.user_data.get('age', 25)
        gender = self.user_data.get('gender', 'male')
        nutrition = self.user_data.get('nutrition_plan', {})
        
        bmi = weight / ((height / 100) ** 2)
        
        recs = {}
        
        # === ВОДА ===
        water_base = nutrition.get('water_base_ml', int(weight * 33))
        water_train = nutrition.get('water_training_ml', water_base + 500)
        water_liters = round(water_base / 1000, 1)
        water_train_liters = round(water_train / 1000, 1)
        recs['water_daily'] = self.t('rec_water_daily').replace('{amount}', str(water_liters))
        recs['water_training'] = self.t('rec_water_training').replace('{amount}', str(water_train_liters))
        recs['water_why'] = self.t('rec_water_why').replace('{weight}', str(weight))
        recs['water_morning'] = self.t('rec_water_morning')
        
        # === ПИТАНИЕ ПО РАСПИСАНИЮ ===
        meals = nutrition.get('meals_count', 5)
        recs['meal_count'] = self.t('rec_meal_count').replace('{count}', str(meals))
        recs['meal_pre_workout'] = self.t('rec_meal_pre_workout')
        recs['meal_post_workout'] = self.t('rec_meal_post_workout')
        recs['meal_pre_detail'] = self.t('rec_meal_pre_detail')
        recs['meal_post_detail'] = self.t('rec_meal_post_detail')
        recs['meal_evening'] = self.t('rec_meal_evening')
        
        if goal == 'weight_loss':
            recs['meal_goal_tip'] = self.t('rec_meal_tip_loss')
        else:
            recs['meal_goal_tip'] = self.t('rec_meal_tip_gain')
        
        # === ТРЕНИРОВКИ ===
        if goal == 'weight_loss':
            recs['cardio'] = self.t('rec_cardio_weight_loss')
        else:
            recs['cardio'] = self.t('rec_cardio_muscle')
        
        rest_count = 7 - days
        recs['rest_days'] = self.t('rec_rest_days').replace('{count}', str(rest_count))
        
        if level == 'beginner':
            recs['duration'] = self.t('rec_duration_beginner')
        elif level == 'intermediate':
            recs['duration'] = self.t('rec_duration_intermediate')
        else:
            recs['duration'] = self.t('rec_duration_advanced')
        
        recs['warmup'] = self.t('rec_warmup')
        recs['progression'] = self.t('rec_progression')
        
        # === СОН И ВОССТАНОВЛЕНИЕ ===
        if level == 'advanced' or days >= 5:
            sleep_hours = '8-9'
        elif age >= 50:
            sleep_hours = '7-9'
        elif age < 18:
            sleep_hours = '9-10'
        else:
            sleep_hours = '7-8'
        recs['sleep_hours'] = self.t('rec_sleep_hours').replace('{hours}', sleep_hours)
        recs['sleep_schedule'] = self.t('rec_sleep_schedule')
        recs['sleep_recovery'] = self.t('rec_sleep_recovery')
        
        # === ОБРАЗ ЖИЗНИ ===
        recs['steps'] = self.t('rec_steps')
        recs['stretch'] = self.t('rec_stretch')
        if goal == 'weight_loss':
            recs['lifestyle_tip'] = self.t('rec_lifestyle_loss')
        else:
            recs['lifestyle_tip'] = self.t('rec_lifestyle_gain')
        
        # === ИМТ-персонализация ===
        if bmi < 18.5:
            recs['bmi_tip'] = self.t('rec_bmi_under')
        elif bmi < 25:
            recs['bmi_tip'] = self.t('rec_bmi_normal')
        elif bmi < 30:
            recs['bmi_tip'] = self.t('rec_bmi_over')
        else:
            recs['bmi_tip'] = self.t('rec_bmi_obese')
        
        # === ВОЗРАСТНЫЕ ===
        if age >= 50:
            recs['age_tip'] = self.t('rec_age_50plus')
        elif age < 18:
            recs['age_tip'] = self.t('rec_age_teen')
        
        return recs
    
    def generate_program(self):

        gender = self.user_data.get('gender', 'male')
        focus = self.user_data.get('focus', 'Full Body')
        level = self.user_data.get('level', 'beginner')
        days = self.user_data.get('days', 3)
        weeks = self.user_data.get('weeks', 5)
        age = self.user_data.get('age', 25)
        weight = self.user_data.get('weight', 70)
        height = self.user_data.get('height', 175)
        goal = self.user_data.get('goal', 'weight_loss')
        
        bmi = weight / ((height / 100) ** 2)
        
        if level == 'advanced':
            ex_count = 15
        elif level == 'intermediate':
            ex_count = 13
        else:
            ex_count = 11
        
        program = {
            'metadata': {
                'gender': gender,
                'focus': focus,
                'level': level,
                'days': days,
                'weeks': weeks,
                'age': age,
                'weight': weight,
                'height': height,
                'bmi': round(bmi, 1),
                'goal': goal,
                'created': datetime.datetime.now().strftime('%d.%m.%Y'),
            },
            'recommendations': self.generate_recommendations(),
            'schedule': []
        }
        
        weekday_keys = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        
        if days <= 3:
            training_weekdays = [0, 2, 4][:days]
        elif days == 4:
            training_weekdays = [0, 1, 3, 4]
        elif days == 5:
            training_weekdays = [0, 1, 2, 4, 5]
        else:
            training_weekdays = [0, 1, 2, 3, 4, 5][:days]
        
        for week_num in range(1, weeks + 1):
            week = {'week': week_num, 'days': []}
            
            for day_num in range(1, days + 1):
                if goal == 'weight_loss':
                    group = 'Weight Loss'
                else:
                    group = focus
                
                exercises = self.pick_exercises(group, ex_count, level, week_num, gender, age)
                
                if gender == 'female':
                    rest_between_sets = 15
                else:
                    rest_between_sets = 10
                
                if age >= 60:
                    rest_between_sets = int(rest_between_sets * 1.5)
                elif age >= 50:
                    rest_between_sets = int(rest_between_sets * 1.25)
                
                workout_exercises = []
                for i, ex in enumerate(exercises):
                    is_first = (i == 0)
                    sets, reps = self.calculate_sets_reps(ex, goal, level, week_num, is_first, gender, age, weight, height, bmi)
                    
                    workout_exercises.append({
                        'name': ex['name'],
                        'gif': ex.get('gif', ''),
                        'type': ex['type'],
                        'difficulty': ex['difficulty'],
                        'sets': sets,
                        'reps': reps,
                        'is_hold': ex.get('is_hold', False),
                        'rest_seconds': rest_between_sets,
                    })
                
                emoji_map = {
                    'Full Body': '🏋️', 'Legs': '🦵', 'Chest': '💪', 
                    'Back': '🔙', 'Arms': '💪', 'Shoulders': '🏋️',
                    'Core': '🎯', 'Weight Loss': '🔥'
                }
                
                wd_idx = training_weekdays[day_num - 1] if day_num - 1 < len(training_weekdays) else (day_num - 1) % 7
                
                day_data = {
                    'day': day_num,
                    'weekday_key': weekday_keys[wd_idx],
                    'weekday_idx': wd_idx,
                    'group': group,
                    'emoji': emoji_map.get(group, '💪'),
                    'exercises': workout_exercises,
                }
                week['days'].append(day_data)
            
            program['schedule'].append(week)
        
        return program
    
    def pick_exercises(self, group, count, level, week, gender, age):

        pool = EXERCISES.get(group, EXERCISES['Full Body'])
        
        if group == 'Weight Loss':
            if gender == 'female':
                female_exercises = [ex for ex in pool if ex.get('female_focused', False)]
                universal_exercises = [ex for ex in pool if not ex.get('male_focused', False) and not ex.get('female_focused', False)]
                pool = female_exercises + universal_exercises
            else:
                male_exercises = [ex for ex in pool if ex.get('male_focused', False)]
                universal_exercises = [ex for ex in pool if not ex.get('male_focused', False) and not ex.get('female_focused', False)]
                pool = male_exercises + universal_exercises
        
        elif group == 'Full Body':
            if gender == 'female':
                female_exercises = [ex for ex in pool if ex.get('female_focused', False)]
                other_exercises = [ex for ex in pool if not ex.get('female_focused', False) and not ex.get('male_focused', False)]
                pool = female_exercises + other_exercises
            else:
                male_exercises = [ex for ex in pool if ex.get('male_focused', False)]
                other_exercises = [ex for ex in pool if not ex.get('male_focused', False) and not ex.get('female_focused', False)]
                pool = male_exercises + other_exercises
        
        if level == 'beginner':
            suitable = [ex for ex in pool if ex['difficulty'] == 'beginner']
            if week > 2:
                intermediate = [ex for ex in pool if ex['difficulty'] == 'intermediate']
                suitable.extend(intermediate)
        elif level == 'intermediate':
            suitable = [ex for ex in pool if ex['difficulty'] in ['beginner', 'intermediate']]
        else:
            suitable = pool[:]
        
        if len(suitable) < count:
            for ex in pool:
                if ex not in suitable:
                    suitable.append(ex)
        
        random.seed(week * 100 + hash(group) + hash(gender))
        random.shuffle(suitable)
        result = suitable[:count]
        
        while len(result) < count and len(suitable) > 0:
            for ex in suitable:
                if len(result) >= count:
                    break
                result.append(ex.copy())
        
        return result
    
    def calculate_sets_reps(self, exercise, goal, level, week, is_first, gender, age, weight, height, bmi):

        
        if exercise.get('is_hold', False):
            base_time = 20 if level == 'beginner' else (30 if level == 'intermediate' else 40)
            progression = 1 + (week - 1) * 0.08
            reps = int(base_time * progression)
            reps = min(reps, 60)
            sets = 2
            if gender == 'female':
                sets = 2
            if age >= 60:
                reps = int(reps * 0.7)
            elif age >= 50:
                reps = int(reps * 0.85)
            
            return sets, reps
        
        ex_type = exercise.get('type', 'compound')
        
        if ex_type == 'compound':
            base_sets = 3
            if goal == 'muscle_gain':
                base_reps = 12 if level == 'advanced' else (10 if level == 'intermediate' else 8)
            elif goal == 'weight_loss':
                base_reps = 18 if level == 'advanced' else (15 if level == 'intermediate' else 12)
            else:
                base_reps = 10
        elif ex_type in ['core', 'hiit']:
            base_sets = 2
            base_reps = 25 if goal == 'weight_loss' else 20
        elif ex_type == 'cardio':
            base_sets = 1
            base_reps = 25 if goal == 'weight_loss' else 15
        else:
            base_sets = 2
            base_reps = 18 if goal == 'muscle_gain' else 22
        
        week_progression = (week - 1) // 2
        final_reps = base_reps + week_progression
        
        if week > 4 and level != 'beginner' and ex_type == 'compound':
            base_sets += 1
        
        if gender == 'female':
            base_sets = max(2, int(base_sets * 0.85))
            final_reps = int(final_reps * 1.15)
        
        if age < 18:
            base_sets = max(2, base_sets - 1)
            final_reps = max(6, int(final_reps * 0.9))
        elif age >= 60:
            base_sets = max(2, base_sets - 1)
            final_reps = max(5, int(final_reps * 0.7))
        elif age >= 50:
            final_reps = max(6, int(final_reps * 0.85))
        
        return base_sets, final_reps
    
    # ============== ЭКРАН РЕЗУЛЬТАТА ==============
    def show_result(self):
        self.current_screen = 'result'
        
        if not self.program_data:
            self.generate_and_show_program()
            return
        
        meta = self.program_data['metadata']
        # Регенерируем рекомендации для текущего языка
        recs = self.generate_recommendations()
        nutrition = self.user_data.get('nutrition_plan', {})
        
        # Информационная панель
        gender_text = self.t('male') if meta['gender'] == 'male' else self.t('female')
        focus_text = self.t(meta['focus'])
        level_text = self.t(meta['level'])
        goal_text = self.t('goal_weight_loss') if meta['goal'] == 'weight_loss' else self.t('goal_muscle_gain')
        
        info_panel = ft.Container(
                 content=ft.Column([
                  ft.Text(f"👤 {gender_text} | 🎯 {focus_text} | {level_text}",
                      size=12, color=self.colors['text']),
                  ft.Text(f"📊 {self.t('bmi')}: {meta['bmi']:.1f} → {goal_text}",
                      size=11, color=self.colors['text_secondary']),
                  ft.Text(f"📅 {meta['weeks']} {self.t('weeks')} • {meta['days']} {self.t('days')}",
                      size=11, color=self.colors['text_secondary']),
                 ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=3),
                 padding=14,
                 border_radius=12,
                 bgcolor=self.colors['bg_card'],
                 width=800,
        )
        
        # Карточка рекомендаций — полная с секциями
        def rec_section(icon, title, items):
            """Создаёт секцию рекомендаций с заголовком и пунктами"""
            section_items = [
                ft.Container(
                    content=ft.Text(f"{icon} {title}", size=13, weight=ft.FontWeight.BOLD,
                                   color=self.colors['primary']),
                    margin=ft.Margin(left=0, top=8, right=0, bottom=2),
                ),
            ]
            for item in items:
                section_items.append(
                    ft.Text(f"  • {item}", size=11, color=self.colors['text_secondary'])
                )
            return section_items
        
        # Собираем все секции рекомендаций
        all_rec_items = []
        
        # 💧 Вода
        water_items = [recs['water_daily'], recs['water_training'], recs['water_why'], recs['water_morning']]
        all_rec_items.extend(rec_section('💧', self.t('rec_water_title'), water_items))
        
        # 🕐 Режим питания
        meal_items = [recs['meal_count'], recs['meal_pre_workout'], recs['meal_pre_detail'],
                      recs['meal_post_workout'], recs['meal_post_detail'],
                      recs['meal_evening'], recs['meal_goal_tip']]
        all_rec_items.extend(rec_section('🕐', self.t('rec_meal_title'), meal_items))
        
        # 🏋️ Тренировки
        train_items = [recs['cardio'], recs['duration'], recs['rest_days'],
                       recs['warmup'], recs['progression']]
        all_rec_items.extend(rec_section('🏋️', self.t('rec_train_title'), train_items))
        
        # 😴 Сон
        sleep_items = [recs['sleep_hours'], recs['sleep_schedule'], recs['sleep_recovery']]
        all_rec_items.extend(rec_section('😴', self.t('rec_sleep_title'), sleep_items))
        
        # 🚶 Образ жизни
        lifestyle_items = [recs['steps'], recs['stretch'], recs['lifestyle_tip']]
        if recs.get('bmi_tip'):
            lifestyle_items.append(recs['bmi_tip'])
        if recs.get('age_tip'):
            lifestyle_items.append(recs['age_tip'])
        all_rec_items.extend(rec_section('🚶', self.t('rec_lifestyle_title'), lifestyle_items))
        
        rec_card = ft.Container(
            content=ft.Column([
                ft.Text(self.t('rec_title'), size=15, weight=ft.FontWeight.BOLD,
                       color=self.colors['text']),
                *all_rec_items,
            ], spacing=2),
            padding=16,
            border_radius=12,
            bgcolor=self.colors['bg_card'],
            width=800,
        )
        
        # Карточка питания — расширенная
        goal_emoji = "📉" if meta['goal'] == 'weight_loss' else "📈"
        delta = nutrition.get('deficit_or_surplus', 0)
        delta_text = f"{delta:+d} {self.t('kcal_day').lower()}"
        
        nutrition_card = ft.Container(
            content=ft.Column([
                ft.Text(self.t('nutrition_title'), size=15, weight=ft.FontWeight.BOLD,
                       color=self.colors['text']),
                ft.Container(height=5),
                # Калории
                ft.Row([
                    ft.Text(goal_emoji, size=22),
                    ft.Column([
                        ft.Text(f"{nutrition.get('calories', 0)} {self.t('kcal_day').lower()}",
                               size=18, weight=ft.FontWeight.BOLD, color=self.colors['primary']),
                        ft.Text(f"{goal_text} ({delta_text})",
                               size=10, color=self.colors['text_secondary']),
                    ], spacing=0),
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=8),
                ft.Container(height=5),
                # Макронутриенты
                ft.Row([
                    ft.Container(
                        content=ft.Column([
                            ft.Text("🥩", size=18),
                            ft.Text(f"{nutrition.get('protein', 0)}{self.t('g')}", size=13,
                                   weight=ft.FontWeight.BOLD, color=self.colors['text']),
                            ft.Text(self.t('protein'), size=9, color=self.colors['text_secondary']),
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=1),
                        padding=8, border_radius=10, bgcolor=self.colors['bg_hover'], expand=True,
                    ),
                    ft.Container(
                        content=ft.Column([
                            ft.Text("🥑", size=18),
                            ft.Text(f"{nutrition.get('fat', 0)}{self.t('g')}", size=13,
                                   weight=ft.FontWeight.BOLD, color=self.colors['text']),
                            ft.Text(self.t('fats'), size=9, color=self.colors['text_secondary']),
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=1),
                        padding=8, border_radius=10, bgcolor=self.colors['bg_hover'], expand=True,
                    ),
                    ft.Container(
                        content=ft.Column([
                            ft.Text("🍞", size=18),
                            ft.Text(f"{nutrition.get('carbs', 0)}{self.t('g')}", size=13,
                                   weight=ft.FontWeight.BOLD, color=self.colors['text']),
                            ft.Text(self.t('carbs'), size=9, color=self.colors['text_secondary']),
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=1),
                        padding=8, border_radius=10, bgcolor=self.colors['bg_hover'], expand=True,
                    ),
                ], spacing=8),
                ft.Container(height=5),
                # Доп. инфо: BMR и TDEE
                ft.Text(f"⚡ BMR: {nutrition.get('bmr', '—')} | TDEE: {nutrition.get('tdee', '—')} {self.t('kcal_day').lower()}",
                       size=10, color=self.colors['text_secondary'], text_align=ft.TextAlign.CENTER),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
            padding=16,
            border_radius=12,
            bgcolor=self.colors['bg_card'],
            width=800,
        )
        
        # Карточки дней
        day_cards = []
        global_day_num = 1
        
        weekday_keys = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        
        for week in self.program_data['schedule']:
            day_cards.append(ft.Container(
                content=ft.Text(f"══ {self.t('week').upper()} {week['week']} ══", 
                               size=13, weight=ft.FontWeight.BOLD,
                               color=self.colors['primary'], text_align=ft.TextAlign.CENTER),
                padding=10,
                bgcolor=self.colors['bg_card'],
                border_radius=8,
                width=800,
            ))
            
            training_by_weekday = {}
            for day_data in week['days']:
                wd_idx = day_data.get('weekday_idx', 0)
                training_by_weekday[wd_idx] = day_data
            
            for wd_idx in range(7):
                day_label = f"{self.t('day_num')} {global_day_num}"
                rest_key = (week['week'], wd_idx)
                
                if wd_idx in training_by_weekday:
                    day_data = training_by_weekday[wd_idx]
                    workout_key = (week['week'], day_data['day'])
                    is_completed = workout_key in self.completed_workouts
                    
                    prev_wd = wd_idx - 1
                    if prev_wd >= 0:
                        if prev_wd in training_by_weekday:
                            prev_training = training_by_weekday[prev_wd]
                            can_start = (week['week'], prev_training['day']) in self.completed_workouts
                        else:
                            can_start = (week['week'], prev_wd) in self.completed_rest_days
                    else:
                        if week['week'] == 1:
                            can_start = True
                        else:
                            can_start = (week['week'] - 1, 6) in self.completed_rest_days or any(
                                (week['week'] - 1, d['day']) in self.completed_workouts
                                for d in self.program_data['schedule'][week['week'] - 2]['days']
                                if d.get('weekday_idx', 0) == 6 or d.get('weekday_idx', 0) == max(
                                    dd.get('weekday_idx', 0) for dd in self.program_data['schedule'][week['week'] - 2]['days']
                                )
                            )
                    
                    is_first_ever = (global_day_num == 1)
                    if is_first_ever:
                        can_start = True
                    
                    if is_completed:
                        status_color = self.colors['success']
                        btn_text = "✅"
                        btn_disabled = True
                    elif can_start:
                        status_color = self.colors['primary']
                        btn_text = "▶️"
                        btn_disabled = False
                    else:
                        status_color = self.colors['text_secondary']
                        btn_text = "🔒"
                        btn_disabled = True
                    
                    ex_count = len(day_data['exercises'])
                    total_sets = sum([ex['sets'] for ex in day_data['exercises']])
                    group_name = self.t(day_data['group'])
                    
                    ex_list = ", ".join([self.t(ex['name'])[:12] for ex in day_data['exercises'][:3]])
                    if len(day_data['exercises']) > 3:
                        ex_list += f" +{len(day_data['exercises']) - 3}"
                    
                    day_cards.append(ft.Container(
                        content=ft.Row([
                            ft.Column([
                                ft.Text(f"📅 {day_label}",
                                       size=11, color=self.colors['primary'], weight=ft.FontWeight.BOLD),
                                ft.Text(f"{day_data['emoji']} {group_name}",
                                       size=14, weight=ft.FontWeight.BOLD,
                                       color=self.colors['text']),
                                ft.Text(ex_list,
                                       size=10, color=self.colors['text_secondary'],
                                       max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
                                ft.Text(f"📊 {ex_count} {self.t('exercises')} • {total_sets} {self.t('sets')}",
                                       size=10, color=status_color, weight=ft.FontWeight.BOLD),
                            ], spacing=2, expand=True),
                            ft.ElevatedButton(
                                btn_text,
                                bgcolor=status_color if not btn_disabled else self.colors['bg_hover'],
                                color="white" if not btn_disabled else self.colors['text_secondary'],
                                disabled=btn_disabled,
                                width=60,
                                height=38,
                                on_click=lambda e, w=week['week'], d=day_data: self.start_workout(w, d)
                            ),
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        padding=12,
                        border_radius=12,
                        bgcolor=self.colors['bg_card'],
                        border=ft.border.all(2, status_color),
                        width=800,
                    ))
                else:
                    is_rest_completed = rest_key in self.completed_rest_days
                    
                    prev_wd = wd_idx - 1
                    if prev_wd >= 0:
                        if prev_wd in training_by_weekday:
                            prev_training = training_by_weekday[prev_wd]
                            rest_unlocked = (week['week'], prev_training['day']) in self.completed_workouts
                        else:
                            rest_unlocked = (week['week'], prev_wd) in self.completed_rest_days
                    else:
                        if week['week'] == 1:
                            rest_unlocked = False
                        else:
                            prev_week_num = week['week'] - 1
                            rest_unlocked = (prev_week_num, 6) in self.completed_rest_days or any(
                                (prev_week_num, d['day']) in self.completed_workouts
                                for d in self.program_data['schedule'][prev_week_num - 1]['days']
                            )
                    
                    if global_day_num == 1:
                        rest_unlocked = True
                    
                    if is_rest_completed:
                        rest_color = self.colors['success']
                        rest_btn_widget = ft.Text("✅", size=24)
                    elif rest_unlocked:
                        rest_color = self.colors['primary']
                        rest_btn_widget = ft.ElevatedButton(
                            self.t('rest_btn'),
                            bgcolor=self.colors['primary'],
                            color="white",
                            width=100,
                            height=38,
                            on_click=lambda e, wk=week['week'], wi=wd_idx: self._do_rest(wk, wi)
                        )
                    else:
                        rest_color = self.colors['text_secondary']
                        rest_btn_widget = ft.Text("🔒", size=24)
                    
                    day_cards.append(ft.Container(
                        content=ft.Row([
                            ft.Column([
                                ft.Text(f"📅 {day_label}",
                                       size=11, color=rest_color, weight=ft.FontWeight.BOLD),
                                ft.Text(self.t('rest_day'),
                                       size=14, weight=ft.FontWeight.BOLD,
                                       color=self.colors['text_secondary']),
                            ], spacing=2, expand=True),
                            rest_btn_widget,
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        padding=12,
                        border_radius=12,
                        bgcolor=self.colors['bg_card'],
                        border=ft.border.all(2, rest_color),
                        width=800,
                        opacity=1.0 if (is_rest_completed or rest_unlocked) else 0.5,
                    ))
                
                global_day_num += 1
        
        # Контейнер с ограниченной шириной для консистентности
        inner_content = ft.Container(
                 content=ft.Column([
                  ft.Container(height=10),
                  ft.Text(self.t('program_ready'), size=20, weight=ft.FontWeight.BOLD,
                      color=self.colors['text'], text_align=ft.TextAlign.CENTER),
                  ft.Container(height=10),
                
                  info_panel,
                  ft.Container(height=10),
                  rec_card,
                  ft.Container(height=10),
                  nutrition_card,
                
                  ft.Container(height=15),
                  ft.Text(self.t('training_program_title'), size=16, weight=ft.FontWeight.BOLD,
                      color=self.colors['text']),
                  ft.Container(height=10),
                
                  *day_cards,
                
                  ft.Container(height=15),
                 ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8),
                 width=800,  # Фиксированная ширина контента
        )
        
        content = ft.Container(
            content=ft.Row(
                [inner_content],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=ft.Padding.symmetric(horizontal=20),
        )
        
        self.build_page(content)
    
    def _do_rest(self, week_num, wd_idx):
        self.completed_rest_days.add((week_num, wd_idx))
        dlg = ft.AlertDialog(
            title=ft.Text("💤"),
            content=ft.Text(self.t('rest_today_msg'), size=16),
            open=True,
            on_dismiss=lambda e: self.show_result(),
        )
        self.page.overlay.append(dlg)
        self.page.update()
    
    def start_workout(self, week, day_data):
        self.current_workout = {
            'week': week,
            'day_data': day_data,
            'current_exercise': 0,
            'current_set': 1,
            'completed_sets': 0,
            'skipped_exercises': 0,
            'start_time': datetime.datetime.now(),
            'exercise_results': [],
            'exercise_start_time': datetime.datetime.now(),
        }
        self.timer_running = False
        self.show_workout()
    
    # ============== ЭКРАН ТРЕНИРОВКИ ==============
    def show_workout(self, show_rest=False, rest_seconds=0):
        self.current_screen = 'workout'
        self.timer_running = False
        
        cw = self.current_workout
        day_data = cw['day_data']
        exercises = day_data['exercises']
        
        if cw['current_exercise'] >= len(exercises):
            self.complete_workout()
            return
        
        ex = exercises[cw['current_exercise']]
        
        # Тип упражнения
        type_info = {
            'compound': ('🔸', self.t('type_compound')),
            'isolation': ('🔹', self.t('type_isolation')),
            'core': ('🎯', self.t('type_core')),
            'cardio': ('🏃', self.t('type_cardio')),
            'hiit': ('🔥', 'HIIT'),
            'strength': ('💪', self.t('type_compound')),
        }.get(ex['type'], ('💪', self.t('type_compound')))
        
        diff_text = self.t(f"diff_{ex['difficulty']}")
        
        # GIF или эмодзи
        gif_widget = ft.Text(type_info[0], size=70)
        gif_name = ex.get('gif', '')
        if gif_name:
            try:
                # Формируем полный путь к GIF
                gif_path = self.gifs_dir / gif_name
                if gif_path.exists():
                    gif_widget = ft.Image(src=str(gif_path), width=220, height=165, fit="cover", border_radius=ft.border_radius.all(8))
                else:
                    print(f"⚠️ GIF не найден: {gif_path}")
            except Exception as e:
                print(f"⚠️ Ошибка GIF {gif_name}: {e}")
        
        if show_rest:
            self.show_rest_screen(rest_seconds, ex)
            return
        
        if ex.get('is_hold', False):
            self.show_hold_exercise(ex, gif_widget, type_info, diff_text)
            return
        
        content = ft.Container(
            content=ft.Column([
                ft.Container(height=10),
                
                ft.Text(f"▶️ {self.t('week')} {cw['week']} • {self.t('day')} {day_data['day']}",
                       size=14, weight=ft.FontWeight.BOLD, color=self.colors['primary']),
                ft.Text(f"{self.t('exercise')} {cw['current_exercise'] + 1} {self.t('of')} {len(exercises)}",
                       size=12, color=self.colors['text_secondary']),
                
                ft.Container(height=15),
                
                ft.Row(
                    [ft.Container(
                        content=gif_widget,
                        padding=4,
                        border_radius=12,
                        border=ft.border.all(3, self.colors['success']),
                    )],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                
                ft.Container(height=10),
                
                ft.Text(self.t(ex['name']), size=18, weight=ft.FontWeight.BOLD,
                       color=self.colors['text'], text_align=ft.TextAlign.CENTER),
                ft.Text(f"{type_info[0]} {type_info[1]} • {diff_text}",
                       size=11, color=self.colors['text_secondary']),
                
                ft.Container(height=18),
                
                # Подход и повторения
                ft.Container(
                    content=ft.Column([
                        ft.Text(f"{self.t('set')} {cw['current_set']} {self.t('of')} {ex['sets']}",
                               size=20, weight=ft.FontWeight.BOLD, color=self.colors['text']),
                        ft.Text(f"🔄 {ex['reps']} {self.t('reps')}", size=16, color=self.colors['primary']),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4),
                    padding=14,
                    border_radius=12,
                    bgcolor=self.colors['bg_card'],
                ),
                
                ft.Container(height=18),
                
                # Кнопка выполнения
                ft.Container(
                    content=ft.Text(self.t('complete_set'), size=16, weight=ft.FontWeight.BOLD, color="white"),
                    padding=ft.Padding(left=50, right=50, top=14, bottom=14),
                    border_radius=25,
                    bgcolor=self.colors['success'],
                    on_click=lambda e: self.complete_set_with_rest(),
                ),
                
                ft.Container(height=15),
                
                ft.Row([
                    ft.Container(
                        content=ft.Row([
                            ft.Icon(ft.Icons.SKIP_NEXT, color="white", size=18),
                            ft.Text(self.t('skip'), size=13, color="white"),
                        ], spacing=5),
                        padding=ft.Padding(left=20, right=20, top=10, bottom=10),
                        border_radius=20,
                        bgcolor=self.colors['warning'],
                        on_click=lambda e: self.skip_exercise_with_rest(),
                    ),
                    ft.Container(
                        content=ft.Row([
                            ft.Icon(ft.Icons.CLOSE, color="white", size=18),
                            ft.Text(self.t('finish'), size=13, color="white"),
                        ], spacing=5),
                        padding=ft.Padding(left=20, right=20, top=10, bottom=10),
                        border_radius=20,
                        bgcolor=self.colors['danger'],
                        on_click=lambda e: self.show_result(),
                    ),
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=15),
                
                ft.Container(height=10),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO),
            padding=ft.Padding.symmetric(horizontal=20),
        )
        
        self.build_page(content)
    
    def show_hold_exercise(self, ex, gif_widget, type_info, diff_text):
        cw = self.current_workout
        day_data = cw['day_data']
        exercises = day_data['exercises']
        
        # Таймер
        self.timer_seconds = ex['reps']
        self.timer_text = ft.Text(
            f"{self.timer_seconds}",
            size=48,
            weight=ft.FontWeight.BOLD,
            color="white"
        )
        
        self.timer_status = ft.Text(
            "⏱️ " + self.t('press_start'),
            size=12,
            color=self.colors['text_secondary']
        )
        
        content = ft.Container(
            content=ft.Column([
                ft.Container(height=10),
                
                ft.Text(f"▶️ {self.t('week')} {cw['week']} • {self.t('day')} {day_data['day']}",
                       size=14, weight=ft.FontWeight.BOLD, color=self.colors['primary']),
                ft.Text(f"{self.t('exercise')} {cw['current_exercise'] + 1} {self.t('of')} {len(exercises)}",
                       size=12, color=self.colors['text_secondary']),
                
                ft.Container(height=15),
                
                ft.Row(
                    [ft.Container(
                        content=gif_widget,
                        padding=4,
                        border_radius=12,
                        border=ft.border.all(3, self.colors['success']),
                    )],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                
                ft.Container(height=10),
                
                ft.Text(self.t(ex['name']), size=18, weight=ft.FontWeight.BOLD,
                       color=self.colors['text'], text_align=ft.TextAlign.CENTER),
                ft.Text(f"{type_info[0]} {type_info[1]} • {diff_text}",
                       size=11, color=self.colors['text_secondary']),
                
                ft.Container(height=15),
                
                ft.Container(
                    content=ft.Column([
                        self.timer_text,
                        self.timer_status,
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2),
                    padding=15,
                    border_radius=16,
                    bgcolor=self.colors['success'],
                ),
                
                ft.Container(height=12),
                
                # Подход
                ft.Text(f"{self.t('set')} {cw['current_set']} {self.t('of')} {ex['sets']}",
                       size=18, weight=ft.FontWeight.BOLD, color=self.colors['text']),
                
                ft.Container(height=14),
                
                # Кнопка старт/стоп
                ft.Container(
                    content=ft.Text("▶️ " + self.t('start_timer'), size=16, weight=ft.FontWeight.BOLD, color="white"),
                    padding=ft.Padding(left=50, right=50, top=14, bottom=14),
                    border_radius=25,
                    bgcolor=self.colors['primary'],
                    on_click=lambda e: self.start_hold_timer(ex),
                ),
                
                ft.Container(height=15),
                
                ft.Row([
                    ft.Container(
                        content=ft.Row([
                            ft.Icon(ft.Icons.SKIP_NEXT, color="white", size=18),
                            ft.Text(self.t('skip'), size=13, color="white"),
                        ], spacing=5),
                        padding=ft.Padding(left=20, right=20, top=10, bottom=10),
                        border_radius=20,
                        bgcolor=self.colors['warning'],
                        on_click=lambda e: self.skip_exercise_with_rest(),
                    ),
                    ft.Container(
                        content=ft.Row([
                            ft.Icon(ft.Icons.CLOSE, color="white", size=18),
                            ft.Text(self.t('finish'), size=13, color="white"),
                        ], spacing=5),
                        padding=ft.Padding(left=20, right=20, top=10, bottom=10),
                        border_radius=20,
                        bgcolor=self.colors['danger'],
                        on_click=lambda e: self.show_result(),
                    ),
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=15),
                
                ft.Container(height=10),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO),
            padding=ft.Padding.symmetric(horizontal=20),
        )
        
        self.build_page(content)
    
    def start_hold_timer(self, ex):
        if self.timer_running:
            return
        
        self.timer_running = True
        self.timer_generation += 1
        my_gen = self.timer_generation
        # Сбросить таймер на правильное значение
        self.timer_seconds = ex['reps']
        self.timer_text.value = f"{self.timer_seconds}"
        self.timer_text.color = "white"
        self.timer_status.value = "⏳ " + self.t('hold') + "..."
        self.page.update()
        
        async def countdown():
            while self.timer_seconds > 0 and self.timer_running and self.timer_generation == my_gen:
                await asyncio.sleep(1)
                if self.timer_generation != my_gen:
                    return
                self.timer_seconds -= 1
                if self.timer_running and self.timer_generation == my_gen:
                    self.timer_text.value = f"{self.timer_seconds}"
                    if self.timer_seconds <= 5:
                        self.timer_text.color = self.colors['danger']
                    try:
                        self.page.update()
                    except:
                        break
            
            if self.timer_running and self.timer_seconds <= 0 and self.timer_generation == my_gen:
                self.timer_running = False
                self.timer_status.value = "✅ " + self.t('done')
                try:
                    self.page.update()
                except:
                    pass
                await asyncio.sleep(0.5)
                self.complete_set_with_rest()
        
        self.page.run_task(countdown)
    
    def show_rest_screen(self, seconds, next_ex=None):
        self.timer_running = True
        self.timer_generation += 1
        my_gen = self.timer_generation
        self.timer_seconds = seconds
        
        self.timer_text = ft.Text(
            f"{seconds}",
            size=72,
            weight=ft.FontWeight.BOLD,
            color=self.colors['primary']
        )
        
        next_text = ""
        if next_ex:
            next_text = f"➡️ {self.t(next_ex['name'])}"
        
        content = ft.Container(
            content=ft.Column([
                ft.Container(height=60),
                ft.Text("💤", size=60),
                ft.Container(height=15),
                ft.Text(self.t('rest'), size=24, weight=ft.FontWeight.BOLD,
                       color=self.colors['text']),
                ft.Container(height=20),
                
                # Таймер обратного отсчёта
                ft.Container(
                    content=self.timer_text,
                    padding=30,
                    border_radius=100,
                    bgcolor=self.colors['bg_card'],
                    border=ft.border.all(3, self.colors['primary']),
                    width=160,
                    height=160,
                    alignment=ft.Alignment(0, 0),
                ),
                
                ft.Container(height=15),
                
                # Следующее упражнение
                ft.Text(next_text, size=14, color=self.colors['text_secondary'],
                       text_align=ft.TextAlign.CENTER) if next_text else ft.Container(),
                
                ft.Container(height=25),
                
                # Кнопки: +10 сек и пропуск отдыха
                ft.Row([
                    ft.Container(
                        content=ft.Text(f"⏱️ {self.t('add_10_sec')}", size=14,
                                       weight=ft.FontWeight.BOLD, color="white"),
                        padding=ft.Padding(left=25, right=25, top=12, bottom=12),
                        border_radius=25,
                        bgcolor=self.colors['secondary'],
                        on_click=lambda e: self.add_rest_time(10),
                    ),
                    ft.Container(
                        content=ft.Text(f"⏭️ {self.t('skip_rest')}", size=14,
                                       weight=ft.FontWeight.BOLD, color="white"),
                        padding=ft.Padding(left=25, right=25, top=12, bottom=12),
                        border_radius=25,
                        bgcolor=self.colors['warning'],
                        on_click=lambda e: self.skip_rest(),
                    ),
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=15),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
               alignment=ft.MainAxisAlignment.CENTER, spacing=5),
        )
        self.build_page(content)
        
        # Запускаем обратный отсчёт
        async def countdown():
            while self.timer_seconds > 0 and self.timer_running and self.timer_generation == my_gen:
                await asyncio.sleep(1)
                if self.timer_generation != my_gen:
                    return
                self.timer_seconds -= 1
                if self.timer_running and self.timer_generation == my_gen:
                    self.timer_text.value = f"{self.timer_seconds}"
                    if self.timer_seconds <= 3:
                        self.timer_text.color = self.colors['success']
                    try:
                        self.page.update()
                    except:
                        break
            
            if self.timer_running and self.timer_generation == my_gen:
                self.timer_running = False
                self.show_workout()
        
        self.page.run_task(countdown)
    
    def skip_rest(self):
        self.timer_running = False
        self.show_workout()
    
    def add_rest_time(self, extra_seconds):
        self.timer_seconds += extra_seconds
        if hasattr(self, 'timer_text') and self.timer_text:
            self.timer_text.value = f"{self.timer_seconds}"
            self.timer_text.color = self.colors['primary']
            try:
                self.page.update()
            except:
                pass
    
    def complete_set_with_rest(self):
        cw = self.current_workout
        ex = cw['day_data']['exercises'][cw['current_exercise']]
        
        cw['completed_sets'] += 1
        cw['current_set'] += 1
        
        if cw['current_set'] > ex['sets']:
            ex_time = (datetime.datetime.now() - cw.get('exercise_start_time', cw['start_time'])).seconds
            cw['exercise_results'].append({
                'name': ex['name'],
                'status': 'done',
                'sets': ex['sets'],
                'time_seconds': ex_time,
            })
            cw['current_exercise'] += 1
            cw['current_set'] = 1
            cw['exercise_start_time'] = datetime.datetime.now()
            
            if cw['current_exercise'] < len(cw['day_data']['exercises']):
                next_ex = cw['day_data']['exercises'][cw['current_exercise']]
                self.show_rest_screen(ex['rest_seconds'] + 10, next_ex)
            else:
                self.complete_workout()
        else:
            self.show_rest_screen(ex['rest_seconds'], ex)
    
    def skip_exercise_with_rest(self):
        cw = self.current_workout
        ex = cw['day_data']['exercises'][cw['current_exercise']]
        ex_time = (datetime.datetime.now() - cw.get('exercise_start_time', cw['start_time'])).seconds
        cw['exercise_results'].append({
            'name': ex['name'],
            'status': 'skipped',
            'sets': ex['sets'],
            'time_seconds': ex_time,
        })
        cw['skipped_exercises'] = cw.get('skipped_exercises', 0) + 1
        cw['current_exercise'] += 1
        cw['current_set'] = 1
        cw['exercise_start_time'] = datetime.datetime.now()
        
        if cw['current_exercise'] < len(cw['day_data']['exercises']):
            next_ex = cw['day_data']['exercises'][cw['current_exercise']]
            self.show_rest_screen(10, next_ex)
        else:
            self.complete_workout()
    
    def complete_workout(self):

        cw = self.current_workout
        workout_key = (cw['week'], cw['day_data']['day'])
        self.completed_workouts.add(workout_key)
        
        # Расчёт времени
        duration_seconds = (datetime.datetime.now() - cw['start_time']).seconds
        duration_min = duration_seconds // 60
        duration_sec = duration_seconds % 60
        
        # Пропущенные упражнения
        skipped = cw.get('skipped_exercises', 0)
        total_exercises = len(cw['day_data']['exercises'])
        completed_exercises = total_exercises - skipped
        
        self.workout_history.append({
            'date': datetime.datetime.now(),
            'week': cw['week'],
            'day': cw['day_data']['day'],
            'group': cw['day_data']['group'],
            'duration_seconds': duration_seconds,
            'exercises': cw['day_data']['exercises'],
            'completed_sets': cw['completed_sets'],
            'skipped_exercises': skipped,
            'exercise_results': cw.get('exercise_results', []),
        })
        
        # Создаём конфетти на весь экран
        confetti_items = []
        
        import random as rnd
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD', '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E9']
        
        # Используем ширину страницы
        try:
            screen_width = int(self.page.width) if self.page.width else 500
        except:
            screen_width = 500
        
        for i in range(120):  # Много конфетти
            left_pos = rnd.randint(0, screen_width)
            size = rnd.randint(8, 18)
            color = rnd.choice(colors)
            
            confetti_items.append(
                ft.Container(
                    width=size,
                    height=size * rnd.uniform(0.3, 1.0),
                    bgcolor=color,
                    border_radius=rnd.randint(0, 4),
                    left=left_pos,
                    top=rnd.randint(-300, -20),
                    rotate=ft.Rotate(rnd.uniform(0, 3.14)),
                    animate_position=ft.Animation(rnd.randint(1500, 3500), ft.AnimationCurve.EASE_OUT),
                    animate_opacity=ft.Animation(3500),
                    opacity=1,
                )
            )
        
        # Градиенты для статистики
        success_gradient = ['#00d4aa', '#00b894']
        primary_gradient = ['#667eea', '#764ba2']
        

        stats_row1 = ft.Row([
            ft.Container(
                content=ft.Column([
                    ft.Text("⏱️", size=30),
                    ft.Text(f"{duration_min}:{duration_sec:02d}", size=24, weight=ft.FontWeight.BOLD, color="white"),
                    ft.Text(self.t('time_label'), size=11, color="rgba(255,255,255,0.8)"),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4),
                gradient=ft.LinearGradient(
                    begin=ft.Alignment(-1, -1),
                    end=ft.Alignment(1, 1),
                    colors=primary_gradient,
                ),
                border_radius=16,
                padding=16,
                width=130,
                shadow=ft.BoxShadow(
                    spread_radius=0,
                    blur_radius=15,
                    color=ft.Colors.with_opacity(0.3, self.colors['primary']),
                    offset=ft.Offset(0, 5),
                ),
                animate_scale=ft.Animation(400, ft.AnimationCurve.ELASTIC_OUT),
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text("✅", size=30),
                    ft.Text(f"{cw['completed_sets']}", size=24, weight=ft.FontWeight.BOLD, color="white"),
                    ft.Text(self.t('sets_done_label'), size=11, color="rgba(255,255,255,0.8)"),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4),
                gradient=ft.LinearGradient(
                    begin=ft.Alignment(-1, -1),
                    end=ft.Alignment(1, 1),
                    colors=success_gradient,
                ),
                border_radius=16,
                padding=16,
                width=100,
                shadow=ft.BoxShadow(
                    spread_radius=0,
                    blur_radius=15,
                    color=ft.Colors.with_opacity(0.3, self.colors['success']),
                    offset=ft.Offset(0, 5),
                ),
                animate_scale=ft.Animation(400, ft.AnimationCurve.ELASTIC_OUT),
            ),
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=12)
        
        stats_row2 = ft.Row([
            ft.Container(
                content=ft.Column([
                    ft.Text("🎯", size=26),
                    ft.Text(f"{completed_exercises}/{total_exercises}", size=18, weight=ft.FontWeight.BOLD, color=self.colors['success']),
                    ft.Text(self.t('exercises_done_label'), size=11, color=self.colors['text_secondary']),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=3),
                bgcolor=self.colors['bg_card'],
                border_radius=14,
                padding=14,
                width=130,
                shadow=ft.BoxShadow(
                    spread_radius=0,
                    blur_radius=12,
                    color=ft.Colors.with_opacity(0.2, self.colors['success']),
                    offset=ft.Offset(0, 4),
                ),
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text("⏭️", size=26),
                    ft.Text(f"{skipped}", size=18, weight=ft.FontWeight.BOLD, color=self.colors['warning'] if skipped > 0 else self.colors['success']),
                    ft.Text(self.t('skipped_label'), size=11, color=self.colors['text_secondary']),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=3),
                bgcolor=self.colors['bg_card'],
                border_radius=14,
                padding=14,
                width=130,
                shadow=ft.BoxShadow(
                    spread_radius=0,
                    blur_radius=12,
                    color=ft.Colors.with_opacity(0.2, self.colors['warning'] if skipped > 0 else self.colors['success']),
                    offset=ft.Offset(0, 4),
                ),
            ),
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=12)
        

        main_content = ft.Container(
            content=ft.Column([
                ft.Container(height=40),
                
                # Большой эмодзи с анимацией
                ft.Container(
                    content=ft.Text("🎉", size=80),
                    animate_scale=ft.Animation(600, ft.AnimationCurve.ELASTIC_OUT),
                    shadow=ft.BoxShadow(
                        blur_radius=40,
                        color=ft.Colors.with_opacity(0.5, self.colors['success']),
                    ),
                ),
                
                ft.Container(height=12),
                
                # Заголовок с свечением
                ft.Container(
                    content=ft.Text(
                        self.t('workout_complete'),
                        size=26,
                        weight=ft.FontWeight.BOLD,
                        color=self.colors['success'],
                        text_align=ft.TextAlign.CENTER,
                    ),
                    shadow=ft.BoxShadow(
                        blur_radius=30,
                        color=ft.Colors.with_opacity(0.5, self.colors['success']),
                    ),
                    animate_opacity=ft.Animation(500, ft.AnimationCurve.EASE_OUT),
                ),
                
                ft.Text(
                    self.t('great_job'),
                    size=15,
                    color=self.colors['text_secondary'],
                ),
                ft.Text(
                    f"{self.t('week')} {cw['week']}, {self.t('day')} {cw['day_data']['day']}",
                    size=12,
                    color=self.colors['text_secondary'],
                ),
                
                ft.Container(height=25),
                stats_row1,
                ft.Container(height=12),
                stats_row2,
                ft.Container(height=30),
                
                # Опрос сложности тренировки
                ft.Text(self.t('how_was_workout'), size=18, weight=ft.FontWeight.BOLD,
                       color=self.colors['text']),
                ft.Container(height=12),
                
                ft.Row([
                    ft.Container(
                        content=ft.Text(self.t('workout_too_easy'), size=13, color="white",
                                       text_align=ft.TextAlign.CENTER),
                        padding=ft.Padding(left=14, right=14, top=12, bottom=12),
                        border_radius=14,
                        bgcolor="#4ECDC4",
                        on_click=lambda e: self.adjust_difficulty('easy'),
                        width=110,
                    ),
                    ft.Container(
                        content=ft.Text(self.t('workout_just_right'), size=13, color="white",
                                       text_align=ft.TextAlign.CENTER),
                        padding=ft.Padding(left=14, right=14, top=12, bottom=12),
                        border_radius=14,
                        bgcolor=self.colors['success'],
                        on_click=lambda e: self.adjust_difficulty('ok'),
                        width=110,
                    ),
                    ft.Container(
                        content=ft.Text(self.t('workout_too_hard'), size=13, color="white",
                                       text_align=ft.TextAlign.CENTER),
                        padding=ft.Padding(left=14, right=14, top=12, bottom=12),
                        border_radius=14,
                        bgcolor=self.colors['danger'],
                        on_click=lambda e: self.adjust_difficulty('hard'),
                        width=110,
                    ),
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=8),
                
                ft.Container(height=20),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO),
            expand=True,
        )
        
        # Stack с конфетти
        content = ft.Stack(
            controls=[main_content] + confetti_items,
            expand=True,
        )
        
        self.page.controls.clear()
        self.page.add(content)
        self.page.update()
        
        # Анимация конфетти падающего на весь экран
        async def animate_confetti():
            await asyncio.sleep(0.1)
            for item in confetti_items:
                item.top = rnd.randint(700, 1000)
                item.left = item.left + rnd.randint(-30, 30)
                item.opacity = 0
            try:
                self.page.update()
            except:
                pass
        
        self.page.run_task(animate_confetti)
    
    def adjust_difficulty(self, feedback):
        if not self.program_data or not self.program_data.get('schedule'):
            self.show_result()
            return
        
        if feedback == 'easy':
            # Увеличить нагрузку
            for week in self.program_data['schedule']:
                for day in week['days']:
                    wk = (week['week'], day['day'])
                    if wk in self.completed_workouts:
                        continue
                    for ex in day['exercises']:
                        if not ex.get('is_hold', False):
                            ex['sets'] = min(ex['sets'] + 1, 7)
                            if isinstance(ex['reps'], int):
                                ex['reps'] = min(ex['reps'] + 2, 25)
                        else:
                            if isinstance(ex['reps'], int):
                                ex['reps'] = min(ex['reps'] + 5, 90)
                        ex['rest_seconds'] = max(ex.get('rest_seconds', 30) - 5, 15)
            self.show_result()
            
        elif feedback == 'hard':
            # Показываем диалог подтверждения с предпросмотром изменений
            self._show_ease_dialog()
            
        else:  # 'ok'
            self.show_result()
    
    def _show_ease_dialog(self):
        # Собираем предпросмотр изменений (первые 3 упражнения)
        changes_preview = []
        count = 0
        for week in self.program_data['schedule']:
            for day in week['days']:
                wk = (week['week'], day['day'])
                if wk in self.completed_workouts:
                    continue
                for ex in day['exercises']:
                    if count >= 3:
                        break
                    name = self.t(ex['name'])
                    old_sets = ex['sets']
                    old_reps = ex['reps']
                    old_rest = ex.get('rest_seconds', 30)
                    new_sets = max(old_sets - 1, 2)
                    new_reps = max(old_reps - 2, 5) if isinstance(old_reps, int) else old_reps
                    new_rest = min(old_rest + 15, 120)
                    
                    changes_preview.append(
                        f"{name}:\n"
                        f"  {self.t('ease_sets')}: {old_sets} → {new_sets}\n"
                        f"  {self.t('ease_reps')}: {old_reps} → {new_reps}\n"
                        f"  {self.t('ease_rest')}: {old_rest}с → {new_rest}с"
                    )
                    count += 1
                if count >= 3:
                    break
            if count >= 3:
                break
        
        preview_text = "\n\n".join(changes_preview)
        if not preview_text:
            preview_text = self.t('ease_no_exercises')
        
        content = ft.Container(
            content=ft.Column([
                ft.Container(height=30),
                ft.Text(self.t('ease_title'), size=22, weight=ft.FontWeight.BOLD,
                       color=self.colors['warning'], text_align=ft.TextAlign.CENTER),
                ft.Container(height=10),
                ft.Text(
                    self.t('ease_desc'),
                    size=13, color=self.colors['text_secondary'],
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(height=15),
                ft.Text(self.t('ease_preview'), size=15, weight=ft.FontWeight.BOLD,
                       color=self.colors['text']),
                ft.Container(height=8),
                ft.Container(
                    content=ft.Text(preview_text, size=12, color=self.colors['text']),
                    padding=14,
                    border_radius=12,
                    bgcolor=self.colors['bg_card'],
                    border=ft.border.all(1, self.colors['warning']),
                    width=400,
                ),
                ft.Container(height=20),
                ft.Row([
                    ft.Container(
                        content=ft.Text(self.t('ease_yes'), size=14, weight=ft.FontWeight.BOLD, color="white"),
                        padding=ft.Padding(left=30, right=30, top=12, bottom=12),
                        border_radius=20,
                        bgcolor=self.colors['success'],
                        on_click=lambda e: self._apply_ease(),
                    ),
                    ft.Container(
                        content=ft.Text(self.t('ease_no'), size=14, weight=ft.FontWeight.BOLD, color="white"),
                        padding=ft.Padding(left=30, right=30, top=12, bottom=12),
                        border_radius=20,
                        bgcolor=self.colors['danger'],
                        on_click=lambda e: self.show_result(),
                    ),
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=15),
                ft.Container(height=20),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO),
            padding=ft.Padding.symmetric(horizontal=20),
        )
        self.build_page(content)
    
    def _apply_ease(self):

        for week in self.program_data['schedule']:
            for day in week['days']:
                wk = (week['week'], day['day'])
                if wk in self.completed_workouts:
                    continue
                for ex in day['exercises']:
                    if not ex.get('is_hold', False):
                        ex['sets'] = max(ex['sets'] - 1, 2)
                        if isinstance(ex['reps'], int):
                            ex['reps'] = max(ex['reps'] - 2, 5)
                    else:
                        if isinstance(ex['reps'], int):
                            ex['reps'] = max(ex['reps'] - 5, 10)
                    ex['rest_seconds'] = min(ex.get('rest_seconds', 30) + 15, 120)
        self.show_result()
    
    # ============== ЭКРАН ПРОГРЕССА ==============
    def show_progress(self):
        self.current_screen = 'progress'
        
        current_weight = self.user_data.get('weight', 70)
        if self.progress_data['weight']:
            current_weight = self.progress_data['weight'][-1][1]
        
        self.weight_input = ft.TextField(
            label=f"⚖️ {self.t('weight')} ({self.t('kg')})",
            width=170,
            keyboard_type=ft.KeyboardType.NUMBER,
            value=str(current_weight),
            border_radius=10,
            border_color=self.colors['border'],
            text_style=ft.TextStyle(color=self.colors['text']),
        )
        
        content = ft.Container(
            content=ft.Column([
                ft.Container(height=15),
                ft.Text(self.t('progress_title'), size=22, weight=ft.FontWeight.BOLD,
                       color=self.colors['text']),
                ft.Container(height=18),
                
                ft.Container(
                    content=ft.Column([
                        ft.Text(self.t('weight_title'), size=16, weight=ft.FontWeight.BOLD,
                               color=self.colors['text']),
                        ft.Text(f"{current_weight} {self.t('kg')}", size=36, weight=ft.FontWeight.BOLD,
                               color=self.colors['primary']),
                        ft.Row([
                            self.weight_input,
                            ft.ElevatedButton(
                                self.t('add_btn'),
                                bgcolor=self.colors['primary'],
                                color="white",
                                on_click=self.add_weight
                            ),
                        ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8),
                    padding=22,
                    border_radius=18,
                    bgcolor=self.colors['bg_card'],
                ),
                
                ft.Container(height=18),
                
                ft.Container(
                    content=ft.Column([
                        ft.Text(f"📊 {self.t('total_workouts')}: {len(self.workout_history)}", 
                               size=16, color=self.colors['text']),
                        ft.Text(self.t('great_progress') if len(self.workout_history) >= 3 else "",
                               size=13, color=self.colors['success']),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4),
                    padding=18,
                    border_radius=14,
                    bgcolor=self.colors['bg_card'],
                ),
                
                ft.Container(height=28),
                
                ft.ElevatedButton(
                    self.t('back_to_program'),
                    bgcolor=self.colors['text_secondary'],
                    color="white",
                    width=800,
                    height=48,
                    on_click=lambda e: self.show_result()
                ),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=ft.Padding.symmetric(horizontal=20),
        )
        
        self.build_page(content)
    
    def add_weight(self, e):
        try:
            weight = float(self.weight_input.value)
            if 40 <= weight <= 200:
                self.progress_data['weight'].append((datetime.datetime.now(), weight))
                self.user_data['weight'] = weight
                self.show_progress()
        except:
            pass
    
    # ============== ЭКРАН ДНЕВНИКА ==============
    def show_diary(self):
        self.current_screen = 'diary'
        
        # === СВОДНАЯ СТАТИСТИКА ===
        total_w = len(self.workout_history)
        total_sec = sum(h.get('duration_seconds', 0) for h in self.workout_history)
        total_min = total_sec // 60
        avg_min = (total_sec // total_w // 60) if total_w > 0 else 0
        
        # Считаем количество дней программы
        total_program_days = 0
        total_training_days = 0
        completed_count = 0
        rest_done_count = 0
        missed_count = 0
        upcoming_count = 0
        
        if self.program_data and self.program_data.get('schedule'):
            for week in self.program_data['schedule']:
                training_by_wd = {}
                for d in week['days']:
                    training_by_wd[d.get('weekday_idx', 0)] = d
                for wd_idx in range(7):
                    total_program_days += 1
                    if wd_idx in training_by_wd:
                        total_training_days += 1
                        wk_key = (week['week'], training_by_wd[wd_idx]['day'])
                        if wk_key in self.completed_workouts:
                            completed_count += 1
                        elif any(h['week'] == week['week'] and h['day'] == training_by_wd[wd_idx]['day'] for h in self.workout_history):
                            completed_count += 1
                        else:
                            has_later_done = False
                            found_current = False
                            gdn = 0
                            for wk2 in self.program_data['schedule']:
                                t2 = {dd.get('weekday_idx', 0): dd for dd in wk2['days']}
                                for wi2 in range(7):
                                    gdn += 1
                                    if wk2['week'] == week['week'] and wi2 == wd_idx:
                                        found_current = True
                                        continue
                                    if found_current and wi2 in t2:
                                        if (wk2['week'], t2[wi2]['day']) in self.completed_workouts:
                                            has_later_done = True
                                            break
                                if has_later_done:
                                    break
                            if has_later_done:
                                missed_count += 1
                            else:
                                upcoming_count += 1
                    else:
                        rk = (week['week'], wd_idx)
                        if rk in self.completed_rest_days:
                            rest_done_count += 1
        
        # Серия подряд
        streak = 0
        if self.program_data and self.program_data.get('schedule'):
            day_list = []
            for week in self.program_data['schedule']:
                t_by_wd = {dd.get('weekday_idx', 0): dd for dd in week['days']}
                for wd_idx in range(7):
                    if wd_idx in t_by_wd:
                        day_list.append(('train', (week['week'], t_by_wd[wd_idx]['day'])))
                    else:
                        day_list.append(('rest', (week['week'], wd_idx)))
            for dtype, dkey in reversed(day_list):
                if dtype == 'train' and dkey in self.completed_workouts:
                    streak += 1
                elif dtype == 'rest' and dkey in self.completed_rest_days:
                    streak += 1
                else:
                    break
        
        # Карточка статистики
        def stat_box(emoji, value, label, color=None):
            return ft.Container(
                content=ft.Column([
                    ft.Text(emoji, size=20),
                    ft.Text(str(value), size=18, weight=ft.FontWeight.BOLD,
                           color=color or self.colors['text']),
                    ft.Text(label, size=9, color=self.colors['text_secondary'],
                           text_align=ft.TextAlign.CENTER),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2),
                bgcolor=self.colors['bg_hover'],
                border_radius=12,
                padding=10,
                expand=True,
            )
        
        stats_row1 = ft.Row([
            stat_box("🏋️", total_w, self.t('diary_workouts_word')),
            stat_box("⏱️", f"{total_min} {self.t('diary_min')}", self.t('diary_total_time')),
            stat_box("📊", f"{avg_min} {self.t('diary_min')}", self.t('diary_avg_time')),
        ], spacing=8)
        
        stats_row2 = ft.Row([
            stat_box("✅", completed_count, self.t('diary_completion'), self.colors['success']),
            stat_box("❌", missed_count, self.t('diary_missed'), self.colors['danger']),
            stat_box("⏳", upcoming_count, self.t('diary_upcoming'), self.colors['text_secondary']),
            stat_box("🔥", streak, self.t('diary_streak'), self.colors['warning']),
        ], spacing=8)
        
        stats_card = ft.Container(
            content=ft.Column([stats_row1, ft.Container(height=6), stats_row2], spacing=0),
            padding=14,
            border_radius=14,
            bgcolor=self.colors['bg_card'],
            border=ft.border.all(1, self.colors['border']),
            width=800,
        )
        
        # === ПРОГРЕСС ПО ДНЯМ ===
        progress_items = []
        if self.program_data and self.program_data.get('schedule'):
            global_day = 1
            for week in self.program_data['schedule']:
                progress_items.append(ft.Container(
                    content=ft.Text(f"══ {self.t('week').upper()} {week['week']} ══",
                                   size=12, weight=ft.FontWeight.BOLD,
                                   color=self.colors['primary'], text_align=ft.TextAlign.CENTER),
                    padding=6,
                    width=800,
                ))
                training_by_wd = {dd.get('weekday_idx', 0): dd for dd in week['days']}
                
                for wd_idx in range(7):
                    day_label = f"{self.t('day_num')} {global_day}"
                    
                    if wd_idx in training_by_wd:
                        d = training_by_wd[wd_idx]
                        wk_key = (week['week'], d['day'])
                        group_name = self.t(d['group'])
                        
                        if wk_key in self.completed_workouts:
                            status_text = self.t('diary_status_done')
                            status_color = self.colors['success']
                            bg_color = ft.Colors.with_opacity(0.1, self.colors['success'])
                            log_entry = next((h for h in self.workout_history
                                            if h['week'] == week['week'] and h['day'] == d['day']), None)
                            if log_entry:
                                dur = log_entry.get('duration_seconds', 0)
                                extra = f" • {dur // 60}:{dur % 60:02d}"
                            else:
                                extra = ""
                        else:
                            has_later = False
                            found = False
                            for wk2 in self.program_data['schedule']:
                                t2 = {dd.get('weekday_idx', 0): dd for dd in wk2['days']}
                                for wi2 in range(7):
                                    if wk2['week'] == week['week'] and wi2 == wd_idx:
                                        found = True
                                        continue
                                    if found and wi2 in t2:
                                        if (wk2['week'], t2[wi2]['day']) in self.completed_workouts:
                                            has_later = True
                                            break
                                if has_later:
                                    break
                            if has_later:
                                status_text = self.t('diary_status_missed')
                                status_color = self.colors['danger']
                                bg_color = ft.Colors.with_opacity(0.1, self.colors['danger'])
                            else:
                                status_text = self.t('diary_status_upcoming')
                                status_color = self.colors['text_secondary']
                                bg_color = None
                            extra = ""
                        
                        progress_items.append(ft.Container(
                            content=ft.Row([
                                ft.Text(f"📅 {day_label}", size=11, color=self.colors['text'],
                                       weight=ft.FontWeight.BOLD, width=70),
                                ft.Text(f"{d.get('emoji', '💪')} {group_name}", size=11,
                                       color=self.colors['text'], expand=True),
                                ft.Text(f"{status_text}{extra}", size=10,
                                       color=status_color, weight=ft.FontWeight.BOLD),
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, spacing=4),
                            padding=ft.padding.symmetric(horizontal=12, vertical=8),
                            border_radius=8,
                            bgcolor=bg_color or self.colors['bg_card'],
                            border=ft.border.all(1, status_color),
                            width=800,
                        ))
                    else:
                        rk = (week['week'], wd_idx)
                        if rk in self.completed_rest_days:
                            status_text = self.t('diary_status_rest_done')
                            status_color = self.colors['success']
                        else:
                            status_text = self.t('rest_day')
                            status_color = self.colors['text_secondary']
                        
                        progress_items.append(ft.Container(
                            content=ft.Row([
                                ft.Text(f"📅 {day_label}", size=11, color=self.colors['text_secondary'],
                                       width=70),
                                ft.Text(f"😴 {self.t('rest_day')}", size=11,
                                       color=self.colors['text_secondary'], expand=True),
                                ft.Text(status_text, size=10, color=status_color),
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, spacing=4),
                            padding=ft.padding.symmetric(horizontal=12, vertical=6),
                            border_radius=8,
                            bgcolor=self.colors['bg_card'],
                            width=800,
                            opacity=0.7,
                        ))
                    
                    global_day += 1
        
        # === ИСТОРИЯ ТРЕНИРОВОК ===
        history_items = []
        if self.workout_history:
            for i, log in enumerate(reversed(self.workout_history), 1):
                idx = len(self.workout_history) - i + 1
                date_str = log['date'].strftime("%d.%m.%Y %H:%M")
                dur_sec = log.get('duration_seconds', 0)
                dur_min = dur_sec // 60
                dur_s = dur_sec % 60
                total_ex = len(log.get('exercises', []))
                skipped = log.get('skipped_exercises', 0)
                completed_ex = total_ex - skipped
                
                # Детальный список упражнений
                ex_detail_items = []
                ex_results = log.get('exercise_results', [])
                
                if ex_results:
                    for er in ex_results:
                        er_time = er.get('time_seconds', 0)
                        er_min = er_time // 60
                        er_s = er_time % 60
                        if er['status'] == 'done':
                            ex_icon = "✅"
                            ex_color = self.colors['success']
                            time_str = f" • {er_min}:{er_s:02d}"
                        else:
                            ex_icon = "❌"
                            ex_color = self.colors['danger']
                            time_str = ""
                        ex_detail_items.append(
                            ft.Row([
                                ft.Text(ex_icon, size=12),
                                ft.Text(self.t(er['name']), size=11,
                                       color=ex_color, expand=True),
                                ft.Text(f"{er['sets']} {self.t('sets_short')}{time_str}",
                                       size=10, color=self.colors['text_secondary']),
                            ], spacing=6)
                        )
                else:
                    for ex in log.get('exercises', []):
                        ex_detail_items.append(
                            ft.Row([
                                ft.Text("•", size=12, color=self.colors['text_secondary']),
                                ft.Text(self.t(ex['name']), size=11,
                                       color=self.colors['text_secondary']),
                            ], spacing=6)
                        )
                
                history_items.append(ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Text(f"#{idx}", size=16, weight=ft.FontWeight.BOLD,
                                   color=self.colors['primary']),
                            ft.Text(date_str, size=12, color=self.colors['text_secondary']),
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Text(f"{self.t('week')} {log['week']}, {self.t('day')} {log['day']} — {self.t(log['group'])}",
                               size=13, weight=ft.FontWeight.BOLD, color=self.colors['text']),
                        ft.Container(height=4),
                        ft.Row([
                            ft.Container(
                                content=ft.Column([
                                    ft.Text("⏱️", size=16),
                                    ft.Text(f"{dur_min}:{dur_s:02d}", size=14, weight=ft.FontWeight.BOLD,
                                           color=self.colors['text']),
                                    ft.Text(self.t('time_label'), size=9, color=self.colors['text_secondary']),
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2),
                                bgcolor=self.colors['bg_hover'], border_radius=10, padding=8, width=90,
                            ),
                            ft.Container(
                                content=ft.Column([
                                    ft.Text("✅", size=16),
                                    ft.Text(f"{log.get('completed_sets', 0)}", size=14,
                                           weight=ft.FontWeight.BOLD, color=self.colors['success']),
                                    ft.Text(self.t('sets_short'), size=9, color=self.colors['text_secondary']),
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2),
                                bgcolor=self.colors['bg_hover'], border_radius=10, padding=8, width=90,
                            ),
                            ft.Container(
                                content=ft.Column([
                                    ft.Text("🎯", size=16),
                                    ft.Text(f"{completed_ex}/{total_ex}", size=14,
                                           weight=ft.FontWeight.BOLD, color=self.colors['text']),
                                    ft.Text(self.t('exercises_done_label'), size=9, color=self.colors['text_secondary']),
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2),
                                bgcolor=self.colors['bg_hover'], border_radius=10, padding=8, width=90,
                            ),
                        ], alignment=ft.MainAxisAlignment.CENTER, spacing=8),
                        ft.Container(height=6),
                        ft.Container(
                            content=ft.Column([
                                ft.Text(f"📋 {self.t('diary_exercises_list')}:", size=12,
                                       weight=ft.FontWeight.BOLD, color=self.colors['text']),
                                ft.Container(height=4),
                                *ex_detail_items,
                            ], spacing=3),
                            bgcolor=self.colors['bg_hover'],
                            border_radius=10,
                            padding=10,
                        ),
                    ], spacing=4),
                    padding=14,
                    border_radius=14,
                    bgcolor=self.colors['bg_card'],
                    border=ft.border.all(1, self.colors['border']),
                    width=800,
                ))
        else:
            history_items.append(
                ft.Container(
                    content=ft.Text(self.t('no_records'), size=14,
                                   color=self.colors['text_secondary'],
                                   text_align=ft.TextAlign.CENTER),
                    padding=20,
                    width=800,
                )
            )
        
        # Прогресс-бар (процент выполнения)
        completion_pct = 0
        if total_training_days > 0:
            completion_pct = int(completed_count / total_training_days * 100)
        
        progress_bar = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text(f"📈 {self.t('diary_completion')}", size=13,
                           weight=ft.FontWeight.BOLD, color=self.colors['text']),
                    ft.Text(f"{completion_pct}%", size=13,
                           weight=ft.FontWeight.BOLD, color=self.colors['primary']),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.ProgressBar(
                    value=completion_pct / 100 if completion_pct > 0 else 0,
                    color=self.colors['primary'],
                    bgcolor=self.colors['bg_hover'],
                    bar_height=10,
                    border_radius=5,
                ),
            ], spacing=6),
            padding=14,
            border_radius=14,
            bgcolor=self.colors['bg_card'],
            width=800,
        )
        
        # Мотивационное сообщение
        if total_w >= 3:
            motivation = ft.Text(self.t('great_progress'), size=14,
                                color=self.colors['success'], text_align=ft.TextAlign.CENTER)
        else:
            motivation = ft.Container()
        
        content = ft.Container(
            content=ft.Column([
                ft.Container(height=15),
                ft.Text(self.t('diary_title'), size=22, weight=ft.FontWeight.BOLD,
                       color=self.colors['text']),
                ft.Container(height=10),
                
                stats_card,
                ft.Container(height=8),
                progress_bar,
                ft.Container(height=5),
                motivation,
                
                ft.Container(height=15),
                ft.Text(self.t('diary_progress_title'), size=16, weight=ft.FontWeight.BOLD,
                       color=self.colors['text']),
                ft.Container(height=8),
                *progress_items,
                
                ft.Container(height=15),
                ft.Text(self.t('diary_history_title'), size=16, weight=ft.FontWeight.BOLD,
                       color=self.colors['text']),
                ft.Container(height=8),
                *history_items,
                
                ft.Container(height=18),
                ft.ElevatedButton(
                    self.t('back_to_program'),
                    bgcolor=self.colors['primary'],
                    color="white",
                    width=800,
                    height=48,
                    on_click=lambda e: self.show_result()
                ),
                ft.Container(height=15),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8),
            padding=ft.Padding.symmetric(horizontal=20),
        )
        
        self.build_page(content)
    
    def save_program(self):
        if not self.program_data:
            return
        try:
            save_dir = Path.home() / "Desktop"
            if not save_dir.exists():
                save_dir = Path.home()
            filename = f"TrainerWizard_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.txt"
            save_path = save_dir / filename
            
            meta = self.program_data.get('metadata', {})
            weekday_keys = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
            lines = []
            lines.append('=' * 55)
            lines.append('   💪 TrainerWizard')
            lines.append('=' * 55)
            created_label = self.t("created") if has_translation("created", self.lang) else "Дата"
            lines.append(f'{created_label}: {meta.get("created", "")}')
            lines.append(f'{self.t("goal_weight_loss") if meta.get("goal") == "weight_loss" else self.t("goal_muscle_gain")}')
            lines.append(f'{self.t(meta.get("level", ""))}')
            lines.append(f'{meta.get("focus", "")}')
            lines.append(f'{meta.get("age", "")} | {meta.get("weight", "")} {self.t("kg")} | {meta.get("height", "")} {self.t("cm")}')
            lines.append(f'{self.t("bmi")}: {meta.get("bmi", "")}')
            lines.append('')
            
            training_days_set = set()
            if self.program_data.get('schedule') and self.program_data['schedule']:
                for d in self.program_data['schedule'][0]['days']:
                    training_days_set.add(d.get('weekday_idx', 0))
            
            for i, wk in enumerate(weekday_keys):
                if i in training_days_set:
                    lines.append(f'  {self.t(wk)}: 🏋️')
                else:
                    lines.append(f'  {self.t(wk)}: {self.t("rest_day")}')
            lines.append('')
            
            for week in self.program_data.get('schedule', []):
                lines.append('━' * 55)
                lines.append(f'  {self.t("week").upper()} {week["week"]}')
                lines.append('━' * 55)
                
                for day_data in week['days']:
                    wd_key = day_data.get('weekday_key', 'monday')
                    weekday = self.t(wd_key)
                    group_name = self.t(day_data['group'])
                    lines.append('')
                    lines.append(f'  📅 {weekday} — {self.t("day")} {day_data["day"]} — {day_data["emoji"]} {group_name}')
                    lines.append(f'  {"─" * 45}')
                    
                    for j, ex in enumerate(day_data['exercises'], 1):
                        name = self.t(ex['name'])
                        if ex.get('is_hold', False):
                            reps_str = f'{ex["reps"]} {self.t("sec")}'
                        else:
                            reps_str = f'{ex["reps"]} {self.t("reps")}'
                        diff = self.t(f"diff_{ex['difficulty']}")
                        lines.append(f'    {j:2d}. {name}')
                        lines.append(f'        {ex["sets"]} {self.t("sets")} × {reps_str} | {ex["rest_seconds"]}{self.t("sec")} | {diff}')
                    lines.append('')
            
            recs = self.program_data.get('recommendations', {})
            if recs:
                lines.append('━' * 55)
                for key, val in recs.items():
                    lines.append(f'  • {val}')
                lines.append('')
            
            lines.append('=' * 55)
            lines.append('  TrainerWizard')
            lines.append('=' * 55)
            
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
            
            dlg = ft.AlertDialog(
                title=ft.Text("✅ " + self.t('program_saved')),
                content=ft.Text(f"📁 {save_path}", size=12),
                open=True,
            )
            self.page.overlay.append(dlg)
            self.page.update()
        except Exception as ex:
            dlg = ft.AlertDialog(
                title=ft.Text("❌"),
                content=ft.Text(str(ex), size=12),
                open=True,
            )
            self.page.overlay.append(dlg)
            self.page.update()


# ============== ЗАПУСК ==============

def main(page: ft.Page):
    page.window_width = 900
    page.window_height = 1100
    page.window_resizable = True
    app = TrainingApp(page)


if __name__ == "__main__":
    # Указываем путь к папке с GIF
    assets_path = Path(__file__).parent.parent / "exercise_gifs"
    if not assets_path.exists():
        assets_path = Path(__file__).parent / "assets"
    print(f"📂 Assets path: {assets_path}")
    print(f"📂 Exists: {assets_path.exists()}")
    if assets_path.exists():
        print(f"📂 Files: {list(assets_path.glob('*.gif'))[:5]}")
    ft.app(target=main, assets_dir=str(assets_path))
