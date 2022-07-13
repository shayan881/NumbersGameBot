from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup,
                            CallbackQuery,
                            Message)
                            
from plugins.Cls.game import NumbersGame, _Gamers



@Client.on_message(filters.command('start'))
async def On_Message(client, message:Message):
    await message.reply_text(
        'برای شروع بازی روی دکمه **Start** بزنید',
        quote=True,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton('Start', 'Start'),
                InlineKeyboardButton('About game', 'About')
            ]
        ])
    )



@Client.on_callback_query()
async def On_Callback_Query(client:Client, message:CallbackQuery):
    userid = message.from_user.id
    data = message.data

    if data == 'Start':
        Game = NumbersGame(client, message)
        await _Gamers.Add(userid, Game)
        await Game.Start()

    if data in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        Game:NumbersGame = await _Gamers.Get(userid)
        if Game:
            await Game.ChekAsnwer(data, message.id)
        else:
            await message.edit_message_text(
                '❗️ بازی قبلا تمام شده❗️'
            )
    
    if data == 'Back':
        await message.edit_message_text(
            'برای شروع بازی روی /start بزنید'
        )

    if data == 'About':
        await message.edit_message_text(
            """
            📌 آموزش


            🖋 در این بازی ربات یک عدد در نظر میگیره که
            شما باید اون عدد رو حدث بزنی و فقط ۳ شانس  
            دارید و اگر عددی که حدث زدید کوچک تر یا بزرگتر
            از عدد ربات باشه ربات بهتون میگه تا شانس بیشتری 
            واسه حدث عدد داشته باشید""", 
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton('Back', 'Back')
                ]
            ])
        )

