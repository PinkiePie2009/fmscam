import tkinter as tk
from tkinter import font
import os
from PIL import Image, ImageTk, ImageDraw
def ensure_images_exist():
    if not os.path.exists("images"):
        os.makedirs("images")
    story_images = {
        "roblox.jpg": ("#1E90FF", "ЧАТ В ИГРЕ"),
        "telegram.jpg": ("#0088cc", "СООБЩЕНИЕ В МЕССЕНДЖЕРЕ"),
        "avito.jpg": ("#9370DB", "МАРКЕТПЛЕЙС Б/У ТЕХНИКИ"),
        "olympiad.jpg": ("#2E8B57", "ПИСЬМО: ОЛИМПИАДА"),
        "eljur.jpg": ("#FF8C00", "УВЕДОМЛЕНИЕ ЭЛЖУР"),
        "sms.jpg": ("#808080", "SMS ОТ 'РАБОТОДАТЕЛЯ'"),
        "call.jpg": ("#B22222", "ВХОДЯЩИЙ ЗВОНОК"),
        "success.jpg": ("#32CD32", "УСПЕХ!"),
        "fail.jpg": ("#DC143C", "ПРОВАЛ...")
    }
    menu_portraits = {
        "child.jpg": ("#FFB6C1", "ДЕТИ"),
        "teen.jpg": ("#87CEFA", "ПОДРОСТОК"),
        "adult.jpg": ("#98FB98", "ВЗРОСЛЫЙ"),
        "senior.jpg": ("#DDA0DD", "ПЕНСИОНЕР")
    }
    for filename, (color, text) in story_images.items():
        filepath = os.path.join("images", filename)
        if not os.path.exists(filepath):
            img = Image.new('RGB', (800, 400), color=color)
            d = ImageDraw.Draw(img)
            d.text((350, 180), text, fill="white")
            img.save(filepath)
    for filename, (color, text) in menu_portraits.items():
        filepath = os.path.join("images", filename)
        if not os.path.exists(filepath):
            img = Image.new('RGB', (200, 400), color=color)
            d = ImageDraw.Draw(img)
            d.text((60, 200), text, fill="black")
            img.save(filepath)
STORY_GRAPH = {
    "start": {
        "type": "menu",
        "text": "Выберите вашего персонажа:",
        "choices": [
            ("Дети", "child.jpg", "child_start"),
            ("Подросток", "teen.jpg", "teen_hub"),
            ("Взрослый", "adult.jpg", "adult_start"),
            ("Пенсионер", "senior.jpg", "senior_start")
        ]
    },
    "child_start": {
        "image": "roblox.jpg",
        "text": "[ROBLOX CHAT]\nAdmin6742: Раздаю бесплатные робуксы! Перейди по ссылке на сайт и авторизуйся.",
        "choices": [
            ("Перейти по ссылке", "child_bad"),
            ("Кинуть репорт", "child_good")
        ]
    },
    "child_bad": {
        "image": "fail.jpg",
        "text": "ФИНАЛ: Ваш аккаунт угнан.\n\nЗакон РФ: Действия мошенника квалифицируются по ст. 272 УК РФ (Неправомерный доступ к компьютерной информации) и ст. 159.6 УК РФ (Мошенничество в сфере компьютерной информации).",
        "choices": [("В главное меню", "start")]
    },
    "child_good": {
        "image": "success.jpg",
        "text": "ФИНАЛ: Аккаунт в безопасности.\n\nЗакон РФ: Вы предотвратили покушение на преступление (ст. 30 УК РФ).",
        "choices": [("В главное меню", "start")]
    },
    "teen_hub": {
        "image": "start.jpg",
        "text": "Выберите ситуацию:",
        "choices": [
            ("Предложение 'быстрого заработка' в сети", "teen_job"),
            ("Покупка б/у планшета с рук", "teen_market"),
            ("Приглашение в олимпиадную школу", "teen_olympiad")
        ]
    },
    "teen_job": {
        "image": "telegram.jpg",
        "text": "Неизвестный: Привет! Нужно получать переводы на свою карту и отправлять их дальше. Твой процент - 10%.",
        "choices": [
            ("Согласиться", "teen_job_bad"),
            ("Проигнорировать", "teen_job_good")
        ]
    },
    "teen_job_bad": {
        "image": "fail.jpg",
        "text": "ФИНАЛ: Вы стали «дропом».\n\nЗакон РФ: Банк блокирует карту по 115-ФЗ (Противодействие отмыванию доходов). Вам может грозить ответственность по ст. 187 УК РФ (Неправомерный оборот средств платежей) и ст. 174 УК РФ.",
        "choices": [("В главное меню", "start")]
    },
    "teen_job_good": {
        "image": "success.jpg",
        "text": "ФИНАЛ: Успех! Вы не ввязались в криминал.",
        "choices": [("В главное меню", "start")]
    },
    "teen_market": {
        "image": "avito.jpg",
        "text": "Вы нашли б/у планшет по очень вкусной цене. Продавец просит перейти в мессенджер и кидает ссылку на 'безопасную доставку', где нужно ввести данные карты для 'заморозки' средств.",
        "choices": [
            ("Ввести данные карты по ссылке", "teen_market_bad"),
            ("Оформлять сделку только внутри приложения", "teen_market_good")
        ]
    },
    "teen_market_bad": {
        "image": "fail.jpg",
        "text": "ФИНАЛ: Деньги списались, продавец пропал.\n\nЗакон РФ: Это классическая схема фишинга. Квалифицируется по ст. 159 УК РФ (Мошенничество). Вернуть деньги через банк практически невозможно, так как вы сами ввели код подтверждения.",
        "choices": [("В главное меню", "start")]
    },
    "teen_market_good": {
        "image": "success.jpg",
        "text": "ФИНАЛ: Успех! Продавец-мошенник слился, ваши деньги целы.",
        "choices": [("В главное меню", "start")]
    },
    "teen_olympiad": {
        "image": "olympiad.jpg",
        "text": "На почту пришло письмо: 'Поздравляем! Вы прошли на летнюю школу олимпиадной подготовки по программированию. Оплатите оргвзнос 5000 руб. по ссылке ниже до конца дня'.",
        "choices": [
            ("Срочно оплатить", "teen_olympiad_bad"),
            ("Найти списки зачисленных на официальном сайте", "teen_olympiad_good")
        ]
    },
    "teen_olympiad_bad": {
        "image": "fail.jpg",
        "text": "ФИНАЛ: Данные карты украдены.\n\nЗакон РФ: Злоумышленники подделали рассылку (ст. 159.6 УК РФ). Организаторы настоящих олимпиад никогда не требуют срочной оплаты через сомнительные ссылки в письмах.",
        "choices": [("В главное меню", "start")]
    },
    "teen_olympiad_good": {
        "image": "success.jpg",
        "text": "ФИНАЛ: На официальном сайте вашей фамилии пока нет, а письмо оказалось скамом. Деньги сохранены.",
        "choices": [("В главное меню", "start")]
    },
    "adult_start": {
        "image": "start.jpg",
        "text": "Выберите угрозу:",
        "choices": [
            ("Сообщение от школы", "adult_kids"),
            ("Смс с вакансией", "adult_nokids")
        ]
    },
    "adult_kids": {
        "image": "eljur.jpg",
        "text": "[ЭЛЖУР] Ваш пароль скомпрометирован! Срочно подтвердите личность через Госуслуги по ссылке.",
        "choices": [
            ("Перейти и ввести данные", "adult_kids_bad"),
            ("Зайти через приложение", "adult_kids_good")
        ]
    },
    "adult_kids_bad": {
        "image": "fail.jpg",
        "text": "ФИНАЛ: Кража личности.\n\nЗакон РФ: На вас оформили микрозаймы. Мошенники нарушили ст. 272 УК РФ (Неправомерный доступ) и ст. 159.1 УК РФ (Мошенничество в сфере кредитования). Доказывать свою непричастность придется через суд.",
        "choices": [("В главное меню", "start")]
    },
    "adult_kids_good": {
        "image": "success.jpg",
        "text": "ФИНАЛ: Успех! Данные в безопасности.",
        "choices": [("В главное меню", "start")]
    },
    "adult_nokids": {
        "image": "sms.jpg",
        "text": "[SMS] Вы прошли отбор на удаленку! ЗП от 150к. Перейдите по ссылке и заполните реквизиты карты.",
        "choices": [
            ("Заполнить анкету", "adult_nokids_bad"),
            ("Удалить SMS", "adult_nokids_good")
        ]
    },
    "adult_nokids_bad": {
        "image": "fail.jpg",
        "text": "ФИНАЛ: С карты списаны средства.\n\nЗакон РФ: Нарушение ст. 158 ч.3 п.г УК РФ (Кража с банковского счета). В отличие от обычного мошенничества, это тяжкое преступление, но найти виновных за границей крайне сложно.",
        "choices": [("В главное меню", "start")]
    },
    "adult_nokids_good": {
        "image": "success.jpg",
        "text": "ФИНАЛ: Успех! Финансы сохранены.",
        "choices": [("В главное меню", "start")]
    },
    "senior_start": {
        "image": "call.jpg",
        "text": "[ВХОДЯЩИЙ ЗВОНОК] 'На вас оформляется кредит! Чтобы отменить операцию, продиктуйте код из SMS'.",
        "choices": [
            ("Продиктовать код", "senior_bad"),
            ("Сбросить вызов", "senior_good")
        ]
    },
    "senior_bad": {
        "image": "fail.jpg",
        "text": "ФИНАЛ: Вишинг сработал.\n\nЗакон РФ: Ст. 159 УК РФ (Мошенничество). Так как клиент сам передал код подтверждения (простая электронная подпись по 63-ФЗ), банк имеет право требовать выплату кредита по договору.",
        "choices": [("В главное меню", "start")]
    },
    "senior_good": {
        "image": "success.jpg",
        "text": "ФИНАЛ: Успех! Кредитов нет, мошенники ни с чем.",
        "choices": [("В главное меню", "start")]
    }
}
class VisualNovelApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FM(not)SCAM")
        self.geometry("850x650")
        self.configure(bg="#1e1e1e")
        self.resizable(False, False)
        ensure_images_exist()
        self.text_font = font.Font(family="Helvetica", size=14)
        self.btn_font = font.Font(family="Helvetica", size=12, weight="bold")
        self.current_images = []
        self.render_node("start")
    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.current_images.clear()
    def render_node(self, node_id):
        node = STORY_GRAPH.get(node_id)
        if not node: return
        self.clear_screen()
        if node.get("type") == "menu":
            self.render_menu_screen(node)
        else:
            self.render_story_screen(node)
    def render_menu_screen(self, node):
        title = tk.Label(self, text=node["text"], font=self.text_font, bg="#1e1e1e", fg="#ffffff")
        title.pack(pady=30)
        container = tk.Frame(self, bg="#1e1e1e")
        container.pack(expand=True, fill="both", padx=20, pady=10)
        for choice_text, img_file, next_node_id in node["choices"]:
            col = tk.Frame(container, bg="#2b2b2b", bd=2, relief="groove")
            col.pack(side="left", expand=True, fill="both", padx=10, pady=20)
            img_path = os.path.join("images", img_file)
            if os.path.exists(img_path):
                img = Image.open(img_path)
                img = img.resize((170, 350), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                self.current_images.append(photo)
                img_btn = tk.Button(col, image=photo, bg="#2b2b2b", relief="flat", cursor="hand2",
                                    command=lambda n_id=next_node_id: self.render_node(n_id))
                img_btn.pack(expand=True, pady=10)
            btn = tk.Button(
                col, text=choice_text, font=self.btn_font,
                bg="#4a4a4a", fg="#ffffff", activebackground="#6b6b6b", activeforeground="#ffffff",
                relief="flat", pady=10, cursor="hand2",
                command=lambda n_id=next_node_id: self.render_node(n_id)
            )
            btn.pack(fill="x", side="bottom", padx=10, pady=10)
    def render_story_screen(self, node):
        img_path = os.path.join("images", node.get("image", "fail.jpg"))
        if os.path.exists(img_path):
            img = Image.open(img_path)
            img = img.resize((760, 350), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            self.current_images.append(photo)

            img_label = tk.Label(self, image=photo, bg="#1e1e1e")
            img_label.pack(pady=15)
        text_frame = tk.Frame(self, bg="#2b2b2b", bd=2, relief="groove")
        text_frame.pack(fill="x", padx=20, pady=5)
        story_label = tk.Label(
            text_frame, text=node["text"], font=self.text_font,
            bg="#2b2b2b", fg="#ffffff", wraplength=760, justify="left", padx=15, pady=15
        )
        story_label.pack(expand=True, fill="both")
        buttons_frame = tk.Frame(self, bg="#1e1e1e")
        buttons_frame.pack(fill="x", padx=40, pady=10)
        for choice_text, next_node_id in node["choices"]:
            btn = tk.Button(
                buttons_frame, text=choice_text, font=self.btn_font,
                bg="#4a4a4a", fg="#ffffff", activebackground="#6b6b6b", activeforeground="#ffffff",
                relief="flat", pady=8, cursor="hand2",
                command=lambda n_id=next_node_id: self.render_node(n_id)
            )
            btn.pack(fill="x", pady=5)

app = VisualNovelApp()
app.mainloop()