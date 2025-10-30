import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import time
# Инициализация состояния для текущей страницы
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'main'

# Функции для смены страниц
def show_main(): st.session_state.current_page = 'main'
def show_materials(): st.session_state.current_page = 'materials'
def show_tasks(): st.session_state.current_page = 'tasks'
def show_progress(): st.session_state.current_page = 'progress'
def show_settings(): st.session_state.current_page = 'settings'

def check_secret_code(code):
    return code == 907561499

def check_secret_code_teacher(code):
    return check_secret_code(code)
    
def check_secret_code_parent(code):
    return check_secret_code(code)

# Функция для закрытия приложения
def close_app():
    st.session_state.registered = False
    st.session_state.current_page = 'main'
    st.rerun()

# Регистрация
if 'registered' not in st.session_state:
    st.session_state.registered = False

if not st.session_state.registered:
    st.title("Регистрация")

    user = st.text_input("Введите имя", help="Имя не должно быть пустым.", placeholder="Ваше имя на русском языке")
    roli = st.selectbox("Выберете роль", ["Ученик", "Учитель", "Родитель"], help="Выбирите кто вы, это важно для дальнейшей регистрации")

    go = False
    code_correct = False

    if roli == "Ученик":
        age = st.slider("Выберете возраст", 6, 18)
        clas = st.selectbox("Выберете класс", ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"])
        code_correct = True
        go = st.button("Зарегестрироваться как ученик")   

    if roli == "Учитель":
        p = st.number_input("Введите код учителя", value=0)
        code_correct = check_secret_code_teacher(p)
        go = st.button("Зарегестрироваться как учитель")
        
    if roli == "Родитель":
        p = st.number_input("Введите код Родителя", value=0)
        code_correct = check_secret_code_parent(p)
        go = st.button("Зарегестрироваться как родитель")
        
    if go:
        if user != "" and code_correct:
            st.success("Вы успешно зарегитрированны!")
            st.session_state.registered = True
            st.rerun()
        else:
            if user == "":
                st.error("Имя не может быть пустым. Попробуйте еще раз.")
            if not code_correct:
                st.error("Неверный код. Попробуйте еще раз.")
        x = user

else:
    # Отображение текущей страницы
    if st.session_state.current_page == 'main':
        st.title("Добро пожаловать на Shcool.Gos.Yslugi")
        st.write("Это главная страница приложения - здесь отображается общая информация и новости")
        st.write("Shcool.Gos.Yslugi - это новая площадка для школьников, как сташих, так и для младших классов")
        st.title("Почему решили перенести на новую платформу?")
        st.write("Перенесли на новую платформу для удобства.Теперь вы можете смотреть: расписание, домашнее задание и оценки в одном месте")
        st.title("Что нового?")
        st.write("""1) Полявилась гибкая система настроек выставления оценок для учителей
                 
                 2) Удобно смотреть расписание и оценки, родителям проще узнавать всю школьную правду

                 3) Смотреть ДЗ стало гораздо легче, теперь можно без труда смотреть домашку за каждый предмет и не спрашивать в чате

                 4) Можно связяться на сайте с учтелями

                 5)Если что-то не понял на уроке, то встроенная нейросеть "Gos" поможет обЪяснить весь непонятый материал

                 """)

    elif st.session_state.current_page == 'materials':
        st.title("📚 Домашние задание ")
        
        # Добавляем состояние для отображения сообщения о бане
        if 'show_ban_message' not in st.session_state:
            st.session_state.show_ban_message = False
            
        if st.button("Загрузить домашнее задание") and not st.session_state.show_ban_message:
            st.session_state.show_ban_message = True
            st.rerun()
        
        if st.session_state.show_ban_message:
            my_bar = st.progress(10)
            
            
            for percent_complete in range(100):
                    time.sleep(0.1)
                    my_bar.progress(percent_complete + 1)
                    
                    
            s = st.error("🚫 ОШИБКА, ВЫ ЗАБАНЕНЫ!")
            st.write("К сожалению, у вас нет доступа к домашним заданиям.")
            st.write("Причина:  взлом системы и вы сидели за компьютером слишком долго ('28.10.2025')")
            st.stop()            

    elif st.session_state.current_page == 'tasks':
        st.title("Рассписание")
        rasspisanie = st.selectbox("Выберете день недели", ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"])
        if rasspisanie == "Понедельник":
            st.title("Понедельник")
            st.write("Химия")
            st.write("Розговоры о важном")
            st.write("Литература")
            st.write("Английский язык")
            st.write("Технология")
            st.write("Игровые виды спорта")
            st.write("Алгебра")
        elif rasspisanie == "Bторник":
            st.title("Вторник")
            st.write("Физкультура")
            st.write("Биология")
            st.write("Русский язык")
            st.write("Геометрия ")
            st.write("Физика")
            st.write("Музыка")
            st.write("ОБиЗР")
        elif rasspisanie == "Среда":
            st.title("Среда")
            st.write("Химия")
            st.write("Физкультура")
            st.write("География")
            st.write("Английския язык")
            st.write("Русский язык")
            st.write("Алгебра")
            st.write("История")
        elif rasspisanie == "Четверг":
            st.write("Физика")
            st.write("Английчкия язык")
            st.write("Информатика")
        elif rasspisanie == "Пятница":
            st.title("Пятница")
            st.write("Русский язык")
            st.write("-Нет--Урока-")
            st.write("Биология")
            st.write("Обществознание")
            st.write("История")
            st.write("География")
            st.write("Алгебра")
    elif st.session_state.current_page == 'progress':
        st.title("📊 Оценки")
        
        # Создаем данные для таблицы оценок
        data = {
            'Предмет': [
                'Математика', 'Русский язык', 'Литература', 'Английский язык',
                'Физика', 'Химия', 'Биология', 'История',
                'География', 'Обществознание', 'Информатика', 'Физкультура',
                'Музыка', 'ИЗО', 'Технология', 'ОБЖ'
            ],
            'Оценка за четверть': [4.8, 4.2, 4.7, 4.1, 3.8, 4.3, 4.6, 4.4, 4.5, 4.3, 4.7, 4.9, 4.2, 4.8, 4.1, 4.7],
            'Последняя оценка': [4, 2, 4, 4, 3, 3, 4, 4, 5, 4, 2, 4, 2, 4, 4, 4],
            'Средний балл': [4.8, 4.2, 4.7, 4.1, 3.8, 4.3, 4.6, 4.4, 4.5, 3.2, 4.7, 4.9, 4.2, 4.8, 4.1, 4.7]
        }
        
        df = pd.DataFrame(data)
        
        # Отображаем таблицу с оценками
        st.subheader("Таблица успеваемости")
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Предмет": st.column_config.TextColumn("Предмет", width="medium"),
                "Оценка за четверть": st.column_config.NumberColumn("Оценка за четверть", format="%d"),
                "Последняя оценка": st.column_config.NumberColumn("Последняя оценка", format="%d"),
                "Средний балл": st.column_config.NumberColumn("Средний балл", format="%.1f")
            }
        )
        
        # Дополнительная информация
        st.subheader("Статистика успеваемости")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Средний балл", "4.5")
        with col2:
            st.metric("Лучший предмет", "Математика")
        with col3:
            st.metric("Худший предмет", "Физика")
        
        # Визуализация оценок
        st.subheader("Визуализация оценок")
        fig, ax = plt.subplots(figsize=(10, 6))
        subjects = data['Предмет']
        grades = data['Оценка за четверть']
        
        bars = ax.barh(subjects, grades, color=['#FF6B6B' if x < 4 else '#4ECDC4' for x in grades])
        ax.set_xlabel('Оценка')
        ax.set_title('Оценки за четверть по предметам')
        ax.set_xlim(0, 5)
        
        # Добавляем значения на столбцы
        for bar, grade in zip(bars, grades):
            ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2, 
                   f'{grade}', ha='left', va='center')
        
        st.pyplot(fig)

    elif st.session_state.current_page == 'settings':
        st.title("⚙️ Настройки Профиля")
        st.write("Это окно настроек профиля")
        st.write("Роль - ученик")
        st.write("Класс - 8")
        st.write("Буква  - 'Б'")
    # Боковое меню для навигации
    with st.sidebar:
        st.header("Навигация")
        
        # Определяем текущую страницу для подсветки кнопки
        current_page = st.session_state.current_page
        
        if st.button("🏠 Главная Страница", 
                    use_container_width=True,
                    type="primary" if current_page == 'main' else "secondary"):
            show_main()
            st.rerun()
        if st.button("📚 Домашние задание ", 
                    use_container_width=True,
                    type="primary" if current_page == 'materials' else "secondary"):
            show_materials()
            st.rerun()
            
        if st.button("📝Рассписание", 
                    use_container_width=True,
                    type="primary" if current_page == 'tasks' else "secondary"):
            show_tasks()
            st.rerun()
            
        if st.button("📈 Оценки", 
                    use_container_width=True,
                    type="primary" if current_page == 'progress' else "secondary"):
            show_progress()
            st.rerun()
            
        if st.button("⚙️ Настройки Профиля", 
                    use_container_width=True,
                    type="primary" if current_page == 'settings' else "secondary"):
            show_settings()
            st.rerun()