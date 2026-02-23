# -*- coding: utf-8 -*-
# 🏋️ Мобильный Тренировочный Планировщик - Полная версия
# Flet Mobile App - точная копия CustomTkinter приложения
# Запуск: flet run trainer_v3.py
# Сборка APK: flet build apk

import flet as ft
import sys
import io

# Принудительно устанавливаем UTF-8 для вывода
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
import random
import datetime
import json
import os
from pathlib import Path

# ============== БАЗА УПРАЖНЕНИЙ ==============

EXERCISES = {
    'Full Body': [
        # Женские упражнения
        {'name': 'Вариации планки', 'gif': 'планка.gif', 'type': 'core', 'difficulty': 'beginner', 'is_hold': True, 'female_focused': True},
        {'name': 'Приседания с собственным весом', 'gif': 'приседания.gif', 'type': 'compound', 'difficulty': 'beginner', 'female_focused': True},
        {'name': 'Ягодичный мостик', 'gif': 'ягодичный моститк.gif', 'type': 'isolation', 'difficulty': 'beginner', 'female_focused': True},
        {'name': 'Упражнение Супермен', 'gif': 'Superman Hold.gif', 'type': 'core', 'difficulty': 'beginner', 'female_focused': True},
        {'name': 'Вариации отжиманий', 'gif': 'отжимания.gif', 'type': 'compound', 'difficulty': 'intermediate', 'female_focused': True},
        {'name': 'Бёрпи (женский вариант)', 'gif': 'Берпи (женский вариант).gif', 'type': 'cardio', 'difficulty': 'intermediate', 'female_focused': True},
        {'name': 'Глубокие приседания с наклоном', 'gif': 'Deep Squat Bend.gif', 'type': 'compound', 'difficulty': 'intermediate', 'female_focused': True},
        {'name': 'Королевская становая тяга', 'gif': 'King Deadlift.gif', 'type': 'compound', 'difficulty': 'intermediate', 'female_focused': True},
        {'name': 'Поза ребёнка', 'gif': 'Child Pose.gif', 'type': 'core', 'difficulty': 'beginner', 'female_focused': True, 'is_hold': True},
        # Мужские упражнения
        {'name': 'Берпи с отжиманиями', 'gif': 'берпи с отжиманиями.gif', 'type': 'compound', 'difficulty': 'advanced', 'male_focused': True},
        {'name': 'Динамическая боковая планка', 'gif': 'динамическая боковая планка.gif', 'type': 'core', 'difficulty': 'intermediate', 'male_focused': True},
        {'name': 'Выпады вперёд-назад', 'gif': 'выпады.gif', 'type': 'compound', 'difficulty': 'intermediate', 'male_focused': True},
        {'name': 'Скручивания локтем к колену', 'gif': 'Elbow To Knee Crunches.gif', 'type': 'core', 'difficulty': 'intermediate', 'male_focused': True},
        {'name': 'Подъём таза на одной ноге', 'gif': 'Single Leg Hip Raise.gif', 'type': 'compound', 'difficulty': 'intermediate', 'male_focused': True},
        {'name': 'Подъём ног лёжа вверх', 'gif': 'подъемы ног.gif', 'type': 'core', 'difficulty': 'intermediate', 'male_focused': True},
        {'name': 'Супермен (удержание)', 'gif': 'Superman Hold.gif', 'type': 'core', 'difficulty': 'beginner', 'is_hold': True, 'male_focused': True},
        {'name': 'Велосипед (скручивания)', 'gif': 'Велосипед (скручивания).gif', 'type': 'core', 'difficulty': 'intermediate', 'male_focused': True},
    ],
    'Legs': [
        {'name': 'Приседания', 'gif': 'приседания.gif', 'type': 'compound', 'difficulty': 'beginner'},
        {'name': 'Выпады', 'gif': 'выпады.gif', 'type': 'compound', 'difficulty': 'beginner'},
        {'name': 'Болгарские сплит-приседания', 'gif': 'Bulgarian Split Squats.gif', 'type': 'compound', 'difficulty': 'intermediate'},
        {'name': 'Выпады в ходьбе', 'gif': 'выпады.gif', 'type': 'compound', 'difficulty': 'intermediate'},
        {'name': 'Ягодичный мостик', 'gif': 'ягодичный моститк.gif', 'type': 'isolation', 'difficulty': 'beginner'},
        {'name': 'Становая тяга на одной ноге', 'gif': 'Single Leg Deadlift.gif', 'type': 'compound', 'difficulty': 'intermediate'},
        {'name': 'Приседания у стены', 'gif': 'Wall Sit.gif', 'type': 'compound', 'difficulty': 'beginner', 'is_hold': True},
        {'name': 'Подъёмы на носки', 'gif': 'Calf Raises.gif', 'type': 'isolation', 'difficulty': 'beginner'},
        {'name': 'Приседания с прыжком', 'gif': 'приседания.gif', 'type': 'compound', 'difficulty': 'intermediate'},
        {'name': 'Приседания плие', 'gif': 'приседания.gif', 'type': 'compound', 'difficulty': 'beginner'},
        {'name': 'Подъёмы ног в сторону', 'gif': 'Side Leg Raises.gif', 'type': 'isolation', 'difficulty': 'beginner', 'female_focused': True},
    ],
    'Chest': [
        {'name': 'Отжимания', 'gif': 'отжимания.gif', 'type': 'compound', 'difficulty': 'beginner'},
        {'name': 'Широкие отжимания', 'gif': 'Широкие отжимания.gif', 'type': 'compound', 'difficulty': 'beginner'},
        {'name': 'Алмазные отжимания', 'gif': 'алмазные отжимания.gif', 'type': 'compound', 'difficulty': 'intermediate'},
        {'name': 'Отжимания с ногами на возвышении', 'gif': 'Decline Push-ups.gif', 'type': 'compound', 'difficulty': 'intermediate'},
        {'name': 'Отжимания на брусьях', 'gif': 'Chest Dips.gif', 'type': 'compound', 'difficulty': 'advanced'},
        {'name': 'Псевдо-планш отжимания', 'gif': 'Pseudo Planche Push-ups.gif', 'type': 'compound', 'difficulty': 'advanced'},
    ],
    'Back': [
        {'name': 'Подтягивания', 'gif': 'подтягивания.gif', 'type': 'compound', 'difficulty': 'intermediate'},
        {'name': 'Супермен (удержание)', 'gif': 'Superman Hold.gif', 'type': 'core', 'difficulty': 'beginner', 'is_hold': True},
        {'name': 'Обратные снежные ангелы', 'gif': 'Reverse Snow Angels.gif', 'type': 'isolation', 'difficulty': 'beginner'},
        {'name': 'Тяга в дверном проёме', 'gif': 'Door Frame Rows.gif', 'type': 'compound', 'difficulty': 'beginner'},
        {'name': 'Скольжения по стене', 'gif': 'Wall Slides.gif', 'type': 'isolation', 'difficulty': 'beginner'},
        {'name': 'Обратные подтягивания', 'gif': 'Inverted Rows.gif', 'type': 'compound', 'difficulty': 'intermediate'},
        {'name': 'Подъёмы Y-T-W', 'gif': 'Y-T-W Raises.gif', 'type': 'isolation', 'difficulty': 'beginner'},
    ],
    'Arms': [
        {'name': 'Обратные отжимания на трицепс', 'gif': 'Tricep Dips.gif', 'type': 'compound', 'difficulty': 'beginner'},
        {'name': 'Алмазные отжимания', 'gif': 'алмазные отжимания.gif', 'type': 'compound', 'difficulty': 'intermediate'},
        {'name': 'Сгибания с полотенцем', 'gif': 'Towel Bicep Curls.gif', 'type': 'isolation', 'difficulty': 'beginner'},
        {'name': 'Узкие отжимания', 'gif': 'узкие отжимания.gif', 'type': 'compound', 'difficulty': 'intermediate'},
        {'name': 'Круги руками', 'gif': 'Arm Circles.gif', 'type': 'isolation', 'difficulty': 'beginner'},
        {'name': 'Планка в собаку мордой вниз', 'gif': 'Планка с переходом в собаку мордой вниз.gif', 'type': 'compound', 'difficulty': 'intermediate'},
        {'name': 'Подтягивания', 'gif': 'подтягивания.gif', 'type': 'compound', 'difficulty': 'intermediate'},
    ],
    'Shoulders': [
        {'name': 'Отжимания уголком', 'gif': 'отжимания уголком.gif', 'type': 'compound', 'difficulty': 'intermediate'},
        {'name': 'Касания плеч', 'gif': 'Shoulder Taps.gif', 'type': 'core', 'difficulty': 'beginner'},
        {'name': 'Стойка на руках у стены', 'gif': 'Wall Handstand Hold.gif', 'type': 'compound', 'difficulty': 'advanced', 'is_hold': True},
        {'name': 'Планка с касанием плеч', 'gif': 'планка.gif', 'type': 'core', 'difficulty': 'beginner'},
        {'name': 'Обратная планка', 'gif': 'Обратная планка.gif', 'type': 'core', 'difficulty': 'intermediate', 'is_hold': True},
    ],
    'Core': [
        {'name': 'Планка', 'gif': 'планка.gif', 'type': 'core', 'difficulty': 'beginner', 'is_hold': True},
        {'name': 'Боковая планка', 'gif': 'Боковая планка.gif', 'type': 'core', 'difficulty': 'intermediate', 'is_hold': True},
        {'name': 'Скручивания на полу', 'gif': 'Скручивания на полу.gif', 'type': 'core', 'difficulty': 'beginner'},
        {'name': 'Русские скручивания', 'gif': 'Русские скручивания.gif', 'type': 'core', 'difficulty': 'intermediate'},
        {'name': 'Подъёмы ног', 'gif': 'подъемы ног.gif', 'type': 'core', 'difficulty': 'intermediate'},
        {'name': 'Мёртвый жук', 'gif': 'Мёртвый жук.gif', 'type': 'core', 'difficulty': 'beginner'},
        {'name': 'Ножницы', 'gif': 'ножницы.gif', 'type': 'core', 'difficulty': 'intermediate'},
        {'name': 'Скалолаз', 'gif': 'скалолаз.gif', 'type': 'cardio', 'difficulty': 'intermediate'},
        {'name': 'Велосипед', 'gif': 'Велосипед (скручивания).gif', 'type': 'core', 'difficulty': 'intermediate'},
        {'name': 'Русские скручивания сидя', 'gif': 'Русские скручивания сидя.gif', 'type': 'core', 'difficulty': 'intermediate', 'male_focused': True},
        {'name': 'Боковые наклоны', 'gif': 'Боковые наклоны.gif', 'type': 'core', 'difficulty': 'beginner', 'female_focused': True},
    ],
    'Cardio': [
        {'name': 'Прыжки с хлопками над головой', 'gif': 'Прыжки с хлопками над головой.gif', 'type': 'cardio', 'difficulty': 'beginner'},
        {'name': 'Бег с высоким подниманием коленей', 'gif': 'Бег с высоким подниманием коленей.gif', 'type': 'cardio', 'difficulty': 'beginner'},
        {'name': 'Скалолаз', 'gif': 'скалолаз.gif', 'type': 'cardio', 'difficulty': 'intermediate'},
        {'name': 'Берпи', 'gif': 'берпи.gif', 'type': 'cardio', 'difficulty': 'intermediate'},
        {'name': 'Конькобежец', 'gif': 'Конькобежец.gif', 'type': 'cardio', 'difficulty': 'intermediate'},
        {'name': 'Бег на месте', 'gif': 'Бег на месте.gif', 'type': 'cardio', 'difficulty': 'beginner'},
    ],
    'Weight Loss': [
        {'name': 'Берпи', 'gif': 'берпи.gif', 'type': 'cardio', 'difficulty': 'intermediate'},
        {'name': 'Скалолаз', 'gif': 'скалолаз.gif', 'type': 'cardio', 'difficulty': 'intermediate'},
        {'name': 'Прыжки с хлопками над головой', 'gif': 'Прыжки с хлопками над головой.gif', 'type': 'cardio', 'difficulty': 'beginner'},
        {'name': 'Приседания с прыжком', 'gif': 'приседания.gif', 'type': 'compound', 'difficulty': 'intermediate'},
        {'name': 'Выпады с прыжком', 'gif': 'выпады.gif', 'type': 'compound', 'difficulty': 'intermediate'},
        {'name': 'Планка', 'gif': 'планка.gif', 'type': 'core', 'difficulty': 'beginner', 'is_hold': True},
        {'name': 'Бег с высоким подниманием коленей', 'gif': 'Бег с высоким подниманием коленей.gif', 'type': 'cardio', 'difficulty': 'beginner'},
        {'name': 'Планка с переходом в собаку мордой вниз', 'gif': 'Планка с переходом в собаку мордой вниз.gif', 'type': 'core', 'difficulty': 'intermediate'},
        {'name': 'Отжимания', 'gif': 'отжимания.gif', 'type': 'compound', 'difficulty': 'beginner'},
        {'name': 'Конькобежец', 'gif': 'Конькобежец.gif', 'type': 'cardio', 'difficulty': 'intermediate'},
        {'name': 'Ягодичный мостик на одной ноге', 'gif': 'ягодичный моститк.gif', 'type': 'compound', 'difficulty': 'intermediate', 'female_focused': True},
        {'name': 'Берпи с отжиманиями', 'gif': 'берпи с отжиманиями.gif', 'type': 'cardio', 'difficulty': 'advanced', 'male_focused': True},
    ],
}

# ============== РЕЦЕПТЫ (45 рецептов на 5 языках) ==============

RECIPES = [
    # ЗАВТРАКИ
    {
        'id': 'oatmeal',
        'category': 'breakfast',
        'name': {'ru': 'Овсянка с бананом', 'en': 'Oatmeal with Banana', 'de': 'Haferflocken mit Banane', 'es': 'Avena con plátano', 'zh': '香蕉燕麦片'},
        'calories': 350, 'protein': 10, 'fat': 6, 'carbs': 65,
        'time': 10,
        'ingredients': {
            'ru': ['100г овсянки', '1 банан', '200мл молока', '1 ложка мёда'],
            'en': ['100g oatmeal', '1 banana', '200ml milk', '1 tbsp honey'],
            'de': ['100g Haferflocken', '1 Banane', '200ml Milch', '1 EL Honig'],
            'es': ['100g avena', '1 plátano', '200ml leche', '1 cda miel'],
            'zh': ['100克燕麦', '1根香蕉', '200毫升牛奶', '1勺蜂蜜']
        },
        'steps': {
            'ru': ['Залить овсянку молоком', 'Варить 5 минут', 'Добавить нарезанный банан', 'Полить мёдом'],
            'en': ['Pour milk over oatmeal', 'Cook 5 minutes', 'Add sliced banana', 'Drizzle with honey'],
            'de': ['Milch über Haferflocken gießen', '5 Minuten kochen', 'Banane hinzufügen', 'Mit Honig beträufeln'],
            'es': ['Verter leche sobre avena', 'Cocinar 5 minutos', 'Añadir plátano', 'Rociar con miel'],
            'zh': ['将牛奶倒在燕麦上', '煮5分钟', '加入切片香蕉', '淋上蜂蜜']
        }
    },
    {
        'id': 'scrambled_eggs',
        'category': 'breakfast',
        'name': {'ru': 'Яичница с овощами', 'en': 'Scrambled Eggs with Veggies', 'de': 'Rührei mit Gemüse', 'es': 'Huevos revueltos con verduras', 'zh': '蔬菜炒蛋'},
        'calories': 280, 'protein': 18, 'fat': 20, 'carbs': 8,
        'time': 15,
        'ingredients': {
            'ru': ['3 яйца', '1 помидор', '50г шпината', 'Соль, перец'],
            'en': ['3 eggs', '1 tomato', '50g spinach', 'Salt, pepper'],
            'de': ['3 Eier', '1 Tomate', '50g Spinat', 'Salz, Pfeffer'],
            'es': ['3 huevos', '1 tomate', '50g espinacas', 'Sal, pimienta'],
            'zh': ['3个鸡蛋', '1个番茄', '50克菠菜', '盐、胡椒']
        },
        'steps': {
            'ru': ['Взбить яйца', 'Обжарить овощи 2 мин', 'Залить яйцами', 'Готовить до готовности'],
            'en': ['Beat eggs', 'Fry veggies 2 min', 'Pour eggs', 'Cook until done'],
            'de': ['Eier verquirlen', 'Gemüse 2 Min anbraten', 'Eier dazugeben', 'Fertig garen'],
            'es': ['Batir huevos', 'Freír verduras 2 min', 'Verter huevos', 'Cocinar hasta listo'],
            'zh': ['打散鸡蛋', '炒蔬菜2分钟', '倒入鸡蛋', '煮至熟透']
        }
    },
    {
        'id': 'protein_pancakes',
        'category': 'breakfast',
        'name': {'ru': 'Протеиновые панкейки', 'en': 'Protein Pancakes', 'de': 'Protein-Pfannkuchen', 'es': 'Tortitas proteicas', 'zh': '蛋白质煎饼'},
        'calories': 320, 'protein': 25, 'fat': 8, 'carbs': 35,
        'time': 20,
        'ingredients': {
            'ru': ['1 банан', '2 яйца', '30г протеина', '50г овсянки'],
            'en': ['1 banana', '2 eggs', '30g protein', '50g oats'],
            'de': ['1 Banane', '2 Eier', '30g Protein', '50g Haferflocken'],
            'es': ['1 plátano', '2 huevos', '30g proteína', '50g avena'],
            'zh': ['1根香蕉', '2个鸡蛋', '30克蛋白粉', '50克燕麦']
        },
        'steps': {
            'ru': ['Смешать всё в блендере', 'Жарить на среднем огне', 'По 2 мин с каждой стороны'],
            'en': ['Blend everything', 'Cook on medium heat', '2 min each side'],
            'de': ['Alles mixen', 'Bei mittlerer Hitze braten', '2 Min pro Seite'],
            'es': ['Mezclar todo', 'Cocinar a fuego medio', '2 min por lado'],
            'zh': ['将所有材料混合', '中火煎', '每面2分钟']
        }
    },
    {
        'id': 'cottage_cheese',
        'category': 'breakfast',
        'name': {'ru': 'Творог с ягодами', 'en': 'Cottage Cheese with Berries', 'de': 'Quark mit Beeren', 'es': 'Requesón con bayas', 'zh': '浆果奶酪'},
        'calories': 200, 'protein': 25, 'fat': 5, 'carbs': 15,
        'time': 5,
        'ingredients': {
            'ru': ['200г творога', '100г ягод', '1 ложка мёда'],
            'en': ['200g cottage cheese', '100g berries', '1 tbsp honey'],
            'de': ['200g Quark', '100g Beeren', '1 EL Honig'],
            'es': ['200g requesón', '100g bayas', '1 cda miel'],
            'zh': ['200克奶酪', '100克浆果', '1勺蜂蜜']
        },
        'steps': {
            'ru': ['Выложить творог', 'Добавить ягоды', 'Полить мёдом'],
            'en': ['Put cottage cheese', 'Add berries', 'Drizzle honey'],
            'de': ['Quark anrichten', 'Beeren hinzufügen', 'Mit Honig beträufeln'],
            'es': ['Poner requesón', 'Añadir bayas', 'Rociar miel'],
            'zh': ['放奶酪', '加浆果', '淋蜂蜜']
        }
    },
    # ОБЕДЫ
    {
        'id': 'chicken_rice',
        'category': 'lunch',
        'name': {'ru': 'Курица с рисом', 'en': 'Chicken with Rice', 'de': 'Hähnchen mit Reis', 'es': 'Pollo con arroz', 'zh': '鸡肉饭'},
        'calories': 450, 'protein': 35, 'fat': 10, 'carbs': 50,
        'time': 30,
        'ingredients': {
            'ru': ['200г куриной грудки', '100г риса', 'Овощи', 'Специи'],
            'en': ['200g chicken breast', '100g rice', 'Vegetables', 'Spices'],
            'de': ['200g Hähnchenbrust', '100g Reis', 'Gemüse', 'Gewürze'],
            'es': ['200g pechuga de pollo', '100g arroz', 'Verduras', 'Especias'],
            'zh': ['200克鸡胸肉', '100克米饭', '蔬菜', '调料']
        },
        'steps': {
            'ru': ['Отварить рис', 'Обжарить курицу', 'Добавить овощи', 'Подавать вместе'],
            'en': ['Cook rice', 'Fry chicken', 'Add vegetables', 'Serve together'],
            'de': ['Reis kochen', 'Hähnchen braten', 'Gemüse hinzufügen', 'Zusammen servieren'],
            'es': ['Cocinar arroz', 'Freír pollo', 'Añadir verduras', 'Servir junto'],
            'zh': ['煮米饭', '煎鸡肉', '加蔬菜', '一起上桌']
        }
    },
    {
        'id': 'salmon_veggies',
        'category': 'lunch',
        'name': {'ru': 'Лосось с овощами', 'en': 'Salmon with Vegetables', 'de': 'Lachs mit Gemüse', 'es': 'Salmón con verduras', 'zh': '三文鱼配蔬菜'},
        'calories': 400, 'protein': 30, 'fat': 22, 'carbs': 15,
        'time': 25,
        'ingredients': {
            'ru': ['200г лосося', 'Брокколи', 'Лимон', 'Оливковое масло'],
            'en': ['200g salmon', 'Broccoli', 'Lemon', 'Olive oil'],
            'de': ['200g Lachs', 'Brokkoli', 'Zitrone', 'Olivenöl'],
            'es': ['200g salmón', 'Brócoli', 'Limón', 'Aceite de oliva'],
            'zh': ['200克三文鱼', '西兰花', '柠檬', '橄榄油']
        },
        'steps': {
            'ru': ['Запечь лосось 15 мин', 'Отварить брокколи', 'Полить лимоном'],
            'en': ['Bake salmon 15 min', 'Boil broccoli', 'Squeeze lemon'],
            'de': ['Lachs 15 Min backen', 'Brokkoli kochen', 'Zitrone auspressen'],
            'es': ['Hornear salmón 15 min', 'Hervir brócoli', 'Exprimir limón'],
            'zh': ['烤三文鱼15分钟', '煮西兰花', '挤柠檬汁']
        }
    },
    {
        'id': 'beef_buckwheat',
        'category': 'lunch',
        'name': {'ru': 'Говядина с гречкой', 'en': 'Beef with Buckwheat', 'de': 'Rindfleisch mit Buchweizen', 'es': 'Ternera con trigo sarraceno', 'zh': '牛肉荞麦饭'},
        'calories': 480, 'protein': 40, 'fat': 15, 'carbs': 45,
        'time': 35,
        'ingredients': {
            'ru': ['200г говядины', '100г гречки', 'Лук', 'Морковь'],
            'en': ['200g beef', '100g buckwheat', 'Onion', 'Carrot'],
            'de': ['200g Rindfleisch', '100g Buchweizen', 'Zwiebel', 'Karotte'],
            'es': ['200g ternera', '100g trigo sarraceno', 'Cebolla', 'Zanahoria'],
            'zh': ['200克牛肉', '100克荞麦', '洋葱', '胡萝卜']
        },
        'steps': {
            'ru': ['Обжарить мясо', 'Отварить гречку', 'Тушить с овощами'],
            'en': ['Fry meat', 'Cook buckwheat', 'Stew with veggies'],
            'de': ['Fleisch anbraten', 'Buchweizen kochen', 'Mit Gemüse schmoren'],
            'es': ['Freír carne', 'Cocinar trigo', 'Estofar con verduras'],
            'zh': ['煎牛肉', '煮荞麦', '与蔬菜炖']
        }
    },
    # УЖИНЫ
    {
        'id': 'fish_salad',
        'category': 'dinner',
        'name': {'ru': 'Рыба с салатом', 'en': 'Fish with Salad', 'de': 'Fisch mit Salat', 'es': 'Pescado con ensalada', 'zh': '鱼配沙拉'},
        'calories': 300, 'protein': 28, 'fat': 15, 'carbs': 10,
        'time': 20,
        'ingredients': {
            'ru': ['200г белой рыбы', 'Листья салата', 'Огурец', 'Помидор'],
            'en': ['200g white fish', 'Lettuce', 'Cucumber', 'Tomato'],
            'de': ['200g Weißfisch', 'Salat', 'Gurke', 'Tomate'],
            'es': ['200g pescado blanco', 'Lechuga', 'Pepino', 'Tomate'],
            'zh': ['200克白鱼', '生菜', '黄瓜', '番茄']
        },
        'steps': {
            'ru': ['Запечь рыбу', 'Нарезать овощи', 'Подавать вместе'],
            'en': ['Bake fish', 'Cut vegetables', 'Serve together'],
            'de': ['Fisch backen', 'Gemüse schneiden', 'Zusammen servieren'],
            'es': ['Hornear pescado', 'Cortar verduras', 'Servir junto'],
            'zh': ['烤鱼', '切蔬菜', '一起上桌']
        }
    },
    {
        'id': 'turkey_veggies',
        'category': 'dinner',
        'name': {'ru': 'Индейка с овощами', 'en': 'Turkey with Vegetables', 'de': 'Pute mit Gemüse', 'es': 'Pavo con verduras', 'zh': '火鸡配蔬菜'},
        'calories': 320, 'protein': 35, 'fat': 12, 'carbs': 15,
        'time': 25,
        'ingredients': {
            'ru': ['200г индейки', 'Кабачок', 'Перец', 'Чеснок'],
            'en': ['200g turkey', 'Zucchini', 'Pepper', 'Garlic'],
            'de': ['200g Pute', 'Zucchini', 'Paprika', 'Knoblauch'],
            'es': ['200g pavo', 'Calabacín', 'Pimiento', 'Ajo'],
            'zh': ['200克火鸡', '西葫芦', '辣椒', '大蒜']
        },
        'steps': {
            'ru': ['Нарезать индейку', 'Обжарить с овощами', 'Тушить 15 мин'],
            'en': ['Cut turkey', 'Fry with vegetables', 'Stew 15 min'],
            'de': ['Pute schneiden', 'Mit Gemüse braten', '15 Min schmoren'],
            'es': ['Cortar pavo', 'Freír con verduras', 'Estofar 15 min'],
            'zh': ['切火鸡', '与蔬菜一起炒', '炖15分钟']
        }
    },
    {
        'id': 'omelette',
        'category': 'dinner',
        'name': {'ru': 'Омлет с сыром', 'en': 'Cheese Omelette', 'de': 'Käseomelett', 'es': 'Tortilla de queso', 'zh': '芝士煎蛋'},
        'calories': 250, 'protein': 20, 'fat': 18, 'carbs': 3,
        'time': 10,
        'ingredients': {
            'ru': ['3 яйца', '50г сыра', 'Зелень', 'Молоко'],
            'en': ['3 eggs', '50g cheese', 'Herbs', 'Milk'],
            'de': ['3 Eier', '50g Käse', 'Kräuter', 'Milch'],
            'es': ['3 huevos', '50g queso', 'Hierbas', 'Leche'],
            'zh': ['3个鸡蛋', '50克奶酪', '香草', '牛奶']
        },
        'steps': {
            'ru': ['Взбить яйца с молоком', 'Вылить на сковороду', 'Посыпать сыром', 'Готовить 5 мин'],
            'en': ['Beat eggs with milk', 'Pour on pan', 'Sprinkle cheese', 'Cook 5 min'],
            'de': ['Eier mit Milch verquirlen', 'In Pfanne gießen', 'Käse streuen', '5 Min garen'],
            'es': ['Batir huevos con leche', 'Verter en sartén', 'Espolvorear queso', 'Cocinar 5 min'],
            'zh': ['打蛋加牛奶', '倒入锅中', '撒奶酪', '煮5分钟']
        }
    },
    # ПЕРЕКУСЫ
    {
        'id': 'greek_yogurt',
        'category': 'snack',
        'name': {'ru': 'Греческий йогурт', 'en': 'Greek Yogurt', 'de': 'Griechischer Joghurt', 'es': 'Yogur griego', 'zh': '希腊酸奶'},
        'calories': 150, 'protein': 15, 'fat': 5, 'carbs': 10,
        'time': 2,
        'ingredients': {
            'ru': ['200г греческого йогурта', 'Орехи', 'Мёд'],
            'en': ['200g Greek yogurt', 'Nuts', 'Honey'],
            'de': ['200g griechischer Joghurt', 'Nüsse', 'Honig'],
            'es': ['200g yogur griego', 'Nueces', 'Miel'],
            'zh': ['200克希腊酸奶', '坚果', '蜂蜜']
        },
        'steps': {
            'ru': ['Выложить йогурт', 'Добавить орехи', 'Полить мёдом'],
            'en': ['Put yogurt', 'Add nuts', 'Drizzle honey'],
            'de': ['Joghurt anrichten', 'Nüsse hinzufügen', 'Honig drüber'],
            'es': ['Poner yogur', 'Añadir nueces', 'Rociar miel'],
            'zh': ['放酸奶', '加坚果', '淋蜂蜜']
        }
    },
    {
        'id': 'protein_shake',
        'category': 'snack',
        'name': {'ru': 'Протеиновый коктейль', 'en': 'Protein Shake', 'de': 'Proteinshake', 'es': 'Batido de proteínas', 'zh': '蛋白质奶昔'},
        'calories': 200, 'protein': 25, 'fat': 3, 'carbs': 15,
        'time': 5,
        'ingredients': {
            'ru': ['30г протеина', '300мл молока', '1 банан'],
            'en': ['30g protein', '300ml milk', '1 banana'],
            'de': ['30g Protein', '300ml Milch', '1 Banane'],
            'es': ['30g proteína', '300ml leche', '1 plátano'],
            'zh': ['30克蛋白粉', '300毫升牛奶', '1根香蕉']
        },
        'steps': {
            'ru': ['Смешать всё в блендере', 'Взбить до однородности'],
            'en': ['Blend everything', 'Mix until smooth'],
            'de': ['Alles mixen', 'Glatt rühren'],
            'es': ['Mezclar todo', 'Batir hasta suave'],
            'zh': ['将所有材料混合', '搅拌至顺滑']
        }
    },
    {
        'id': 'nuts_fruits',
        'category': 'snack',
        'name': {'ru': 'Орехи с сухофруктами', 'en': 'Nuts with Dried Fruits', 'de': 'Nüsse mit Trockenfrüchten', 'es': 'Nueces con frutas secas', 'zh': '坚果干果'},
        'calories': 180, 'protein': 5, 'fat': 12, 'carbs': 15,
        'time': 1,
        'ingredients': {
            'ru': ['30г миндаля', '30г грецких орехов', '20г изюма'],
            'en': ['30g almonds', '30g walnuts', '20g raisins'],
            'de': ['30g Mandeln', '30g Walnüsse', '20g Rosinen'],
            'es': ['30g almendras', '30g nueces', '20g pasas'],
            'zh': ['30克杏仁', '30克核桃', '20克葡萄干']
        },
        'steps': {
            'ru': ['Смешать орехи', 'Добавить сухофрукты'],
            'en': ['Mix nuts', 'Add dried fruits'],
            'de': ['Nüsse mischen', 'Trockenfrüchte hinzufügen'],
            'es': ['Mezclar nueces', 'Añadir frutas secas'],
            'zh': ['混合坚果', '加干果']
        }
    },
    # ВЫСОКОБЕЛКОВЫЕ
    {
        'id': 'chicken_breast',
        'category': 'high_protein',
        'name': {'ru': 'Куриная грудка гриль', 'en': 'Grilled Chicken Breast', 'de': 'Gegrillte Hähnchenbrust', 'es': 'Pechuga de pollo a la parrilla', 'zh': '烤鸡胸肉'},
        'calories': 250, 'protein': 45, 'fat': 6, 'carbs': 0,
        'time': 20,
        'ingredients': {
            'ru': ['250г куриной грудки', 'Специи', 'Лимон'],
            'en': ['250g chicken breast', 'Spices', 'Lemon'],
            'de': ['250g Hähnchenbrust', 'Gewürze', 'Zitrone'],
            'es': ['250g pechuga de pollo', 'Especias', 'Limón'],
            'zh': ['250克鸡胸肉', '调料', '柠檬']
        },
        'steps': {
            'ru': ['Замариновать курицу', 'Жарить на гриле 7 мин с каждой стороны'],
            'en': ['Marinate chicken', 'Grill 7 min each side'],
            'de': ['Hähnchen marinieren', '7 Min pro Seite grillen'],
            'es': ['Marinar pollo', 'Asar 7 min por lado'],
            'zh': ['腌制鸡肉', '每面烤7分钟']
        }
    },
    {
        'id': 'tuna_salad',
        'category': 'high_protein',
        'name': {'ru': 'Салат с тунцом', 'en': 'Tuna Salad', 'de': 'Thunfischsalat', 'es': 'Ensalada de atún', 'zh': '金枪鱼沙拉'},
        'calories': 280, 'protein': 35, 'fat': 12, 'carbs': 8,
        'time': 10,
        'ingredients': {
            'ru': ['1 банка тунца', 'Листья салата', 'Яйцо', 'Огурец'],
            'en': ['1 can tuna', 'Lettuce', 'Egg', 'Cucumber'],
            'de': ['1 Dose Thunfisch', 'Salat', 'Ei', 'Gurke'],
            'es': ['1 lata atún', 'Lechuga', 'Huevo', 'Pepino'],
            'zh': ['1罐金枪鱼', '生菜', '鸡蛋', '黄瓜']
        },
        'steps': {
            'ru': ['Смешать тунец с овощами', 'Добавить нарезанное яйцо', 'Заправить'],
            'en': ['Mix tuna with veggies', 'Add sliced egg', 'Dress'],
            'de': ['Thunfisch mit Gemüse mischen', 'Ei hinzufügen', 'Anmachen'],
            'es': ['Mezclar atún con verduras', 'Añadir huevo', 'Aliñar'],
            'zh': ['将金枪鱼与蔬菜混合', '加切片鸡蛋', '调味']
        }
    },
    {
        'id': 'egg_whites',
        'category': 'high_protein',
        'name': {'ru': 'Белковый омлет', 'en': 'Egg White Omelette', 'de': 'Eiweiß-Omelett', 'es': 'Tortilla de claras', 'zh': '蛋白煎蛋'},
        'calories': 120, 'protein': 22, 'fat': 2, 'carbs': 2,
        'time': 10,
        'ingredients': {
            'ru': ['5 белков', 'Шпинат', 'Грибы'],
            'en': ['5 egg whites', 'Spinach', 'Mushrooms'],
            'de': ['5 Eiweiß', 'Spinat', 'Pilze'],
            'es': ['5 claras', 'Espinacas', 'Champiñones'],
            'zh': ['5个蛋白', '菠菜', '蘑菇']
        },
        'steps': {
            'ru': ['Взбить белки', 'Обжарить овощи', 'Залить белками', 'Готовить 5 мин'],
            'en': ['Beat whites', 'Fry veggies', 'Pour whites', 'Cook 5 min'],
            'de': ['Eiweiß schlagen', 'Gemüse braten', 'Eiweiß drüber', '5 Min garen'],
            'es': ['Batir claras', 'Freír verduras', 'Verter claras', 'Cocinar 5 min'],
            'zh': ['打蛋白', '炒蔬菜', '倒入蛋白', '煮5分钟']
        }
    },
    # Дополнительные рецепты
    {
        'id': 'avocado_toast',
        'category': 'breakfast',
        'name': {'ru': 'Авокадо-тост', 'en': 'Avocado Toast', 'de': 'Avocado-Toast', 'es': 'Tostada de aguacate', 'zh': '牛油果吐司'},
        'calories': 290, 'protein': 8, 'fat': 18, 'carbs': 25,
        'time': 8,
        'ingredients': {
            'ru': ['1 авокадо', '2 ломтика хлеба', 'Лимонный сок', 'Соль'],
            'en': ['1 avocado', '2 bread slices', 'Lemon juice', 'Salt'],
            'de': ['1 Avocado', '2 Brotscheiben', 'Zitronensaft', 'Salz'],
            'es': ['1 aguacate', '2 rebanadas de pan', 'Jugo de limón', 'Sal'],
            'zh': ['1个牛油果', '2片面包', '柠檬汁', '盐']
        },
        'steps': {
            'ru': ['Поджарить хлеб', 'Размять авокадо', 'Намазать на хлеб', 'Добавить лимон и соль'],
            'en': ['Toast bread', 'Mash avocado', 'Spread on bread', 'Add lemon and salt'],
            'de': ['Brot toasten', 'Avocado zerdrücken', 'Auf Brot verteilen', 'Zitrone und Salz dazu'],
            'es': ['Tostar pan', 'Machacar aguacate', 'Untar en pan', 'Añadir limón y sal'],
            'zh': ['烤面包', '捣碎牛油果', '涂在面包上', '加柠檬和盐']
        }
    },
    {
        'id': 'smoothie_bowl',
        'category': 'breakfast',
        'name': {'ru': 'Смузи-боул', 'en': 'Smoothie Bowl', 'de': 'Smoothie-Bowl', 'es': 'Bowl de smoothie', 'zh': '思慕雪碗'},
        'calories': 320, 'protein': 12, 'fat': 8, 'carbs': 50,
        'time': 10,
        'ingredients': {
            'ru': ['Замороженные ягоды', 'Банан', 'Йогурт', 'Гранола'],
            'en': ['Frozen berries', 'Banana', 'Yogurt', 'Granola'],
            'de': ['Gefrorene Beeren', 'Banane', 'Joghurt', 'Müsli'],
            'es': ['Bayas congeladas', 'Plátano', 'Yogur', 'Granola'],
            'zh': ['冷冻浆果', '香蕉', '酸奶', '格兰诺拉麦片']
        },
        'steps': {
            'ru': ['Смешать ягоды и банан', 'Добавить йогурт', 'Выложить в миску', 'Украсить гранолой'],
            'en': ['Blend berries and banana', 'Add yogurt', 'Pour in bowl', 'Top with granola'],
            'de': ['Beeren und Banane mixen', 'Joghurt dazu', 'In Schüssel geben', 'Mit Müsli toppen'],
            'es': ['Mezclar bayas y plátano', 'Añadir yogur', 'Verter en bol', 'Decorar con granola'],
            'zh': ['混合浆果和香蕉', '加酸奶', '倒入碗中', '撒上格兰诺拉']
        }
    },
    {
        'id': 'pasta_chicken',
        'category': 'lunch',
        'name': {'ru': 'Паста с курицей', 'en': 'Chicken Pasta', 'de': 'Hähnchen-Pasta', 'es': 'Pasta con pollo', 'zh': '鸡肉意面'},
        'calories': 520, 'protein': 35, 'fat': 15, 'carbs': 60,
        'time': 25,
        'ingredients': {
            'ru': ['150г пасты', '200г курицы', 'Томатный соус', 'Базилик'],
            'en': ['150g pasta', '200g chicken', 'Tomato sauce', 'Basil'],
            'de': ['150g Pasta', '200g Hähnchen', 'Tomatensauce', 'Basilikum'],
            'es': ['150g pasta', '200g pollo', 'Salsa de tomate', 'Albahaca'],
            'zh': ['150克意面', '200克鸡肉', '番茄酱', '罗勒']
        },
        'steps': {
            'ru': ['Сварить пасту', 'Обжарить курицу', 'Добавить соус', 'Смешать всё'],
            'en': ['Cook pasta', 'Fry chicken', 'Add sauce', 'Mix everything'],
            'de': ['Pasta kochen', 'Hähnchen braten', 'Sauce dazu', 'Alles mischen'],
            'es': ['Cocinar pasta', 'Freír pollo', 'Añadir salsa', 'Mezclar todo'],
            'zh': ['煮意面', '煎鸡肉', '加酱', '混合']
        }
    },
    {
        'id': 'quinoa_bowl',
        'category': 'lunch',
        'name': {'ru': 'Боул с киноа', 'en': 'Quinoa Bowl', 'de': 'Quinoa-Bowl', 'es': 'Bowl de quinoa', 'zh': '藜麦碗'},
        'calories': 420, 'protein': 18, 'fat': 14, 'carbs': 55,
        'time': 20,
        'ingredients': {
            'ru': ['100г киноа', 'Авокадо', 'Нут', 'Овощи'],
            'en': ['100g quinoa', 'Avocado', 'Chickpeas', 'Vegetables'],
            'de': ['100g Quinoa', 'Avocado', 'Kichererbsen', 'Gemüse'],
            'es': ['100g quinoa', 'Aguacate', 'Garbanzos', 'Verduras'],
            'zh': ['100克藜麦', '牛油果', '鹰嘴豆', '蔬菜']
        },
        'steps': {
            'ru': ['Сварить киноа', 'Нарезать овощи', 'Выложить в миску', 'Добавить нут и авокадо'],
            'en': ['Cook quinoa', 'Chop vegetables', 'Put in bowl', 'Add chickpeas and avocado'],
            'de': ['Quinoa kochen', 'Gemüse schneiden', 'In Schüssel geben', 'Kichererbsen und Avocado dazu'],
            'es': ['Cocinar quinoa', 'Cortar verduras', 'Poner en bol', 'Añadir garbanzos y aguacate'],
            'zh': ['煮藜麦', '切蔬菜', '放入碗中', '加鹰嘴豆和牛油果']
        }
    },
    {
        'id': 'steak_veggies',
        'category': 'dinner',
        'name': {'ru': 'Стейк с овощами', 'en': 'Steak with Vegetables', 'de': 'Steak mit Gemüse', 'es': 'Filete con verduras', 'zh': '牛排配蔬菜'},
        'calories': 450, 'protein': 42, 'fat': 25, 'carbs': 12,
        'time': 25,
        'ingredients': {
            'ru': ['200г говядины', 'Спаржа', 'Грибы', 'Розмарин'],
            'en': ['200g beef', 'Asparagus', 'Mushrooms', 'Rosemary'],
            'de': ['200g Rindfleisch', 'Spargel', 'Pilze', 'Rosmarin'],
            'es': ['200g ternera', 'Espárragos', 'Champiñones', 'Romero'],
            'zh': ['200克牛肉', '芦笋', '蘑菇', '迷迭香']
        },
        'steps': {
            'ru': ['Обжарить стейк', 'Отдельно обжарить овощи', 'Подавать вместе'],
            'en': ['Fry steak', 'Fry vegetables separately', 'Serve together'],
            'de': ['Steak braten', 'Gemüse separat braten', 'Zusammen servieren'],
            'es': ['Freír filete', 'Freír verduras por separado', 'Servir junto'],
            'zh': ['煎牛排', '另外炒蔬菜', '一起上桌']
        }
    },
    {
        'id': 'shrimp_salad',
        'category': 'dinner',
        'name': {'ru': 'Салат с креветками', 'en': 'Shrimp Salad', 'de': 'Garnelensalat', 'es': 'Ensalada de gambas', 'zh': '虾沙拉'},
        'calories': 280, 'protein': 28, 'fat': 14, 'carbs': 10,
        'time': 15,
        'ingredients': {
            'ru': ['200г креветок', 'Руккола', 'Черри', 'Оливковое масло'],
            'en': ['200g shrimp', 'Arugula', 'Cherry tomatoes', 'Olive oil'],
            'de': ['200g Garnelen', 'Rúcula', 'Kirschtomaten', 'Olivenöl'],
            'es': ['200g gambas', 'Rúcula', 'Tomates cherry', 'Aceite de oliva'],
            'zh': ['200克虾', '芝麻菜', '樱桃番茄', '橄榄油']
        },
        'steps': {
            'ru': ['Обжарить креветки', 'Смешать с зеленью', 'Заправить маслом'],
            'en': ['Fry shrimp', 'Mix with greens', 'Dress with oil'],
            'de': ['Garnelen braten', 'Mit Grün mischen', 'Mit Öl anmachen'],
            'es': ['Freír gambas', 'Mezclar con verdes', 'Aliñar'],
            'zh': ['煎虾', '与蔬菜混合', '用油调味']
        }
    },
    {
        'id': 'hummus_veggies',
        'category': 'snack',
        'name': {'ru': 'Хумус с овощами', 'en': 'Hummus with Veggies', 'de': 'Hummus mit Gemüse', 'es': 'Hummus con verduras', 'zh': '鹰嘴豆泥配蔬菜'},
        'calories': 200, 'protein': 8, 'fat': 10, 'carbs': 20,
        'time': 5,
        'ingredients': {
            'ru': ['100г хумуса', 'Морковь', 'Сельдерей', 'Огурец'],
            'en': ['100g hummus', 'Carrot', 'Celery', 'Cucumber'],
            'de': ['100g Hummus', 'Karotte', 'Sellerie', 'Gurke'],
            'es': ['100g hummus', 'Zanahoria', 'Apio', 'Pepino'],
            'zh': ['100克鹰嘴豆泥', '胡萝卜', '芹菜', '黄瓜']
        },
        'steps': {
            'ru': ['Нарезать овощи палочками', 'Подавать с хумусом'],
            'en': ['Cut veggies into sticks', 'Serve with hummus'],
            'de': ['Gemüse in Sticks schneiden', 'Mit Hummus servieren'],
            'es': ['Cortar verduras en palitos', 'Servir con hummus'],
            'zh': ['把蔬菜切成条', '配鹰嘴豆泥']
        }
    },
    {
        'id': 'cottage_apple',
        'category': 'snack',
        'name': {'ru': 'Творог с яблоком', 'en': 'Cottage Cheese with Apple', 'de': 'Quark mit Apfel', 'es': 'Requesón con manzana', 'zh': '苹果奶酪'},
        'calories': 180, 'protein': 20, 'fat': 4, 'carbs': 18,
        'time': 5,
        'ingredients': {
            'ru': ['150г творога', '1 яблоко', 'Корица'],
            'en': ['150g cottage cheese', '1 apple', 'Cinnamon'],
            'de': ['150g Quark', '1 Apfel', 'Zimt'],
            'es': ['150g requesón', '1 manzana', 'Canela'],
            'zh': ['150克奶酪', '1个苹果', '肉桂']
        },
        'steps': {
            'ru': ['Нарезать яблоко', 'Смешать с творогом', 'Посыпать корицей'],
            'en': ['Dice apple', 'Mix with cottage cheese', 'Sprinkle cinnamon'],
            'de': ['Apfel würfeln', 'Mit Quark mischen', 'Zimt drüber'],
            'es': ['Cortar manzana', 'Mezclar con requesón', 'Espolvorear canela'],
            'zh': ['切苹果', '与奶酪混合', '撒肉桂']
        }
    },
    {
        'id': 'beef_stir_fry',
        'category': 'high_protein',
        'name': {'ru': 'Говядина стир-фрай', 'en': 'Beef Stir Fry', 'de': 'Rindfleisch Stir-Fry', 'es': 'Salteado de ternera', 'zh': '牛肉炒菜'},
        'calories': 380, 'protein': 38, 'fat': 18, 'carbs': 12,
        'time': 20,
        'ingredients': {
            'ru': ['250г говядины', 'Брокколи', 'Соевый соус', 'Имбирь'],
            'en': ['250g beef', 'Broccoli', 'Soy sauce', 'Ginger'],
            'de': ['250g Rindfleisch', 'Brokkoli', 'Sojasauce', 'Ingwer'],
            'es': ['250g ternera', 'Brócoli', 'Salsa de soja', 'Jengibre'],
            'zh': ['250克牛肉', '西兰花', '酱油', '姜']
        },
        'steps': {
            'ru': ['Нарезать мясо', 'Обжарить на сильном огне', 'Добавить овощи и соус'],
            'en': ['Slice meat', 'Stir fry on high heat', 'Add veggies and sauce'],
            'de': ['Fleisch schneiden', 'Bei hoher Hitze braten', 'Gemüse und Sauce dazu'],
            'es': ['Cortar carne', 'Saltear a fuego alto', 'Añadir verduras y salsa'],
            'zh': ['切肉', '大火翻炒', '加蔬菜和酱']
        }
    },
    {
        'id': 'tofu_bowl',
        'category': 'high_protein',
        'name': {'ru': 'Боул с тофу', 'en': 'Tofu Bowl', 'de': 'Tofu-Bowl', 'es': 'Bowl de tofu', 'zh': '豆腐碗'},
        'calories': 340, 'protein': 25, 'fat': 16, 'carbs': 28,
        'time': 20,
        'ingredients': {
            'ru': ['200г тофу', 'Рис', 'Эдамаме', 'Кунжут'],
            'en': ['200g tofu', 'Rice', 'Edamame', 'Sesame'],
            'de': ['200g Tofu', 'Reis', 'Edamame', 'Sesam'],
            'es': ['200g tofu', 'Arroz', 'Edamame', 'Sésamo'],
            'zh': ['200克豆腐', '米饭', '毛豆', '芝麻']
        },
        'steps': {
            'ru': ['Обжарить тофу', 'Сварить рис', 'Выложить в миску', 'Украсить кунжутом'],
            'en': ['Fry tofu', 'Cook rice', 'Put in bowl', 'Top with sesame'],
            'de': ['Tofu braten', 'Reis kochen', 'In Schüssel geben', 'Mit Sesam toppen'],
            'es': ['Freír tofu', 'Cocinar arroz', 'Poner en bol', 'Decorar con sésamo'],
            'zh': ['煎豆腐', '煮米饭', '放入碗中', '撒芝麻']
        }
    },
]

# ============== ЛОКАЛИЗАЦИЯ (5 языков) ==============

LOCALES = {
    'ru': {
        'app_title': '💪 FitWizard Pro',
        'welcome': 'Добро пожаловать!',
        'welcome_subtitle': 'Создадим идеальную программу тренировок для вас',
        'motivation_text': 'Начни путь к своей лучшей форме',
        'male': 'Мужской',
        'female': 'Женский',
        'select': 'Выбрать',
        'male_desc': 'Силовые тренировки\nНабор массы',
        'female_desc': 'Тонус и стройность\nГибкость',
        'continue_btn': 'ПРОДОЛЖИТЬ',
        'back_btn': '← НАЗАД',
        # Параметры
        'enter_data': 'ВВЕДИТЕ ВАШИ ДАННЫЕ',
        'height': 'Рост',
        'weight': 'Вес',
        'age': 'Возраст',
        'cm': 'СМ',
        'kg': 'КГ',
        'years': 'ЛЕТ',
        'days_per_week': 'Дней в неделю:',
        'weeks_program': 'Недель программы:',
        'level': 'Уровень:',
        'beginner': 'Новичок',
        'intermediate': 'Средний',
        'advanced': 'Продвинутый',
        # Валидация
        'error_height': '⚠️ Введите рост!',
        'error_weight': '⚠️ Введите вес!',
        'error_age': '⚠️ Введите возраст!',
        'error_height_range': '⚠️ Рост: 120-250 см!',
        'error_weight_range': '⚠️ Вес: 40-200 кг!',
        'error_age_range': '⚠️ Возраст: 14-80 лет!',
        # Цели
        'choose_goal': 'ВЫБЕРИТЕ ЦЕЛЬ',
        'goal_subtitle': 'Что вы хотите достичь?',
        'weight_loss': 'Сброс веса',
        'weight_loss_desc': 'HIIT-тренировки для сжигания калорий',
        'muscle_gain': 'Набор массы',
        'muscle_gain_desc': 'Силовые упражнения для роста мышц',
        # Фокус
        'choose_zone': 'ВЫБЕРИТЕ ЗОНУ',
        'Full Body': 'Всё тело',
        'Legs': 'Ноги',
        'Chest': 'Грудь',
        'Back': 'Спина',
        'Arms': 'Руки',
        'Shoulders': 'Плечи',
        'Core': 'Пресс',
        # Безопасность
        'safety_title': '⚠️ БЕЗОПАСНОСТЬ',
        'safety_subtitle': 'Ознакомьтесь с рекомендациями',
        'safety_60plus': '🔴 ВАЖНО ДЛЯ 60+',
        'safety_60_1': '⚠️ Обязательно проконсультируйтесь с врачом',
        'safety_60_2': '🫀 Разрешение кардиолога при болезнях сердца',
        'safety_60_3': '🚫 Избегайте резких движений',
        'safety_50plus': '🟡 РЕКОМЕНДАЦИИ ДЛЯ 50+',
        'safety_50_1': '👨‍⚕️ Рекомендуется консультация врача',
        'safety_50_2': '🔥 Особое внимание к разминке',
        'safety_50_3': '💪 Контролируйте пульс',
        'safety_teen': '🟢 ДЛЯ ПОДРОСТКОВ (14-17)',
        'safety_teen_1': '📚 Тренировки адаптированы для роста',
        'safety_teen_2': '🚫 Избегайте нагрузок на позвоночник',
        'safety_teen_3': '👨‍👩‍👦 Согласуйте с родителями',
        'safety_general': '✅ ОБЩИЕ РЕКОМЕНДАЦИИ',
        'safety_gen_1': '👨‍⚕️ При болезнях - к врачу',
        'safety_gen_2': '🛑 Остановитесь при боли',
        'safety_gen_3': '🔥 Всегда делайте разминку',
        'safety_agree': 'Я ознакомился и готов начать',
        # Питание
        'nutrition_title': '🍽️ ПЛАН ПИТАНИЯ',
        'nutrition_subtitle': 'Калории для вашей цели',
        'kcal_day': 'ККАЛ/ДЕНЬ',
        'protein': 'БЕЛКИ',
        'fats': 'ЖИРЫ',
        'carbs': 'УГЛЕВОДЫ',
        'g': 'г',
        'nutrition_tips': '💡 Рекомендации:',
        'tip1': '• Пейте 2-3 литра воды в день',
        'tip2': '• Ешьте 4-5 раз небольшими порциями',
        'tip3': '• Белок в каждом приёме пищи',
        'tip4': '• Углеводы до 16:00',
        'tip5': '• Избегайте сахара',
        'to_program': 'К ПРОГРАММЕ',
        # Результат
        'program_ready': '📋 ВАША ПРОГРАММА',
        'week': 'Неделя',
        'day': 'День',
        'exercises': 'упражнений',
        'sets': 'подходов',
        'start_btn': '▶️ Начать',
        'completed': 'Завершено',
        'locked': '🔒',
        'save_program': '💾 Сохранить',
        'my_progress': '📈 Прогресс',
        'diary': '📊 Дневник',
        'new_program': '🔄 Новая',
        # Тренировка
        'workout_title': '▶️ ТРЕНИРОВКА',
        'exercise': 'Упражнение',
        'set': 'Подход',
        'of': 'из',
        'reps': 'повторений',
        'seconds': 'секунд',
        'hold': 'Держать',
        'rest': 'Отдых',
        'complete_set': '✅ Подход выполнен',
        'skip_exercise': '⏭️ Пропустить',
        'simplify': '😓 Упростить',
        'finish_workout': '❌ Завершить',
        'rest_between': 'Отдых между подходами',
        'sec': 'сек',
        'start_timer': '▶️ Старт',
        # Типы упражнений
        'compound': '🔸 Базовое',
        'isolation': '🔹 Изоляция',
        'core': '🎯 Пресс',
        'cardio': '🏃 Кардио',
        # Прогресс
        'progress_title': '📊 МОЙ ПРОГРЕСС',
        'weight_title': '⚖️ ВЕС',
        'measurements': '📏 ЗАМЕРЫ (см)',
        'chest_label': '💪 Грудь:',
        'waist_label': '👖 Талия:',
        'hips_label': '🍑 Бёдра:',
        'arms_label': '💪 Руки:',
        'add_btn': '➕ Добавить',
        'save_btn': '💾 Сохранить',
        'photos_title': '📷 ФОТО ПРОГРЕССА',
        'no_photos': 'Нет фотографий',
        'add_photo': '📸 Добавить фото',
        'back_to_program': '← К ПРОГРАММЕ',
        # Дневник
        'diary_title': '📊 ДНЕВНИК ТРЕНИРОВОК',
        'total_workouts': 'Всего тренировок',
        'great_progress': '✅ Отличный прогресс!',
        # Результаты тренировки
        'workout_complete': '🎉 ОТЛИЧНО!',
        'workout_finished': 'Тренировка завершена!',
        # Рекомендации
        'rec_title': '💡 Рекомендации',
        # Настройки
        'settings': '⚙️ Настройки',
        'language': 'Язык',
        'theme': 'Тема',
        'dark': 'Тёмная',
        'light': 'Светлая',
        # Рецепты
        'recipes_title': '🍽️ РЕЦЕПТЫ',
        'recipes_subtitle': 'Полезные блюда для вашей цели',
        'all_recipes': '📋 Все',
        'breakfast': '🌅 Завтраки',
        'lunch': '🍲 Обеды',
        'dinner': '🌙 Ужины',
        'snack': '🍎 Перекусы',
        'high_protein': '💪 Высокобелковые',
        'recipe_ingredients': '📝 Ингредиенты',
        'recipe_steps': '👨‍🍳 Приготовление',
        'cooking_time': '⏱️ Время:',
        'minutes': 'мин',
        'view_recipes': '🍽️ Рецепты',
        # Дневник и статистика
        'diary': '📓 Дневник',
        'workout_history': 'История тренировок',
        'no_history': 'История пуста. Начните тренировку!',
        'completed_workouts': 'Тренировок',
        'load_program': '📂 Загрузить',
        'program_saved': 'Программа сохранена!',
        'program_loaded': 'Программа загружена!',
        'no_saved_program': 'Нет сохранённой программы',
        'hold_time': 'Удерживайте!',
        'seconds': 'секунд',
        'skip_rest': '⏩ Пропустить',
        'hold_exercise': '💪 Удержание',
        # Разминка и растяжка
        'warmup': 'РАЗМИНКА',
        'stretching': 'РАСТЯЖКА',
        'stretching_complete': 'Растяжка завершена!',
        'great_job': 'Отличная работа!',
        # Достижения
        'achievements': '🏆 Достижения',
        'unlocked': 'открыто',
        'ach_first': 'Первый шаг',
        'ach_first_desc': 'Первая тренировка!',
        'ach_five': 'На старте',
        'ach_five_desc': '5 тренировок',
        'ach_ten': 'Набираем темп',
        'ach_ten_desc': '10 тренировок',
        'ach_twentyfive': 'Железная воля',
        'ach_twentyfive_desc': '25 тренировок',
        'ach_fifty': 'Машина',
        'ach_fifty_desc': '50 тренировок',
        'ach_hundred': 'Легенда',
        'ach_hundred_desc': '100 тренировок',
        'ach_week': 'Неделя огня',
        'ach_week_desc': '7 дней подряд',
        # Калькуляторы
        'calculators': '🧮 Калькуляторы',
        'bmi_calc': '📊 Калькулятор ИМТ',
        'calorie_calc': '🔥 Калории',
        'water_calc': '💧 Норма воды',
        'ideal_weight_calc': '⚖️ Идеальный вес',
        'body_fat_calc': '📐 Процент жира',
        'bmi_underweight': 'Недостаточный вес',
        'bmi_normal': 'Нормальный вес',
        'bmi_overweight': 'Избыточный вес',
        'bmi_obese': 'Ожирение',
        'bmi_scale': 'Шкала ИМТ:',
        'bmr_desc': 'Базовый обмен веществ',
        'daily_calories': 'Дневная норма калорий:',
        'activity_sedentary': 'Сидячий образ жизни',
        'activity_light': 'Лёгкая активность',
        'activity_moderate': 'Умеренная активность',
        'activity_active': 'Высокая активность',
        'activity_very_active': 'Очень высокая',
        'per_day': 'в день',
        'glasses': 'стаканов',
        'water_tips': 'Советы:',
        'water_tip_1': 'Пейте воду до жажды',
        'water_tip_2': 'Стакан воды утром натощак',
        'water_tip_3': 'Увеличьте норму при тренировках',
        'ideal_weight_range': 'По разным формулам',
        'your_height': 'Ваш рост',
        'bf_athlete': 'Атлет',
        'bf_fitness': 'Фитнес',
        'bf_average': 'Средний',
        'bf_above': 'Выше нормы',
        'bf_note': 'Примерная оценка по формуле Deurenberg',
        # Советы
        'tips_title': '💡 Советы',
        'tip_warmup_title': 'Разминка обязательна',
        'tip_warmup_text': 'Всегда разогревайте мышцы перед тренировкой',
        'tip_water_title': 'Пейте воду',
        'tip_water_text': 'Пейте воду во время и после тренировки',
        'tip_sleep_title': 'Высыпайтесь',
        'tip_sleep_text': 'Мышцы растут во время сна. Спите 7-9 часов',
        'tip_nutrition_title': 'Правильное питание',
        'tip_nutrition_text': 'Питайтесь сбалансированно, ешьте достаточно белка',
        'tip_progress_title': 'Прогрессия нагрузок',
        'tip_progress_text': 'Постепенно увеличивайте нагрузку',
        'tip_rest_title': 'Отдых важен',
        'tip_rest_text': 'Давайте мышцам время на восстановление',
        'tip_technique_title': 'Техника важнее веса',
        'tip_technique_text': 'Правильная техника предотвращает травмы',
        'tip_goals_title': 'Ставьте цели',
        'tip_goals_text': 'Конкретные цели мотивируют лучше',
        # Статистика
        'statistics': '📊 Статистика',
        'workouts': 'тренировок',
        'calories_burned': 'ккал сожжено',
        'total_time': 'минут',
        'muscle_groups': 'Группы мышц:',
        'no_data': 'Нет данных',
        # О приложении
        'about': 'ℹ️ О приложении',
        'about_desc': 'Персональный тренер в вашем кармане. Создавайте программы тренировок, отслеживайте прогресс, достигайте целей!',
        'supported_languages': 'Языки',
        'platforms': 'Платформы',
    },
    'en': {
        'app_title': '💪 FitWizard Pro',
        'welcome': 'Welcome!',
        'welcome_subtitle': "Let's create the perfect workout program for you",
        'motivation_text': 'Start your journey to your best shape',
        'male': 'Male',
        'female': 'Female',
        'select': 'Select',
        'male_desc': 'Strength Training\nMuscle Building',
        'female_desc': 'Toning and Fitness\nFlexibility',
        'continue_btn': 'CONTINUE',
        'back_btn': '← BACK',
        'enter_data': 'ENTER YOUR DATA',
        'height': 'Height',
        'weight': 'Weight',
        'age': 'Age',
        'cm': 'CM',
        'kg': 'KG',
        'years': 'YEARS',
        'days_per_week': 'Days per week:',
        'weeks_program': 'Program weeks:',
        'level': 'Level:',
        'beginner': 'Beginner',
        'intermediate': 'Intermediate',
        'advanced': 'Advanced',
        'error_height': '⚠️ Enter height!',
        'error_weight': '⚠️ Enter weight!',
        'error_age': '⚠️ Enter age!',
        'error_height_range': '⚠️ Height: 120-250 cm!',
        'error_weight_range': '⚠️ Weight: 40-200 kg!',
        'error_age_range': '⚠️ Age: 14-80 years!',
        'choose_goal': 'CHOOSE YOUR GOAL',
        'goal_subtitle': 'What do you want to achieve?',
        'weight_loss': 'Weight Loss',
        'weight_loss_desc': 'HIIT workouts for burning calories',
        'muscle_gain': 'Build Muscle',
        'muscle_gain_desc': 'Strength exercises for muscle growth',
        'choose_zone': 'CHOOSE ZONE',
        'Full Body': 'Full Body',
        'Legs': 'Legs',
        'Chest': 'Chest',
        'Back': 'Back',
        'Arms': 'Arms',
        'Shoulders': 'Shoulders',
        'Core': 'Core',
        'safety_title': '⚠️ SAFETY FIRST',
        'safety_subtitle': 'Please read the recommendations',
        'safety_60plus': '🔴 IMPORTANT FOR 60+',
        'safety_60_1': '⚠️ Consult your doctor',
        'safety_60_2': '🫀 Cardiologist approval for heart conditions',
        'safety_60_3': '🚫 Avoid sudden movements',
        'safety_50plus': '🟡 RECOMMENDATIONS FOR 50+',
        'safety_50_1': '👨‍⚕️ Doctor consultation recommended',
        'safety_50_2': '🔥 Pay attention to warm-up',
        'safety_50_3': '💪 Controle Siehr Puls',
        'safety_teen': '🟢 FOR TEENAGERS (14-17)',
        'safety_teen_1': '📚 Training adapted for growth',
        'safety_teen_2': '🚫 Avoid spine overload',
        'safety_teen_3': '👨‍👩‍👦 Coordinate with parents',
        'safety_general': '✅ GENERAL RECOMMENDATIONS',
        'safety_gen_1': '👨‍⚕️ Consult doctor if ill',
        'safety_gen_2': '🛑 Stop if you feel pain',
        'safety_gen_3': '🔥 Always warm up',
        'safety_agree': "I've read and ready to start",
        'nutrition_title': '🍽️ NUTRITION PLAN',
        'nutrition_subtitle': 'Calories for your goal',
        'kcal_day': 'KCAL/DAY',
        'protein': 'PROTEIN',
        'fats': 'FETTE',
        'carbs': 'CARBOHIDRATOS',
        'g': 'g',
        'nutrition_tips': '💡 Tips:',
        'tip1': '• Drink 2-3 liters of water daily',
        'tip2': '• Eat 4-5 small meals',
        'tip3': '• Protein with every meal',
        'tip4': '• Carbs before 4 PM',
        'tip5': '• Avoid sugar',
        'to_program': 'TO PROGRAM',
        'program_ready': '📋 YOUR PROGRAM',
        'week': 'Week',
        'day': 'Day',
        'exercises': 'exercises',
        'sets': 'sets',
        'start_btn': '▶️ Start',
        'completed': 'Completed',
        'locked': '🔒',
        'save_program': '💾 Save',
        'my_progress': '📈 Progress',
        'diary': '📊 Diary',
        'new_program': '🔄 New',
        'workout_title': '▶️ TRAINING',
        'exercise': 'Exercise',
        'set': 'Serie',
        'of': 'de',
        'reps': 'reps',
        'seconds': 'seconds',
        'hold': 'Hold',
        'rest': 'Rest',
        'complete_set': '✅ Satz fertig',
        'skip_exercise': '⏭️ Skip',
        'simplify': '😓 Simplify',
        'finish_workout': '❌ Finish',
        'rest_between': 'Rest between sets',
        'sec': 'sec',
        'start_timer': '▶️ Start',
        'compound': '🔸 Compound',
        'isolation': '🔹 Isolation',
        'core': '🎯 Core',
        'cardio': '🏃 Cardio',
        'progress_title': '📊 MY PROGRESS',
        'weight_title': '⚖️ WEIGHT',
        'measurements': '📏 MEASUREMENTS (cm)',
        'chest_label': '💪 Chest:',
        'waist_label': '👖 Waist:',
        'hips_label': '🍑 Hips:',
        'arms_label': '💪 Arms:',
        'add_btn': '➕ Add',
        'save_btn': '💾 Save',
        'photos_title': '📷 PROGRESS PHOTOS',
        'no_photos': 'No photos',
        'add_photo': '📸 Add photo',
        'back_to_program': '← TO PROGRAM',
        'diary_title': '📊 TRAININGSTAGEBUCH',
        'total_workouts': 'Trainings gesamt',
        'great_progress': '✅ Super Fortschritt!',
        'workout_complete': '🎉 SUPER!',
        'workout_finished': 'Training beendet!',
        'rec_title': '💡 Recommendations',
        'settings': '⚙️ Settings',
        'language': 'Language',
        'theme': 'Theme',
        'dark': 'Dark',
        'light': 'Light',
        # Recipes
        'recipes_title': '🍽️ RECIPES',
        'recipes_subtitle': 'Healthy meals for your goal',
        'all_recipes': '📋 All',
        'breakfast': '🌅 Breakfast',
        'lunch': '🍲 Lunch',
        'dinner': '🌙 Dinner',
        'snack': '🍎 Snacks',
        'high_protein': '💪 High Protein',
        'recipe_ingredients': '📝 Ingredients',
        'recipe_steps': '👨‍🍳 Preparation',
        'cooking_time': '⏱️ Time:',
        'minutes': 'min',
        'view_recipes': '🍽️ Recipes',
        # Diary and stats
        'diary': '📓 Diary',
        'workout_history': 'Workout History',
        'no_history': 'History is empty. Start a workout!',
        'completed_workouts': 'Workouts',
        'load_program': '📂 Load',
        'program_saved': 'Program saved!',
        'program_loaded': 'Program loaded!',
        'no_saved_program': 'No saved program',
        'hold_time': 'Hold it!',
        'seconds': 'seconds',
        'skip_rest': '⏩ Skip',
        'hold_exercise': '💪 Hold',
        # Warmup and stretching
        'warmup': 'WARM UP',
        'stretching': 'STRETCHING',
        'stretching_complete': 'Stretching complete!',
        'great_job': 'Great job!',
        # Achievements
        'achievements': '🏆 Achievements',
        'unlocked': 'unlocked',
        'ach_first': 'First Step',
        'ach_first_desc': 'First workout!',
        'ach_five': 'Getting Started',
        'ach_five_desc': '5 workouts',
        'ach_ten': 'Building Momentum',
        'ach_ten_desc': '10 workouts',
        'ach_twentyfive': 'Iron Will',
        'ach_twentyfive_desc': '25 workouts',
        'ach_fifty': 'Machine',
        'ach_fifty_desc': '50 workouts',
        'ach_hundred': 'Legend',
        'ach_hundred_desc': '100 workouts',
        'ach_week': 'Week on Fire',
        'ach_week_desc': '7 days in a row',
        # Calculators
        'calculators': '🧮 Calculators',
        'bmi_calc': '📊 BMI Calculator',
        'calorie_calc': '🔥 Calories',
        'water_calc': '💧 Water Intake',
        'ideal_weight_calc': '⚖️ Ideal Weight',
        'body_fat_calc': '📐 Body Fat',
        'bmi_underweight': 'Underweight',
        'bmi_normal': 'Normal weight',
        'bmi_overweight': 'Overweight',
        'bmi_obese': 'Obese',
        'bmi_scale': 'BMI Scale:',
        'bmr_desc': 'Basal Metabolic Rate',
        'daily_calories': 'Daily calorie needs:',
        'activity_sedentary': 'Sedentary',
        'activity_light': 'Light activity',
        'activity_moderate': 'Moderate activity',
        'activity_active': 'Active',
        'activity_very_active': 'Very active',
        'per_day': 'per day',
        'glasses': 'glasses',
        'water_tips': 'Tips:',
        'water_tip_1': 'Drink water before thirst',
        'water_tip_2': 'Glass of water in the morning',
        'water_tip_3': 'Increase intake during workouts',
        'ideal_weight_range': 'Based on different formulas',
        'your_height': 'Your height',
        'bf_athlete': 'Athlete',
        'bf_fitness': 'Fitness',
        'bf_average': 'Average',
        'bf_above': 'Above average',
        'bf_note': 'Estimate based on Deurenberg formula',
        # Tips
        'tips_title': '💡 Tips',
        'tip_warmup_title': 'Warm up is essential',
        'tip_warmup_text': 'Always warm up muscles before training',
        'tip_water_title': 'Stay hydrated',
        'tip_water_text': 'Drink water during and after workout',
        'tip_sleep_title': 'Get enough sleep',
        'tip_sleep_text': 'Muscles grow during sleep. Get 7-9 hours',
        'tip_nutrition_title': 'Proper nutrition',
        'tip_nutrition_text': 'Eat balanced, get enough protein',
        'tip_progress_title': 'Progressive overload',
        'tip_progress_text': 'Gradually increase the load',
        'tip_rest_title': 'Rest is important',
        'tip_rest_text': 'Give muscles time to recover',
        'tip_technique_title': 'Technique over weight',
        'tip_technique_text': 'Proper technique prevents injuries',
        'tip_goals_title': 'Set goals',
        'tip_goals_text': 'Specific goals motivate better',
        # Statistics
        'statistics': '📊 Statistics',
        'workouts': 'workouts',
        'calories_burned': 'kcal burned',
        'total_time': 'minutes',
        'muscle_groups': 'Muscle groups:',
        'no_data': 'No data',
        # About
        'about': 'ℹ️ About',
        'about_desc': 'Personal trainer in your pocket. Create workout programs, track progress, achieve goals!',
        'supported_languages': 'Languages',
        'platforms': 'Platforms',
    },
    'de': {
        'app_title': '💪 FitWizard Pro',
        'welcome': 'Willkommen!',
        'welcome_subtitle': 'Wir erstellen das perfekte Trainingsprogramm für Sie',
        'motivation_text': 'Starten Sie Ihre Reise zu Ihrer besten Form',
        'male': 'Männlich',
        'female': 'Weiblich',
        'select': 'Wählen',
        'male_desc': 'Krafttraining\nMuskelaufbau',
        'female_desc': 'Toning und Fitness\nFlexibilität',
        'continue_btn': 'WEITER',
        'back_btn': '← ZURÜCK',
        'enter_data': 'GEBEN SIE IHRE DATEN EIN',
        'height': 'Größe',
        'weight': 'Gewicht',
        'age': 'Alter',
        'cm': 'CM',
        'kg': 'KG',
        'years': 'JAHRE',
        'days_per_week': 'Tage pro Woche:',
        'weeks_program': 'Programmwochen:',
        'level': 'Level:',
        'beginner': 'Anfänger',
        'intermediate': 'Mittelstufe',
        'advanced': 'Fortgeschritten',
        'error_height': '⚠️ Größe eingeben!',
        'error_weight': '⚠️ Gewicht eingeben!',
        'error_age': '⚠️ Alter eingeben!',
        'error_height_range': '⚠️ Größe: 120-250 cm!',
        'error_weight_range': '⚠️ Gewicht: 40-200 kg!',
        'error_age_range': '⚠️ Alter: 14-80 Jahre!',
        'choose_goal': 'WÄHLEN SIE IHR ZIEL',
        'goal_subtitle': 'Was möchten Sie erreichen?',
        'weight_loss': 'Abnehmen',
        'weight_loss_desc': 'HIIT-Training zum Kalorienverbrennen',
        'muscle_gain': 'Muskelaufbau',
        'muscle_gain_desc': 'Kraftübungen für Muskelwachstum',
        'choose_zone': 'ZONE WÄHLEN',
        'Full Body': 'Ganzkörper',
        'Legs': 'Beine',
        'Chest': 'Brust',
        'Back': 'Rücken',
        'Arms': 'Arme',
        'Shoulders': 'Schultern',
        'Core': 'Core',
        'safety_title': '⚠️ SICHERHEIT',
        'safety_subtitle': 'Bitte lesen Sie die Empfehlungen',
        'safety_60plus': '🔴 WICHTIG FÜR 60+',
        'safety_60_1': '⚠️ Konsultieren Sie Ihren Arzt',
        'safety_60_2': '🫀 Kardiologe bei Herzerkrankungen',
        'safety_60_3': '🚫 Vermeiden Sie plötzliche Bewegungen',
        'safety_50plus': '🟡 EMPFEHLUNGEN FÜR 50+',
        'safety_50_1': '👨‍⚕️ Arztbesuch empfohlen',
        'safety_50_2': '🔥 Achten Sie auf Aufwärmen',
        'safety_50_3': '💪 Controle Sie Ihren Puls',
        'safety_teen': '🟢 FÜR TEENAGER (14-17)',
        'safety_teen_1': '📚 Training angepasst für Wachstum',
        'safety_teen_2': '🚫 Wirbelsäule nicht überlasten',
        'safety_teen_3': '👨‍👩‍👦 Mit Eltern abstimmen',
        'safety_general': '✅ ALLGEMEINE EMPFEHLUNGEN',
        'safety_gen_1': '👨‍⚕️ Bei Krankheit zum Arzt',
        'safety_gen_2': '🛑 Bei Schmerzen aufhören',
        'safety_gen_3': '🔥 Immer aufwärmen',
        'safety_agree': 'Ich habe gelesen und bin bereit',
        'nutrition_title': '🍽️ ERNÄHRUNGSPLAN',
        'nutrition_subtitle': 'Kalorien für Ihr Ziel',
        'kcal_day': 'KCAL/TAG',
        'protein': 'PROTEIN',
        'fats': 'FETTE',
        'carbs': 'KOHLENHYDRATE',
        'g': 'g',
        'nutrition_tips': '💡 Tipps:',
        'tip1': '• 2-3 Liter Wasser täglich',
        'tip2': '• 4-5 kleine Mahlzeiten',
        'tip3': '• Protein bei jeder Mahlzeit',
        'tip4': '• Kohlenhydrate vor 16 Uhr',
        'tip5': '• Evite Zucker',
        'to_program': 'ZUM PROGRAMM',
        'program_ready': '📋 IHR PROGRAMM',
        'week': 'Woche',
        'day': 'Tag',
        'exercises': 'Übungen',
        'sets': 'Sätze',
        'start_btn': '▶️ Start',
        'completed': 'Fertig',
        'locked': '🔒',
        'save_program': '💾 Speichern',
        'my_progress': '📈 Fortschritt',
        'diary': '📊 Tagebuch',
        'new_program': '🔄 Neu',
        'workout_title': '▶️ TRAINING',
        'exercise': 'Übung',
        'set': 'Satz',
        'of': 'von',
        'reps': 'Wdh',
        'seconds': 'Sekunden',
        'hold': 'Halten',
        'rest': 'Pause',
        'complete_set': '✅ Satz fertig',
        'skip_exercise': '⏭️ Überspringen',
        'simplify': '😓 Vereinfachen',
        'finish_workout': '❌ Beenden',
        'rest_between': 'Pause zwischen Sätzen',
        'sec': 'Sek',
        'start_timer': '▶️ Start',
        'compound': '🔸 Grundübung',
        'isolation': '🔹 Isolation',
        'core': '🎯 Core',
        'cardio': '🏃 Kardio',
        'progress_title': '📊 MEIN FORTSCHRITT',
        'weight_title': '⚖️ GEWICHT',
        'measurements': '📏 MASSE (cm)',
        'chest_label': '💪 Brust:',
        'waist_label': '👖 Taille:',
        'hips_label': '🍑 Hüfte:',
        'arms_label': '💪 Arme:',
        'add_btn': '➕ Hinzufügen',
        'save_btn': '💾 Speichern',
        'photos_title': '📷 FORTSCHRITTSFOTOS',
        'no_photos': 'Keine Fotos',
        'add_photo': '📸 Foto hinzufügen',
        'back_to_program': '← ZUM PROGRAMM',
        'diary_title': '📊 TRAININGSTAGEBUCH',
        'total_workouts': 'Trainings gesamt',
        'great_progress': '✅ Super Fortschritt!',
        'workout_complete': '🎉 SUPER!',
        'workout_finished': 'Training beendet!',
        'rec_title': '💡 Empfehlungen',
        'settings': '⚙️ Einstellungen',
        'language': 'Sprache',
        'theme': 'Thema',
        'dark': 'Dunkel',
        'light': 'Hell',
        'recipes_title': '🍽️ RECIPES',
        'recipes_subtitle': 'Gesunde Mahlzeiten für Ihr Ziel',
        'all_recipes': '📋 Alle',
        'breakfast': '🌅 Frühstück',
        'lunch': '🍲 Mittagessen',
        'dinner': '🌙 Cenas',
        'snack': '🍎 Meriendas',
        'high_protein': '💪 Proteinreich',
        'recipe_ingredients': '📝 Zutaten',
        'recipe_steps': '👨‍🍳 Zubereitung',
        'cooking_time': '⏱️ Zeit:',
        'minutes': 'Min',
        'view_recipes': '🍽️ Rezepte',
        # Tagebuch
        'diary': '📓 Tagebuch',
        'workout_history': 'Trainingsgeschichte',
        'no_history': 'Geschichte ist leer. Starten Sie ein Training!',
        'completed_workouts': 'Trainings',
        'load_program': '📂 Laden',
        'program_saved': 'Programm gespeichert!',
        'program_loaded': 'Programm geladen!',
        'no_saved_program': 'Kein gespeichertes Programm',
        'hold_time': 'Halten!',
        'seconds': 'Sekunden',
        'skip_rest': '⏩ Überspringen',
        'hold_exercise': '💪 Halten',
    },
    'es': {
        'app_title': '💪 FitWizard Pro',
        'welcome': '¡Bienvenido!',
        'welcome_subtitle': 'Crearemos el programa de entrenamiento perfecto para ti',
        'motivation_text': 'Comienza tu camino hacia tu mejor forma',
        'male': 'Masculino',
        'female': 'Femenino',
        'select': 'Elegir',
        'male_desc': 'Entrenamiento de fuerza\nGanancia muscular',
        'female_desc': 'Tonificación y fitness\nFlexibilidad',
        'continue_btn': 'CONTINUAR',
        'back_btn': '← ATRÁS',
        'enter_data': 'INGRESE SUS DATOS',
        'height': 'Altura',
        'weight': 'Peso',
        'age': 'Edad',
        'cm': 'CM',
        'kg': 'KG',
        'years': 'AÑOS',
        'days_per_week': 'Días por semana:',
        'weeks_program': 'Semanas del programa:',
        'level': 'Nivel:',
        'beginner': 'Principiante',
        'intermediate': 'Intermedio',
        'advanced': 'Avanzado',
        'error_height': '⚠️ ¡Ingrese altura!',
        'error_weight': '⚠️ ¡Ingrese peso!',
        'error_age': '⚠️ ¡Ingrese edad!',
        'error_height_range': '⚠️ Altura: 120-250 cm!',
        'error_weight_range': '⚠️ Peso: 40-200 kg!',
        'error_age_range': '⚠️ Edad: 14-80 años!',
        'choose_goal': 'ELIJA SU OBJETIVO',
        'goal_subtitle': '¿Qué quieres lograr?',
        'weight_loss': 'Pérdida de peso',
        'weight_loss_desc': 'Entrenamientos HIIT para quemar calorías',
        'muscle_gain': 'Ganar músculo',
        'muscle_gain_desc': 'Ejercicios de fuerza para crecimiento muscular',
        'choose_zone': 'ELEGIR ZONA',
        'Full Body': 'Cuerpo completo',
        'Legs': 'Piernas',
        'Chest': 'Pecho',
        'Back': 'Espalda',
        'Arms': 'Brazos',
        'Shoulders': 'Hombros',
        'Core': 'Core',
        'safety_title': '⚠️ SEGURIDAD',
        'safety_subtitle': 'Por favor lea las recomendaciones',
        'safety_60plus': '🔴 IMPORTANTE PARA 60+',
        'safety_60_1': '⚠️ Consulte a su médico',
        'safety_60_2': '🫀 Aprobación del cardiólogo para condiciones cardíacas',
        'safety_60_3': '🚫 Evite movimientos bruscos',
        'safety_50plus': '🟡 RECOMENDACIONES PARA 50+',
        'safety_50_1': '👨‍⚕️ Se recomienda consulta médica',
        'safety_50_2': '🔥 Preste atención al calentamiento',
        'safety_50_3': '💪 Controle su pulso',
        'safety_teen': '🟢 PARA ADOLESCENTES (14-17)',
        'safety_teen_1': '📚 Entrenamientos adaptados para el crecimiento',
        'safety_teen_2': '🚫 Evite sobrecargar la columna',
        'safety_teen_3': '👨‍👩‍👦 Coordine con los padres',
        'safety_general': '✅ RECOMENDACIONES GENERALES',
        'safety_gen_1': '👨‍⚕️ Consulte al médico si está enfermo',
        'safety_gen_2': '🛑 Pare si siente dolor',
        'safety_gen_3': '🔥 Siempre caliente',
        'safety_agree': 'He leído y estoy listo para empezar',
        'nutrition_title': '🍽️ PLAN DE NUTRICIÓN',
        'nutrition_subtitle': 'Calorías para su objetivo',
        'kcal_day': 'KCAL/DÍA',
        'protein': 'PROTEÍNA',
        'fats': 'GRASAS',
        'carbs': 'CARBOHIDRATOS',
        'g': 'g',
        'nutrition_tips': '💡 Consejos:',
        'tip1': '• Beba 2-3 litros de agua diarios',
        'tip2': '• Coma 4-5 comidas pequeñas',
        'tip3': '• Proteína en cada comida',
        'tip4': '• Carbohidratos antes de las 16:00',
        'tip5': '• Evite el azúcar',
        'to_program': 'AL PROGRAMA',
        'program_ready': '📋 SU PROGRAMA',
        'week': 'Semana',
        'day': 'Día',
        'exercises': 'ejercicios',
        'sets': 'series',
        'start_btn': '▶️ Iniciar',
        'completed': 'Completado',
        'locked': '🔒',
        'save_program': '💾 Guardar',
        'my_progress': '📈 Progreso',
        'diary': '📊 Diario',
        'new_program': '🔄 Nuevo',
        'workout_title': '▶️ ENTRENAMIENTO',
        'exercise': 'Ejercicio',
        'set': 'Serie',
        'of': 'de',
        'reps': 'reps',
        'seconds': 'segundos',
        'hold': 'Mantener',
        'rest': 'Descanso',
        'complete_set': '✅ Serie completa',
        'skip_exercise': '⏭️ Saltar',
        'simplify': '😓 Simplificar',
        'finish_workout': '❌ Terminar',
        'rest_between': 'Descanso entre series',
        'sec': 'seg',
        'start_timer': '▶️ Iniciar',
        'compound': '🔸 Compuesto',
        'isolation': '🔹 Aislamiento',
        'core': '🎯 Core',
        'cardio': '🏃 Cardio',
        'progress_title': '📊 MI PROGRESO',
        'weight_title': '⚖️ PESO',
        'measurements': '📏 MEDIDAS (cm)',
        'chest_label': '💪 Pecho:',
        'waist_label': '👖 Cintura:',
        'hips_label': '🍑 Caderas:',
        'arms_label': '💪 Brazos:',
        'add_btn': '➕ Añadir',
        'save_btn': '💾 Guardar',
        'photos_title': '📷 FOTOS DE PROGRESO',
        'no_photos': 'Sin fotos',
        'add_photo': '📸 Foto hinzufügen',
        'back_to_program': '← AL PROGRAMA',
        'diary_title': '📊 DIARIO DE ENTRENAMIENTO',
        'total_workouts': 'Entrenamientos totales',
        'great_progress': '✅ ¡Gran progreso!',
        'workout_complete': '🎉 ¡GENIAL!',
        'workout_finished': 'Training beendet!',
        'rec_title': '💡 Recomendaciones',
        'settings': '⚙️ Configuración',
        'language': 'Idioma',
        'theme': 'Tema',
        'dark': 'Oscuro',
        'light': 'Claro',
        'recipes_title': '🍽️ RECETAS',
        'recipes_subtitle': 'Comidas saludables para tu objetivo',
        'all_recipes': '📋 Todas',
        'breakfast': '🌅 Desayunos',
        'lunch': '🍲 Almuerzos',
        'dinner': '🌙 Cenas',
        'snack': '🍎 Meriendas',
        'high_protein': '💪 Alta proteína',
        'recipe_ingredients': '📝 Ingredientes',
        'recipe_steps': '👨‍🍳 Preparación',
        'cooking_time': '⏱️ Tiempo:',
        'minutes': 'min',
        'view_recipes': '🍽️ Recetas',
        # Diario
        'diary': '📓 Diario',
        'workout_history': 'Historial de entrenamientos',
        'no_history': 'Historial vacío. ¡Comienza un entrenamiento!',
        'completed_workouts': 'Entrenamientos',
        'load_program': '📂 Cargar',
        'program_saved': '¡Programa guardado!',
        'program_loaded': '¡Programa cargado!',
        'no_saved_program': 'No hay programa guardado',
        'hold_time': '¡Mantén!',
        'seconds': 'segundos',
        'skip_rest': '⏩ Saltar',
        'hold_exercise': '💪 Mantener',
    },
    'zh': {
        'app_title': '💪 FitWizard Pro',
        'welcome': '欢迎！',
        'welcome_subtitle': '让我们为您创建完美的训练计划',
        'motivation_text': '开始您的最佳状态之旅',
        'male': '男性',
        'female': '女性',
        'select': '选择',
        'male_desc': '力量训练\n增肌',
        'female_desc': '塑形健身\n柔韧性',
        'continue_btn': '继续',
        'back_btn': '← 返回',
        'enter_data': '输入您的数据',
        'height': '身高',
        'weight': '体重',
        'age': '年龄',
        'cm': '厘米',
        'kg': '公斤',
        'years': '岁',
        'days_per_week': '每周天数：',
        'weeks_program': '计划周数：',
        'level': '级别：',
        'beginner': '初学者',
        'intermediate': '中级',
        'advanced': '高级',
        'error_height': '⚠️ 请输入身高！',
        'error_weight': '⚠️ 请输入体重！',
        'error_age': '⚠️ 请输入年龄！',
        'error_height_range': '⚠️ 身高：120-250厘米！',
        'error_weight_range': '⚠️ 体重：40-200公斤！',
        'error_age_range': '⚠️ 年龄：14-80岁！',
        'choose_goal': '选择您的目标',
        'goal_subtitle': '您想达到什么目标？',
        'weight_loss': '减重',
        'weight_loss_desc': 'HIIT训练燃烧卡路里',
        'muscle_gain': '增肌',
        'muscle_gain_desc': '力量练习促进肌肉生长',
        'choose_zone': '选择区域',
        'Full Body': '全身',
        'Legs': '腿部',
        'Chest': '胸部',
        'Back': '背部',
        'Arms': '手臂',
        'Shoulders': '肩部',
        'Core': '核心',
        'safety_title': '⚠️ 安全须知',
        'safety_subtitle': '请阅读建议',
        'safety_60plus': '🔴 60岁以上重要提示',
        'safety_60_1': '⚠️ 请咨询医生',
        'safety_60_2': '🫀 心脏病需心脏科批准',
        'safety_60_3': '🚫 避免突然动作',
        'safety_50plus': '🟡 50岁以上建议',
        'safety_50_1': '👨‍⚕️ 建议咨询医生',
        'safety_50_2': '🔥 注意热身',
        'safety_50_3': '💪 监测脉搏',
        'safety_teen': '🟢 青少年（14-17岁）',
        'safety_teen_1': '📚 训练适合成长期',
        'safety_teen_2': '🚫 避免脊柱过度负荷',
        'safety_teen_3': '👨‍👩‍👦 与父母协调',
        'safety_general': '✅ 一般建议',
        'safety_gen_1': '👨‍⚕️ 生病时咨询医生',
        'safety_gen_2': '🛑 感到疼痛时停止',
        'safety_gen_3': '🔥 始终热身',
        'safety_agree': '我已阅读并准备开始',
        'nutrition_title': '🍽️ 营养计划',
        'nutrition_subtitle': '您目标的卡路里',
        'kcal_day': '千卡/天',
        'protein': '蛋白质',
        'fats': '脂肪',
        'carbs': '碳水化合物',
        'g': '克',
        'nutrition_tips': '💡 建议：',
        'tip1': '• 每天喝2-3升水',
        'tip2': '• 吃4-5顿小餐',
        'tip3': '• 每餐都吃蛋白质',
        'tip4': '• 碳水化合物在下午4点前',
        'tip5': '• 避免糖分',
        'to_program': '进入计划',
        'program_ready': '📋 您的计划',
        'week': '周',
        'day': '天',
        'exercises': '个练习',
        'sets': '组',
        'start_btn': '▶️ 开始',
        'completed': '已完成',
        'locked': '🔒',
        'save_program': '💾 保存',
        'my_progress': '📈 进度',
        'diary': '📊 日记',
        'new_program': '🔄 新建',
        'workout_title': '▶️ 训练',
        'exercise': '练习',
        'set': '组',
        'of': '/',
        'reps': '次',
        'seconds': '秒',
        'hold': '保持',
        'rest': '休息',
        'complete_set': '✅ 组完成',
        'skip_exercise': '⏭️ 跳过',
        'simplify': '😓 简化',
        'finish_workout': '❌ 结束',
        'rest_between': '组间休息',
        'sec': '秒',
        'start_timer': '▶️ 开始',
        'compound': '🔸 复合动作',
        'isolation': '🔹 孤立动作',
        'core': '🎯 Core',
        'cardio': '🏃 有氧',
        'progress_title': '📊 我的进度',
        'weight_title': '⚖️ 体重',
        'measurements': '📏 测量（厘米）',
        'chest_label': '💪 胸围：',
        'waist_label': '👖 腰围：',
        'hips_label': '🍑 臀围：',
        'arms_label': '💪 臂围：',
        'add_btn': '➕ 添加',
        'save_btn': '💾 保存',
        'photos_title': '📷 进度照片',
        'no_photos': '没有照片',
        'add_photo': '📸 添加照片',
        'back_to_program': '← 返回计划',
        'diary_title': '📊 训练日记',
        'total_workouts': '总训练次数',
        'great_progress': '✅ 进步很大！',
        'workout_complete': '🎉 太棒了！',
        'workout_finished': '训练完成！',
        'rec_title': '💡 建议',
        'settings': '⚙️ 设置',
        'language': '语言',
        'theme': '主题',
        'dark': '深色',
        'light': '浅色',
        'recipes_title': '🍽️ 食谱',
        'recipes_subtitle': '适合您目标的健康餐',
        'all_recipes': '📋 全部',
        'breakfast': '🌅 早餐',
        'lunch': '🍲 午餐',
        'dinner': '🌙 晚餐',
        'snack': '🍎 小食',
        'high_protein': '💪 高蛋白',
        'recipe_ingredients': '📝 食材',
        'recipe_steps': '👨‍🍳 做法',
        'cooking_time': '⏱️ 时间：',
        'minutes': '分钟',
        'view_recipes': '🍽️ 食谱',
        # 日记
        'diary': '📓 日记',
        'workout_history': '训练历史',
        'no_history': '历史为空。开始训练！',
        'completed_workouts': '完成训练',
        'load_program': '📂 加载计划',
        'program_saved': '计划已保存！',
        'program_loaded': '计划已加载！',
        'no_saved_program': '没有保存的计划',
        'hold_time': '保持！',
        'seconds': '秒',
        'skip_rest': '⏩ 跳过',
        'hold_exercise': '💪 保持',
    },
}

# ============== ГЛАВНЫЙ КЛАСС ПРИЛОЖЕНИЯ ==============

class TrainingApp:
    def app_background(self, content):
        # Надёжный full-screen фон: всегда возвращаем Stack, где фон — первый слой,
        # затем полупрозрачный оверлей и контент. Компоненты используют expand=True,
        # чтобы занять всю доступную область.
        if self.theme == 'dark':
            bg = ft.Image(src="exercise_gifs/bg_dark.png", fit="cover", expand=True)
            overlay = ft.Container(bgcolor="#18192bcc", expand=True)
            inner = ft.Stack([
                ft.Container(content=bg, expand=True, padding=0, margin=0),
                overlay,
                ft.Container(content=content, expand=True, alignment=ft.alignment.center, padding=0, margin=0),
            ], expand=True)
            return inner
        else:
            bg_gradient = ft.LinearGradient(
                begin=ft.Alignment(0, -1),
                end=ft.Alignment(0, 1),
                colors=["#2a2340", "#18192b", "#2a2340"]
            )
            inner = ft.Stack([
                ft.Container(gradient=bg_gradient, expand=True, padding=0, margin=0),
                ft.Container(content=content, expand=True, alignment=ft.alignment.center, padding=0, margin=0)
            ], expand=True)
            return inner

    def on_resize(self, e):
        # устаревший — оставлен для совместимости
        try:
            self.page.update()
        except Exception:
            pass

    def on_resized(self, e):
        # Современный обработчик изменения размеров окна — просто обновляем страницу
        try:
            self.page.update()
        except Exception:
            pass

    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "💪 FitWizard Pro"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.padding = 0
        self.page.scroll = ft.ScrollMode.AUTO
        # подписываем современный обработчик изменения размера окна
        try:
            self.page.on_resized = self.on_resized
        except Exception:
            # fallback для старых версий
            try:
                self.page.on_resize = self.on_resize
            except Exception:
                pass
        
        # Настройки
        self.lang = 'ru'
        self.theme = 'dark'
        # Для тёмной темы показываем изображение фона страницы и используем cover
        self.page.bgcolor = None
        if self.theme == 'dark':
            try:
                self.page.bgimage = "exercise_gifs/bg_dark.png"
            except Exception:
                self.page.bgimage = None
            try:
                # Попытка установить режим заливки (если поддерживается)
                self.page.bgimage_fit = ft.ImageFit.COVER
            except Exception:
                try:
                    self.page.bgimage_fit = 'cover'
                except Exception:
                    pass
        else:
            self.page.bgimage = None
        
        # Данные пользователя
        self.user_data = {}
        self.program_data = None
        self.completed_workouts = set()
        self.workout_history = []
        self.progress_data = {
            'weight': [],
            'measurements': {'chest': [], 'waist': [], 'hips': [], 'arms': []},
            'photos': []
        }
        
        # Цвета
        self.set_colors()

        # Путь к GIF
        self.gifs_dir = Path(__file__).parent.parent / "exercise_gifs"
        

        # Показываем экран приветствия
        self.show_welcome()

    def add_content(self, content):
        """Добавляет контент на страницу.
        Для тёмной темы используем `page.bgimage` и простой контейнер, чтобы фон занимал весь экран.
        В противном случае используем `app_background` как раньше.
        """
        # Всегда используем `app_background` — он строит Stack с фоном и контентом.
        # Убедимся, что page.bgimage задан для тёмной темы (на случай, если его сбросили).
        if self.theme == 'dark':
            try:
                self.page.bgimage = "exercise_gifs/bg_dark.png"
            except Exception:
                pass
        else:
            try:
                self.page.bgimage = None
            except Exception:
                pass
        # Оборачиваем Stack в контейнер с expand=True, чтобы он точно занял весь экран
        self.page.add(ft.Container(content=self.app_background(content), expand=True, padding=0, margin=0))
    
    def t(self, key):
        """Получить перевод"""
        return LOCALES.get(self.lang, LOCALES['ru']).get(key, key)
    
    def set_colors(self):
        """Установка цветовой темы"""
        if self.theme == 'dark':
            self.colors = {
                'bg': None,
                'card': '#1a1f3a',
                'primary': '#667eea',
                'secondary': '#f093fb',
                'success': '#00d4aa',
                'warning': '#ffa726',
                'text': '#ffffff',
                'text_secondary': '#a0aec0',
            }
        else:
            self.colors = {
                'bg': '#f0f4f8',
                'card': '#ffffff',
                'primary': '#667eea',
                'secondary': '#f093fb',
                'success': '#00d4aa',
                'warning': '#ffa726',
                'text': '#1a202c',
                'text_secondary': '#718096',
            }
    
    def clear_page(self):
        """Очистить страницу и добавить фон"""
        self.page.controls.clear()
    
    def show_settings_panel(self):
        """Показать панель настроек"""
        def change_lang(lang):
            self.lang = lang
            self.set_colors()
            self.page.theme_mode = ft.ThemeMode.DARK if self.theme == 'dark' else ft.ThemeMode.LIGHT
            self.page.overlay.clear()
            self.show_settings_panel()

        def change_theme(theme):
            self.theme = theme
            self.set_colors()
            self.page.theme_mode = ft.ThemeMode.DARK if theme == 'dark' else ft.ThemeMode.LIGHT
            # При смене темы просто обновим страницу — фон формируется в app_background
            pass
            try:
                self.page.update()
            except Exception:
                pass
            self.page.overlay.clear()
            self.show_settings_panel()
        
        def close_sheet(e):
            self.page.overlay.clear()
            self.show_welcome()
        
        bs = ft.BottomSheet(
            open=True,
            on_dismiss=lambda e: None,
            content=ft.Container(
                content=ft.Column([
                    ft.Text(self.t('settings'), size=24, weight=ft.FontWeight.BOLD, color=self.colors['text']),
                    ft.Divider(),
                    ft.Text(self.t('language'), size=16, color=self.colors['text']),
                    ft.Row([
                        ft.ElevatedButton("🇷🇺 Русский", bgcolor=self.colors['primary'] if self.lang == 'ru' else self.colors['card'], color="white", on_click=lambda e: change_lang('ru')),
                        ft.ElevatedButton("🇬🇧 English", bgcolor=self.colors['primary'] if self.lang == 'en' else self.colors['card'], color="white", on_click=lambda e: change_lang('en')),
                    ], wrap=True),
                    ft.Row([
                        ft.ElevatedButton("🇩🇪 Deutsch", bgcolor=self.colors['primary'] if self.lang == 'de' else self.colors['card'], color="white", on_click=lambda e: change_lang('de')),
                        ft.ElevatedButton("🇪🇸 Español", bgcolor=self.colors['primary'] if self.lang == 'es' else self.colors['card'], color="white", on_click=lambda e: change_lang('es')),
                    ], wrap=True),
                    ft.Row([
                        ft.ElevatedButton("🇨🇳 中文", bgcolor=self.colors['primary'] if self.lang == 'zh' else self.colors['card'], color="white", on_click=lambda e: change_lang('zh')),
                    ], wrap=True),
                    ft.Container(height=10),
                    ft.Text(self.t('theme'), size=16, color=self.colors['text']),
                    ft.Row([
                        ft.ElevatedButton(f"🌙 {self.t('dark')}", bgcolor=self.colors['primary'] if self.theme == 'dark' else self.colors['card'], color="white", on_click=lambda e: change_theme('dark')),
                        ft.ElevatedButton(f"☀️ {self.t('light')}", bgcolor=self.colors['primary'] if self.theme == 'light' else self.colors['card'], color="white", on_click=lambda e: change_theme('light')),
                    ]),
                    ft.Container(height=20),
                    ft.ElevatedButton("✅ OK", bgcolor=self.colors['success'], color="white", width=200, on_click=close_sheet),
                ], spacing=10, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=20,
                bgcolor=self.colors['card'],
            ),
        )
        self.page.overlay.append(bs)
        self.page.update()
    
    # ============== ЭКРАН ПРИВЕТСТВИЯ ==============
    def show_welcome(self):
        """Экран выбора пола с красивыми карточками"""
        self.clear_page()
        
        # Путь к изображениям
        # --- Новый экран выбора пола в стиле макета ---
        # Используем реальные фото
        male_img = "exercise_gifs/male.jpg"
        female_img = "exercise_gifs/female.png"

        def gender_card(img_path, label, selected, on_click):
            return ft.GestureDetector(
                content=ft.Container(
                    content=ft.Stack([
                        ft.Image(
                            src=img_path,
                            width=260,
                            height=320,
                            fit="cover",
                            border_radius=18,
                        ),
                        ft.Container(
                            content=ft.Text(label, size=28, weight=ft.FontWeight.BOLD, color="white"),
                            alignment=ft.alignment.bottom_center,
                            margin=ft.margin.only(bottom=18),
                        ),
                    ]),
                    width=260,
                    height=320,
                    border=ft.border.all(3, "#a78bfd" if selected else "#7c5fd6"),
                    border_radius=18,
                    bgcolor=None,
                    margin=ft.margin.only(left=18, right=18),
                ),
                on_tap=on_click,
                mouse_cursor=ft.MouseCursor.CLICK,
            )

        selected = getattr(self, "selected_gender", None)

        def select_and_next(gender):
            self.selected_gender = gender
            self.show_params() if gender else None

        # Градиентный фон (имитация)
        bg_gradient = ft.LinearGradient(
            begin=ft.Alignment(0, -1),
            end=ft.Alignment(0, 1),
            colors=["#2a2340", "#18192b", "#2a2340"]
        )

        # Красивая круглая кнопка настроек справа
        settings_btn = ft.Container(
            content=ft.IconButton(
                icon=ft.Icons.SETTINGS,
                icon_color="#6c8cff",
                tooltip="Настройки",
                on_click=lambda e: self.show_settings_panel(),
            ),
            bgcolor="#23243a",
            border_radius=30,
            padding=8,
            margin=ft.margin.only(right=18, top=8),
            alignment=ft.alignment.top_right,
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=8,
                color="#6c8cff33",
                offset=ft.Offset(0, 2),
            ),
            width=44,
            height=44,
        )

        content = ft.Column([
            ft.Container(height=24),
            ft.Row([
                ft.Text("💪 Добро пожаловать!", size=38, weight=ft.FontWeight.BOLD, color="#aabaff", text_align=ft.TextAlign.CENTER, expand=True),
                settings_btn,
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Container(height=8),
            ft.Text("Создадим идеальную программу тренировок для вас", size=18, color="#e0e6ff", text_align=ft.TextAlign.CENTER),
            ft.Text("✨ Начни путь к своей лучшей форме", size=15, color="#e0aaff", italic=True, text_align=ft.TextAlign.CENTER),
            ft.Container(height=30),
            ft.Row([
                gender_card(male_img, "Мужской", selected == "male", lambda e: select_and_next("male")),
                gender_card(female_img, "Женский", selected == "female", lambda e: select_and_next("female")),
            ], alignment=ft.MainAxisAlignment.CENTER),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        self.add_content(content)
        self.page.update()

    def show_body_zone_screen(self):
        """Экран выбора зоны тела по фото"""
        self.clear_page()
        # Координаты точек (относительно картинки 380x657)
        points = {
            'arms': (320, 110),
            'chest': (170, 140),
            'abs': (200, 250),
            'legs': (250, 500),
        }
        labels = {
            'arms': 'Руки',
            'chest': 'Грудь',
            'abs': 'Пресс',
            'legs': 'Ноги',
        }
        # Картинка
        img = ft.Image(src="exercise_gifs/ТЕЛЛОЛ.png", width=380, height=657, fit="contain")
        # Кликабельные точки
        dots = []
        for key, (x, y) in points.items():
            dots.append(
                ft.Positioned(
                    left=x, top=y,
                    child=ft.GestureDetector(
                        content=ft.Container(
                            content=ft.CircleAvatar(bgcolor="#aabaff", radius=10),
                            tooltip=labels[key],
                        ),
                        on_tap=lambda e, k=key: self.select_body_zone(k)
                    )
                )
            )
        # Подписи
        label_widgets = []
        for key, (x, y) in points.items():
            label_widgets.append(
                ft.Positioned(
                    left=x+30, top=y-10,
                    child=ft.Container(
                        content=ft.Text(labels[key], size=16, bgcolor="#fff", color="#3a2340", border_radius=8, padding=6),
                        tooltip=labels[key],
                    )
                )
            )
        # Кнопки
        btns = ft.Row([
            ft.ElevatedButton("Продолжить", on_click=lambda e: self.show_result(), bgcolor="#6c8cff", color="white", width=150),
            ft.ElevatedButton("Назад", on_click=lambda e: self.show_welcome(), bgcolor="#fff", color="#3a2340", width=150),
        ], alignment=ft.MainAxisAlignment.CENTER)
        # Всё вместе
        content = ft.Column([
            ft.Container(height=20),
            ft.Text("На какую зону сделать упор?", size=22, weight=ft.FontWeight.BOLD, color="#aabaff", text_align=ft.TextAlign.CENTER),
            ft.Container(height=10),
            ft.Stack([
                img,
                *dots,
                *label_widgets,
            ], width=380, height=657),
            ft.Container(height=20),
            btns
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        self.add_content(content)
        self.page.update()
    
    def select_gender(self, gender):
        """Выбор пола и переход к параметрам"""
        self.user_data = {'gender': gender}
        self.program_data = None
        self.completed_workouts = set()
        self.workout_history = []
        self.show_params()
    
    # ============== ЭКРАН ПАРАМЕТРОВ ==============
    def show_params(self):
        """Экран ввода параметров"""
        self.clear_page()
        
        # Создаём стилизованные поля ввода
        self.height_field = ft.TextField(
            label=f"📏 {self.t('height')} ({self.t('cm')})",
            keyboard_type=ft.KeyboardType.NUMBER,
            width=350,
            border_radius=10,
            bgcolor="#1a1a2e",
            border_color="#333355",
            focused_border_color=self.colors['primary'],
        )
        
        self.weight_field = ft.TextField(
            label=f"⚖️ {self.t('weight')} ({self.t('kg')})",
            keyboard_type=ft.KeyboardType.NUMBER,
            width=350,
            border_radius=10,
            bgcolor="#1a1a2e",
            border_color="#333355",
            focused_border_color=self.colors['primary'],
        )
        
        self.age_field = ft.TextField(
            label=f"🎂 {self.t('age')} ({self.t('years')})",
            keyboard_type=ft.KeyboardType.NUMBER,
            width=350,
            border_radius=10,
            bgcolor="#1a1a2e",
            border_color="#333355",
            focused_border_color=self.colors['primary'],
        )
        
        self.days_dropdown = ft.Dropdown(
            label=self.t('days_per_week'),
            width=350,
            options=[ft.dropdown.Option(str(i)) for i in range(2, 7)],
            value="3",
            border_radius=10,
            bgcolor="#1a1a2e",
            border_color="#333355",
            focused_border_color=self.colors['primary'],
        )
        
        self.weeks_dropdown = ft.Dropdown(
            label=self.t('weeks_program'),
            width=350,
            options=[ft.dropdown.Option(str(i)) for i in range(2, 13)],
            value="5",
            border_radius=10,
            bgcolor="#1a1a2e",
            border_color="#333355",
            focused_border_color=self.colors['primary'],
        )
        
        self.level_dropdown = ft.Dropdown(
            label=self.t('level'),
            width=350,
            options=[
                ft.dropdown.Option("beginner", f"🌱 {self.t('beginner')}"),
                ft.dropdown.Option("intermediate", f"💪 {self.t('intermediate')}"),
                ft.dropdown.Option("advanced", f"🔥 {self.t('advanced')}"),
            ],
            value="beginner",
            border_radius=10,
            bgcolor="#1a1a2e",
            border_color="#333355",
            focused_border_color=self.colors['primary'],
        )
        
        self.error_text = ft.Text("", color="red", size=14)
        
        # Подсказки под полями
        def hint_text(text):
            return ft.Text(text, size=11, color=self.colors['text_secondary'], text_align=ft.TextAlign.CENTER)
        
        content = ft.Column([
            ft.Container(height=30),
            
            # Заголовок
            ft.Text(f"📊 {self.t('enter_data').upper()}", size=24, weight=ft.FontWeight.BOLD,
                   color=self.colors['text']),
            
            ft.Container(height=30),
            
            # Поля ввода с подсказками
            self.height_field,
            hint_text("120-250 см"),
            
            self.weight_field,
            hint_text("40-200 кг"),
            
            self.age_field,
            hint_text("14-80 лет"),
            
            ft.Container(height=10),
            
            # Dropdowns
            self.days_dropdown,
            self.weeks_dropdown,
            self.level_dropdown,
            
            self.error_text,
            
            ft.Container(height=30),
            
            # Кнопка продолжить
            ft.ElevatedButton(
                f"{self.t('continue_btn').upper()} →",
                bgcolor=self.colors['primary'],
                color="white",
                width=350,
                height=55,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=30)),
                on_click=self.validate_params
            ),
            
            ft.Container(height=10),
            
            # Кнопка назад
            ft.TextButton(
                f"← {self.t('back_btn').upper()}",
                on_click=lambda e: self.show_welcome()
            ),
            
            ft.Container(height=30),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO)
        
        self.add_content(ft.Container(content=content, bgcolor=self.colors['bg'], expand=True))
        self.page.update()
    
    def validate_params(self, e):
        """Валидация параметров"""
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
                # Всё OK
                self.user_data['height'] = height
                self.user_data['weight'] = weight
                self.user_data['age'] = age
                self.user_data['days'] = int(self.days_dropdown.value)
                self.user_data['weeks'] = int(self.weeks_dropdown.value)
                self.user_data['level'] = self.level_dropdown.value
                self.show_goal()
                return
            
            self.page.update()
        except:
            self.error_text.value = "⚠️ Ошибка ввода"
            self.page.update()
    
    # ============== ЭКРАН ВЫБОРА ЦЕЛИ ==============
    def show_goal(self):
        """Экран выбора цели с красивыми карточками"""
        self.clear_page()
        
        img_path = "exercise_gifs/"
        
        # Карточка похудения - зелёная рамка
        weight_loss_card = ft.Container(
            content=ft.Stack([
                ft.Image(
                    src=img_path + "cut.png",
                    width=350,
                    height=140,
                    fit="cover",
                    border_radius=15,
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Text(self.t('weight_loss'), size=26, weight=ft.FontWeight.BOLD, color="white"),
                        ft.Text("🔥", size=32),
                    ], spacing=5),
                    padding=ft.Padding(left=20, top=15, right=0, bottom=0),
                ),
            ]),
            border_radius=15,
            border=ft.border.all(3, "#00ff88"),
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            on_click=lambda e: self.select_goal("weight_loss"),
            ink=True,
        )
        
        # Карточка набора массы - фиолетовая рамка
        muscle_gain_card = ft.Container(
            content=ft.Stack([
                ft.Image(
                    src=img_path + "bulk.avif",
                    width=350,
                    height=140,
                    fit="cover",
                    border_radius=15,
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Text(self.t('muscle_gain'), size=26, weight=ft.FontWeight.BOLD, color="white"),
                        ft.Text("💪", size=32),
                    ], spacing=5),
                    padding=ft.Padding(left=20, top=15, right=0, bottom=0),
                ),
            ]),
            border_radius=15,
            border=ft.border.all(3, self.colors['primary']),
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            on_click=lambda e: self.select_goal("muscle_gain"),
            ink=True,
        )
        
        content = ft.Column([
            ft.Container(height=40),
            
            # Заголовок
            ft.Text(f"🎯 {self.t('choose_goal').upper()}", size=28, weight=ft.FontWeight.BOLD,
                   color=self.colors['text']),
            ft.Text(self.t('goal_subtitle'), size=14, color=self.colors['text_secondary']),
            
            ft.Container(height=40),
            
            weight_loss_card,
            ft.Container(height=25),
            muscle_gain_card,
            
            ft.Container(height=40),
            
            ft.TextButton(
                f"← {self.t('back_btn').upper()}",
                on_click=lambda e: self.show_params()
            ),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO)
        
        self.add_content(ft.Container(content=content, bgcolor=self.colors['bg'], expand=True))
        self.page.update()
    
    def select_goal(self, goal):
        """Выбор цели"""
        self.user_data['goal'] = goal
        if goal == 'weight_loss':
            # Для похудения сразу на безопасность
            self.user_data['focus'] = 'Weight Loss'
            self.show_safety()
        else:
            # Для набора массы - выбор зоны
            self.show_focus()
    
    # ============== ЭКРАН ВЫБОРА ЗОНЫ ==============
    def show_focus(self):
        """Экран выбора зоны тренировки с картинкой тела"""
        self.clear_page()
        
        img_path = "exercise_gifs/"
        
        # Кнопка "Все группы мышц"
        all_muscles_btn = ft.Container(
            content=ft.Text("ВСЕ ГРУППЫ МЫШЦ", size=14, weight=ft.FontWeight.BOLD, color=self.colors['text']),
            padding=ft.Padding(left=20, right=20, top=10, bottom=10),
            border_radius=20,
            border=ft.border.all(2, self.colors['text_secondary']),
            on_click=lambda e: self.select_focus("Full Body"),
            ink=True,
        )
        
        # Определяем зоны с относительными позициями
        zones = [
            ("Arms", "РУКИ", 0.82, 0.18),
            ("Chest", "ГРУДЬ", 0.12, 0.22),
            ("Core", "ПРЕСС", 0.12, 0.38),
            ("Legs", "НОГИ", 0.72, 0.60),
        ]
        
        # Создаём кнопки зон поверх изображения
        zone_buttons = []
        for zone_key, zone_name, left_pct, top_pct in zones:
            zone_buttons.append(
                ft.Container(
                    content=ft.Text(zone_name, size=11, weight=ft.FontWeight.BOLD, color=self.colors['primary']),
                    bgcolor="white",
                    padding=ft.Padding(left=12, right=12, top=6, bottom=6),
                    border_radius=12,
                    border=ft.border.all(2, self.colors['primary']),
                    left=left_pct * 380,
                    top=top_pct * 420,
                    on_click=lambda e, z=zone_key: self.select_focus(z),
                )
            )
        
        # Stack с изображением и кнопками
        body_stack = ft.Stack(
            [
                ft.Image(
                    src=img_path + "ntkj.png",
                    width=380,
                    height=420,
                    fit="contain",
                ),
            ] + zone_buttons,
            width=380,
            height=420,
        )
        
        content = ft.Column([
            ft.Container(height=15),
            
            # Заголовок
            ft.Text("НА КАКУЮ ЧАСТЬ ТЕЛА ХОТИТЕ", size=18, weight=ft.FontWeight.BOLD,
                   color=self.colors['text'], text_align=ft.TextAlign.CENTER),
            ft.Text("СДЕЛАТЬ УПОР?", size=18, weight=ft.FontWeight.BOLD,
                   color=self.colors['text'], text_align=ft.TextAlign.CENTER),
            
            ft.Container(height=10),
            all_muscles_btn,
            ft.Container(height=5),
            
            body_stack,
            
            ft.Container(height=15),
            
            # Кнопки навигации
            ft.Row([
                ft.ElevatedButton(
                    "ПРОДОЛЖИТЬ",
                    bgcolor=self.colors['primary'],
                    color="white",
                    width=140,
                    height=45,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=25)),
                    on_click=lambda e: self.show_safety()
                ),
                ft.ElevatedButton(
                    "НАЗАД",
                    bgcolor="#333355",
                    color="white",
                    width=110,
                    height=45,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=25)),
                    on_click=lambda e: self.show_goal()
                ),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=15),
            
            ft.Container(height=15),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO)
        
        self.add_content(ft.Container(content=content, bgcolor=self.colors['bg'], expand=True))
        self.page.update()
    
    def select_focus(self, focus):
        """Выбор зоны и переход к безопасности"""
        self.user_data['focus'] = focus
        self.show_safety()
    
    # ============== ЭКРАН БЕЗОПАСНОСТИ ==============
    def show_safety(self):
        """Экран безопасности"""
        self.clear_page()
        
        age = self.user_data.get('age', 25)
        
        warnings = []
        
        # Возрастные предупреждения
        if age < 18:
            warnings.append(ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Container(width=10, height=10, bgcolor="yellow", border_radius=5),
                        ft.Text("ДЛЯ ПОДРОСТКОВ (14-17 лет)", size=16, weight=ft.FontWeight.BOLD,
                               color="#FFD700"),
                    ], spacing=10),
                    ft.Text("📗 Тренировки адаптированы для растущего организма", size=13, color=self.colors['text']),
                    ft.Text("🔴 Избегайте чрезмерных нагрузок на позвоночник", size=13, color=self.colors['text']),
                    ft.Text("👨‍👩‍👦 Согласуйте программу с родителями", size=13, color=self.colors['text']),
                ], spacing=8),
                padding=20,
                border_radius=15,
                border=ft.border.all(2, "#FFD700"),
                bgcolor="#1a1a2e",
            ))
        elif age >= 50:
            warnings.append(ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Container(width=10, height=10, bgcolor="orange", border_radius=5),
                        ft.Text(f"ДЛЯ ВОЗРАСТА {age}+", size=16, weight=ft.FontWeight.BOLD,
                               color="orange"),
                    ], spacing=10),
                    ft.Text("🏥 Рекомендуется консультация врача", size=13, color=self.colors['text']),
                    ft.Text("🦴 Особое внимание суставам", size=13, color=self.colors['text']),
                    ft.Text("📊 Регулярно контролируйте давление", size=13, color=self.colors['text']),
                ], spacing=8),
                padding=20,
                border_radius=15,
                border=ft.border.all(2, "orange"),
                bgcolor="#1a1a2e",
            ))
        
        # Общие рекомендации всегда
        warnings.append(ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text("✅", size=16),
                    ft.Text("ОБЩИЕ РЕКОМЕНДАЦИИ", size=16, weight=ft.FontWeight.BOLD,
                           color=self.colors['success']),
                ], spacing=10),
                ft.Text("⚠️ При хронических заболеваниях консультируйтесь с врачом", size=13, color=self.colors['text']),
                ft.Text("🔴 Немедленно остановитесь при боли или дискомфорте", size=13, color=self.colors['text']),
                ft.Text("🔥 Всегда начинайте с разминки 5-10 минут", size=13, color=self.colors['text']),
            ], spacing=8),
            padding=20,
            border_radius=15,
            border=ft.border.all(2, self.colors['success']),
            bgcolor="#1a1a2e",
        ))
        
        self.agree_checkbox = ft.Checkbox(
            label="Я ознакомился с рекомендациями и готов начать",
            value=False,
            check_color=self.colors['primary'],
        )
        
        content = ft.Column([
            ft.Container(height=30),
            
            # Заголовок
            ft.Text(f"⚠️ БЕЗОПАСНОСТЬ", size=28, weight=ft.FontWeight.BOLD,
                   color=self.colors['warning']),
            ft.Text("Пожалуйста, ознакомьтесь с рекомендациями", size=14, 
                   color=self.colors['text_secondary']),
            
            ft.Container(height=25),
            
            *warnings,
            
            ft.Container(height=25),
            
            # Чекбоксы
            ft.Row([
                ft.Checkbox(value=True, check_color=self.colors['success']),
                self.agree_checkbox,
            ], spacing=5),
            
            ft.Container(height=25),
            
            # Кнопка продолжить
            ft.ElevatedButton(
                "ПРОДОЛЖИТЬ →",
                bgcolor=self.colors['primary'],
                color="white",
                width=350,
                height=55,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=30)),
                on_click=self.check_safety_agree
            ),
            
            ft.Container(height=10),
            
            ft.TextButton(
                "← НАЗАД",
                on_click=lambda e: self.show_goal() if self.user_data.get('goal') == 'weight_loss' else self.show_focus()
            ),
            
            ft.Container(height=20),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO)
        
        self.add_content(ft.Container(content=content, bgcolor=self.colors['bg'], expand=True))
        self.page.update()
    
    def check_safety_agree(self, e):
        """Проверка согласия с безопасностью"""
        if self.agree_checkbox.value:
            self.show_nutrition()
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("⚠️ Подтвердите согласие!"))
            self.page.snack_bar.open = True
            self.page.update()
    
    # ============== ЭКРАН ПИТАНИЯ ==============
    def show_nutrition(self):
        """Экран плана питания"""
        self.clear_page()
        
        # Расчёт калорий
        gender = self.user_data.get('gender', 'male')
        age = self.user_data.get('age', 25)
        weight = self.user_data.get('weight', 70)
        height = self.user_data.get('height', 175)
        goal = self.user_data.get('goal', 'weight_loss')
        
        # BMR по формуле Mifflin-St Jeor
        if gender == 'male':
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161
        
        activity = 1.55 if days >= 4 else 1.375
        tdee = int(bmr * activity)
        
        if goal == 'weight_loss':
            calories = int(tdee - 500)
            protein = int(weight * 1.8)
            fat = int(weight * 0.8)
            goal_emoji = "📉"
            goal_text = self.t('weight_loss')
        else:
            calories = int(tdee + 300)
            protein = int(weight * 2.0)
            fat = int(weight * 1.0)
            goal_emoji = "📈"
            goal_text = self.t('muscle_gain')
        
        protein_cal = protein * 4
        fat_cal = fat * 9
        carbs_cal = calories - protein_cal - fat_cal
        carbs = int(carbs_cal / 4)
        
        # Сохраняем план питания
        self.user_data['nutrition_plan'] = {
            'calories': calories,
            'protein': protein,
            'fat': fat,
            'carbs': carbs,
        }
        
        content = ft.Column([
            ft.Container(height=30),
            
            # Заголовок
            ft.Text("🍽️ ПЛАН ПИТАНИЯ", size=28, weight=ft.FontWeight.BOLD,
                   color=self.colors['text']),
            
            ft.Container(height=20),
            
            # Главная карточка калорий
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text(goal_emoji, size=24),
                        ft.Text(goal_text, size=18, weight=ft.FontWeight.BOLD,
                               color=self.colors['text']),
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Text(f"{calories}", size=56, weight=ft.FontWeight.BOLD,
                           color=self.colors['primary']),
                    ft.Text("ККАЛ/ДЕНЬ", size=14, color=self.colors['text_secondary']),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                padding=25,
                border_radius=20,
                bgcolor="#1a1a2e",
            ),
            
            ft.Container(height=20),
            
            # БЖУ - три блока
            ft.Row([
                ft.Container(
                    content=ft.Column([
                        ft.Text("🥩", size=28),
                        ft.Text("БЕЛКИ", size=11, color=self.colors['text_secondary']),
                        ft.Text(f"{protein}г", size=20, weight=ft.FontWeight.BOLD,
                               color="#ff6b6b"),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                    padding=15,
                    border_radius=15,
                    bgcolor="#1a1a2e",
                    width=100,
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Text("🥑", size=28),
                        ft.Text("ЖИРЫ", size=11, color=self.colors['text_secondary']),
                        ft.Text(f"{fat}г", size=20, weight=ft.FontWeight.BOLD,
                               color="#4ecdc4"),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                    padding=15,
                    border_radius=15,
                    bgcolor="#1a1a2e",
                    width=100,
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Text("🍞", size=28),
                        ft.Text("УГЛЕВОДЫ", size=11, color=self.colors['text_secondary']),
                        ft.Text(f"{carbs}г", size=20, weight=ft.FontWeight.BOLD,
                               color="#ffd93d"),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                    padding=15,
                    border_radius=15,
                    bgcolor="#1a1a2e",
                    width=100,
                ),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            
            ft.Container(height=25),
            
            # Рекомендации
            ft.Container(
                content=ft.Column([
                    ft.Text("💡 Рекомендации по питанию:", size=15, weight=ft.FontWeight.BOLD,
                           color=self.colors['text']),
                    ft.Text("• Пейте 2-3 литра воды в день", size=13, color=self.colors['text_secondary']),
                    ft.Text("• Ешьте 4-5 раз небольшими порциями", size=13, color=self.colors['text_secondary']),
                    ft.Text("• Белок в каждом приёме пищи", size=13, color=self.colors['text_secondary']),
                    ft.Text("• Сложные углеводы до 16:00", size=13, color=self.colors['text_secondary']),
                    ft.Text("• Избегайте сахара и фастфуда", size=13, color=self.colors['text_secondary']),
                ], spacing=8),
                padding=20,
                border_radius=15,
                bgcolor="#1a1a2e",
            ),
            
            ft.Container(height=30),
            
            # Кнопка к программе
            ft.ElevatedButton(
                "К ПРОГРАММЕ →",
                bgcolor=self.colors['primary'],
                color="white",
                width=300,
                height=55,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=30)),
                on_click=lambda e: self.generate_and_show_program()
            ),
            
            ft.Container(height=10),
            
            ft.TextButton(
                "← НАЗАД",
                on_click=lambda e: self.show_safety()
            ),
            
            ft.Container(height=20),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO)
        
        self.add_content(ft.Container(content=content, bgcolor=self.colors['bg'], expand=True, padding=20))
        self.page.update()
    
    # ============== ГЕНЕРАТОР ПРОГРАММЫ ==============
    def generate_and_show_program(self):
        """Генерация программы тренировок"""
        self.program_data = self.generate_program()
        self.show_result()
    
    def generate_program(self):
        """Генерация программы тренировок"""
        gender = self.user_data.get('gender', 'male')
        focus = self.user_data.get('focus', 'Full Body')
        level = self.user_data.get('level', 'beginner')
        days = self.user_data.get('days', 3)
        weeks = self.user_data.get('weeks', 4)
        age = self.user_data.get('age', 25)
        weight = self.user_data.get('weight', 70)
        height = self.user_data.get('height', 175)
        goal = self.user_data.get('goal', 'weight_loss')
        
        bmi = weight / ((height / 100) ** 2)
        
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
            'schedule': []
        }
        
        # Генерация расписания по неделям
        for week_num in range(1, weeks + 1):
            week = {'week': week_num, 'days': []}
            
            for day_num in range(1, days + 1):
                # Выбор группы мышц
                if goal == 'weight_loss':
                    group = 'Weight Loss'
                else:
                    group = focus
                
                # Выбор упражнений
                exercises = self.pick_exercises(group, 5, level, week_num, gender)
                
                # Расчёт подходов и повторений
                workout_exercises = []
                for ex in exercises:
                    sets, reps = self.calculate_sets_reps(ex, level, week_num, gender, age)
                    
                    workout_exercises.append({
                        'name': ex['name'],
                        'gif': ex.get('gif', ''),
                        'type': ex['type'],
                        'difficulty': ex['difficulty'],
                        'sets': sets,
                        'reps': reps,
                        'is_hold': ex.get('is_hold', False),
                        'rest_seconds': 45 if level == 'beginner' else (30 if level == 'intermediate' else 20),
                    })
                
                # Эмодзи группы
                emoji_map = {
                    'Full Body': '🏋️', 'Legs': '🦵', 'Chest': '💪', 
                    'Back': '🔙', 'Arms': '💪', 'Shoulders': '🏋️',
                    'Core': '🎯', 'Weight Loss': '🔥'
                }
                
                day_data = {
                    'day': day_num,
                    'group': group,
                    'emoji': emoji_map.get(group, '💪'),
                    'exercises': workout_exercises,
                }
                week['days'].append(day_data)
            
            program['schedule'].append(week)
        
        return program
    
    def pick_exercises(self, group, count, level, week, gender):
        """Выбор упражнений"""
        pool = EXERCISES.get(group, EXERCISES['Full Body'])
        
        # Фильтрация по полу
        if gender == 'female':
            suitable = [ex for ex in pool if not ex.get('male_focused', False)]
        else:
            suitable = [ex for ex in pool if not ex.get('female_focused', False)]
        
        # Фильтрация по уровню
        level_map = {
            'beginner': ['beginner'],
            'intermediate': ['beginner', 'intermediate'],
            'advanced': ['beginner', 'intermediate', 'advanced']
        }
        allowed = level_map.get(level, ['beginner'])
        suitable = [ex for ex in suitable if ex['difficulty'] in allowed]
        
        # Добавляем упражнения для среднего уровня после 2 недели
        if level == 'beginner' and week > 2:
            intermediate_ex = [ex for ex in pool if ex['difficulty'] == 'intermediate' 
                              and not ex.get('male_focused' if gender == 'female' else 'female_focused', False)]
            suitable.extend(intermediate_ex[:2])
        
        random.seed(week * 100 + hash(group))
        
        if len(suitable) >= count:
            return random.sample(suitable, count)
        return suitable[:]
    
    def calculate_sets_reps(self, exercise, level, week, gender, age):
        """Расчёт подходов и повторений"""
        # Базовые значения по уровню
        base_sets = {'beginner': 3, 'intermediate': 4, 'advanced': 5}
        base_reps = {'beginner': 10, 'intermediate': 12, 'advanced': 15}
        
        sets = base_sets.get(level, 3)
        reps = base_reps.get(level, 10)
        
        # Прогрессия по неделям
        reps += (week - 1) * 1
        
        # Для статических упражнений
        if exercise.get('is_hold', False):
            reps = 20 if level == 'beginner' else (30 if level == 'intermediate' else 45)
            reps += (week - 1) * 5
            reps = min(reps, 60)
        
        # Корректировка по возрасту
        if age >= 60:
            sets = max(2, sets - 1)
            reps = int(reps * 0.7)
        elif age >= 50:
            reps = int(reps * 0.85)
        elif age < 18:
            sets = min(sets, 3)
        
        # Корректировка по полу
        if gender == 'female':
            sets = max(2, sets - 1)
        
        return sets, reps
    
    # ============== ЭКРАН РЕЗУЛЬТАТА ==============
    def show_result(self):
        """Экран с программой тренировок"""
        self.clear_page()
        
        if not self.program_data:
            self.generate_and_show_program()
            return
        
        meta = self.program_data['metadata']
        nutrition = self.user_data.get('nutrition_plan', {})
        
        # Заголовок
        header = ft.Column([
            ft.Text("📋 ВАША ПРОГРАММА ГОТОВА", size=24, weight=ft.FontWeight.BOLD,
                   color=self.colors['text']),
            ft.Container(height=5),
            ft.Text(f"👤 {self.t(self.user_data.get('gender', 'male'))} | 🎯 {self.t(self.user_data.get('focus', 'Full Body'))} | 🌱 {self.t(meta['level'])}",
                   size=12, color=self.colors['text_secondary']),
            ft.Text(f"📊 ИМТ: {meta['bmi']} → {self.t(self.user_data.get('goal', 'muscle_gain'))}",
                   size=12, color=self.colors['text_secondary']),
            ft.Text(f"📅 {meta['weeks']} недель • {meta['days']} дней/неделю",
                   size=12, color=self.colors['text_secondary']),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
        # Персональные рекомендации
        recommendations = ft.Container(
            content=ft.Column([
                ft.Text("💡 Персональные рекомендации", size=15, weight=ft.FontWeight.BOLD,
                       color=self.colors['warning']),
                ft.Text("⚡ Ограничьте кардио 10-15 минутами для сохранения массы", size=12, color=self.colors['text']),
                ft.Text("📅 Отдых 4 дня в неделю для восстановления мышц", size=12, color=self.colors['text']),
                ft.Text("⏱️ Оптимальная продолжительность тренировки 30-45 минут", size=12, color=self.colors['text']),
                ft.Text("🔥 Профицит +300 ккал/день для набора качественной массы", size=12, color=self.colors['text']),
                ft.Text("🏃 Всегда начинайте с разминки 5-10 минут", size=12, color=self.colors['text']),
            ], spacing=5),
            padding=15,
            border_radius=15,
            bgcolor="#1a1a2e",
        )
        
        # План питания краткий
        protein = nutrition.get('protein', 130)
        fat = nutrition.get('fat', 65)
        carbs = nutrition.get('carbs', 343)
        calories = nutrition.get('calories', 2500)
        
        nutrition_card = ft.Container(
            content=ft.Column([
                ft.Text("🍽️ ПЛАН ПИТАНИЯ", size=14, weight=ft.FontWeight.BOLD,
                       color=self.colors['primary']),
                ft.Text(f"📈 {self.t(self.user_data.get('goal', 'muscle_gain'))}: {calories} ккал/день",
                       size=13, color=self.colors['text']),
                ft.Text(f"🥩 {protein}г  🥑 {fat}г  🍞 {carbs}г", size=12, color=self.colors['text_secondary']),
            ], spacing=5, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=15,
            border_radius=15,
            bgcolor="#1a1a2e",
        )
        
        # Список дней тренировок
        day_cards = []
        day_counter = 1
        
        for week in self.program_data['schedule']:
            # Заголовок недели - стилизованный
            day_cards.append(ft.Container(
                content=ft.Text(f"— НЕДЕЛЯ {week['week']} —", 
                               size=14, weight=ft.FontWeight.BOLD,
                               color=self.colors['text_secondary']),
                padding=ft.Padding(left=0, right=0, top=15, bottom=5),
                bgcolor="#252540",
                border_radius=20,
                alignment=ft.alignment.center,
            ))
            
            for day_data in week['days']:
                workout_key = (week['week'], day_data['day'])
                is_completed = workout_key in self.completed_workouts
                
                # Проверяем, можно ли начать
                is_first = day_counter == 1
                can_start = is_first or (week['week'], day_data['day'] - 1) in self.completed_workouts or (week['week'] - 1, self.user_data.get('days', 3)) in self.completed_workouts
                
                ex_count = len(day_data['exercises'])
                total_sets = sum([ex['sets'] for ex in day_data['exercises']])
                exercise_names = ", ".join([ex['name'].split()[0] for ex in day_data['exercises'][:3]])
                if len(day_data['exercises']) > 3:
                    exercise_names += f" +{len(day_data['exercises']) - 3}"
                group_name = self.t(day_data['group']) if day_data['group'] in LOCALES[self.lang] else day_data['group']
                
                # Определяем цвет рамки и кнопку
                if is_completed:
                    border_color = self.colors['success']
                    btn_icon = "✅"
                    btn_bgcolor = self.colors['success']
                elif can_start:
                    border_color = self.colors['primary']
                    btn_icon = "▶️"
                    btn_bgcolor = self.colors['primary']
                else:
                    border_color = "#333355"
                    btn_icon = "🔒"
                    btn_bgcolor = "#333355"
                
                day_cards.append(ft.Container(
                    content=ft.Row([
                        ft.Column([
                            ft.Text(f"🏋️ День {day_counter} — {group_name}",
                                   size=15, weight=ft.FontWeight.BOLD,
                                   color=self.colors['text']),
                            ft.Text(exercise_names,
                                   size=11, color=self.colors['text_secondary']),
                            ft.Text(f"📊 {ex_count} упр. • {total_sets} подх.",
                                   size=11, color=self.colors['primary']),
                        ], spacing=3, expand=True),
                        ft.Container(
                            content=ft.Text(btn_icon, size=20),
                            width=50,
                            height=50,
                            bgcolor=btn_bgcolor,
                            border_radius=25,
                            alignment=ft.alignment.center,
                            on_click=lambda e, w=week['week'], d=day_data: self.start_workout(w, d) if can_start and not is_completed else None
                        ),
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    padding=15,
                    border_radius=15,
                    border=ft.border.all(2, border_color),
                    bgcolor="#1a1a2e",
                    margin=ft.margin.only(bottom=10, left=5, right=5),
                ))
                
                day_counter += 1
        
        content = ft.Column([
            ft.Container(height=15),
            header,
            ft.Container(height=15),
            recommendations,
            ft.Container(height=15),
            nutrition_card,
            ft.Container(height=15),
            ft.Text("📋 ПРОГРАММА ТРЕНИРОВОК", size=16, weight=ft.FontWeight.BOLD,
                   color=self.colors['text']),
            ft.Container(height=5),
            ft.Container(
                content=ft.Column(day_cards, scroll=ft.ScrollMode.AUTO),
                height=350,
            ),
            ft.Container(height=15),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO)
        
        self.add_content(ft.Container(content=content, padding=15, alignment=ft.alignment.center))
        self.page.update()
    
    # ============== ЭКРАН ТРЕНИРОВКИ ==============
    def start_workout(self, week, day_data):
        """Запуск тренировки с разминкой"""
        self.current_workout = {
            'week': week,
            'day_data': day_data,
            'current_exercise': 0,
            'current_set': 1,
            'completed_sets': 0,
        }
        # Показываем разминку перед тренировкой
        self.show_warmup(on_complete=self.show_workout)
    
    def start_workout_direct(self, week, day_data):
        """Запуск тренировки без разминки"""
        self.current_workout = {
            'week': week,
            'day_data': day_data,
            'current_exercise': 0,
            'current_set': 1,
            'completed_sets': 0,
        }
        self.show_workout()
    
    def show_workout(self):
        """Экран тренировки"""
        self.clear_page()
        
        cw = self.current_workout
        day_data = cw['day_data']
        exercises = day_data['exercises']
        
        if cw['current_exercise'] >= len(exercises):
            self.complete_workout()
            return
        
        ex = exercises[cw['current_exercise']]
        
        # GIF или эмодзи
        type_emoji = {'compound': '🏋️', 'isolation': '💪', 'core': '🎯', 'cardio': '🏃'}.get(ex['type'], '💪')
        
        # Проверяем наличие GIF
        gif_widget = ft.Text(type_emoji, size=80)
        if self.gifs_dir.exists():
            gif_path = self.gifs_dir / ex.get('gif', '')
            if gif_path.exists():
                try:
                    gif_widget = ft.Image(
                        src=str(gif_path),
                        width=150,
                        height=150,
                        fit="contain",
                    )
                except:
                    pass
        
        # Информация о повторениях
        if ex.get('is_hold', False):
            reps_text = f"{self.t('hold')} {ex['reps']} {self.t('seconds')}"
        else:
            reps_text = f"{ex['reps']} {self.t('reps')}"
        
        content = ft.Column([
            ft.Container(height=10),
            
            # Заголовок
            ft.Text(f"▶️ {self.t('week')} {cw['week']} {self.t('day')} {day_data['day']}",
                   size=18, weight=ft.FontWeight.BOLD, color=self.colors['primary']),
            ft.Text(f"{self.t('exercise')} {cw['current_exercise'] + 1} {self.t('of')} {len(exercises)}",
                   size=12, color=self.colors['text_secondary']),
            
            ft.Container(height=10),
            
            # Карточка упражнения
            ft.Container(
                content=ft.Column([
                    gif_widget,
                    ft.Text(ex['name'], size=18, weight=ft.FontWeight.BOLD,
                           color="white", text_align=ft.TextAlign.CENTER),
                    ft.Text(f"{self.t(ex['type'])} • {self.t(ex['difficulty'])}",
                           size=12, color="rgba(255,255,255,0.8)"),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                padding=20,
                border_radius=15,
                bgcolor=self.colors['success'],
            ),
            
            ft.Container(height=15),
            
            # Подход и повторения
            ft.Container(
                content=ft.Column([
                    ft.Text(f"{self.t('set')} {cw['current_set']} {self.t('of')} {ex['sets']}",
                           size=20, weight=ft.FontWeight.BOLD, color=self.colors['text']),
                    ft.Text(reps_text, size=18, color=self.colors['primary']),
                    ft.Text(f"{self.t('rest')}: {ex['rest_seconds']} {self.t('sec')}",
                           size=12, color=self.colors['text_secondary']),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                padding=15,
                border_radius=10,
                bgcolor=self.colors['card'],
            ),
            
            ft.Container(height=20),
            
            # Кнопки
            ft.ElevatedButton(
                self.t('complete_set'),
                bgcolor=self.colors['success'],
                color="white",
                width=280,
                height=50,
                on_click=lambda e: self.complete_set()
            ),
            
            ft.ElevatedButton(
                self.t('skip_exercise'),
                bgcolor=self.colors['text_secondary'],
                color="white",
                width=280,
                on_click=lambda e: self.skip_exercise()
            ),
            
            ft.ElevatedButton(
                self.t('finish_workout'),
                bgcolor=self.colors['warning'],
                color="white",
                width=280,
                on_click=lambda e: self.show_result()
            ),
            
            ft.Container(height=20),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO)
        
        self.add_content(ft.Container(content=content, padding=15, alignment=ft.alignment.center))
        self.page.update()
    
    def complete_set(self):
        """Завершение подхода"""
        cw = self.current_workout
        ex = cw['day_data']['exercises'][cw['current_exercise']]
        
        cw['completed_sets'] += 1
        cw['current_set'] += 1
        
        if cw['current_set'] > ex['sets']:
            # Переход к следующему упражнению
            cw['current_exercise'] += 1
            cw['current_set'] = 1
            self.show_workout()
        else:
            # Показываем таймер отдыха
            self.show_rest_timer(ex['rest_seconds'])
    
    def show_hold_exercise(self, exercise_name, hold_seconds, on_complete):
        """Экран для изометрического упражнения с таймером удержания"""
        self.clear_page()
        
        self.hold_timer_text = ft.Text(f"{hold_seconds}", size=100, weight=ft.FontWeight.BOLD, color=self.colors['success'])
        self.hold_progress = ft.ProgressBar(width=300, value=1.0, color=self.colors['success'], bgcolor=self.colors['card'])
        
        content = ft.Column([
            ft.Container(height=50),
            ft.Text("💪", size=80),
            ft.Text(exercise_name, size=22, weight=ft.FontWeight.BOLD, color=self.colors['text'], text_align=ft.TextAlign.CENTER),
            ft.Container(height=10),
            ft.Text(self.t('hold_time'), size=16, color=self.colors['text_secondary']),
            ft.Container(height=20),
            self.hold_timer_text,
            ft.Text(self.t('seconds'), size=18, color=self.colors['text_secondary']),
            ft.Container(height=20),
            self.hold_progress,
            ft.Container(height=30),
            ft.Text("🔥 " + self.get_motivation_message(), size=14, color=self.colors['warning'], text_align=ft.TextAlign.CENTER),
            ft.Container(height=30),
            ft.ElevatedButton(
                self.t('skip_rest'),
                bgcolor=self.colors['text_secondary'],
                color="white",
                width=200,
                on_click=lambda e: on_complete()
            ),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
        self.add_content(ft.Container(content=content, bgcolor=self.colors['bg'], expand=True))
        self.page.update()
        
        # Запускаем таймер удержания
        import threading
        def hold_countdown():
            import time
            for i in range(hold_seconds, 0, -1):
                self.hold_timer_text.value = str(i)
                self.hold_progress.value = i / hold_seconds
                try:
                    self.page.update()
                except:
                    return
                time.sleep(1)
            on_complete()
        
        threading.Thread(target=hold_countdown, daemon=True).start()
    
    def get_motivation_message(self):
        """Случайное мотивационное сообщение"""
        messages = {
            'ru': [
                "Ты можешь! Не сдавайся!",
                "Каждый подход делает тебя сильнее!",
                "Боль временна, гордость навсегда!",
                "Держись! Результат того стоит!",
                "Ты уже лучше, чем вчера!",
                "Финиш близко! Давай!",
                "Сильнее с каждым днём!",
            ],
            'en': [
                "You can do it! Don't give up!",
                "Every set makes you stronger!",
                "Pain is temporary, pride is forever!",
                "Keep going! Results are worth it!",
                "You're already better than yesterday!",
            ],
            'de': [
                "Du schaffst das! Gib nicht auf!",
                "Jeder Satz macht dich stärker!",
                "Schmerz ist vorübergehend!",
            ],
            'es': [
                "¡Tú puedes! ¡No te rindas!",
                "¡Cada serie te hace más fuerte!",
            ],
            'zh': [
                "你可以的！不要放弃！",
                "每一组都让你更强！",
            ],
        }
        import random
        return random.choice(messages.get(self.lang, messages['en']))

    def show_rest_timer(self, seconds):
        """Экран отдыха с таймером"""
        self.clear_page()
        self.rest_seconds = seconds
        
        self.timer_text = ft.Text(f"{seconds}", size=80, weight=ft.FontWeight.BOLD, color=self.colors['primary'])
        
        # Мотивационное сообщение
        motivation = self.get_motivation_message()
        
        content = ft.Column([
            ft.Container(height=60),
            ft.Text("😤", size=60),
            ft.Text(self.t('rest'), size=28, weight=ft.FontWeight.BOLD, color=self.colors['text']),
            ft.Container(height=20),
            self.timer_text,
            ft.Text(self.t('sec'), size=18, color=self.colors['text_secondary']),
            ft.Container(height=30),
            ft.Text(f"💪 {motivation}", size=14, color=self.colors['warning'], text_align=ft.TextAlign.CENTER),
            ft.Container(height=30),
            ft.ElevatedButton(
                self.t('skip_rest'),
                bgcolor=self.colors['text_secondary'],
                color="white",
                width=200,
                on_click=lambda e: self.show_workout()
            ),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
        self.add_content(ft.Container(content=content, bgcolor=self.colors['bg'], expand=True))
        self.page.update()
        
        # Запускаем таймер
        import threading
        def countdown():
            import time
            for i in range(seconds, 0, -1):
                self.timer_text.value = str(i)
                try:
                    self.page.update()
                except:
                    return
                time.sleep(1)
            self.show_workout()
        
        threading.Thread(target=countdown, daemon=True).start()
    
    def skip_exercise(self):
        """Пропуск упражнения"""
        cw = self.current_workout
        cw['current_exercise'] += 1
        cw['current_set'] = 1
        self.show_workout()
    
    def complete_workout(self):
        """Завершение тренировки"""
        cw = self.current_workout
        workout_key = (cw['week'], cw['day_data']['day'])
        self.completed_workouts.add(workout_key)
        
        # Добавляем в историю
        self.workout_history.append({
            'date': datetime.datetime.now(),
            'week': cw['week'],
            'day': cw['day_data']['day'],
            'group': cw['day_data']['group'],
            'exercises': cw['day_data']['exercises'],
            'completed_sets': cw['completed_sets'],
        })
        
        # Показываем сообщение завершения
        self.show_workout_complete_screen()
    
    def show_workout_complete_screen(self):
        """Экран завершения тренировки"""
        self.clear_page()
        cw = self.current_workout
        
        content = ft.Column([
            ft.Container(height=60),
            ft.Text("🎉", size=100),
            ft.Text(self.t('workout_complete'), size=32, weight=ft.FontWeight.BOLD,
                   color=self.colors['success']),
            ft.Text(self.t('workout_finished'), size=18, color=self.colors['text_secondary']),
            ft.Text(f"{self.t('week')} {cw['week']}, {self.t('day')} {cw['day_data']['day']}",
                   size=14, color=self.colors['text_secondary']),
            ft.Container(height=30),
            ft.ElevatedButton(
                "🧘 " + self.t('stretching'),
                bgcolor=self.colors['secondary'],
                color="white",
                width=250,
                on_click=lambda e: self.show_stretching()
            ),
            ft.Container(height=10),
            ft.ElevatedButton(
                self.t('back_to_program'),
                bgcolor=self.colors['primary'],
                color="white",
                width=250,
                on_click=lambda e: self.show_result()
            ),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
        self.add_content(ft.Container(content=content, bgcolor=self.colors['bg'], expand=True))
        self.page.update()
    
    # ============== ЭКРАН ПРОГРЕССА ==============
    def show_progress(self):
        """Экран отслеживания прогресса"""
        self.clear_page()
        
        current_weight = self.user_data.get('weight', 70)
        if self.progress_data['weight']:
            current_weight = self.progress_data['weight'][-1][1]
        
        # Поля ввода
        self.weight_input = ft.TextField(
            label=f"⚖️ {self.t('weight')} ({self.t('kg')})",
            width=200,
            keyboard_type=ft.KeyboardType.NUMBER,
            value=str(current_weight),
        )
        
        self.chest_input = ft.TextField(label=self.t('chest_label'), width=120, keyboard_type=ft.KeyboardType.NUMBER)
        self.waist_input = ft.TextField(label=self.t('waist_label'), width=120, keyboard_type=ft.KeyboardType.NUMBER)
        self.hips_input = ft.TextField(label=self.t('hips_label'), width=120, keyboard_type=ft.KeyboardType.NUMBER)
        self.arms_input = ft.TextField(label=self.t('arms_label'), width=120, keyboard_type=ft.KeyboardType.NUMBER)
        
        content = ft.Column([
            ft.Container(height=10),
            ft.Text(self.t('progress_title'), size=28, weight=ft.FontWeight.BOLD,
                   color=self.colors['text']),
            ft.Container(height=15),
            
            # Вес
            ft.Container(
                content=ft.Column([
                    ft.Text(self.t('weight_title'), size=18, weight=ft.FontWeight.BOLD,
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
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                padding=20,
                border_radius=15,
                bgcolor=self.colors['card'],
            ),
            
            ft.Container(height=15),
            
            # Замеры
            ft.Container(
                content=ft.Column([
                    ft.Text(self.t('measurements'), size=18, weight=ft.FontWeight.BOLD,
                           color=self.colors['text']),
                    ft.Row([self.chest_input, self.waist_input], 
                          alignment=ft.MainAxisAlignment.CENTER, spacing=10),
                    ft.Row([self.hips_input, self.arms_input],
                          alignment=ft.MainAxisAlignment.CENTER, spacing=10),
                    ft.ElevatedButton(
                        self.t('save_btn'),
                        bgcolor=self.colors['success'],
                        color="white",
                        on_click=self.save_measurements
                    ),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                padding=20,
                border_radius=15,
                bgcolor=self.colors['card'],
            ),
            
            ft.Container(height=15),
            
            # История тренировок
            ft.Container(
                content=ft.Column([
                    ft.Text(f"📊 {self.t('total_workouts')}: {len(self.workout_history)}", 
                           size=16, color=self.colors['text']),
                    ft.Text(self.t('great_progress') if len(self.workout_history) >= 3 else "",
                           size=14, color=self.colors['success']),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=15,
                border_radius=10,
                bgcolor=self.colors['card'],
            ),
            
            ft.Container(height=20),
            
            ft.ElevatedButton(
                self.t('back_to_program'),
                bgcolor=self.colors['text_secondary'],
                color="white",
                on_click=lambda e: self.show_result()
            ),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO)
        
        self.add_content(ft.Container(content=content, padding=15, alignment=ft.alignment.center))
        self.page.update()
    
    def add_weight(self, e):
        """Добавление записи веса"""
        try:
            weight = float(self.weight_input.value)
            if 40 <= weight <= 200:
                self.progress_data['weight'].append((datetime.datetime.now(), weight))
                self.user_data['weight'] = weight
                self.show_progress()
        except:
            pass
    
    def save_measurements(self, e):
        """Сохранение замеров"""
        date = datetime.datetime.now()
        
        if self.chest_input.value:
            try:
                val = float(self.chest_input.value)
                if 50 <= val <= 200:
                    self.progress_data['measurements']['chest'].append((date, val))
            except:
                pass
        
        if self.waist_input.value:
            try:
                val = float(self.waist_input.value)
                if 40 <= val <= 150:
                    self.progress_data['measurements']['waist'].append((date, val))
            except:
                pass
        
        if self.hips_input.value:
            try:
                val = float(self.hips_input.value)
                if 50 <= val <= 180:
                    self.progress_data['measurements']['hips'].append((date, val))
            except:
                pass
        
        if self.arms_input.value:
            try:
                val = float(self.arms_input.value)
                if 20 <= val <= 60:
                    self.progress_data['measurements']['arms'].append((date, val))
            except:
                pass
        
        self.page.snack_bar = ft.SnackBar(ft.Text("✅ Замеры сохранены!"))
        self.page.snack_bar.open = True
        self.page.update()
    
    def save_program(self):
        """Сохранение программы в JSON файл"""
        try:
            save_data = {
                'user_data': self.user_data,
                'program_data': self.program_data,
                'completed_workouts': list(self.completed_workouts),
                'workout_history': [
                    {
                        'date': h['date'].isoformat() if isinstance(h['date'], datetime.datetime) else h['date'],
                        'week': h['week'],
                        'day': h['day'],
                        'group': h['group'],
                        'completed_sets': h.get('completed_sets', 0),
                    } for h in self.workout_history
                ],
                'progress_data': {
                    'weight': [(d.isoformat() if isinstance(d, datetime.datetime) else d, w) for d, w in self.progress_data['weight']],
                    'measurements': {
                        k: [(d.isoformat() if isinstance(d, datetime.datetime) else d, v) for d, v in vals]
                        for k, vals in self.progress_data['measurements'].items()
                    },
                },
                'lang': self.lang,
                'theme': self.theme,
            }
            
            save_path = Path(__file__).parent / 'saved_program.json'
            with open(save_path, 'w', encoding='utf-8') as f:
                json.dump(save_data, f, ensure_ascii=False, indent=2)
            
            self.page.snack_bar = ft.SnackBar(ft.Text(f"✅ {self.t('program_saved')}"))
            self.page.snack_bar.open = True
            self.page.update()
        except Exception as e:
            self.page.snack_bar = ft.SnackBar(ft.Text(f"❌ Ошибка: {e}"))
            self.page.snack_bar.open = True
            self.page.update()
    
    def load_program(self):
        """Загрузка программы из JSON файла"""
        try:
            save_path = Path(__file__).parent / 'saved_program.json'
            if not save_path.exists():
                self.page.snack_bar = ft.SnackBar(ft.Text(f"❌ {self.t('no_saved_program')}"))
                self.page.snack_bar.open = True
                self.page.update()
                return
            
            with open(save_path, 'r', encoding='utf-8') as f:
                save_data = json.load(f)
            
            self.user_data = save_data.get('user_data', {})
            self.program_data = save_data.get('program_data')
            self.completed_workouts = set(tuple(x) for x in save_data.get('completed_workouts', []))
            self.lang = save_data.get('lang', 'ru')
            self.theme = save_data.get('theme', 'dark')
            self.set_colors()
            
            # Восстанавливаем историю
            self.workout_history = []
            for h in save_data.get('workout_history', []):
                self.workout_history.append({
                    'date': datetime.datetime.fromisoformat(h['date']) if isinstance(h['date'], str) else h['date'],
                    'week': h['week'],
                    'day': h['day'],
                    'group': h['group'],
                    'completed_sets': h.get('completed_sets', 0),
                    'exercises': [],
                })
            
            # Восстанавливаем прогресс
            weight_data = save_data.get('progress_data', {}).get('weight', [])
            self.progress_data['weight'] = [
                (datetime.datetime.fromisoformat(d) if isinstance(d, str) else d, w)
                for d, w in weight_data
            ]
            
            self.page.snack_bar = ft.SnackBar(ft.Text(f"✅ {self.t('program_loaded')}"))
            self.page.snack_bar.open = True
            self.page.update()
            
            self.show_result()
        except Exception as e:
            self.page.snack_bar = ft.SnackBar(ft.Text(f"❌ Ошибка загрузки: {e}"))
            self.page.snack_bar.open = True
            self.page.update()
    
    # ============== ДНЕВНИК ТРЕНИРОВОК ==============
    def show_diary(self):
        """Экран дневника тренировок"""
        self.clear_page()
        
        # Статистика
        total_workouts = len(self.workout_history)
        total_sets = sum(h.get('completed_sets', 0) for h in self.workout_history)
        
        # Группы мышц
        groups_count = {}
        for h in self.workout_history:
            g = h.get('group', 'unknown')
            groups_count[g] = groups_count.get(g, 0) + 1
        
        # История карточки
        history_cards = []
        for h in reversed(self.workout_history[-10:]):  # Последние 10
            date_str = h['date'].strftime('%d.%m.%Y %H:%M') if isinstance(h['date'], datetime.datetime) else str(h['date'])
            group_name = self.t(h['group']) if h['group'] in LOCALES[self.lang] else h['group']
            history_cards.append(
                ft.Container(
                    content=ft.Row([
                        ft.Column([
                            ft.Text(f"📅 {date_str}", size=12, color=self.colors['text_secondary']),
                            ft.Text(f"{self.t('week')} {h['week']}, {self.t('day')} {h['day']} - {group_name}",
                                   size=14, weight=ft.FontWeight.BOLD, color=self.colors['text']),
                            ft.Text(f"✅ {h.get('completed_sets', 0)} {self.t('sets')}",
                                   size=12, color=self.colors['success']),
                        ], spacing=3, expand=True),
                        ft.Text("🏋️", size=30),
                    ]),
                    padding=15,
                    border_radius=10,
                    bgcolor=self.colors['card'],
                    margin=ft.margin.only(bottom=8),
                )
            )
        
        if not history_cards:
            history_cards = [ft.Text(self.t('no_history'), size=14, color=self.colors['text_secondary'])]
        
        content = ft.Column([
            ft.Container(height=10),
            ft.Row([
                ft.Container(content=ft.Text("←", size=24, color=self.colors['text']), on_click=lambda e: self.show_result()),
                ft.Text(self.t('diary'), size=24, weight=ft.FontWeight.BOLD, color=self.colors['text']),
            ]),
            ft.Container(height=15),
            
            # Статистика
            ft.Container(
                content=ft.Column([
                    ft.Text(self.t('workout_history'), size=18, weight=ft.FontWeight.BOLD, color=self.colors['text']),
                    ft.Row([
                        ft.Container(
                            content=ft.Column([
                                ft.Text(str(total_workouts), size=32, weight=ft.FontWeight.BOLD, color=self.colors['primary']),
                                ft.Text(self.t('completed_workouts'), size=11, color=self.colors['text_secondary']),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            expand=True,
                        ),
                        ft.Container(
                            content=ft.Column([
                                ft.Text(str(total_sets), size=32, weight=ft.FontWeight.BOLD, color=self.colors['success']),
                                ft.Text(self.t('sets'), size=11, color=self.colors['text_secondary']),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            expand=True,
                        ),
                    ]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                padding=20,
                border_radius=15,
                bgcolor=self.colors['card'],
            ),
            
            ft.Container(height=15),
            
            # История
            ft.Text(f"📋 {self.t('workout_history')}", size=16, weight=ft.FontWeight.BOLD, color=self.colors['text']),
            ft.Container(
                content=ft.Column(history_cards, scroll=ft.ScrollMode.AUTO),
                height=300,
            ),
            
            ft.Container(height=15),
            
            ft.ElevatedButton(
                self.t('back_to_program'),
                bgcolor=self.colors['primary'],
                color="white",
                on_click=lambda e: self.show_result()
            ),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO)
        
        self.add_content(ft.Container(content=content, padding=15, alignment=ft.alignment.center))
        self.page.update()
    
    # ============== ЭКРАН РЕЦЕПТОВ ==============
    def show_recipes(self, category='all'):
        """Экран рецептов"""
        self.clear_page()
        
        # Фильтруем рецепты
        if category == 'all':
            filtered = RECIPES
        else:
            filtered = [r for r in RECIPES if r['category'] == category]
        
        # Категории
        categories = [
            ('all', self.t('all_recipes')),
            ('breakfast', self.t('breakfast')),
            ('lunch', self.t('lunch')),
            ('dinner', self.t('dinner')),
            ('snack', self.t('snack')),
            ('high_protein', self.t('high_protein')),
        ]
        
        category_chips = ft.Row([
            ft.Container(
                content=ft.Text(name, size=12, color="white" if cat == category else self.colors['text']),
                bgcolor=self.colors['primary'] if cat == category else self.colors['card'],
                padding=ft.Padding(left=12, right=12, top=8, bottom=8),
                border_radius=20,
                on_click=lambda e, c=cat: self.show_recipes(c),
            ) for cat, name in categories
        ], wrap=True, spacing=8)
        
        # Карточки рецептов
        recipe_cards = []
        for recipe in filtered:
            name = recipe['name'].get(self.lang, recipe['name']['en'])
            card = ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text(name[:4], size=32),  # Emoji из названия
                        ft.Column([
                            ft.Text(name, size=14, weight=ft.FontWeight.BOLD, color=self.colors['text']),
                            ft.Text(f"⏱️ {recipe['time']} {self.t('minutes')}", size=11, color=self.colors['text_secondary']),
                        ], spacing=2, expand=True),
                        ft.Text("›", size=24, color=self.colors['text_secondary']),
                    ]),
                    ft.Row([
                        ft.Container(
                            content=ft.Text(f"{recipe['calories']}\nККал", size=10, text_align=ft.TextAlign.CENTER, color=self.colors['primary']),
                            expand=True,
                        ),
                        ft.Container(
                            content=ft.Text(f"{recipe['protein']}г\nБелок", size=10, text_align=ft.TextAlign.CENTER, color=self.colors['success']),
                            expand=True,
                        ),
                        ft.Container(
                            content=ft.Text(f"{recipe['fat']}г\nЖиры", size=10, text_align=ft.TextAlign.CENTER, color=self.colors['warning']),
                            expand=True,
                        ),
                        ft.Container(
                            content=ft.Text(f"{recipe['carbs']}г\nУглев", size=10, text_align=ft.TextAlign.CENTER, color=self.colors['secondary']),
                            expand=True,
                        ),
                    ]),
                ], spacing=10),
                padding=15,
                border_radius=15,
                bgcolor=self.colors['card'],
                on_click=lambda e, r=recipe: self.show_recipe_detail(r),
            )
            recipe_cards.append(card)
        
        content = ft.Column([
            ft.Container(height=10),
            ft.Row([
                ft.Container(content=ft.Text("←", size=24, color=self.colors['text']), on_click=lambda e: self.show_nutrition()),
                ft.Text(self.t('recipes_title'), size=24, weight=ft.FontWeight.BOLD, color=self.colors['text']),
            ]),
            ft.Text(self.t('recipes_subtitle'), size=14, color=self.colors['text_secondary']),
            ft.Container(height=10),
            category_chips,
            ft.Container(height=15),
            ft.Column(recipe_cards, spacing=10, scroll=ft.ScrollMode.AUTO),
        ], spacing=5, scroll=ft.ScrollMode.AUTO)
        
        self.add_content(ft.Container(content=content, padding=15, alignment=ft.alignment.center))
        self.page.update()
    
    def show_recipe_detail(self, recipe):
        """Показать детали рецепта"""
        name = recipe['name'].get(self.lang, recipe['name']['en'])
        ingredients = recipe['ingredients'].get(self.lang, recipe['ingredients']['en'])
        steps = recipe['steps'].get(self.lang, recipe['steps']['en'])
        
        def close_sheet(e):
            bs.open = False
            self.page.update()
        
        bs = ft.BottomSheet(
            open=True,
            content=ft.Container(
                content=ft.Column([
                    ft.Text(name, size=20, weight=ft.FontWeight.BOLD, color=self.colors['text']),
                    ft.Row([
                        ft.Text(f"🔥 {recipe['calories']} ккал", size=12, color=self.colors['primary']),
                        ft.Text(f"⏱️ {recipe['time']} мин", size=12, color=self.colors['text_secondary']),
                    ]),
                    ft.Divider(),
                    ft.Text(self.t('recipe_ingredients'), size=16, weight=ft.FontWeight.BOLD, color=self.colors['text']),
                    ft.Column([ft.Text(f"• {ing}", size=13, color=self.colors['text_secondary']) for ing in ingredients], spacing=3),
                    ft.Container(height=10),
                    ft.Text(self.t('recipe_steps'), size=16, weight=ft.FontWeight.BOLD, color=self.colors['text']),
                    ft.Column([ft.Text(f"{i+1}. {step}", size=13, color=self.colors['text_secondary']) for i, step in enumerate(steps)], spacing=5),
                    ft.Container(height=15),
                    ft.ElevatedButton("✅ OK", bgcolor=self.colors['primary'], color="white", width=200, on_click=close_sheet),
                ], spacing=8, scroll=ft.ScrollMode.AUTO),
                padding=20,
                bgcolor=self.colors['card'],
            ),
        )
        self.page.overlay.append(bs)
        self.page.update()

    # ============== ЭКРАН РАЗМИНКИ ==============
    def show_warmup(self, on_complete=None):
        """Экран разминки перед тренировкой"""
        self.clear_page()
        
        warmup_exercises = [
            {'name': 'Вращения головой', 'duration': 30, 'emoji': '🔄'},
            {'name': 'Вращения плечами', 'duration': 30, 'emoji': '💪'},
            {'name': 'Махи руками', 'duration': 30, 'emoji': '🙌'},
            {'name': 'Наклоны в стороны', 'duration': 30, 'emoji': '↔️'},
            {'name': 'Вращения тазом', 'duration': 30, 'emoji': '🔃'},
            {'name': 'Приседания разминочные', 'duration': 45, 'emoji': '🦵'},
            {'name': 'Выпады на месте', 'duration': 45, 'emoji': '🚶'},
            {'name': 'Прыжки на месте', 'duration': 30, 'emoji': '⬆️'},
        ]
        
        self.warmup_index = 0
        self.warmup_exercises = warmup_exercises
        self.warmup_callback = on_complete
        
        self.show_warmup_exercise()
    
    def show_warmup_exercise(self):
        """Показать текущее упражнение разминки"""
        self.clear_page()
        
        if self.warmup_index >= len(self.warmup_exercises):
            # Разминка завершена
            if self.warmup_callback:
                self.warmup_callback()
            else:
                self.show_workout()
            return
        
        ex = self.warmup_exercises[self.warmup_index]
        total = len(self.warmup_exercises)
        
        self.warmup_timer_text = ft.Text(f"{ex['duration']}", size=80, weight=ft.FontWeight.BOLD, color=self.colors['success'])
        
        content = ft.Column([
            ft.Container(height=30),
            ft.Text(f"🔥 {self.t('warmup')}", size=24, weight=ft.FontWeight.BOLD, color=self.colors['warning']),
            ft.Text(f"{self.warmup_index + 1} / {total}", size=14, color=self.colors['text_secondary']),
            ft.Container(height=30),
            ft.Text(ex['emoji'], size=100),
            ft.Text(ex['name'], size=22, weight=ft.FontWeight.BOLD, color=self.colors['text'], text_align=ft.TextAlign.CENTER),
            ft.Container(height=20),
            self.warmup_timer_text,
            ft.Text(self.t('sec'), size=16, color=self.colors['text_secondary']),
            ft.Container(height=30),
            ft.ProgressBar(width=300, value=1.0, color=self.colors['success'], bgcolor=self.colors['card']),
            ft.Container(height=20),
            ft.ElevatedButton(
                self.t('skip_rest'),
                bgcolor=self.colors['text_secondary'],
                color="white",
                on_click=lambda e: self.next_warmup_exercise()
            ),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
        self.add_content(ft.Container(content=content, bgcolor=self.colors['bg'], expand=True))
        self.page.update()
        
        # Таймер
        import threading
        def countdown():
            import time
            for i in range(ex['duration'], 0, -1):
                self.warmup_timer_text.value = str(i)
                try:
                    self.page.update()
                except:
                    return
                time.sleep(1)
            self.next_warmup_exercise()
        
        threading.Thread(target=countdown, daemon=True).start()
    
    def next_warmup_exercise(self):
        """Следующее упражнение разминки"""
        self.warmup_index += 1
        self.show_warmup_exercise()

    # ============== ЭКРАН РАСТЯЖКИ ==============
    def show_stretching(self):
        """Экран растяжки после тренировки"""
        self.clear_page()
        
        stretching_exercises = [
            {'name': 'Растяжка шеи', 'duration': 20, 'emoji': '🧘'},
            {'name': 'Растяжка плеч', 'duration': 25, 'emoji': '💆'},
            {'name': 'Растяжка трицепса', 'duration': 20, 'emoji': '💪'},
            {'name': 'Наклон вперёд', 'duration': 30, 'emoji': '🙇'},
            {'name': 'Растяжка квадрицепса', 'duration': 25, 'emoji': '🦵'},
            {'name': 'Растяжка бедра', 'duration': 30, 'emoji': '🧎'},
            {'name': 'Поза ребёнка', 'duration': 30, 'emoji': '🙏'},
            {'name': 'Глубокое дыхание', 'duration': 30, 'emoji': '🌬️'},
        ]
        
        self.stretch_index = 0
        self.stretch_exercises = stretching_exercises
        
        self.show_stretch_exercise()
    
    def show_stretch_exercise(self):
        """Показать текущее упражнение растяжки"""
        self.clear_page()
        
        if self.stretch_index >= len(self.stretch_exercises):
            self.show_stretching_complete()
            return
        
        ex = self.stretch_exercises[self.stretch_index]
        total = len(self.stretch_exercises)
        
        self.stretch_timer_text = ft.Text(f"{ex['duration']}", size=80, weight=ft.FontWeight.BOLD, color=self.colors['secondary'])
        
        content = ft.Column([
            ft.Container(height=30),
            ft.Text(f"🧘 {self.t('stretching')}", size=24, weight=ft.FontWeight.BOLD, color=self.colors['secondary']),
            ft.Text(f"{self.stretch_index + 1} / {total}", size=14, color=self.colors['text_secondary']),
            ft.Container(height=30),
            ft.Text(ex['emoji'], size=100),
            ft.Text(ex['name'], size=22, weight=ft.FontWeight.BOLD, color=self.colors['text'], text_align=ft.TextAlign.CENTER),
            ft.Container(height=20),
            self.stretch_timer_text,
            ft.Text(self.t('sec'), size=16, color=self.colors['text_secondary']),
            ft.Container(height=30),
            ft.ElevatedButton(
                self.t('skip_rest'),
                bgcolor=self.colors['text_secondary'],
                color="white",
                on_click=lambda e: self.next_stretch_exercise()
            ),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
        self.add_content(ft.Container(content=content, bgcolor=self.colors['bg'], expand=True))
        self.page.update()
        
        import threading
        def countdown():
            import time
            for i in range(ex['duration'], 0, -1):
                self.stretch_timer_text.value = str(i)
                try:
                    self.page.update()
                except:
                    return
                time.sleep(1)
            self.next_stretch_exercise()
        
        threading.Thread(target=countdown, daemon=True).start()
    
    def next_stretch_exercise(self):
        self.stretch_index += 1
        self.show_stretch_exercise()
    
    def show_stretching_complete(self):
        """Экран завершения растяжки"""
        self.clear_page()
        
        content = ft.Column([
            ft.Container(height=80),
            ft.Text("🧘", size=100),
            ft.Text(self.t('stretching_complete'), size=28, weight=ft.FontWeight.BOLD, color=self.colors['secondary']),
            ft.Text(self.t('great_job'), size=16, color=self.colors['text_secondary']),
            ft.Container(height=40),
            ft.ElevatedButton(
                self.t('back_to_program'),
                bgcolor=self.colors['primary'],
                color="white",
                width=250,
                on_click=lambda e: self.show_result()
            ),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
        self.add_content(ft.Container(content=content, bgcolor=self.colors['bg'], expand=True))
        self.page.update()

    # ============== ДОСТИЖЕНИЯ / БЕЙДЖИ ==============
    def get_achievements(self):
        """Получить список достижений"""
        achievements = []
        total_workouts = len(self.workout_history)
        
        # Первая тренировка
        if total_workouts >= 1:
            achievements.append({'id': 'first', 'name': self.t('ach_first'), 'emoji': '🌟', 'desc': self.t('ach_first_desc')})
        
        # 5 тренировок
        if total_workouts >= 5:
            achievements.append({'id': 'five', 'name': self.t('ach_five'), 'emoji': '🔥', 'desc': self.t('ach_five_desc')})
        
        # 10 тренировок
        if total_workouts >= 10:
            achievements.append({'id': 'ten', 'name': self.t('ach_ten'), 'emoji': '💪', 'desc': self.t('ach_ten_desc')})
        
        # 25 тренировок
        if total_workouts >= 25:
            achievements.append({'id': 'twentyfive', 'name': self.t('ach_twentyfive'), 'emoji': '🏆', 'desc': self.t('ach_twentyfive_desc')})
        
        # 50 тренировок
        if total_workouts >= 50:
            achievements.append({'id': 'fifty', 'name': self.t('ach_fifty'), 'emoji': '👑', 'desc': self.t('ach_fifty_desc')})
        
        # 100 тренировок
        if total_workouts >= 100:
            achievements.append({'id': 'hundred', 'name': self.t('ach_hundred'), 'emoji': '🎖️', 'desc': self.t('ach_hundred_desc')})
        
        # Неделя подряд
        if self.check_streak(7):
            achievements.append({'id': 'week_streak', 'name': self.t('ach_week'), 'emoji': '📅', 'desc': self.t('ach_week_desc')})
        
        return achievements
    
    def check_streak(self, days):
        """Проверить серию тренировок"""
        if len(self.workout_history) < days:
            return False
        # Упрощённая проверка
        return len(self.workout_history) >= days
    
    def show_achievements(self):
        """Экран достижений"""
        self.clear_page()
        
        achievements = self.get_achievements()
        total_workouts = len(self.workout_history)
        
        # Все возможные достижения
        all_achievements = [
            {'id': 'first', 'name': self.t('ach_first'), 'emoji': '🌟', 'required': 1},
            {'id': 'five', 'name': self.t('ach_five'), 'emoji': '🔥', 'required': 5},
            {'id': 'ten', 'name': self.t('ach_ten'), 'emoji': '💪', 'required': 10},
            {'id': 'twentyfive', 'name': self.t('ach_twentyfive'), 'emoji': '🏆', 'required': 25},
            {'id': 'fifty', 'name': self.t('ach_fifty'), 'emoji': '👑', 'required': 50},
            {'id': 'hundred', 'name': self.t('ach_hundred'), 'emoji': '🎖️', 'required': 100},
        ]
        
        ach_cards = []
        for ach in all_achievements:
            unlocked = total_workouts >= ach['required']
            progress = min(total_workouts / ach['required'], 1.0)
            
            ach_cards.append(
                ft.Container(
                    content=ft.Row([
                        ft.Text(ach['emoji'] if unlocked else '🔒', size=40),
                        ft.Column([
                            ft.Text(ach['name'], size=14, weight=ft.FontWeight.BOLD, 
                                   color=self.colors['text'] if unlocked else self.colors['text_secondary']),
                            ft.ProgressBar(width=150, value=progress, 
                                          color=self.colors['success'] if unlocked else self.colors['text_secondary'],
                                          bgcolor=self.colors['card']),
                            ft.Text(f"{total_workouts}/{ach['required']}", size=11, color=self.colors['text_secondary']),
                        ], spacing=3, expand=True),
                    ]),
                    padding=15,
                    border_radius=10,
                    bgcolor=self.colors['card'] if unlocked else self.colors['bg'],
                    opacity=1.0 if unlocked else 0.6,
                )
            )
        
        content = ft.Column([
            ft.Container(height=10),
            ft.Row([
                ft.Container(content=ft.Text("←", size=24, color=self.colors['text']), on_click=lambda e: self.show_result()),
                ft.Text(self.t('achievements'), size=24, weight=ft.FontWeight.BOLD, color=self.colors['text']),
            ]),
            ft.Text(f"🏅 {len(achievements)} / {len(all_achievements)} {self.t('unlocked')}", size=14, color=self.colors['text_secondary']),
            ft.Container(height=15),
            ft.Column(ach_cards, spacing=10, scroll=ft.ScrollMode.AUTO),
        ], scroll=ft.ScrollMode.AUTO)
        
        self.add_content(ft.Container(content=content, padding=15, alignment=ft.alignment.center))
        self.page.update()

    # ============== КАЛЬКУЛЯТОРЫ ==============
    def show_calculators(self):
        """Экран калькуляторов"""
        self.clear_page()
        
        calcs = [
            {'name': self.t('bmi_calc'), 'emoji': '📊', 'action': self.show_bmi_calculator},
            {'name': self.t('calorie_calc'), 'emoji': '🔥', 'action': self.show_calorie_calculator},
            {'name': self.t('water_calc'), 'emoji': '💧', 'action': self.show_water_calculator},
            {'name': self.t('ideal_weight_calc'), 'emoji': '⚖️', 'action': self.show_ideal_weight_calculator},
            {'name': self.t('body_fat_calc'), 'emoji': '📐', 'action': self.show_body_fat_calculator},
        ]
        
        calc_cards = []
        for calc in calcs:
            calc_cards.append(
                ft.Container(
                    content=ft.Row([
                        ft.Text(calc['emoji'], size=40),
                        ft.Text(calc['name'], size=16, weight=ft.FontWeight.BOLD, color=self.colors['text'], expand=True),
                        ft.Text("→", size=20, color=self.colors['text_secondary']),
                    ]),
                    padding=20,
                    border_radius=15,
                    bgcolor=self.colors['card'],
                    on_click=lambda e, a=calc['action']: a(),
                )
            )
        
        content = ft.Column([
            ft.Container(height=10),
            ft.Row([
                ft.Container(content=ft.Text("←", size=24, color=self.colors['text']), on_click=lambda e: self.show_calculators()),
                ft.Text(self.t('calculators'), size=24, weight=ft.FontWeight.BOLD, color=self.colors['text']),
            ]),
            ft.Container(height=15),
            ft.Column(calc_cards, spacing=12),
        ], scroll=ft.ScrollMode.AUTO)
        
        self.add_content(ft.Container(content=content, padding=15, alignment=ft.alignment.center))
        self.page.update()
    
    def show_bmi_calculator(self):
        """Калькулятор ИМТ"""
        self.clear_page()
        
        height = self.user_data.get('height', 170)
        weight = self.user_data.get('weight', 70)
        
        bmi = weight / ((height / 100) ** 2)
        
        if bmi < 18.5:
            category = self.t('bmi_underweight')
            color = self.colors['warning']
        elif bmi < 25:
            category = self.t('bmi_normal')
            color = self.colors['success']
        elif bmi < 30:
            category = self.t('bmi_overweight')
            color = self.colors['warning']
        else:
            category = self.t('bmi_obese')
            color = '#ff4444'
        
        content = ft.Column([
            ft.Container(height=10),
            ft.Row([
                ft.Container(content=ft.Text("←", size=24, color=self.colors['text']), on_click=lambda e: self.show_calculators()),
                ft.Text(self.t('bmi_calc'), size=24, weight=ft.FontWeight.BOLD, color=self.colors['text']),
            ]),
            ft.Container(height=30),
            ft.Text("📊", size=80),
            ft.Text(f"{bmi:.1f}", size=60, weight=ft.FontWeight.BOLD, color=color),
            ft.Text(category, size=20, color=color),
            ft.Container(height=20),
            ft.Container(
                content=ft.Column([
                    ft.Text(f"📏 {self.t('height')}: {height} {self.t('cm')}", size=14, color=self.colors['text']),
                    ft.Text(f"⚖️ {self.t('weight')}: {weight} {self.t('kg')}", size=14, color=self.colors['text']),
                ], spacing=5),
                padding=15,
                border_radius=10,
                bgcolor=self.colors['card'],
            ),
            ft.Container(height=20),
            ft.Text(self.t('bmi_scale'), size=14, weight=ft.FontWeight.BOLD, color=self.colors['text']),
            ft.Text("< 18.5 - " + self.t('bmi_underweight'), size=12, color=self.colors['text_secondary']),
            ft.Text("18.5-24.9 - " + self.t('bmi_normal'), size=12, color=self.colors['text_secondary']),
            ft.Text("25-29.9 - " + self.t('bmi_overweight'), size=12, color=self.colors['text_secondary']),
            ft.Text("> 30 - " + self.t('bmi_obese'), size=12, color=self.colors['text_secondary']),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO)
        
        self.add_content(ft.Container(content=content, padding=15, alignment=ft.alignment.center))
        self.page.update()
    
    def show_calorie_calculator(self):
        """Калькулятор калорий"""
        self.clear_page()
        
        height = self.user_data.get('height', 170)
        weight = self.user_data.get('weight', 70)
        age = self.user_data.get('age', 25)
        gender = self.user_data.get('gender', 'male')
        
        # Формула Миффлина-Сан Жеора
        if gender == 'male':
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161
        
        # Коэффициенты активности
        activity_levels = [
            (1.2, self.t('activity_sedentary')),
            (1.375, self.t('activity_light')),
            (1.55, self.t('activity_moderate')),
            (1.725, self.t('activity_active')),
            (1.9, self.t('activity_very_active')),
        ]
        
        calorie_cards = []
        for mult, name in activity_levels:
            calories = int(bmr * mult)
            calorie_cards.append(
                ft.Container(
                    content=ft.Row([
                        ft.Text(name, size=12, color=self.colors['text'], expand=True),
                        ft.Text(f"{calories} ккал", size=14, weight=ft.FontWeight.BOLD, color=self.colors['primary']),
                    ]),
                    padding=12,
                    border_radius=8,
                    bgcolor=self.colors['card'],
                )
            )
        
        content = ft.Column([
            ft.Container(height=10),
            ft.Row([
                ft.Container(content=ft.Text("←", size=24, color=self.colors['text']), on_click=lambda e: self.show_calculators()),
                ft.Text(self.t('calorie_calc'), size=24, weight=ft.FontWeight.BOLD, color=self.colors['text']),
            ]),
            ft.Container(height=20),
            ft.Text("🔥", size=60),
            ft.Text(f"BMR: {int(bmr)} ккал", size=28, weight=ft.FontWeight.BOLD, color=self.colors['primary']),
            ft.Text(self.t('bmr_desc'), size=12, color=self.colors['text_secondary']),
            ft.Container(height=20),
            ft.Text(self.t('daily_calories'), size=16, weight=ft.FontWeight.BOLD, color=self.colors['text']),
            ft.Container(height=10),
            ft.Column(calorie_cards, spacing=8),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO)
        
        self.add_content(ft.Container(content=content, bgcolor=self.colors['bg'], expand=True, padding=15))
        self.page.update()
    
    def show_water_calculator(self):
        """Калькулятор воды"""
        self.clear_page()
        
        weight = self.user_data.get('weight', 70)
        water_ml = int(weight * 35)  # 35 мл на кг
        water_liters = water_ml / 1000
        glasses = int(water_ml / 250)  # стаканы по 250 мл
        
        content = ft.Column([
            ft.Container(height=10),
            ft.Row([
                ft.Container(content=ft.Text("←", size=24, color=self.colors['text']), on_click=lambda e: self.show_calculators()),
                ft.Text(self.t('water_calc'), size=24, weight=ft.FontWeight.BOLD, color=self.colors['text']),
            ]),
            ft.Container(height=40),
            ft.Text("💧", size=100),
            ft.Text(f"{water_liters:.1f} л", size=50, weight=ft.FontWeight.BOLD, color=self.colors['primary']),
            ft.Text(self.t('per_day'), size=16, color=self.colors['text_secondary']),
            ft.Container(height=30),
            ft.Container(
                content=ft.Column([
                    ft.Text(f"🥛 {glasses} {self.t('glasses')}", size=18, color=self.colors['text']),
                    ft.Text(f"💧 {water_ml} мл", size=14, color=self.colors['text_secondary']),
                ], spacing=5, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=20,
                border_radius=15,
                bgcolor=self.colors['card'],
            ),
            ft.Container(height=20),
            ft.Text(self.t('water_tips'), size=14, weight=ft.FontWeight.BOLD, color=self.colors['text']),
            ft.Text("• " + self.t('water_tip_1'), size=12, color=self.colors['text_secondary']),
            ft.Text("• " + self.t('water_tip_2'), size=12, color=self.colors['text_secondary']),
            ft.Text("• " + self.t('water_tip_3'), size=12, color=self.colors['text_secondary']),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO)
        
        self.add_content(ft.Container(content=content, bgcolor=self.colors['bg'], expand=True, padding=15))
        self.page.update()
    
    def show_ideal_weight_calculator(self):
        """Калькулятор идеального веса"""
        self.clear_page()
        
        height = self.user_data.get('height', 170)
        gender = self.user_data.get('gender', 'male')
        
        # Формулы
        if gender == 'male':
            devine = 50 + 2.3 * ((height / 2.54) - 60)
            robinson = 52 + 1.9 * ((height / 2.54) - 60)
            miller = 56.2 + 1.41 * ((height / 2.54) - 60)
        else:
            devine = 45.5 + 2.3 * ((height / 2.54) - 60)
            robinson = 49 + 1.7 * ((height / 2.54) - 60)
            miller = 53.1 + 1.36 * ((height / 2.54) - 60)
        
        avg_weight = (devine + robinson + miller) / 3
        
        content = ft.Column([
            ft.Container(height=10),
            ft.Row([
                ft.Container(content=ft.Text("←", size=24, color=self.colors['text']), on_click=lambda e: self.show_calculators()),
                ft.Text(self.t('ideal_weight_calc'), size=22, weight=ft.FontWeight.BOLD, color=self.colors['text']),
            ]),
            ft.Container(height=30),
            ft.Text("⚖️", size=80),
            ft.Text(f"{avg_weight:.1f} {self.t('kg')}", size=50, weight=ft.FontWeight.BOLD, color=self.colors['success']),
            ft.Text(self.t('ideal_weight_range'), size=14, color=self.colors['text_secondary']),
            ft.Container(height=20),
            ft.Container(
                content=ft.Column([
                    ft.Row([ft.Text("Devine:", size=12, expand=True), ft.Text(f"{devine:.1f} кг", size=12, color=self.colors['primary'])]),
                    ft.Row([ft.Text("Robinson:", size=12, expand=True), ft.Text(f"{robinson:.1f} кг", size=12, color=self.colors['primary'])]),
                    ft.Row([ft.Text("Miller:", size=12, expand=True), ft.Text(f"{miller:.1f} кг", size=12, color=self.colors['primary'])]),
                ], spacing=8),
                padding=15,
                border_radius=10,
                bgcolor=self.colors['card'],
            ),
            ft.Container(height=15),
            ft.Text(f"📏 {self.t('your_height')}: {height} {self.t('cm')}", size=14, color=self.colors['text_secondary']),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO)
        
        self.add_content(ft.Container(content=content, bgcolor=self.colors['bg'], expand=True, padding=15))
        self.page.update()
    
    def show_body_fat_calculator(self):
        """Калькулятор процента жира (упрощённый)"""
        self.clear_page()
        
        # Используем ИМТ для оценки
        height = self.user_data.get('height', 170)
        weight = self.user_data.get('weight', 70)
        age = self.user_data.get('age', 25)
        gender = self.user_data.get('gender', 'male')
        
        bmi = weight / ((height / 100) ** 2)
        
        # Формула Deurenberg
        if gender == 'male':
            body_fat = 1.20 * bmi + 0.23 * age - 16.2
        else:
            body_fat = 1.20 * bmi + 0.23 * age - 5.4
        
        body_fat = max(5, min(50, body_fat))  # Ограничение
        
        if gender == 'male':
            if body_fat < 10:
                category = self.t('bf_athlete')
            elif body_fat < 15:
                category = self.t('bf_fitness')
            elif body_fat < 20:
                category = self.t('bf_average')
            else:
                category = self.t('bf_above')
        else:
            if body_fat < 18:
                category = self.t('bf_athlete')
            elif body_fat < 23:
                category = self.t('bf_fitness')
            elif body_fat < 28:
                category = self.t('bf_average')
            else:
                category = self.t('bf_above')
        
        content = ft.Column([
            ft.Container(height=10),
            ft.Row([
                ft.Container(content=ft.Text("←", size=24, color=self.colors['text']), on_click=lambda e: self.show_calculators()),
                ft.Text(self.t('body_fat_calc'), size=22, weight=ft.FontWeight.BOLD, color=self.colors['text']),
            ]),
            ft.Container(height=30),
            ft.Text("📐", size=80),
            ft.Text(f"{body_fat:.1f}%", size=50, weight=ft.FontWeight.BOLD, color=self.colors['primary']),
            ft.Text(category, size=18, color=self.colors['text_secondary']),
            ft.Container(height=20),
            ft.Text(self.t('bf_note'), size=12, color=self.colors['text_secondary'], text_align=ft.TextAlign.CENTER),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO)
        
        self.add_content(ft.Container(content=content, bgcolor=self.colors['bg'], expand=True, padding=15))
        self.page.update()

    # ============== ЭКРАН СОВЕТОВ ==============
    def show_tips(self):
        """Экран советов по тренировкам"""
        self.clear_page()
        
        tips = [
            {'emoji': '🔥', 'title': self.t('tip_warmup_title'), 'text': self.t('tip_warmup_text')},
            {'emoji': '💧', 'title': self.t('tip_water_title'), 'text': self.t('tip_water_text')},
            {'emoji': '😴', 'title': self.t('tip_sleep_title'), 'text': self.t('tip_sleep_text')},
            {'emoji': '🥗', 'title': self.t('tip_nutrition_title'), 'text': self.t('tip_nutrition_text')},
            {'emoji': '📈', 'title': self.t('tip_progress_title'), 'text': self.t('tip_progress_text')},
            {'emoji': '🧘', 'title': self.t('tip_rest_title'), 'text': self.t('tip_rest_text')},
            {'emoji': '💪', 'title': self.t('tip_technique_title'), 'text': self.t('tip_technique_text')},
            {'emoji': '🎯', 'title': self.t('tip_goals_title'), 'text': self.t('tip_goals_text')},
        ]
        
        tip_cards = []
        for tip in tips:
            tip_cards.append(
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Text(tip['emoji'], size=30),
                            ft.Text(tip['title'], size=14, weight=ft.FontWeight.BOLD, color=self.colors['text'], expand=True),
                        ]),
                        ft.Text(tip['text'], size=12, color=self.colors['text_secondary']),
                    ], spacing=8),
                    padding=15,
                    border_radius=12,
                    bgcolor=self.colors['card'],
                )
            )
        
        content = ft.Column([
            ft.Container(height=10),
            ft.Row([
                ft.Container(content=ft.Text("←", size=24, color=self.colors['text']), on_click=lambda e: self.show_result()),
                ft.Text(self.t('tips_title'), size=24, weight=ft.FontWeight.BOLD, color=self.colors['text']),
            ]),
            ft.Container(height=15),
            ft.Column(tip_cards, spacing=12, scroll=ft.ScrollMode.AUTO),
        ], scroll=ft.ScrollMode.AUTO)
        
        self.add_content(ft.Container(content=content, bgcolor=self.colors['bg'], expand=True, padding=15))
        self.page.update()

    # ============== РАСШИРЕННАЯ СТАТИСТИКА ==============
    def show_statistics(self):
        """Экран статистики"""
        self.clear_page()
        
        total_workouts = len(self.workout_history)
        total_sets = sum(h.get('completed_sets', 0) for h in self.workout_history)
        
        # Группы мышц
        groups_count = {}
        for h in self.workout_history:
            g = h.get('group', 'unknown')
            groups_count[g] = groups_count.get(g, 0) + 1
        
        # Калории (примерная оценка)
        est_calories = total_sets * 8  # ~8 ккал на подход
        
        # Время (примерная оценка)
        est_minutes = total_sets * 2  # ~2 мин на подход
        
        # Карточки групп мышц
        group_cards = []
        for group, count in sorted(groups_count.items(), key=lambda x: x[1], reverse=True):
            group_name = self.t(group) if group in LOCALES[self.lang] else group
            group_cards.append(
                ft.Container(
                    content=ft.Row([
                        ft.Text(group_name, size=12, color=self.colors['text'], expand=True),
                        ft.Text(f"{count}x", size=14, weight=ft.FontWeight.BOLD, color=self.colors['primary']),
                    ]),
                    padding=10,
                    border_radius=8,
                    bgcolor=self.colors['card'],
                )
            )
        
        content = ft.Column([
            ft.Container(height=10),
            ft.Row([
                ft.Container(content=ft.Text("←", size=24, color=self.colors['text']), on_click=lambda e: self.show_result()),
                ft.Text(self.t('statistics'), size=24, weight=ft.FontWeight.BOLD, color=self.colors['text']),
            ]),
            ft.Container(height=15),
            
            # Основные показатели
            ft.Row([
                ft.Container(
                    content=ft.Column([
                        ft.Text(str(total_workouts), size=32, weight=ft.FontWeight.BOLD, color=self.colors['primary']),
                        ft.Text(self.t('workouts'), size=11, color=self.colors['text_secondary']),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    expand=True, padding=15, border_radius=10, bgcolor=self.colors['card'],
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Text(str(total_sets), size=32, weight=ft.FontWeight.BOLD, color=self.colors['success']),
                        ft.Text(self.t('sets'), size=11, color=self.colors['text_secondary']),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    expand=True, padding=15, border_radius=10, bgcolor=self.colors['card'],
                ),
            ], spacing=10),
            
            ft.Container(height=10),
            
            ft.Row([
                ft.Container(
                    content=ft.Column([
                        ft.Text(f"~{est_calories}", size=28, weight=ft.FontWeight.BOLD, color=self.colors['warning']),
                        ft.Text(self.t('calories_burned'), size=11, color=self.colors['text_secondary']),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    expand=True, padding=15, border_radius=10, bgcolor=self.colors['card'],
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Text(f"~{est_minutes}", size=28, weight=ft.FontWeight.BOLD, color=self.colors['secondary']),
                        ft.Text(self.t('total_time'), size=11, color=self.colors['text_secondary']),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    expand=True, padding=15, border_radius=10, bgcolor=self.colors['card'],
                ),
            ], spacing=10),
            
            ft.Container(height=15),
            ft.Text(self.t('muscle_groups'), size=16, weight=ft.FontWeight.BOLD, color=self.colors['text']),
            ft.Container(height=5),
            ft.Column(group_cards if group_cards else [ft.Text(self.t('no_data'), size=12, color=self.colors['text_secondary'])], spacing=8),
        ], scroll=ft.ScrollMode.AUTO)
        
        self.add_content(ft.Container(content=content, bgcolor=self.colors['bg'], expand=True, padding=15))
        self.page.update()

    # ============== ЭКРАН "О ПРИЛОЖЕНИИ" ==============
    def show_about(self):
        """Экран информации о приложении"""
        self.clear_page()
        
        content = ft.Column([
            ft.Container(height=10),
            ft.Row([
                ft.Container(content=ft.Text("←", size=24, color=self.colors['text']), on_click=lambda e: self.show_result()),
                ft.Text(self.t('about'), size=24, weight=ft.FontWeight.BOLD, color=self.colors['text']),
            ]),
            ft.Container(height=40),
            ft.Text("💪", size=100),
            ft.Text("FitWizard Pro", size=32, weight=ft.FontWeight.BOLD, color=self.colors['primary']),
            ft.Text("v2.0", size=16, color=self.colors['text_secondary']),
            ft.Container(height=20),
            ft.Container(
                content=ft.Column([
                    ft.Text(self.t('about_desc'), size=14, color=self.colors['text'], text_align=ft.TextAlign.CENTER),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=20,
                border_radius=15,
                bgcolor=self.colors['card'],
            ),
            ft.Container(height=20),
            ft.Text("🌍 " + self.t('supported_languages') + ": RU, EN, DE, ES, ZH", size=12, color=self.colors['text_secondary']),
            ft.Text("📱 " + self.t('platforms') + ": iOS, Android, Web, Desktop", size=12, color=self.colors['text_secondary']),
            ft.Container(height=20),
            ft.Text("Made with ❤️ using Flet", size=14, color=self.colors['text_secondary']),
            ft.Text("© 2024-2026", size=12, color=self.colors['text_secondary']),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO)
        
        self.add_content(ft.Container(content=content, bgcolor=self.colors['bg'], expand=True, padding=15))
        self.page.update()


# ============== ЗАПУСК ПРИЛОЖЕНИЯ ==============

def main(page: ft.Page):
    # Не задаём page.bgcolor, фон теперь всегда градиент
    app = TrainingApp(page)


if __name__ == "__main__":
    ft.app(target=main)  # Используем app() для совместимости
