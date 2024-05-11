from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

web_app = WebAppInfo(url="http://localhost:63342/modul_11.github.io/index.html?_ijt=get7ef4nv64nsd848olceoh24v")

app_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Mini app", web_app=web_app)]
], resize_keyboard=True)