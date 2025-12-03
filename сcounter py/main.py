import flet as ft
import time

def main(page: ft.Page):
    # --- Початкові налаштування ---
    page.title = "The Choice"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT 
    page.bgcolor = "white"
    page.window_width = 700
    page.window_height = 500

    # Стан системи
    is_matrix_mode = False

    # --- Стилі ---
    # Нудний стиль звичайної людини
    normal_style = ft.TextStyle(size=20, color="black", font_family="Arial")
    
    # Стиль обраного
    matrix_style = ft.TextStyle(
        font_family="Courier New", 
        color="#00FF00", 
        size=25, 
        weight=ft.FontWeight.BOLD,
        shadow=ft.BoxShadow(blur_radius=10, color="green")
    )

    # --- Елементи ---
    txt_number = ft.TextField(
        value="0", 
        text_align=ft.TextAlign.RIGHT, 
        width=100,
        text_style=normal_style,
        border_color="black",
        cursor_color="black"
    )
    
    console_text = ft.Text(value="", style=matrix_style)

    # --- Функція друку (БЛОКУЮЧА) ---
    def type_message_blocking(message, speed=0.1):
        console_text.value = ""
        console_text.visible = True
        console_text.style = matrix_style # Завжди пишемо зеленим
        page.update()
        
        for char in message:
            console_text.value += char
            page.update()
            time.sleep(speed) # Система "думає"

    # --- Логіка МІНУСА (Вхід у Матрицю) ---
    def minus_click(e):
        nonlocal is_matrix_mode
        
        current_val = int(txt_number.value) - 1
        txt_number.value = str(current_val)
        
        # Якщо перетнули межу і ще не в Матриці
        if current_val < 0 and not is_matrix_mode:
            is_matrix_mode = True
            
            # 1. Зміна декорацій
            page.bgcolor = "black"
            txt_number.text_style = matrix_style
            txt_number.border_color = "#00FF00"
            txt_number.cursor_color = "#00FF00"
            page.update()
            
            # 2. Класичний сценарій (інтерфейс висне)
            type_message_blocking("Wake up, Neo...", 0.15)
            time.sleep(1.5)
            
            type_message_blocking("The Matrix has you...", 0.15)
            time.sleep(1.5)
            
            type_message_blocking("Follow the white rabbit.", 0.1)
            time.sleep(1)
            
            console_text.value = "Knock, knock."
            page.update()

        else:
            page.update()

    # --- Логіка ПЛЮСА (Синя пігулка) ---
    def plus_click(e):
        nonlocal is_matrix_mode
        
        current_val = int(txt_number.value) + 1
        txt_number.value = str(current_val)
        
        # Якщо повернулися до світла (>= 0) і були в Матриці
        if current_val >= 0 and is_matrix_mode:
            
            # 1. Спочатку висловлюємо розчарування (поки ще чорний фон)
            type_message_blocking("You chose blue pill after all?", 0.1)
            time.sleep(1)
            type_message_blocking("How disappointing....", 0.2)
            time.sleep(2) # Довга пауза для драми
            
            # 2. Повернення в "нудну реальність"
            is_matrix_mode = False
            page.bgcolor = "white"
            
            # Скидаємо стилі текстового поля
            txt_number.text_style = normal_style
            txt_number.border_color = "black"
            txt_number.cursor_color = "black"
            
            # Очищуємо консоль
            console_text.value = ""
            page.update()
            
        else:
            page.update()

    # --- Кнопки ---
    # Робимо їх трохи стильнішими, щоб видно було на чорному
    btn_minus = ft.IconButton(
        icon="remove", 
        on_click=minus_click, 
        icon_color="red" # Червона пігулка?
    )
    btn_plus = ft.IconButton(
        icon="add", 
        on_click=plus_click, 
        icon_color="blue" # Синя пігулка
    )

    # --- Верстка ---
    page.add(
        ft.Column(
            [
                ft.Row(
                    [btn_minus, txt_number, btn_plus],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Container(height=20), # Відступ
                ft.Container(
                    content=console_text, 
                    padding=20,
                    alignment=ft.alignment.center # Текст по центру
                ) 
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)