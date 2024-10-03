class Button():
    def __init__(self, title_text, x_num, y_num):
        self.title = title_text
        self.x = x_num
        self.y = y_num
        self.appearance = True
    def hide(self):
        self.appearance = False
        print(self.title, '- приховано')
    def show(self):
        self.appearance = True
        print(self.title, '- відображається')
    def print_status(self):
        print(f'Кнопка: {self.title}\n Розташування: ({self.x}, {self.y})\nВидимість: {self.appearance}')
       
bA1 = Button('Дізнатися переможця прямо зараз!', 150, 50)
bA2 = Button('Переможець може бути тільки один', 150, -100)
bA1.print_status()
bA2.print_status()
bA2.hide()
