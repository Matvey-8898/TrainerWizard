

import flet as ft
import random
import datetime
import json
import os
import base64
import asyncio
from pathlib import Path

# ============== ЛОКАЛИЗАЦИЯ (5 языков) ==============

LOCALES = {
    'ru': {
        'app_title': '💪 TrainerWizard',
        'welcome': 'Добро пожаловать!',
        'welcome_subtitle': 'Создадим идеальную программу тренировок для вас',
        'motivation_text': '✨ Начни путь к своей лучшей форме',
        'male': 'Мужской',
        'female': 'Женский',
        'select': 'ВЫБРАТЬ',
        'male_desc': '💪 Силовые тренировки\n📈 Набор массы',
        'female_desc': '🎯 Тонус и стройность\n🧘 Гибкость',
        'continue_btn': 'ПРОДОЛЖИТЬ →',
        'back_btn': '← НАЗАД',
        # Параметры
        'enter_data': '📋 ВВЕДИТЕ ВАШИ ДАННЫЕ',
        'height': 'Рост',
        'weight': 'Вес',
        'age': 'Возраст',
        'cm': 'см',
        'kg': 'кг',
        'years': 'лет',
        'days_per_week': 'Дней в неделю',
        'weeks_program': 'Недель программы',
        'level': 'Уровень подготовки',
        'beginner': '🌱 Новичок',
        'intermediate': '💪 Средний',
        'advanced': '🔥 Продвинутый',
        # Валидация
        'error_height': '⚠️ Введите корректный рост!',
        'error_weight': '⚠️ Введите корректный вес!',
        'error_age': '⚠️ Введите корректный возраст!',
        'error_height_range': '⚠️ Рост должен быть 120-250 см!',
        'error_weight_range': '⚠️ Вес должен быть 40-200 кг!',
        'error_age_range': '⚠️ Возраст должен быть 14-80 лет!',
        # Цели
        'choose_goal': '🎯 ВЫБЕРИТЕ ЦЕЛЬ',
        'goal_subtitle': 'Что вы хотите достичь?',
        'weight_loss': 'Сброс веса',
        'weight_loss_desc': '🔥 HIIT-тренировки\n📉 Сжигание калорий',
        'muscle_gain': 'Набор массы',
        'muscle_gain_desc': '💪 Силовые упражнения\n📈 Рост мышц',
        # Фокус
        'choose_zone': '🎯 ВЫБЕРИТЕ ЗОНУ ТРЕНИРОВКИ',
        'focus_question': 'НА КАКУЮ ЧАСТЬ ТЕЛА ХОТИТЕ\nСДЕЛАТЬ УПОР?',
        'all_muscles': 'ВСЕ ГРУППЫ МЫШЦ',
        'chest_zone': 'ГРУДЬ',
        'arms_zone': 'РУКИ',
        'core_zone': 'ПРЕСС',
        'legs_zone': 'НОГИ',
        'Full Body': 'Всё тело',
        'Legs': 'Ноги',
        'Chest': 'Грудь',
        'Back': 'Спина',
        'Arms': 'Руки',
        'Shoulders': 'Плечи',
        'Core': 'Пресс',
        'Weight Loss': 'Похудение',
        # Безопасность
        'safety_title': '⚠️ БЕЗОПАСНОСТЬ',
        'safety_subtitle': 'Пожалуйста, ознакомьтесь с рекомендациями',
        'safety_60plus': '🔴 ВАЖНО ДЛЯ ВОЗРАСТА 60+',
        'safety_60_1': '⚠️ Обязательно проконсультируйтесь с врачом перед началом',
        'safety_60_2': '🫀 Получите разрешение кардиолога при болезнях сердца',
        'safety_60_3': '🚫 Избегайте резких движений и высокой интенсивности',
        'safety_50plus': '🟡 РЕКОМЕНДАЦИИ ДЛЯ 50+',
        'safety_50_1': '👨‍⚕️ Рекомендуется консультация врача',
        'safety_50_2': '🔥 Особое внимание уделяйте разминке (10-15 мин)',
        'safety_50_3': '💪 Контролируйте пульс во время тренировки',
        'safety_teen': '🟢 ДЛЯ ПОДРОСТКОВ (14-17 лет)',
        'safety_teen_1': '📚 Тренировки адаптированы для растущего организма',
        'safety_teen_2': '🚫 Избегайте чрезмерных нагрузок на позвоночник',
        'safety_teen_3': '👨‍👩‍👦 Согласуйте программу с родителями',
        'safety_general': '✅ ОБЩИЕ РЕКОМЕНДАЦИИ',
        'safety_gen_1': '👨‍⚕️ При хронических заболеваниях консультируйтесь с врачом',
        'safety_gen_2': '🛑 Немедленно остановитесь при боли или дискомфорте',
        'safety_gen_3': '🔥 Всегда начинайте с разминки 5-10 минут',
        'safety_agree': '✅ Я ознакомился с рекомендациями и готов начать',
        # Питание
        'nutrition_title': '🍽️ ПЛАН ПИТАНИЯ',
        'nutrition_subtitle': 'Рекомендуемые калории для вашей цели',
        'kcal_day': 'ККАЛ/ДЕНЬ',
        'protein': 'БЕЛКИ',
        'fats': 'ЖИРЫ',
        'carbs': 'УГЛЕВОДЫ',
        'g': 'г',
        'nutrition_tips': '💡 Рекомендации по питанию:',
        'tip1': '• Пейте 2-3 литра воды в день',
        'tip2': '• Ешьте 4-5 раз небольшими порциями',
        'tip3': '• Белок в каждом приёме пищи',
        'tip4': '• Сложные углеводы до 16:00',
        'tip5': '• Избегайте сахара и фастфуда',
        'to_program': 'К ПРОГРАММЕ →',
        # Результат
        'program_ready': '📋 ВАША ПРОГРАММА ГОТОВА',
        'program_subtitle': 'Персональный план тренировок создан',
        'week': 'Неделя',
        'day': 'День',
        'exercises': 'упр.',
        'sets': 'подх.',
        'reps': 'повт.',
        'start_btn': '▶️ НАЧАТЬ',
        'completed': '✅ Выполнено',
        'locked': '🔒 Заблокировано',
        'save_program': '💾 Сохранить',
        'my_progress': '📈 Прогресс',
        'diary': '📊 Дневник',
        'new_program': '🔄 Новая',
        'training_program_title': '📋 ПРОГРАММА ТРЕНИРОВОК',
        # Тренировка
        'workout_title': '▶️ ТРЕНИРОВКА',
        'exercise': 'Упражнение',
        'set': 'Подход',
        'of': 'из',
        'seconds': 'сек',
        'hold': 'Удержание',
        'rest': 'Отдых',
        'complete_set': '✅ ПОДХОД ВЫПОЛНЕН',
        'skip_exercise': '⏭️ Пропустить',
        'simplify': '😓 Упростить',
        'finish_workout': '❌ Завершить',
        'rest_between': 'Отдых между подходами',
        'sec': 'сек',
        'start_timer': 'СТАРТ',
        'add_10_sec': '+10 сек',
        'skip_rest': 'Пропустить',
        'skip': 'Пропустить',
        'done': 'Готово',
        'rest_time': 'Время отдыха',
        'press_start': 'Нажмите СТАРТ',
        # Типы упражнений
        'compound': '🔸 Базовое',
        'isolation': '🔹 Изоляция',
        'core': '🎯 Пресс',
        'cardio': '🏃 Кардио',
        'type_compound': 'Базовое',
        'type_isolation': 'Изоляция',
        'type_core': 'Пресс',
        'type_cardio': 'Кардио',
        'diff_beginner': 'Начальный',
        'diff_intermediate': 'Средний',
        'diff_advanced': 'Продвинутый',
        # Прогресс
        'progress_title': '📊 МОЙ ПРОГРЕСС',
        'weight_title': '⚖️ ОТСЛЕЖИВАНИЕ ВЕСА',
        'measurements': '📏 ЗАМЕРЫ ТЕЛА (см)',
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
        'great_progress': '🎉 Отличный прогресс! Так держать!',
        'diary_total_time': 'Общее время',
        'diary_completion': 'Выполнено',
        'diary_missed': 'Пропущено',
        'diary_upcoming': 'Впереди',
        'diary_streak': 'Серия подряд',
        'diary_avg_time': 'Среднее время',
        'diary_progress_title': '📅 ПРОГРЕСС ПО ДНЯМ',
        'diary_status_done': '✅ Выполнено',
        'diary_status_rest_done': '😴 Отдых',
        'diary_status_missed': '❌ Пропущено',
        'diary_status_upcoming': '⏳ Впереди',
        'diary_history_title': '📋 ИСТОРИЯ ТРЕНИРОВОК',
        'diary_skipped_ex': 'Пропущено упр.',
        'diary_no_skipped': 'Все выполнены',
        'diary_exercises_list': 'Упражнения',
        'diary_min': 'мин',
        'diary_workouts_word': 'тренировок',
        'diary_days_word': 'дней',
        # Результаты тренировки
        'workout_complete': '🎉 ОТЛИЧНО!',
        'workout_finished': 'Тренировка завершена!',
        'great_job': 'Отличная работа!',
        # Настройки
        'settings': '⚙️ Настройки',
        'settings_language': '🌐 Язык интерфейса',
        'settings_theme': '🎨 Тема оформления',
        'theme_dark': 'Тёмная',
        'theme_light': 'Светлая',
        'settings_back': '← Вернуться',
        'settings_exit': '🚪 Выйти из приложения',
        # Рекомендации
        'rec_title': '💡 Персональные рекомендации',
        'rec_cardio_weight_loss': 'Добавьте 20-30 минут кардио после каждой тренировки',
        'rec_cardio_muscle': 'Ограничьте кардио 10-15 минутами для сохранения массы',
        'rec_nutrition_weight_loss': 'Дефицит калорий -500 ккал/день для плавного похудения',
        'rec_nutrition_muscle': 'Профицит +300 ккал/день для набора качественной массы',
        'rec_rest_days': 'Отдых {count} дней в неделю для восстановления мышц',
        'rec_duration_beginner': 'Оптимальная продолжительность тренировки 30-45 минут',
        'rec_duration_intermediate': 'Оптимальная продолжительность тренировки 45-60 минут',
        'rec_duration_advanced': 'Оптимальная продолжительность тренировки 60-90 минут',
        'rec_progression': 'Увеличивайте нагрузку на 5-10% каждые 2 недели',
        'rec_measurements': 'Делайте замеры тела каждые 2 недели',
        'rec_warmup': 'Всегда начинайте с разминки 5-10 минут',
        # BMI
        'bmi': 'ИМТ',
        'goal_weight_loss': 'Сброс веса',
        'goal_muscle_gain': 'Набор массы',
        'weeks': 'недель',
        'days': 'дней/неделю',
            # Переводы упражнений (русский)
            'Приседания': 'Приседания',
            'Отжимания': 'Отжимания',
            'Выпады': 'Выпады',
            'Планка': 'Планка',
            'Скалолаз': 'Скалолаз',
            'Берпи': 'Берпи',
            'Прыжки с хлопками': 'Прыжки с хлопками',
            'Ягодичный мостик': 'Ягодичный мостик',
            'Боковая планка': 'Боковая планка',
            'Велосипед': 'Велосипед',
            'Русские скручивания': 'Русские скручивания',
            'Скручивания на полу': 'Скручивания на полу',
            'Подъёмы ног': 'Подъёмы ног',
            'Мёртвый жук': 'Мёртвый жук',
            'Берпи с отжиманиями': 'Берпи с отжиманиями',
            'Динамическая боковая планка': 'Динамическая боковая планка',
            'Выпады вперёд-назад': 'Выпады вперёд-назад',
            'Скручивания локтем к колену': 'Скручивания локтем к колену',
            'Подъём таза на одной ноге': 'Подъём таза на одной ноге',
            'Подъём ног лёжа вверх': 'Подъём ног лёжа вверх',
            'Супермен': 'Супермен',
            'Берпи (женский вариант)': 'Берпи (женский вариант)',
            'Планка на локтях': 'Планка на локтях',
            'Планка на одной руке': 'Планка на одной руке',
            'Планка на прямых руках': 'Планка на прямых руках',
            'Планка с переходом в собаку мордой вниз': 'Планка с переходом в собаку мордой вниз',
            'Обратные отжимания на трицепс': 'Обратные отжимания на трицепс',
            'Обратные снежные ангелы': 'Обратные снежные ангелы',
            'Обратная планка': 'Обратная планка',
            'Псевдо-планш отжимания': 'Псевдо-планш отжимания',
            'Отжимания с возвышения': 'Отжимания с возвышения',
            'Отжимания с колен': 'Отжимания с колен',
            'Отжимания с ногами на возвышении': 'Отжимания с ногами на возвышении',
            'Отжимания уголком': 'Отжимания уголком',
            'Узкие отжимания': 'Узкие отжимания',
            'Широкие отжимания': 'Широкие отжимания',
            'Подтягивания': 'Подтягивания',
            'Подтягивания колен': 'Подтягивания колен',
            'Жим гантелей': 'Жим гантелей',
            'Королевская становая тяга': 'Королевская становая тяга',
            'Становая тяга на одной ноге': 'Становая тяга на одной ноге',
            'Болгарские сплит-приседания': 'Болгарские сплит-приседания',
            'Глубокие приседания с наклоном': 'Глубокие приседания с наклоном',
            'Приседания плие': 'Приседания плие',
            'Приседания с прыжком': 'Приседания с прыжком',
            'Приседания у стены': 'Приседания у стены',
            'Выпады с ходьбой': 'Выпады с ходьбой',
            'Выпады вперёд': 'Выпады вперёд',
            'Выпады назад': 'Выпады назад',
            'Статические выпады': 'Статические выпады',
            'Боковые наклоны': 'Боковые наклоны',
            'Конькобежец': 'Конькобежец',
            'Мёртвый жук': 'Мёртвый жук',
            'Ножницы': 'Ножницы',
            'Обратные отжимания': 'Обратные отжимания',
            'Подъём таза на скамье': 'Подъём таза на скамье',
            'Подъёмы на носки': 'Подъёмы на носки',
            'Подъёмы ног лёжа': 'Подъёмы ног лёжа',
            'Поза ребёнка': 'Поза ребёнка',
            'Русские скручивания сидя': 'Русские скручивания сидя',
            'Скручивания локтем к колену': 'Скручивания локтем к колену',
            'Скручивания на полу': 'Скручивания на полу',
            'Супермен (удержание)': 'Супермен (удержание)',
            'Ходьба на месте': 'Ходьба на месте',
            'Бег на месте': 'Бег на месте',
            'Бег с высоким подниманием коленей': 'Бег с высоким подниманием коленей',
            'Прыжки с хлопками над головой': 'Прыжки с хлопками над головой',
            'Обратные снежные ангелы': 'Обратные снежные ангелы',
            'Подъём ног лёжа': 'Подъём ног лёжа',
            'Подъём таза на одной ноге': 'Подъём таза на одной ноге',
            'Подъём таза на скамье': 'Подъём таза на скамье',
            'Подъёмы на носки': 'Подъёмы на носки',
            'Планка на локтях': 'Планка на локтях',
            'Планка на одной руке гифка': 'Планка на одной руке гифка',
            'Планка на прямых руках': 'Планка на прямых руках',
            'Планка с переходом в собаку мордой вниз': 'Планка с переходом в собаку мордой вниз',
            'Планка': 'Планка',
        # Переводы упражнений
        'Приседания': 'Приседания',
        'Отжимания': 'Отжимания',
        'Выпады': 'Выпады',
        'Планка': 'Планка',
        'Скалолаз': 'Скалолаз',
        'Берпи': 'Берпи',
        'Прыжки с хлопками': 'Прыжки с хлопками',
        'Ягодичный мостик': 'Ягодичный мостик',
        'Боковая планка': 'Боковая планка',
        'Велосипед': 'Велосипед',
        'Русские скручивания': 'Русские скручивания',
        'Скручивания на полу': 'Скручивания на полу',
        'Подъёмы ног': 'Подъёмы ног',
        'Мёртвый жук': 'Мёртвый жук',
        # Новые ключи
        'no_records': 'Нет записей',
        'finish': 'Завершить',
        'time_label': 'Время',
        'sets_done_label': 'Подходов',
        'exercises_done_label': 'Упражнений',
        'skipped_label': 'Пропущено',
        'min_short': 'мин',
        'sets_short': 'подх.',
        'safety_confirm_error': '⚠️ Подтвердите согласие!',
        'program_saved': '✅ Программа сохранена!',
        # Опрос сложности
        'how_was_workout': '🎯 Как прошла тренировка?',
        'workout_too_easy': '😎 Слишком легко',
        'workout_just_right': '👍 В самый раз',
        'workout_too_hard': '😰 Слишком тяжело',
        'difficulty_adjusted_up': '💪 Нагрузка увеличена! +1 подход/+2 повтора',
        'difficulty_kept': '✅ Отлично! Программа остаётся прежней',
        'difficulty_adjusted_down': '🙏 Нагрузка уменьшена! -1 подход/-2 повтора',
        'monday': 'Понедельник',
        'tuesday': 'Вторник',
        'wednesday': 'Среда',
        'thursday': 'Четверг',
        'friday': 'Пятница',
        'saturday': 'Суббота',
        'sunday': 'Воскресенье',
        'rest_day': '😴 Отдых / Восстановление',
        'rest_btn': '😴 Отдыхать',
        'rest_today_msg': 'Сегодня я отдыхаю! 💤',
        'day_num': 'День',
        'ease_title': '⚙️ Облегчить программу?',
        'ease_desc': 'Безопасное снижение нагрузки:\n• -1 подход на упражнение\n• -2 повторения\n• +15 секунд отдыха',
        'ease_preview': '📋 Пример изменений:',
        'ease_sets': 'Подходы',
        'ease_reps': 'Повтор',
        'ease_rest': 'Отдых',
        'ease_yes': '✅ Да, облегчить',
        'ease_no': '❌ Нет, оставить',
        'ease_no_exercises': 'Нет упражнений для изменения.',
    },
    'en': {
        'app_title': '💪 TrainerWizard',
        'welcome': 'Welcome!',
        'welcome_subtitle': "Let's create the perfect workout program for you",
        'motivation_text': '✨ Start your journey to your best shape',
        'male': 'Male',
        'female': 'Female',
        'select': 'SELECT',
        'male_desc': '💪 Strength Training\n📈 Muscle Building',
        'female_desc': '🎯 Toning & Fitness\n🧘 Flexibility',
        'continue_btn': 'CONTINUE →',
        'back_btn': '← BACK',
        'enter_data': '📋 ENTER YOUR DATA',
        'height': 'Height',
        'weight': 'Weight',
        'age': 'Age',
        'cm': 'cm',
        'kg': 'kg',
        'years': 'years',
        'days_per_week': 'Days per week',
        'weeks_program': 'Program weeks',
        'level': 'Fitness level',
        'beginner': '🌱 Beginner',
        'intermediate': '💪 Intermediate',
        'advanced': '🔥 Advanced',
        'error_height': '⚠️ Enter valid height!',
        'error_weight': '⚠️ Enter valid weight!',
        'error_age': '⚠️ Enter valid age!',
        'error_height_range': '⚠️ Height must be 120-250 cm!',
        'error_weight_range': '⚠️ Weight must be 40-200 kg!',
        'error_age_range': '⚠️ Age must be 14-80 years!',
        'choose_goal': '🎯 CHOOSE YOUR GOAL',
        'goal_subtitle': 'What do you want to achieve?',
        'weight_loss': 'Weight Loss',
        'weight_loss_desc': '🔥 HIIT Workouts\n📉 Burn Calories',
        'muscle_gain': 'Build Muscle',
        'muscle_gain_desc': '💪 Strength Exercises\n📈 Muscle Growth',
        'choose_zone': '🎯 CHOOSE TRAINING ZONE',
        'focus_question': 'WHICH BODY PART DO YOU WANT\nTO FOCUS ON?',
        'all_muscles': 'ALL MUSCLE GROUPS',
        'chest_zone': 'CHEST',
        'arms_zone': 'ARMS',
        'core_zone': 'CORE',
        'legs_zone': 'LEGS',
        'Full Body': 'Full Body',
        'Legs': 'Legs',
        'Chest': 'Chest',
        'Back': 'Back',
        'Arms': 'Arms',
        'Shoulders': 'Shoulders',
        'Core': 'Core',
        'Weight Loss': 'Weight Loss',
        'safety_title': '⚠️ SAFETY FIRST',
        'safety_subtitle': 'Please read the recommendations',
        'safety_60plus': '🔴 IMPORTANT FOR AGE 60+',
        'safety_60_1': '⚠️ Consult your doctor before starting',
        'safety_60_2': '🫀 Get cardiologist approval for heart conditions',
        'safety_60_3': '🚫 Avoid sudden movements and high intensity',
        'safety_50plus': '🟡 RECOMMENDATIONS FOR 50+',
        'safety_50_1': '👨‍⚕️ Doctor consultation recommended',
        'safety_50_2': '🔥 Pay special attention to warm-up (10-15 min)',
        'safety_50_3': '💪 Monitor your heart rate during workout',
        'safety_teen': '🟢 FOR TEENAGERS (14-17)',
        'safety_teen_1': '📚 Workouts adapted for growing body',
        'safety_teen_2': '🚫 Avoid excessive spine stress',
        'safety_teen_3': '👨‍👩‍👦 Coordinate program with parents',
        'safety_general': '✅ GENERAL RECOMMENDATIONS',
        'safety_gen_1': '👨‍⚕️ Consult doctor for chronic conditions',
        'safety_gen_2': '🛑 Stop immediately if you feel pain',
        'safety_gen_3': '🔥 Always start with 5-10 min warm-up',
        'safety_agree': "✅ I've read the recommendations and ready to start",
        'nutrition_title': '🍽️ NUTRITION PLAN',
        'nutrition_subtitle': 'Recommended calories for your goal',
        'kcal_day': 'KCAL/DAY',
        'protein': 'PROTEIN',
        'fats': 'FATS',
        'carbs': 'CARBS',
        'g': 'g',
        'nutrition_tips': '💡 Nutrition tips:',
        'tip1': '• Drink 2-3 liters of water daily',
        'tip2': '• Eat 4-5 small meals',
        'tip3': '• Protein with every meal',
        'tip4': '• Complex carbs before 4 PM',
        'tip5': '• Avoid sugar and fast food',
        'to_program': 'TO PROGRAM →',
        'program_ready': '📋 YOUR PROGRAM IS READY',
        'program_subtitle': 'Personal training plan created',
        'week': 'Week',
        'day': 'Day',
        'exercises': 'ex.',
        'sets': 'sets',
        'reps': 'reps',
        'start_btn': '▶️ START',
        'completed': '✅ Completed',
        'locked': '🔒 Locked',
        'save_program': 'Save',
        'my_progress': 'Progress',
        'diary': 'Diary',
        'new_program': 'New',
        'training_program_title': '📋 TRAINING PROGRAM',
        'workout_title': '▶️ WORKOUT',
        'exercise': 'Exercise',
        'set': 'Set',
        'of': 'of',
        'seconds': 'sec',
        'hold': 'Hold',
        'rest': 'Rest',
        'complete_set': '✅ SET COMPLETE',
        'skip_exercise': '⏭️ Skip',
        'simplify': '😓 Simplify',
        'finish_workout': '❌ Finish',
        'rest_between': 'Rest between sets',
        'sec': 'sec',
        'start_timer': 'START',
        'add_10_sec': '+10 sec',
        'skip': 'Skip',
        'done': 'Done',
        'rest_time': 'Rest Time',
        'press_start': 'Press START',
        'skip_rest': 'Skip',
        'compound': '🔸 Compound',
        'isolation': '🔹 Isolation',
        'core': '🎯 Core',
        'cardio': '🏃 Cardio',
        'type_compound': 'Compound',
        'type_isolation': 'Isolation',
        'type_core': 'Core',
        'type_cardio': 'Cardio',
        'diff_beginner': 'Beginner',
        'diff_intermediate': 'Intermediate',
        'diff_advanced': 'Advanced',
        'progress_title': '📊 MY PROGRESS',
        'weight_title': '⚖️ WEIGHT TRACKING',
        'measurements': '📏 BODY MEASUREMENTS (cm)',
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
        'diary_title': '📊 WORKOUT DIARY',
        'total_workouts': 'Total workouts',
        'great_progress': '🎉 Great progress! Keep it up!',
        'diary_total_time': 'Total time',
        'diary_completion': 'Completed',
        'diary_missed': 'Missed',
        'diary_upcoming': 'Upcoming',
        'diary_streak': 'Streak',
        'diary_avg_time': 'Avg time',
        'diary_progress_title': '📅 DAILY PROGRESS',
        'diary_status_done': '✅ Done',
        'diary_status_rest_done': '😴 Rest',
        'diary_status_missed': '❌ Missed',
        'diary_status_upcoming': '⏳ Upcoming',
        'diary_history_title': '📋 WORKOUT HISTORY',
        'diary_skipped_ex': 'Skipped ex.',
        'diary_no_skipped': 'All completed',
        'diary_exercises_list': 'Exercises',
        'diary_min': 'min',
        'diary_workouts_word': 'workouts',
        'diary_days_word': 'days',
        'workout_complete': '🎉 GREAT!',
        'workout_finished': 'Workout finished!',
        'great_job': 'Great job!',
        'settings': '⚙️ Settings',
        'settings_language': '🌐 Interface Language',
        'settings_theme': '🎨 Theme',
        'theme_dark': 'Dark',
        'theme_light': 'Light',
        'settings_back': '← Back',
        'settings_exit': '🚪 Exit App',
        'rec_title': '💡 Personal Recommendations',
        'rec_cardio_weight_loss': 'Add 20-30 minutes of cardio after each workout',
        'rec_cardio_muscle': 'Limit cardio to 10-15 minutes to preserve mass',
        'rec_nutrition_weight_loss': 'Calorie deficit of -500 kcal/day for gradual weight loss',
        'rec_nutrition_muscle': 'Surplus of +300 kcal/day for quality mass gain',
        'rec_rest_days': 'Rest {count} days per week for muscle recovery',
        'rec_duration_beginner': 'Optimal workout duration 30-45 minutes',
        'rec_duration_intermediate': 'Optimal workout duration 45-60 minutes',
        'rec_duration_advanced': 'Optimal workout duration 60-90 minutes',
        'rec_progression': 'Increase load by 5-10% every 2 weeks',
        'rec_measurements': 'Take body measurements every 2 weeks',
        'rec_warmup': 'Always start with 5-10 min warm-up',
        'bmi': 'BMI',
        'goal_weight_loss': 'Weight Loss',
        'goal_muscle_gain': 'Muscle Gain',
        'weeks': 'weeks',
        'days': 'days/week',
            # Exercise translations (en)
            'Приседания': 'Squat',
            'Отжимания': 'Push-up',
            'Выпады': 'Lunge',
            'Планка': 'Plank',
            'Скалолаз': 'Mountain climber',
            'Берпи': 'Burpee',
            'Прыжки с хлопками': 'Jumping jacks',
            'Ягодичный мостик': 'Glute bridge',
            'Боковая планка': 'Side plank',
            'Велосипед': 'Bicycle crunch',
            'Русские скручивания': 'Russian twist',
            'Скручивания на полу': 'Floor crunch',
            'Подъёмы ног': 'Leg raises',
            'Мёртвый жук': 'Dead bug',
            'Берпи с отжиманиями': 'Burpee with push-up',
            'Динамическая боковая планка': 'Dynamic side plank',
            'Выпады вперёд-назад': 'Forward-backward lunge',
            'Скручивания локтем к колену': 'Elbow-to-knee crunch',
            'Подъём таза на одной ноге': 'Single-leg hip raise',
            'Подъём ног лёжа вверх': 'Lying leg raise',
            'Супермен': 'Superman',
            'Берпи (женский вариант)': 'Burpee (female)',
            'Планка на локтях': 'Elbow plank',
            'Планка на одной руке': 'One-arm plank',
            'Планка на прямых руках': 'Straight-arm plank',
            'Планка с переходом в собаку мордой вниз': 'Plank to downward dog',
            'Обратные отжимания на трицепс': 'Triceps dips',
            'Обратные снежные ангелы': 'Reverse snow angels',
            'Обратная планка': 'Reverse plank',
            'Псевдо-планш отжимания': 'Pseudo planche push-up',
            'Отжимания с возвышения': 'Decline push-up',
            'Отжимания с колен': 'Knee push-up',
            'Отжимания с ногами на возвышении': 'Feet-elevated push-up',
            'Отжимания уголком': 'Pike push-up',
            'Узкие отжимания': 'Close-grip push-up',
            'Широкие отжимания': 'Wide push-up',
            'Подтягивания': 'Pull-up',
            'Подтягивания колен': 'Knee raises',
            'Жим гантелей': 'Dumbbell press',
            'Королевская становая тяга': 'King deadlift',
            'Становая тяга на одной ноге': 'Single-leg deadlift',
            'Болгарские сплит-приседания': 'Bulgarian split squat',
            'Глубокие приседания с наклоном': 'Deep squat with lean',
            'Приседания плие': 'Plie squat',
            'Приседания с прыжком': 'Jump squat',
            'Приседания у стены': 'Wall sit',
            'Выпады с ходьбой': 'Walking lunge',
            'Выпады вперёд': 'Forward lunge',
            'Выпады назад': 'Backward lunge',
            'Статические выпады': 'Static lunge',
            'Боковые наклоны': 'Side bends',
            'Конькобежец': 'Skater',
            'Мёртвый жук': 'Dead bug',
            'Ножницы': 'Scissors',
            'Обратные отжимания': 'Reverse push-up',
            'Подъём таза на скамье': 'Bench hip raise',
            'Подъёмы на носки': 'Calf raises',
            'Подъёмы ног лёжа': 'Lying leg raises',
            'Поза ребёнка': 'Child pose',
            'Русские скручивания сидя': 'Seated Russian twist',
            'Скручивания локтем к колену': 'Elbow-to-knee crunch',
            'Скручивания на полу': 'Floor crunch',
            'Супермен (удержание)': 'Superman (hold)',
            'Ходьба на месте': 'Marching in place',
            'Бег на месте': 'Running in place',
            'Бег с высоким подниманием коленей': 'High knees',
            'Прыжки с хлопками над головой': 'Overhead jumping jacks',
            'Обратные снежные ангелы': 'Reverse snow angels',
            'Подъём ног лёжа': 'Lying leg raise',
            'Подъём таза на одной ноге': 'Single-leg hip raise',
            'Подъём таза на скамье': 'Bench hip raise',
            'Подъёмы на носки': 'Calf raises',
            'Планка на локтях': 'Elbow plank',
            'Планка на одной руке гифка': 'One-arm plank gif',
            'Планка на прямых руках': 'Straight-arm plank',
            'Планка с переходом в собаку мордой вниз': 'Plank to downward dog',
            'Планка': 'Plank',
        # Exercise translations
        'Приседания': 'Squat',
        'Отжимания': 'Push-up',
        'Выпады': 'Lunge',
        'Планка': 'Plank',
        'Скалолаз': 'Mountain climber',
        'Берпи': 'Burpee',
        'Прыжки с хлопками': 'Jumping jacks',
        'Ягодичный мостик': 'Glute bridge',
        'Боковая планка': 'Side plank',
        'Велосипед': 'Bicycle crunch',
        'Русские скручивания': 'Russian twist',
        'Скручивания на полу': 'Floor crunch',
        'Подъёмы ног': 'Leg raises',
        'Мёртвый жук': 'Dead bug',
        # New keys
        'no_records': 'No records',
        'finish': 'Finish',
        'time_label': 'Time',
        'sets_done_label': 'Sets',
        'exercises_done_label': 'Exercises',
        'skipped_label': 'Skipped',
        'min_short': 'min',
        'sets_short': 'sets',
        'safety_confirm_error': '⚠️ Please confirm your agreement!',
        'program_saved': '✅ Program saved!',
        # Difficulty survey
        'how_was_workout': '🎯 How was the workout?',
        'workout_too_easy': '😎 Too easy',
        'workout_just_right': '👍 Just right',
        'workout_too_hard': '😰 Too hard',
        'difficulty_adjusted_up': '💪 Intensity increased! +1 set/+2 reps',
        'difficulty_kept': '✅ Great! Program stays the same',
        'difficulty_adjusted_down': '🙏 Intensity reduced! -1 set/-2 reps',
        'monday': 'Monday',
        'tuesday': 'Tuesday',
        'wednesday': 'Wednesday',
        'thursday': 'Thursday',
        'friday': 'Friday',
        'saturday': 'Saturday',
        'sunday': 'Sunday',
        'rest_day': '😴 Rest / Recovery',
        'rest_btn': '😴 Rest',
        'rest_today_msg': 'Today I\'m resting! 💤',
        'day_num': 'Day',
        'ease_title': '⚙️ Ease the program?',
        'ease_desc': 'Safe load reduction:\n• -1 set per exercise\n• -2 reps\n• +15 seconds rest',
        'ease_preview': '📋 Example changes:',
        'ease_sets': 'Sets',
        'ease_reps': 'Reps',
        'ease_rest': 'Rest',
        'ease_yes': '✅ Yes, ease it',
        'ease_no': '❌ No, keep it',
        'ease_no_exercises': 'No exercises to change.',
    },
    'es': {
        'app_title': '💪 TrainerWizard',
        'welcome': '¡Bienvenido!',
        'welcome_subtitle': 'Creemos el programa de entrenamiento perfecto para ti',
        'motivation_text': '✨ Comienza tu camino hacia tu mejor forma',
        'male': 'Masculino',
        'female': 'Femenino',
        'select': 'SELECCIONAR',
        'male_desc': '💪 Entrenamiento de fuerza\n📈 Ganar masa',
        'female_desc': '🎯 Tonificación y forma\n🧘 Flexibilidad',
        'continue_btn': 'CONTINUAR →',
        'back_btn': '← ATRÁS',
        'enter_data': '📋 INGRESA TUS DATOS',
        'height': 'Altura',
        'weight': 'Peso',
        'age': 'Edad',
        'cm': 'cm',
        'kg': 'kg',
        'years': 'años',
        'days_per_week': 'Días por semana',
        'weeks_program': 'Semanas del programa',
        'level': 'Nivel de condición',
        'beginner': '🌱 Principiante',
        'intermediate': '💪 Intermedio',
        'advanced': '🔥 Avanzado',
        'error_height': '⚠️ ¡Ingresa altura válida!',
        'error_weight': '⚠️ ¡Ingresa peso válido!',
        'error_age': '⚠️ ¡Ingresa edad válida!',
        'error_height_range': '⚠️ ¡Altura debe ser 120-250 cm!',
        'error_weight_range': '⚠️ ¡Peso debe ser 40-200 kg!',
        'error_age_range': '⚠️ ¡Edad debe ser 14-80 años!',
        'choose_goal': '🎯 ELIGE TU OBJETIVO',
        'goal_subtitle': '¿Qué quieres lograr?',
        'weight_loss': 'Pérdida de peso',
        'weight_loss_desc': '🔥 HIIT\n📉 Quemar calorías',
        'muscle_gain': 'Ganar músculo',
        'muscle_gain_desc': '💪 Ejercicios de fuerza\n📈 Crecimiento muscular',
        'choose_zone': '🎯 ELIGE ZONA DE ENTRENAMIENTO',
        'focus_question': '¿EN QUÉ PARTE DEL CUERPO\nQUIERES ENFOCARTE?',
        'all_muscles': 'TODOS LOS MÚSCULOS',
        'chest_zone': 'PECHO',
        'arms_zone': 'BRAZOS',
        'core_zone': 'ABDOMEN',
        'legs_zone': 'PIERNAS',
        'Full Body': 'Cuerpo completo',
        'Legs': 'Piernas',
        'Chest': 'Pecho',
        'Back': 'Espalda',
        'Arms': 'Brazos',
        'Shoulders': 'Hombros',
        'Core': 'Abdomen',
        'Weight Loss': 'Pérdida de peso',
        'safety_title': '⚠️ SEGURIDAD PRIMERO',
        'safety_subtitle': 'Por favor lee las recomendaciones',
        'safety_agree': '✅ He leído las recomendaciones y estoy listo para empezar',
        'nutrition_title': '🍽️ PLAN DE NUTRICIÓN',
        'nutrition_subtitle': 'Calorías recomendadas para tu objetivo',
        'kcal_day': 'KCAL/DÍA',
        'protein': 'PROTEÍNA',
        'fats': 'GRASAS',
        'carbs': 'CARBOHIDRATOS',
        'g': 'g',
        'nutrition_tips': '💡 Consejos de nutrición:',
        'tip1': '• Bebe 2-3 litros de agua al día',
        'tip2': '• Come 4-5 comidas pequeñas',
        'tip3': '• Proteína en cada comida',
        'tip4': '• Carbohidratos complejos antes de las 16:00',
        'tip5': '• Evita azúcar y comida rápida',
        'to_program': 'AL PROGRAMA →',
        'program_ready': '📋 TU PROGRAMA ESTÁ LISTO',
        'program_subtitle': 'Plan de entrenamiento personal creado',
        'week': 'Semana',
        'day': 'Día',
        'exercises': 'ej.',
        'sets': 'series',
        'reps': 'reps',
        'start_btn': '▶️ INICIAR',
        'completed': '✅ Completado',
        'locked': '🔒 Bloqueado',
        'save_program': 'Guardar',
        'my_progress': 'Progreso',
        'diary': 'Diario',
        'new_program': 'Nuevo',
        'training_program_title': '📋 PROGRAMA DE ENTRENAMIENTO',
        'workout_title': '▶️ ENTRENAMIENTO',
        'exercise': 'Ejercicio',
        'set': 'Serie',
        'of': 'de',
        'seconds': 'seg',
        'hold': 'Mantener',
        'rest': 'Descanso',
        'complete_set': '✅ SERIE COMPLETA',
        'skip_exercise': '⏭️ Saltar',
        'simplify': '😓 Simplificar',
        'finish_workout': '❌ Terminar',
        'rest_between': 'Descanso entre series',
        'sec': 'seg',
        'start_timer': 'INICIO',
        'add_10_sec': '+10 seg',
        'skip': 'Saltar',
        'done': 'Listo',
        'rest_time': 'Tiempo de descanso',
        'press_start': 'Presiona INICIO',
        'skip_rest': 'Saltar',
        'workout_complete': '🎉 ¡EXCELENTE!',
        'workout_finished': '¡Entrenamiento terminado!',
        'great_job': '¡Buen trabajo!',
        'settings': '⚙️ Configuración',
        'settings_language': '🌐 Idioma',
        'settings_theme': '🎨 Tema',
        'theme_dark': 'Oscuro',
        'theme_light': 'Claro',
        'settings_back': '← Volver',
        'settings_exit': '🚪 Salir de la app',
        'rec_title': '💡 Recomendaciones personales',
        'rec_cardio_weight_loss': 'Añade 20-30 minutos de cardio después de cada entrenamiento',
        'rec_cardio_muscle': 'Limita el cardio a 10-15 minutos para conservar masa',
        'rec_nutrition_weight_loss': 'Déficit de -500 kcal/día para pérdida gradual',
        'rec_nutrition_muscle': 'Superávit de +300 kcal/día para ganar masa',
        'rec_rest_days': 'Descansa {count} días a la semana para recuperación muscular',
        'rec_duration_beginner': 'Duración óptima del entrenamiento 30-45 minutos',
        'rec_duration_intermediate': 'Duración óptima del entrenamiento 45-60 minutos',
        'rec_duration_advanced': 'Duración óptima del entrenamiento 60-90 minutos',
        'rec_warmup': 'Siempre empieza con calentamiento de 5-10 minutos',
        'bmi': 'IMC',
        'goal_weight_loss': 'Pérdida de peso',
        'goal_muscle_gain': 'Ganar músculo',
        'weeks': 'semanas',
        'days': 'días/semana',
        # Безопасность
        'safety_60plus': '🔴 IMPORTANTE PARA MAYORES DE 60',
        'safety_60_1': '⚠️ Consulte a su médico antes de comenzar',
        'safety_60_2': '🫀 Obtenga aprobación del cardiólogo para enfermedades cardíacas',
        'safety_60_3': '🚫 Evite movimientos bruscos y alta intensidad',
        'safety_50plus': '🟡 RECOMENDACIONES PARA 50+',
        'safety_50_1': '👨‍⚕️ Se recomienda consulta médica',
        'safety_50_2': '🔥 Preste especial atención al calentamiento (10-15 min)',
        'safety_50_3': '💪 Controle su pulso durante el entrenamiento',
        'safety_teen': '🟢 PARA ADOLESCENTES (14-17)',
        'safety_teen_1': '📚 Entrenamientos adaptados para cuerpo en crecimiento',
        'safety_teen_2': '🚫 Evite estrés excesivo en la columna',
        'safety_teen_3': '👨‍👩‍👦 Coordine el programa con los padres',
        'safety_general': '✅ RECOMENDACIONES GENERALES',
        'safety_gen_1': '👨‍⚕️ Consulte médico para condiciones crónicas',
        'safety_gen_2': '🛑 Deténgase inmediatamente si siente dolor',
        'safety_gen_3': '🔥 Siempre comience con 5-10 min de calentamiento',
        # Tipos y dificultad
        'compound': '🔸 Compuesto',
        'isolation': '🔹 Aislamiento',
        'core': '🎯 Abdomen',
        'cardio': '🏃 Cardio',
        'type_compound': 'Compuesto',
        'type_isolation': 'Aislamiento',
        'type_core': 'Abdomen',
        'type_cardio': 'Cardio',
        'diff_beginner': 'Principiante',
        'diff_intermediate': 'Intermedio',
        'diff_advanced': 'Avanzado',
        # Progreso
        'progress_title': '📊 MI PROGRESO',
        'weight_title': '⚖️ SEGUIMIENTO DE PESO',
        'measurements': '📏 MEDIDAS CORPORALES (cm)',
        'chest_label': '💪 Pecho:',
        'waist_label': '👖 Cintura:',
        'hips_label': '🍑 Caderas:',
        'arms_label': '💪 Brazos:',
        'add_btn': '➕ Añadir',
        'save_btn': '💾 Guardar',
        'photos_title': '📷 FOTOS DE PROGRESO',
        'no_photos': 'Sin fotos',
        'add_photo': '📸 Añadir foto',
        'back_to_program': '← AL PROGRAMA',
        'diary_title': '📊 DIARIO DE ENTRENAMIENTOS',
        'total_workouts': 'Total entrenamientos',
        'great_progress': '🎉 ¡Gran progreso! ¡Sigue así!',
        'diary_total_time': 'Tiempo total',
        'diary_completion': 'Completado',
        'diary_missed': 'Perdido',
        'diary_upcoming': 'Próximo',
        'diary_streak': 'Racha',
        'diary_avg_time': 'Tiempo promedio',
        'diary_progress_title': '📅 PROGRESO DIARIO',
        'diary_status_done': '✅ Hecho',
        'diary_status_rest_done': '😴 Descanso',
        'diary_status_missed': '❌ Perdido',
        'diary_status_upcoming': '⏳ Próximo',
        'diary_history_title': '📋 HISTORIAL',
        'diary_skipped_ex': 'Ej. omitidos',
        'diary_no_skipped': 'Todos completados',
        'diary_exercises_list': 'Ejercicios',
        'diary_min': 'min',
        'diary_workouts_word': 'entrenamientos',
        'diary_days_word': 'días',
        'rec_progression': 'Aumente la carga 5-10% cada 2 semanas',
        'rec_measurements': 'Tome medidas corporales cada 2 semanas',
        # Nuevas claves
        'no_records': 'Sin registros',
        'finish': 'Terminar',
        'time_label': 'tiempo',
        'sets_done_label': 'series',
        'exercises_done_label': 'ejercicios',
        'skipped_label': 'omitidos',
        'min_short': 'min',
        'sets_short': 'series',
        'safety_confirm_error': '⚠️ ¡Por favor confirme su acuerdo!',
        'program_saved': '✅ ¡Programa guardado!',
        'how_was_workout': '🎯 ¿Cómo fue el entrenamiento?',
        'workout_too_easy': '😎 Muy fácil',
        'workout_just_right': '👍 Perfecto',
        'workout_too_hard': '😰 Muy difícil',
        'difficulty_adjusted_up': '💪 ¡Intensidad aumentada! +1 serie/+2 reps',
        'difficulty_kept': '✅ ¡Genial! El programa sigue igual',
        'difficulty_adjusted_down': '🙏 ¡Intensidad reducida! -1 serie/-2 reps',
        'monday': 'Lunes',
        'tuesday': 'Martes',
        'wednesday': 'Miércoles',
        'thursday': 'Jueves',
        'friday': 'Viernes',
        'saturday': 'Sábado',
        'sunday': 'Domingo',
        'rest_day': '😴 Descanso / Recuperación',
        'rest_btn': '😴 Descansar',
        'rest_today_msg': '¡Hoy descanso! 💤',
        'day_num': 'Día',
        'ease_title': '⚙️ ¿Aliviar el programa?',
        'ease_desc': 'Reducción segura de carga:\n• -1 serie por ejercicio\n• -2 repeticiones\n• +15 segundos de descanso',
        'ease_preview': '📋 Ejemplo de cambios:',
        'ease_sets': 'Series',
        'ease_reps': 'Reps',
        'ease_rest': 'Descanso',
        'ease_yes': '✅ Sí, aliviar',
        'ease_no': '❌ No, mantener',
        'ease_no_exercises': 'No hay ejercicios para cambiar.',
        # Ejercicios
        'Приседания': 'Sentadilla',
        'Отжимания': 'Flexión',
        'Выпады': 'Zancada',
        'Планка': 'Plancha',
        'Скалолаз': 'Escalador',
        'Берпи': 'Burpee',
        'Прыжки с хлопками': 'Saltos con palmada',
        'Ягодичный мостик': 'Puente de glúteos',
        'Боковая планка': 'Plancha lateral',
        'Велосипед': 'Bicicleta abdominal',
        'Русские скручивания': 'Giro ruso',
        'Скручивания на полу': 'Abdominales en el suelo',
        'Подъёмы ног': 'Elevación de piernas',
        'Мёртвый жук': 'Bicho muerto',
        'Берпи с отжиманиями': 'Burpee con flexión',
        'Динамическая боковая планка': 'Plancha lateral dinámica',
        'Выпады вперёд-назад': 'Zancada adelante-atrás',
        'Скручивания локтем к колену': 'Crunch codo a rodilla',
        'Подъём таза на одной ноге': 'Elevación de cadera a una pierna',
        'Подъём ног лёжа вверх': 'Elevación de piernas acostado',
        'Супермен': 'Superman',
        'Берпи (женский вариант)': 'Burpee (femenino)',
        'Планка на локтях': 'Plancha en codos',
        'Планка на одной руке': 'Plancha a un brazo',
        'Планка на прямых руках': 'Plancha con brazos rectos',
        'Планка с переходом в собаку мордой вниз': 'Plancha a perro boca abajo',
        'Обратные отжимания на трицепс': 'Fondos de tríceps',
        'Обратные снежные ангелы': 'Ángeles de nieve invertidos',
        'Обратная планка': 'Plancha inversa',
        'Псевдо-планш отжимания': 'Flexión pseudo planche',
        'Отжимания с возвышения': 'Flexión declinada',
        'Отжимания с колен': 'Flexión de rodillas',
        'Отжимания с ногами на возвышении': 'Flexión con pies elevados',
        'Отжимания уголком': 'Flexión pike',
        'Узкие отжимания': 'Flexión cerrada',
        'Широкие отжимания': 'Flexión abierta',
        'Подтягивания': 'Dominada',
        'Подтягивания колен': 'Elevación de rodillas',
        'Жим гантелей': 'Press con mancuernas',
        'Королевская становая тяга': 'Peso muerto real',
        'Становая тяга на одной ноге': 'Peso muerto a una pierna',
        'Болгарские сплит-приседания': 'Sentadilla búlgara',
        'Глубокие приседания с наклоном': 'Sentadilla profunda con inclinación',
        'Приседания плие': 'Sentadilla plié',
        'Приседания с прыжком': 'Sentadilla con salto',
        'Приседания у стены': 'Sentadilla en pared',
        'Выпады с ходьбой': 'Zancada caminando',
        'Статические выпады': 'Zancada estática',
        'Боковые наклоны': 'Inclinaciones laterales',
        'Конькобежец': 'Patinador',
        'Ножницы': 'Tijeras',
        'Подъём таза на скамье': 'Elevación de cadera en banco',
        'Подъёмы на носки': 'Elevación de talones',
        'Подъёмы ног лёжа': 'Elevación de piernas acostado',
        'Поза ребёнка': 'Postura del niño',
        'Русские скручивания сидя': 'Giro ruso sentado',
        'Супермен (удержание)': 'Superman (mantener)',
        'Ходьба на месте': 'Marcha en el lugar',
        'Бег на месте': 'Correr en el lugar',
        'Бег с высоким подниманием коленей': 'Rodillas altas',
        'Прыжки с хлопками над головой': 'Saltos con palmada arriba',
        'Подъём ног лёжа': 'Elevación de piernas acostado',
        'Алмазные отжимания': 'Flexión de diamante',
        'Вариации планки': 'Variaciones de plancha',
        'Вариации отжиманий': 'Variaciones de flexión',
        'Глубокие приседания': 'Sentadilla profunda',
        'Ягодичный мостик на одной ноге': 'Puente de glúteos a una pierna',
        'Бёрпи (женский вариант)': 'Burpee (femenino)',
        'Отжимания на брусьях (грудные)': 'Fondos en paralelas (pecho)',
        'Классические скручивания': 'Abdominales clásicos',
        'Подъём ног лёжа вверх': 'Elevación de piernas acostado',
        'Планка на одной руке гифка': 'Plancha a un brazo',
    },
    'de': {
        'app_title': '💪 TrainerWizard',
        'welcome': 'Willkommen!',
        'welcome_subtitle': 'Erstellen wir das perfekte Trainingsprogramm für dich',
        'motivation_text': '✨ Starte deine Reise zur besten Form',
        'male': 'Männlich',
        'female': 'Weiblich',
        'select': 'AUSWÄHLEN',
        'male_desc': '💪 Krafttraining\n📈 Masse aufbauen',
        'female_desc': '🎯 Straffung & Fitness\n🧘 Flexibilität',
        'continue_btn': 'WEITER →',
        'back_btn': '← ZURÜCK',
        'enter_data': '📋 GEBEN SIE IHRE DATEN EIN',
        'height': 'Größe',
        'weight': 'Gewicht',
        'age': 'Alter',
        'cm': 'cm',
        'kg': 'kg',
        'years': 'Jahre',
        'days_per_week': 'Tage pro Woche',
        'weeks_program': 'Programmwochen',
        'level': 'Fitnesslevel',
        'beginner': '🌱 Anfänger',
        'intermediate': '💪 Mittel',
        'advanced': '🔥 Fortgeschritten',
        'error_height': '⚠️ Gültige Größe eingeben!',
        'error_weight': '⚠️ Gültiges Gewicht eingeben!',
        'error_age': '⚠️ Gültiges Alter eingeben!',
        'error_height_range': '⚠️ Größe muss 120-250 cm sein!',
        'error_weight_range': '⚠️ Gewicht muss 40-200 kg sein!',
        'error_age_range': '⚠️ Alter muss 14-80 Jahre sein!',
        'choose_goal': '🎯 WÄHLE DEIN ZIEL',
        'goal_subtitle': 'Was möchtest du erreichen?',
        'weight_loss': 'Gewichtsverlust',
        'weight_loss_desc': '🔥 HIIT\n📉 Kalorien verbrennen',
        'muscle_gain': 'Muskelaufbau',
        'muscle_gain_desc': '💪 Kraftübungen\n📈 Muskelwachstum',
        'choose_zone': '🎯 WÄHLE TRAININGSZONE',
        'focus_question': 'AUF WELCHEN KÖRPERTEIL\nMÖCHTEST DU DICH KONZENTRIEREN?',
        'all_muscles': 'ALLE MUSKELN',
        'chest_zone': 'BRUST',
        'arms_zone': 'ARME',
        'core_zone': 'BAUCH',
        'legs_zone': 'BEINE',
        'Full Body': 'Ganzkörper',
        'Legs': 'Beine',
        'Chest': 'Brust',
        'Back': 'Rücken',
        'Arms': 'Arme',
        'Shoulders': 'Schultern',
        'Core': 'Bauch',
        'Weight Loss': 'Gewichtsverlust',
        'safety_title': '⚠️ SICHERHEIT ZUERST',
        'safety_subtitle': 'Bitte lies die Empfehlungen',
        'safety_agree': '✅ Ich habe die Empfehlungen gelesen und bin bereit',
        'nutrition_title': '🍽️ ERNÄHRUNGSPLAN',
        'nutrition_subtitle': 'Empfohlene Kalorien für dein Ziel',
        'kcal_day': 'KCAL/TAG',
        'protein': 'PROTEIN',
        'fats': 'FETTE',
        'carbs': 'KOHLENHYDRATE',
        'g': 'g',
        'nutrition_tips': '💡 Ernährungstipps:',
        'tip1': '• Trinke 2-3 Liter Wasser täglich',
        'tip2': '• Iss 4-5 kleine Mahlzeiten',
        'tip3': '• Protein bei jeder Mahlzeit',
        'tip4': '• Komplexe Kohlenhydrate vor 16:00',
        'tip5': '• Vermeide Zucker und Fast Food',
        'to_program': 'ZUM PROGRAMM →',
        'program_ready': '📋 DEIN PROGRAMM IST FERTIG',
        'program_subtitle': 'Persönlicher Trainingsplan erstellt',
        'week': 'Woche',
        'day': 'Tag',
        'exercises': 'Üb.',
        'sets': 'Sätze',
        'reps': 'Wdh',
        'start_btn': '▶️ START',
        'completed': '✅ Fertig',
        'locked': '🔒 Gesperrt',
        'save_program': 'Speichern',
        'my_progress': 'Fortschritt',
        'diary': 'Tagebuch',
        'new_program': 'Neu',
        'training_program_title': '📋 TRAININGSPROGRAMM',
        'workout_title': '▶️ TRAINING',
        'exercise': 'Übung',
        'set': 'Satz',
        'of': 'von',
        'seconds': 'Sek',
        'hold': 'Halten',
        'rest': 'Pause',
        'complete_set': '✅ SATZ FERTIG',
        'skip_exercise': '⏭️ Überspringen',
        'simplify': '😓 Vereinfachen',
        'finish_workout': '❌ Beenden',
        'rest_between': 'Pause zwischen Sätzen',
        'sec': 'Sek',
        'start_timer': 'START',
        'add_10_sec': '+10 Sek',
        'skip': 'Überspringen',
        'done': 'Fertig',
        'rest_time': 'Pausenzeit',
        'press_start': 'Drücke START',
        'skip_rest': 'Überspringen',
        'workout_complete': '🎉 SUPER!',
        'workout_finished': 'Training beendet!',
        'great_job': 'Gute Arbeit!',
        'settings': '⚙️ Einstellungen',
        'settings_language': '🌐 Sprache',
        'settings_theme': '🎨 Thema',
        'theme_dark': 'Dunkel',
        'theme_light': 'Hell',
        'settings_back': '← Zurück',
        'settings_exit': '🚪 App beenden',
        'rec_title': '💡 Persönliche Empfehlungen',
        'rec_cardio_weight_loss': 'Füge 20-30 Minuten Cardio nach jedem Training hinzu',
        'rec_cardio_muscle': 'Begrenze Cardio auf 10-15 Minuten um Masse zu erhalten',
        'rec_nutrition_weight_loss': 'Kaloriendefizit von -500 kcal/Tag für sanfte Abnahme',
        'rec_nutrition_muscle': 'Überschuss von +300 kcal/Tag für Masseaufbau',
        'rec_rest_days': 'Ruhe {count} Tage pro Woche für Muskelregeneration',
        'rec_duration_beginner': 'Optimale Trainingsdauer 30-45 Minuten',
        'rec_duration_intermediate': 'Optimale Trainingsdauer 45-60 Minuten',
        'rec_duration_advanced': 'Optimale Trainingsdauer 60-90 Minuten',
        'rec_warmup': 'Beginne immer mit 5-10 Minuten Aufwärmen',
        'bmi': 'BMI',
        'goal_weight_loss': 'Gewichtsverlust',
        'goal_muscle_gain': 'Muskelaufbau',
        'weeks': 'Wochen',
        'days': 'Tage/Woche',
        # Sicherheit
        'safety_60plus': '🔴 WICHTIG FÜR ALTER 60+',
        'safety_60_1': '⚠️ Konsultieren Sie vor Beginn unbedingt einen Arzt',
        'safety_60_2': '🫀 Holen Sie sich die Genehmigung des Kardiologen bei Herzerkrankungen',
        'safety_60_3': '🚫 Vermeiden Sie plötzliche Bewegungen und hohe Intensität',
        'safety_50plus': '🟡 EMPFEHLUNGEN FÜR 50+',
        'safety_50_1': '👨‍⚕️ Ärztliche Beratung empfohlen',
        'safety_50_2': '🔥 Achten Sie besonders auf das Aufwärmen (10-15 Min)',
        'safety_50_3': '💪 Kontrollieren Sie Ihren Puls beim Training',
        'safety_teen': '🟢 FÜR JUGENDLICHE (14-17)',
        'safety_teen_1': '📚 Training angepasst für wachsenden Körper',
        'safety_teen_2': '🚫 Vermeiden Sie übermäßige Wirbelsäulenbelastung',
        'safety_teen_3': '👨‍👩‍👦 Stimmen Sie das Programm mit den Eltern ab',
        'safety_general': '✅ ALLGEMEINE EMPFEHLUNGEN',
        'safety_gen_1': '👨‍⚕️ Bei chronischen Erkrankungen Arzt konsultieren',
        'safety_gen_2': '🛑 Sofort aufhören bei Schmerzen',
        'safety_gen_3': '🔥 Immer mit 5-10 Min Aufwärmen beginnen',
        # Typen und Schwierigkeit
        'compound': '🔸 Grundübung',
        'isolation': '🔹 Isolation',
        'core': '🎯 Bauch',
        'cardio': '🏃 Cardio',
        'type_compound': 'Grundübung',
        'type_isolation': 'Isolation',
        'type_core': 'Bauch',
        'type_cardio': 'Cardio',
        'diff_beginner': 'Anfänger',
        'diff_intermediate': 'Mittel',
        'diff_advanced': 'Fortgeschritten',
        # Fortschritt
        'progress_title': '📊 MEIN FORTSCHRITT',
        'weight_title': '⚖️ GEWICHTSKONTROLLE',
        'measurements': '📏 KÖRPERMASSE (cm)',
        'chest_label': '💪 Brust:',
        'waist_label': '👖 Taille:',
        'hips_label': '🍑 Hüften:',
        'arms_label': '💪 Arme:',
        'add_btn': '➕ Hinzufügen',
        'save_btn': '💾 Speichern',
        'photos_title': '📷 FORTSCHRITTSFOTOS',
        'no_photos': 'Keine Fotos',
        'add_photo': '📸 Foto hinzufügen',
        'back_to_program': '← ZUM PROGRAMM',
        'diary_title': '📊 TRAININGSTAGEBUCH',
        'total_workouts': 'Training insgesamt',
        'great_progress': '🎉 Toller Fortschritt! Weiter so!',
        'diary_total_time': 'Gesamtzeit',
        'diary_completion': 'Abgeschlossen',
        'diary_missed': 'Verpasst',
        'diary_upcoming': 'Bevorstehend',
        'diary_streak': 'Serie',
        'diary_avg_time': 'Durchschn. Zeit',
        'diary_progress_title': '📅 TAGESFORTSCHRITT',
        'diary_status_done': '✅ Erledigt',
        'diary_status_rest_done': '😴 Ruhe',
        'diary_status_missed': '❌ Verpasst',
        'diary_status_upcoming': '⏳ Bevorstehend',
        'diary_history_title': '📋 TRAININGSHISTORIE',
        'diary_skipped_ex': 'Übersprungen',
        'diary_no_skipped': 'Alle abgeschlossen',
        'diary_exercises_list': 'Übungen',
        'diary_min': 'Min',
        'diary_workouts_word': 'Trainings',
        'diary_days_word': 'Tage',
        'rec_progression': 'Steigern Sie die Last alle 2 Wochen um 5-10%',
        'rec_measurements': 'Messen Sie Ihren Körper alle 2 Wochen',
        # Neue Schlüssel
        'no_records': 'Keine Einträge',
        'finish': 'Beenden',
        'time_label': 'Zeit',
        'sets_done_label': 'Sätze',
        'exercises_done_label': 'Übungen',
        'skipped_label': 'übersprungen',
        'min_short': 'Min',
        'sets_short': 'Sätze',
        'safety_confirm_error': '⚠️ Bitte bestätigen Sie Ihre Zustimmung!',
        'program_saved': '✅ Programm gespeichert!',
        'how_was_workout': '🎯 Wie war das Training?',
        'workout_too_easy': '😎 Zu leicht',
        'workout_just_right': '👍 Genau richtig',
        'workout_too_hard': '😰 Zu schwer',
        'difficulty_adjusted_up': '💪 Intensität erhöht! +1 Satz/+2 Wdh',
        'difficulty_kept': '✅ Super! Programm bleibt gleich',
        'difficulty_adjusted_down': '🙏 Intensität gesenkt! -1 Satz/-2 Wdh',
        'monday': 'Montag',
        'tuesday': 'Dienstag',
        'wednesday': 'Mittwoch',
        'thursday': 'Donnerstag',
        'friday': 'Freitag',
        'saturday': 'Samstag',
        'sunday': 'Sonntag',
        'rest_day': '😴 Ruhe / Erholung',
        'rest_btn': '😴 Ausruhen',
        'rest_today_msg': 'Heute ruhe ich mich aus! 💤',
        'day_num': 'Tag',
        'ease_title': '⚙️ Programm erleichtern?',
        'ease_desc': 'Sichere Belastungsreduzierung:\n• -1 Satz pro Übung\n• -2 Wiederholungen\n• +15 Sekunden Pause',
        'ease_preview': '📋 Beispieländerungen:',
        'ease_sets': 'Sätze',
        'ease_reps': 'Wdh',
        'ease_rest': 'Pause',
        'ease_yes': '✅ Ja, erleichtern',
        'ease_no': '❌ Nein, beibehalten',
        'ease_no_exercises': 'Keine Übungen zum Ändern.',
        # Übungen
        'Приседания': 'Kniebeuge',
        'Отжимания': 'Liegestütz',
        'Выпады': 'Ausfallschritt',
        'Планка': 'Planke',
        'Скалолаз': 'Bergsteiger',
        'Берпи': 'Burpee',
        'Прыжки с хлопками': 'Hampelmann',
        'Ягодичный мостик': 'Gesäßbrücke',
        'Боковая планка': 'Seitliche Planke',
        'Велосипед': 'Fahrrad-Crunch',
        'Русские скручивания': 'Russischer Twist',
        'Скручивания на полу': 'Boden-Crunch',
        'Подъёмы ног': 'Beinheben',
        'Мёртвый жук': 'Toter Käfer',
        'Берпи с отжиманиями': 'Burpee mit Liegestütz',
        'Динамическая боковая планка': 'Dynamische seitliche Planke',
        'Выпады вперёд-назад': 'Ausfallschritt vor-zurück',
        'Скручивания локтем к колену': 'Ellbogen-Knie-Crunch',
        'Подъём таза на одной ноге': 'Einbeiniges Beckenheben',
        'Подъём ног лёжа вверх': 'Beinheben liegend',
        'Супермен': 'Superman',
        'Берпи (женский вариант)': 'Burpee (weiblich)',
        'Планка на локтях': 'Unterarm-Planke',
        'Планка на одной руке': 'Einarm-Planke',
        'Планка на прямых руках': 'Planke mit gestreckten Armen',
        'Планка с переходом в собаку мордой вниз': 'Planke zum herabschauenden Hund',
        'Обратные отжимания на трицепс': 'Trizeps-Dips',
        'Обратные снежные ангелы': 'Umgekehrte Schneeengel',
        'Обратная планка': 'Umgekehrte Planke',
        'Псевдо-планш отжимания': 'Pseudo-Planche-Liegestütz',
        'Отжимания с возвышения': 'Erhöhte Liegestütz',
        'Отжимания с колен': 'Knie-Liegestütz',
        'Отжимания с ногами на возвышении': 'Liegestütz mit erhöhten Füßen',
        'Отжимания уголком': 'Pike-Liegestütz',
        'Узкие отжимания': 'Enge Liegestütz',
        'Широкие отжимания': 'Weite Liegestütz',
        'Подтягивания': 'Klimmzug',
        'Подтягивания колен': 'Knieheben',
        'Жим гантелей': 'Kurzhanteldrücken',
        'Королевская становая тяга': 'Königliches Kreuzheben',
        'Становая тяга на одной ноге': 'Einbeiniges Kreuzheben',
        'Болгарские сплит-приседания': 'Bulgarische Split-Kniebeuge',
        'Глубокие приседания с наклоном': 'Tiefe Kniebeuge mit Neigung',
        'Приседания плие': 'Plié-Kniebeuge',
        'Приседания с прыжком': 'Sprung-Kniebeuge',
        'Приседания у стены': 'Wandsitzen',
        'Выпады с ходьбой': 'Gehender Ausfallschritt',
        'Статические выпады': 'Statischer Ausfallschritt',
        'Боковые наклоны': 'Seitliche Neigung',
        'Конькобежец': 'Schlittschuhläufer',
        'Ножницы': 'Schere',
        'Подъём таза на скамье': 'Beckenheben auf Bank',
        'Подъёмы на носки': 'Wadenheben',
        'Подъёмы ног лёжа': 'Beinheben liegend',
        'Поза ребёнка': 'Kindeshaltung',
        'Русские скручивания сидя': 'Sitzender russischer Twist',
        'Супермен (удержание)': 'Superman (Halten)',
        'Ходьба на месте': 'Marschieren auf der Stelle',
        'Бег на месте': 'Laufen auf der Stelle',
        'Бег с высоким подниманием коленей': 'Hohe Knie',
        'Прыжки с хлопками над головой': 'Hampelmann über Kopf',
        'Подъём ног лёжа': 'Beinheben liegend',
        'Алмазные отжимания': 'Diamant-Liegestütz',
        'Вариации планки': 'Planke-Variationen',
        'Вариации отжиманий': 'Liegestütz-Variationen',
        'Глубокие приседания': 'Tiefe Kniebeuge',
        'Ягодичный мостик на одной ноге': 'Einbeinige Gesäßbrücke',
        'Бёрпи (женский вариант)': 'Burpee (weiblich)',
        'Отжимания на брусьях (грудные)': 'Barren-Dips (Brust)',
        'Классические скручивания': 'Klassische Crunches',
        'Подъём ног лёжа вверх': 'Beinheben liegend',
        'Планка на одной руке гифка': 'Einarm-Planke',
    },
    'zh': {
        'app_title': '💪 TrainerWizard',
        'welcome': '欢迎！',
        'welcome_subtitle': '让我们为您创建完美的训练计划',
        'motivation_text': '✨ 开始您的最佳体型之旅',
        'male': '男性',
        'female': '女性',
        'select': '选择',
        'male_desc': '💪 力量训练\n📈 增肌',
        'female_desc': '🎯 塑形\n🧘 柔韧性',
        'continue_btn': '继续 →',
        'back_btn': '← 返回',
        'enter_data': '📋 输入您的数据',
        'height': '身高',
        'weight': '体重',
        'age': '年龄',
        'cm': '厘米',
        'kg': '公斤',
        'years': '岁',
        'days_per_week': '每周天数',
        'weeks_program': '计划周数',
        'level': '健身水平',
        'beginner': '🌱 初学者',
        'intermediate': '💪 中级',
        'advanced': '🔥 高级',
        'error_height': '⚠️ 请输入有效身高！',
        'error_weight': '⚠️ 请输入有效体重！',
        'error_age': '⚠️ 请输入有效年龄！',
        'error_height_range': '⚠️ 身高必须是120-250厘米！',
        'error_weight_range': '⚠️ 体重必须是40-200公斤！',
        'error_age_range': '⚠️ 年龄必须是14-80岁！',
        'choose_goal': '🎯 选择您的目标',
        'goal_subtitle': '您想达到什么目标？',
        'weight_loss': '减肥',
        'weight_loss_desc': '🔥 HIIT训练\n📉 燃烧卡路里',
        'muscle_gain': '增肌',
        'muscle_gain_desc': '💪 力量练习\n📈 肌肉增长',
        'choose_zone': '🎯 选择训练区域',
        'focus_question': '您想专注于\n哪个身体部位？',
        'all_muscles': '全身肌肉',
        'chest_zone': '胸部',
        'arms_zone': '手臂',
        'core_zone': '腹肌',
        'legs_zone': '腿部',
        'Full Body': '全身',
        'Legs': '腿部',
        'Chest': '胸部',
        'Back': '背部',
        'Arms': '手臂',
        'Shoulders': '肩膀',
        'Core': '腹肌',
        'Weight Loss': '减肥',
        'safety_title': '⚠️ 安全第一',
        'safety_subtitle': '请阅读建议',
        'safety_agree': '✅ 我已阅读建议并准备开始',
        'nutrition_title': '🍽️ 营养计划',
        'nutrition_subtitle': '针对您目标的推荐卡路里',
        'kcal_day': '卡路里/天',
        'protein': '蛋白质',
        'fats': '脂肪',
        'carbs': '碳水化合物',
        'g': '克',
        'nutrition_tips': '💡 营养建议：',
        'tip1': '• 每天喝2-3升水',
        'tip2': '• 每天吃4-5顿小餐',
        'tip3': '• 每餐摄入蛋白质',
        'tip4': '• 下午4点前摄入复杂碳水',
        'tip5': '• 避免糖和快餐',
        'to_program': '进入计划 →',
        'program_ready': '📋 您的计划已准备好',
        'program_subtitle': '个人训练计划已创建',
        'week': '周',
        'day': '天',
        'exercises': '练习',
        'sets': '组',
        'reps': '次',
        'start_btn': '▶️ 开始',
        'completed': '✅ 已完成',
        'locked': '🔒 已锁定',
        'save_program': '保存',
        'my_progress': '进度',
        'diary': '日记',
        'new_program': '新建',
        'training_program_title': '📋 训练计划',
        'workout_title': '▶️ 训练',
        'exercise': '练习',
        'set': '组',
        'of': '/',
        'seconds': '秒',
        'hold': '保持',
        'rest': '休息',
        'complete_set': '✅ 完成一组',
        'skip_exercise': '⏭️ 跳过',
        'simplify': '😓 简化',
        'finish_workout': '❌ 结束',
        'rest_between': '组间休息',
        'sec': '秒',
        'start_timer': '开始',
        'add_10_sec': '+10秒',
        'skip': '跳过',
        'done': '完成',
        'rest_time': '休息时间',
        'press_start': '按开始',
        'skip_rest': '跳过',
        'workout_complete': '🎉 太棒了！',
        'workout_finished': '训练完成！',
        'great_job': '干得好！',
        'settings': '⚙️ 设置',
        'settings_language': '🌐 语言',
        'settings_theme': '🎨 主题',
        'theme_dark': '深色',
        'theme_light': '浅色',
        'settings_back': '← 返回',
        'settings_exit': '🚪 退出应用',
        'rec_title': '💡 个人建议',
        'rec_cardio_weight_loss': '每次训练后增加20-30分钟有氧运动',
        'rec_cardio_muscle': '将有氧运动限制在10-15分钟以保持肌肉量',
        'rec_nutrition_weight_loss': '每天减少500卡路里以逐步减重',
        'rec_nutrition_muscle': '每天增加300卡路里以增加肌肉',
        'rec_rest_days': '每周休息{count}天以恢复肌肉',
        'rec_duration_beginner': '最佳训练时长30-45分钟',
        'rec_duration_intermediate': '最佳训练时长45-60分钟',
        'rec_duration_advanced': '最佳训练时长60-90分钟',
        'rec_warmup': '始终以5-10分钟热身开始',
        'bmi': 'BMI',
        'goal_weight_loss': '减肥',
        'goal_muscle_gain': '增肌',
        'weeks': '周',
        'days': '天/周',
        # 安全
        'safety_60plus': '🔴 60岁以上重要提示',
        'safety_60_1': '⚠️ 开始前务必咨询医生',
        'safety_60_2': '🫀 如有心脏病请获得心脏科医生许可',
        'safety_60_3': '🚫 避免突然运动和高强度训练',
        'safety_50plus': '🟡 50岁以上建议',
        'safety_50_1': '👨‍⚕️ 建议咨询医生',
        'safety_50_2': '🔥 特别注意热身（10-15分钟）',
        'safety_50_3': '💪 训练期间监测心率',
        'safety_teen': '🟢 青少年（14-17岁）',
        'safety_teen_1': '📚 训练适应成长中的身体',
        'safety_teen_2': '🚫 避免脊柱过度负荷',
        'safety_teen_3': '👨‍👩‍👦 与父母协调训练计划',
        'safety_general': '✅ 一般建议',
        'safety_gen_1': '👨‍⚕️ 如有慢性疾病请咨询医生',
        'safety_gen_2': '🛑 如感到疼痛立即停止',
        'safety_gen_3': '🔥 始终以5-10分钟热身开始',
        # 类型和难度
        'compound': '🔸 复合动作',
        'isolation': '🔹 孤立动作',
        'core': '🎯 腹肌',
        'cardio': '🏃 有氧',
        'type_compound': '复合动作',
        'type_isolation': '孤立动作',
        'type_core': '腹肌',
        'type_cardio': '有氧',
        'diff_beginner': '初学者',
        'diff_intermediate': '中级',
        'diff_advanced': '高级',
        # 进度
        'progress_title': '📊 我的进度',
        'weight_title': '⚖️ 体重跟踪',
        'measurements': '📏 身体测量（厘米）',
        'chest_label': '💪 胸围:',
        'waist_label': '👖 腰围:',
        'hips_label': '🍑 臀围:',
        'arms_label': '💪 臂围:',
        'add_btn': '➕ 添加',
        'save_btn': '💾 保存',
        'photos_title': '📷 进度照片',
        'no_photos': '没有照片',
        'add_photo': '📸 添加照片',
        'back_to_program': '← 返回计划',
        'diary_title': '📊 训练日记',
        'total_workouts': '总训练次数',
        'great_progress': '🎉 进步很大！继续加油！',
        'diary_total_time': '总时间',
        'diary_completion': '已完成',
        'diary_missed': '已错过',
        'diary_upcoming': '即将到来',
        'diary_streak': '连续',
        'diary_avg_time': '平均时间',
        'diary_progress_title': '📅 每日进度',
        'diary_status_done': '✅ 完成',
        'diary_status_rest_done': '😴 休息',
        'diary_status_missed': '❌ 错过',
        'diary_status_upcoming': '⏳ 即将到来',
        'diary_history_title': '📋 训练历史',
        'diary_skipped_ex': '跳过练习',
        'diary_no_skipped': '全部完成',
        'diary_exercises_list': '练习',
        'diary_min': '分钟',
        'diary_workouts_word': '次训练',
        'diary_days_word': '天',
        'rec_progression': '每2周增加5-10%的负荷',
        'rec_measurements': '每2周测量一次身体数据',
        # 新键
        'no_records': '没有记录',
        'finish': '结束',
        'time_label': '时间',
        'sets_done_label': '组数',
        'exercises_done_label': '练习',
        'skipped_label': '跳过',
        'min_short': '分钟',
        'sets_short': '组',
        'safety_confirm_error': '⚠️ 请确认您的同意！',
        'program_saved': '✅ 计划已保存！',
        'how_was_workout': '🎯 训练感觉如何？',
        'workout_too_easy': '😎 太简单',
        'workout_just_right': '👍 刚刚好',
        'workout_too_hard': '😰 太难了',
        'difficulty_adjusted_up': '💪 强度增加！+1组/+2次',
        'difficulty_kept': '✅ 很好！计划保持不变',
        'difficulty_adjusted_down': '🙏 强度降低！-1组/-2次',
        'monday': '星期一',
        'tuesday': '星期二',
        'wednesday': '星期三',
        'thursday': '星期四',
        'friday': '星期五',
        'saturday': '星期六',
        'sunday': '星期日',
        'rest_day': '😴 休息 / 恢复',
        'rest_btn': '😴 休息',
        'rest_today_msg': '今天我休息！💤',
        'day_num': '第天',
        'ease_title': '⚙️ 降低训练难度？',
        'ease_desc': '安全降低负荷：\n• 每个动作减1组\n• 减2次\n• 增加15秒休息',
        'ease_preview': '📋 变更示例：',
        'ease_sets': '组数',
        'ease_reps': '次数',
        'ease_rest': '休息',
        'ease_yes': '✅ 是，降低',
        'ease_no': '❌ 不，保持',
        'ease_no_exercises': '没有可修改的练习。',
        # 练习
        'Приседания': '深蹲',
        'Отжимания': '俯卧撑',
        'Выпады': '弓步',
        'Планка': '平板支撑',
        'Скалолаз': '登山者',
        'Берпи': '波比跳',
        'Прыжки с хлопками': '开合跳',
        'Ягодичный мостик': '臀桥',
        'Боковая планка': '侧平板支撑',
        'Велосипед': '自行车卷腹',
        'Русские скручивания': '俄式转体',
        'Скручивания на полу': '地面卷腹',
        'Подъёмы ног': '抬腿',
        'Мёртвый жук': '死虫',
        'Берпи с отжиманиями': '波比跳+俯卧撑',
        'Динамическая боковая планка': '动态侧平板',
        'Выпады вперёд-назад': '前后弓步',
        'Скручивания локтем к колену': '肘膝卷腹',
        'Подъём таза на одной ноге': '单腿臀桥',
        'Подъём ног лёжа вверх': '仰卧抬腿',
        'Супермен': '超人式',
        'Берпи (женский вариант)': '波比跳（女性版）',
        'Планка на локтях': '肘支撑平板',
        'Планка на одной руке': '单臂平板',
        'Планка на прямых руках': '直臂平板支撑',
        'Планка с переходом в собаку мордой вниз': '平板转下犬式',
        'Обратные отжимания на трицепс': '三头肌撑体',
        'Обратные снежные ангелы': '反向雪天使',
        'Обратная планка': '反向平板支撑',
        'Псевдо-планш отжимания': '伪倒立俯卧撑',
        'Отжимания с возвышения': '上斜俯卧撑',
        'Отжимания с колен': '跪姿俯卧撑',
        'Отжимания с ногами на возвышении': '下斜俯卧撑',
        'Отжимания уголком': '倒V俯卧撑',
        'Узкие отжимания': '窄距俯卧撑',
        'Широкие отжимания': '宽距俯卧撑',
        'Подтягивания': '引体向上',
        'Подтягивания колен': '悬垂抬膝',
        'Жим гантелей': '哑铃推举',
        'Королевская становая тяга': '皇家硬拉',
        'Становая тяга на одной ноге': '单腿硬拉',
        'Болгарские сплит-приседания': '保加利亚分腿蹲',
        'Глубокие приседания с наклоном': '深蹲前倾',
        'Приседания плие': '芭蕾深蹲',
        'Приседания с прыжком': '跳跃深蹲',
        'Приседания у стены': '靠墙深蹲',
        'Выпады с ходьбой': '行走弓步',
        'Статические выпады': '静态弓步',
        'Боковые наклоны': '侧弯',
        'Конькобежец': '滑冰者',
        'Ножницы': '剪刀腿',
        'Подъём таза на скамье': '凳上臀桥',
        'Подъёмы на носки': '提踵',
        'Подъёмы ног лёжа': '仰卧抬腿',
        'Поза ребёнка': '婴儿式',
        'Русские скручивания сидя': '坐姿俄式转体',
        'Супермен (удержание)': '超人式（保持）',
        'Ходьба на месте': '原地踏步',
        'Бег на месте': '原地跑步',
        'Бег с высоким подниманием коленей': '高抬腿',
        'Прыжки с хлопками над головой': '头顶拍手跳',
        'Подъём ног лёжа': '仰卧抬腿',
        'Алмазные отжимания': '钻石俯卧撑',
        'Вариации планки': '平板支撑变式',
        'Вариации отжиманий': '俯卧撑变式',
        'Глубокие приседания': '深蹲',
        'Ягодичный мостик на одной ноге': '单腿臀桥',
        'Бёрпи (женский вариант)': '波比跳（女性版）',
        'Отжимания на брусьях (грудные)': '双杠撑体（胸部）',
        'Классические скручивания': '经典卷腹',
        'Подъём ног лёжа вверх': '仰卧抬腿',
        'Планка на одной руке гифка': '单臂平板',
    },
}

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
        {'name': 'Выпады', 'type': 'strength', 'difficulty': 'beginner', 'gif': 'выпады.gif'},
        {'name': 'Отжимания', 'type': 'strength', 'difficulty': 'beginner', 'gif': 'отжимания.gif'},
        {'name': 'Планка', 'type': 'core', 'difficulty': 'beginner', 'gif': 'планка.gif', 'is_hold': True},
        {'name': 'Ягодичный мостик', 'type': 'strength', 'difficulty': 'beginner', 'gif': 'ягодичный моститк.gif'},
        {'name': 'Мёртвый жук', 'type': 'core', 'difficulty': 'beginner', 'gif': 'Мёртвый жук.gif'},
        {'name': 'Боковая планка', 'type': 'core', 'difficulty': 'intermediate', 'gif': 'Боковая планка.gif', 'is_hold': True},
        {'name': 'Подъёмы ног лёжа', 'type': 'core', 'difficulty': 'beginner', 'gif': 'Подъём ног лёжа.gif'},
        {'name': 'Супермен', 'type': 'core', 'difficulty': 'beginner', 'gif': 'Супермен (удержание).webp', 'is_hold': True},
        {'name': 'Скручивания на полу', 'type': 'core', 'difficulty': 'beginner', 'gif': 'Скручивания на полу.gif'},
        {'name': 'Велосипед', 'type': 'core', 'difficulty': 'beginner', 'gif': 'Велосипед (скручивания).gif'},
        {'name': 'Русские скручивания', 'type': 'core', 'difficulty': 'beginner', 'gif': 'Русские скручивания.gif'},
        {'name': 'Ножницы', 'type': 'core', 'difficulty': 'beginner', 'gif': 'ножницы.gif'},
        {'name': 'Подъёмы ног', 'type': 'core', 'difficulty': 'beginner', 'gif': 'подъемы ног.gif'},
        {'name': 'Обратная планка', 'type': 'core', 'difficulty': 'intermediate', 'gif': 'Обратная планка.gif', 'is_hold': True},
        {'name': 'Планка на локтях', 'type': 'core', 'difficulty': 'beginner', 'gif': 'планка на локтях.gif', 'is_hold': True},
        
        # ===== СИЛОВЫЕ С ЭЛЕМЕНТАМИ КАРДИО =====
        {'name': 'Выпады с прыжком', 'type': 'hiit', 'difficulty': 'intermediate', 'gif': 'выпады.gif'},
        {'name': 'Планка в собаку мордой вниз', 'type': 'hiit', 'difficulty': 'beginner', 'gif': 'Планка с переходом в собаку мордой вниз.gif'},
        {'name': 'Динамическая боковая планка', 'type': 'hiit', 'difficulty': 'intermediate', 'gif': 'динамическая боковая планка.gif', 'is_hold': True},
        {'name': 'Выпады в ходьбе', 'type': 'strength', 'difficulty': 'beginner', 'gif': 'Выпады с ходьбой.gif'},
        {'name': 'Глубокие приседания', 'type': 'strength', 'difficulty': 'beginner', 'gif': 'Глубокие приседания с наклоном.gif'},
        {'name': 'Подъёмы на носки', 'type': 'strength', 'difficulty': 'beginner', 'gif': 'Подъёмы на носки.gif'},
        {'name': 'Статические выпады', 'type': 'strength', 'difficulty': 'beginner', 'gif': 'Статические выпады.gif'},
        {'name': 'Приседания у стены', 'type': 'strength', 'difficulty': 'beginner', 'gif': 'Приседания у стены.gif', 'is_hold': True},
        
        # ===== МУЖСКИЕ HIIT УПРАЖНЕНИЯ =====
        {'name': 'Берпи с отжиманиями', 'type': 'hiit', 'difficulty': 'intermediate', 'gif': 'берпи с отжиманиями.gif', 'male_focused': True},
        {'name': 'Скалолаз (быстрый)', 'type': 'hiit', 'difficulty': 'intermediate', 'gif': 'скалолаз.gif', 'male_focused': True},
        {'name': 'Широкие отжимания', 'type': 'strength', 'difficulty': 'beginner', 'gif': 'Широкие отжимания.gif', 'male_focused': True},
        {'name': 'Алмазные отжимания', 'type': 'strength', 'difficulty': 'intermediate', 'gif': 'алмазные отжимания.gif', 'male_focused': True},
        {'name': 'Узкие отжимания', 'type': 'strength', 'difficulty': 'intermediate', 'gif': 'узкие отжимания.gif', 'male_focused': True},
        {'name': 'Отжимания уголком', 'type': 'strength', 'difficulty': 'intermediate', 'gif': 'отжимания уголком.gif', 'male_focused': True},
        {'name': 'Обратные отжимания', 'type': 'strength', 'difficulty': 'beginner', 'gif': 'Обратные отжимания на трицепс.gif', 'male_focused': True},
        {'name': 'Отжимания с возвышения', 'type': 'strength', 'difficulty': 'beginner', 'gif': 'Отжимания с возвышения.gif', 'male_focused': True},
        
        # ===== ЖЕНСКИЕ HIIT УПРАЖНЕНИЯ =====
        {'name': 'Бёрпи (женский вариант)', 'type': 'hiit', 'difficulty': 'beginner', 'gif': 'Берпи (женский вариант).gif', 'female_focused': True},
        {'name': 'Приседания плие', 'type': 'strength', 'difficulty': 'beginner', 'gif': 'Приседания плие.gif', 'female_focused': True},
        {'name': 'Ягодичный мостик на одной ноге', 'type': 'strength', 'difficulty': 'intermediate', 'gif': 'Подъём таза на одной ноге.gif', 'female_focused': True},
        {'name': 'Выпады вперёд-назад', 'type': 'hiit', 'difficulty': 'intermediate', 'gif': 'Выпады вперёд-назад.gif', 'female_focused': True},
        {'name': 'Болгарские сплит-приседания', 'type': 'strength', 'difficulty': 'intermediate', 'gif': 'Болгарские сплит-приседания.gif', 'female_focused': True},
        {'name': 'Подъём таза на скамье', 'type': 'strength', 'difficulty': 'intermediate', 'gif': 'Подъём таза на скамье.gif', 'female_focused': True},
        {'name': 'Отжимания с колен', 'type': 'strength', 'difficulty': 'beginner', 'gif': 'Отжимания с колен.gif', 'female_focused': True},
        {'name': 'Поза ребёнка', 'type': 'core', 'difficulty': 'beginner', 'gif': 'Поза ребёнка.gif', 'female_focused': True, 'is_hold': True},
        {'name': 'Боковые наклоны', 'type': 'core', 'difficulty': 'beginner', 'gif': 'Боковые наклоны.gif', 'female_focused': True},
        {'name': 'Подтягивания коленей', 'type': 'core', 'difficulty': 'beginner', 'gif': 'Подтягивания колен.gif', 'female_focused': True},
    ],
}


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
        locale = LOCALES.get(self.lang, LOCALES['en'])
        return locale.get(key, LOCALES['en'].get(key, LOCALES['ru'].get(key, key)))
    
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
        self.lang = lang
        self.settings_visible = True
        self.refresh_screen()
    
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
                
                # Заголовок с эффектом свечения
                ft.Container(
                    content=ft.Text(f"💪 {self.t('welcome')}", 
                           size=34, weight=ft.FontWeight.BOLD,
                           color=self.colors['primary'], text_align=ft.TextAlign.CENTER),
                    shadow=ft.BoxShadow(
                        blur_radius=30,
                        color=ft.Colors.with_opacity(0.4, self.colors['primary']),
                    ),
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
        
        self.weeks_dropdown = ft.Dropdown(
            label=self.t('weeks_program'),
            width=500,
            height=50,
            options=[
                ft.dropdown.Option("5", "5"),
                ft.dropdown.Option("6", "6"),
            ],
            value="5",
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
                self.weeks_dropdown,
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
                self.user_data['weeks'] = int(self.weeks_dropdown.value)
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
        
        content = ft.Container(
            content=ft.Column([
                ft.Container(height=25),
                
                # Заголовок
                ft.Text(self.t('choose_goal'), size=28, weight=ft.FontWeight.BOLD,
                       color=self.colors['text']),
                ft.Text(self.t('goal_subtitle'), size=14, color=self.colors['text_secondary']),
                ft.Container(height=30),
                
                # Карточка похудение
                ft.Container(
                    content=ft.Stack([
                        # Картинка на всю карточку
                        ft.Container(
                            content=ft.Image(
                                src="/cut.png",
                                fit="cover",
                            ),
                            width=700,
                            height=140,
                        ),
                        # Текст поверх слева
                        ft.Container(
                            content=ft.Column([
                                ft.Text(
                                    self.t('weight_loss'),
                                    size=24,
                                    weight=ft.FontWeight.BOLD,
                                    color="white",
                                ),
                                ft.Text("🔥", size=36),
                            ], spacing=8),
                            padding=20,
                        ),
                    ]),
                    width=700,
                    height=140,
                    border_radius=16,
                    border=ft.border.all(3, "#10B981"),
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                    on_click=lambda e: self.select_goal("weight_loss"),
                    scale=1,
                    animate_scale=ft.Animation(150, ft.AnimationCurve.EASE_OUT),
                    on_hover=lambda e: self._on_card_hover(e),
                ),
                
                ft.Container(height=15),
                
                # Карточка набор массы
                ft.Container(
                    content=ft.Stack([
                        # Картинка на всю карточку
                        ft.Container(
                            content=ft.Image(
                                src="/bulk.avif",
                                fit="cover",
                            ),
                            width=700,
                            height=140,
                        ),
                        # Текст поверх слева
                        ft.Container(
                            content=ft.Column([
                                ft.Text(
                                    self.t('muscle_gain'),
                                    size=24,
                                    weight=ft.FontWeight.BOLD,
                                    color="white",
                                ),
                                ft.Text("💪", size=36),
                            ], spacing=8),
                            padding=20,
                        ),
                    ]),
                    width=700,
                    height=140,
                    border_radius=16,
                    border=ft.border.all(3, "#8B5CF6"),
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                    on_click=lambda e: self.select_goal("muscle_gain"),
                    scale=1,
                    animate_scale=ft.Animation(150, ft.AnimationCurve.EASE_OUT),
                    on_hover=lambda e: self._on_card_hover(e),
                ),
                
                ft.Container(height=25),
                
                # Кнопка назад
                ft.TextButton(
                    self.t('back_btn'),
                    on_click=lambda e: self.show_params()
                ),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=ft.Padding.symmetric(horizontal=20),
        )
        
        self.build_page(content)
    
    def select_goal(self, goal):
        self.user_data['goal'] = goal
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
                
                # Рекомендации
                ft.Container(
                    content=ft.Column([
                        ft.Text(self.t('nutrition_tips'), size=13, weight=ft.FontWeight.BOLD,
                               color=self.colors['text']),
                        ft.Text(self.t('tip1'), size=11, color=self.colors['text_secondary']),
                        ft.Text(self.t('tip2'), size=11, color=self.colors['text_secondary']),
                        ft.Text(self.t('tip3'), size=11, color=self.colors['text_secondary']),
                        ft.Text(self.t('tip4'), size=11, color=self.colors['text_secondary']),
                        ft.Text(self.t('tip5'), size=11, color=self.colors['text_secondary']),
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
    
    def calculate_nutrition(self):
        gender = self.user_data.get('gender', 'male')
        age = self.user_data.get('age', 25)
        weight = self.user_data.get('weight', 70)
        height = self.user_data.get('height', 175)
        goal = self.user_data.get('goal', 'weight_loss')
        days = self.user_data.get('days', 3)
        
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
        else:
            calories = int(tdee + 300)
            protein = int(weight * 2.0)
            fat = int(weight * 1.0)
        
        protein_cal = protein * 4
        fat_cal = fat * 9
        carbs_cal = calories - protein_cal - fat_cal
        carbs = int(carbs_cal / 4)
        
        nutrition = {
            'calories': calories,
            'protein': protein,
            'fat': fat,
            'carbs': carbs,
            'tdee': tdee,
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
        
        recs = {}
        
        if goal == 'weight_loss':
            recs['cardio'] = self.t('rec_cardio_weight_loss')
            recs['nutrition'] = self.t('rec_nutrition_weight_loss')
        else:
            recs['cardio'] = self.t('rec_cardio_muscle')
            recs['nutrition'] = self.t('rec_nutrition_muscle')
        
        rest_count = 7 - days
        recs['rest_days'] = self.t('rec_rest_days').replace('{count}', str(rest_count))
        
        if level == 'beginner':
            recs['duration'] = self.t('rec_duration_beginner')
        elif level == 'intermediate':
            recs['duration'] = self.t('rec_duration_intermediate')
        else:
            recs['duration'] = self.t('rec_duration_advanced')
        
        recs['progression'] = self.t('rec_progression')
        recs['measurements'] = self.t('rec_measurements')
        recs['warmup'] = self.t('rec_warmup')
        
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
        
        # Карточка рекомендаций
        rec_items = []
        if recs.get('cardio'):
            rec_items.append(ft.Text(f"🏃 {recs['cardio']}", size=9, color=self.colors['text_secondary']))
        if recs.get('rest_days'):
            rec_items.append(ft.Text(f"😌 {recs['rest_days']}", size=9, color=self.colors['text_secondary']))
        if recs.get('duration'):
            rec_items.append(ft.Text(f"⏱️ {recs['duration']}", size=9, color=self.colors['text_secondary']))
        if recs.get('nutrition'):
            rec_items.append(ft.Text(f"🍎 {recs['nutrition']}", size=9, color=self.colors['text_secondary']))
        if recs.get('warmup'):
            rec_items.append(ft.Text(f"🔥 {recs['warmup']}", size=9, color=self.colors['text_secondary']))
        
        rec_card = ft.Container(
            content=ft.Column([
                ft.Text(self.t('rec_title'), size=14, weight=ft.FontWeight.BOLD,
                       color=self.colors['primary']),
                ft.Container(height=5),
                *rec_items,
            ], spacing=3),
            padding=14,
            border_radius=12,
            bgcolor=self.colors['bg_card'],
            width=800,
        )
        
        # Карточка питания
        goal_emoji = "📉" if meta['goal'] == 'weight_loss' else "📈"
        nutrition_card = ft.Container(
            content=ft.Column([
                ft.Text(self.t('nutrition_title'), size=14, weight=ft.FontWeight.BOLD,
                       color=self.colors['primary']),
                ft.Row([
                    ft.Text(goal_emoji, size=20),
                    ft.Text(f"{goal_text}: {nutrition.get('calories', 0)} {self.t('kcal_day').replace('ККАЛ/ДЕНЬ', 'ккал/день').replace('KCAL/DAY', 'kcal/day')}",
                           size=13, weight=ft.FontWeight.BOLD, color=self.colors['text']),
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=5),
                ft.Row([
                    ft.Text(f"🥩 {nutrition.get('protein', 0)}{self.t('g')}", size=11, color=self.colors['text_secondary']),
                    ft.Text(f"🥑 {nutrition.get('fat', 0)}{self.t('g')}", size=11, color=self.colors['text_secondary']),
                    ft.Text(f"🍞 {nutrition.get('carbs', 0)}{self.t('g')}", size=11, color=self.colors['text_secondary']),
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=15),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
            padding=14,
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
        
        # Кнопки внизу
        bottom_buttons = ft.Row([
            ft.ElevatedButton(
                self.t('save_program'),
                bgcolor=self.colors['primary'],
                color="white",
                height=38,
                width=120,
                style=ft.ButtonStyle(text_style=ft.TextStyle(size=12)),
                on_click=lambda e: self.save_program()
            ),
            ft.ElevatedButton(
                self.t('diary'),
                bgcolor=self.colors['secondary'],
                color="white",
                height=38,
                width=120,
                style=ft.ButtonStyle(text_style=ft.TextStyle(size=12)),
                on_click=lambda e: self.show_diary()
            ),
            ft.ElevatedButton(
                self.t('new_program'),
                bgcolor=self.colors['warning'],
                color="white",
                height=38,
                width=120,
                style=ft.ButtonStyle(text_style=ft.TextStyle(size=12)),
                on_click=lambda e: self.show_welcome()
            ),
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=10)
        
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
                  bottom_buttons,
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
                
                # Кнопка пропуска отдыха
                ft.Container(
                    content=ft.Text(f"⏭️ {self.t('skip_rest')}", size=14,
                                   weight=ft.FontWeight.BOLD, color="white"),
                    padding=ft.Padding(left=40, right=40, top=12, bottom=12),
                    border_radius=25,
                    bgcolor=self.colors['warning'],
                    on_click=lambda e: self.skip_rest(),
                ),
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
    
    def complete_set_with_rest(self):
        cw = self.current_workout
        ex = cw['day_data']['exercises'][cw['current_exercise']]
        
        cw['completed_sets'] += 1
        cw['current_set'] += 1
        
        if cw['current_set'] > ex['sets']:
            # Переходим к следующему упражнению
            cw['current_exercise'] += 1
            cw['current_set'] = 1
            
            # Проверяем есть ли ещё упражнения
            if cw['current_exercise'] < len(cw['day_data']['exercises']):
                next_ex = cw['day_data']['exercises'][cw['current_exercise']]
                # Отдых между упражнениями (побольше)
                self.show_rest_screen(ex['rest_seconds'] + 10, next_ex)
            else:
                self.complete_workout()
        else:
            # Отдых между подходами
            self.show_rest_screen(ex['rest_seconds'], ex)
    
    def skip_exercise_with_rest(self):
        cw = self.current_workout
        cw['skipped_exercises'] = cw.get('skipped_exercises', 0) + 1
        cw['current_exercise'] += 1
        cw['current_set'] = 1
        
        if cw['current_exercise'] < len(cw['day_data']['exercises']):
            next_ex = cw['day_data']['exercises'][cw['current_exercise']]
            self.show_rest_screen(10, next_ex)  # Короткий отдых при пропуске
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
                
                ex_names = [self.t(ex['name']) for ex in log.get('exercises', [])]
                ex_list_text = ", ".join(ex_names[:5])
                if len(ex_names) > 5:
                    ex_list_text += f" +{len(ex_names) - 5}"
                
                if skipped > 0:
                    skip_text = f"⚠️ {self.t('diary_skipped_ex')}: {skipped}"
                    skip_color = self.colors['warning']
                else:
                    skip_text = f"✅ {self.t('diary_no_skipped')}"
                    skip_color = self.colors['success']
                
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
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2),
                                bgcolor=self.colors['bg_hover'], border_radius=10, padding=8, width=70,
                            ),
                            ft.Container(
                                content=ft.Column([
                                    ft.Text("✅", size=16),
                                    ft.Text(f"{log.get('completed_sets', 0)}", size=14,
                                           weight=ft.FontWeight.BOLD, color=self.colors['success']),
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2),
                                bgcolor=self.colors['bg_hover'], border_radius=10, padding=8, width=70,
                            ),
                            ft.Container(
                                content=ft.Column([
                                    ft.Text("🎯", size=16),
                                    ft.Text(f"{completed_ex}/{total_ex}", size=14,
                                           weight=ft.FontWeight.BOLD, color=self.colors['text']),
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2),
                                bgcolor=self.colors['bg_hover'], border_radius=10, padding=8, width=70,
                            ),
                        ], alignment=ft.MainAxisAlignment.CENTER, spacing=8),
                        ft.Container(height=4),
                        ft.Text(f"📋 {self.t('diary_exercises_list')}: {ex_list_text}",
                               size=10, color=self.colors['text_secondary'], max_lines=2,
                               overflow=ft.TextOverflow.ELLIPSIS),
                        ft.Text(skip_text, size=10, color=skip_color),
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
            lines.append(f'{self.t("created") if "created" in LOCALES.get(self.lang, {}) else "Дата"}: {meta.get("created", "")}')
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
