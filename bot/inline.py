from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


anime2022_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Spy Family", callback_data="spy_family", url="")],
        [InlineKeyboardButton(text="Bocchi the rock!", callback_data="bocchi_the_rock", url="")],
        [InlineKeyboardButton(text="Date a live", callback_data="date_a_live", url="")]
    ]
)


anime2023_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Oshi no ko", callback_data="oshi_no_ko", url="")],
        [InlineKeyboardButton(text="Horimiya", callback_data="horimiya", url="")],
        [InlineKeyboardButton(text="Rent-a-girlfriend", callback_data="rent_a_girlfriend", url="")],
    ]
)


anime2024_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Low-tier character Tomozaki kun", url="", callback_data="tomozaki")],
        [InlineKeyboardButton(text="Classroom of the elite", url="", callback_data="cote")],
        [InlineKeyboardButton(text="Alya sometimes hides her feelings in russian", url="", callback_data="alya_russian")]
    ]
)

rate_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="❤️", callback_data="like", url=""), InlineKeyboardButton(text="👎",
                                                                                             callback_data="dislike",
                                                                                             url="")]
    ]
)