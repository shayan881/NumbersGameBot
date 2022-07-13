from pyrogram import Client
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup,
                            CallbackQuery)
from random import randint
from .datatype import _Gamers

import logging
import logging.config as lg

lg.fileConfig('plugins/Cls/file.conf')
logger = logging.getLogger('Pyro')

class NumbersGame:
    def __init__(
        self,
        client:Client,
        message:CallbackQuery
    ):
        
        self.client = client
        self.message = message
        self.step = 0
        self.number:int = None
    
    async def Start(self):

        """To start the game"""

        try:
            await self.SetNumber()
        except Exception:
            logger.error('Error : ', exc_info=True)
    
    async def SetNumber(self):

        """To record the number"""

        try:
            self.number = randint(1, 10)
            await self.SendButtons()
        except Exception:
            logger.error('Error : ' , exc_info=True)
    
    async def ChekAsnwer(
        self,
        answer,
        queryid
    ):

        """To check the answer"""
        
        try:
            self.step += 1
            answer = int(answer)


            if self.number == answer:
                await self.client.answer_callback_query(queryid, 'جواب درست بود')
                await self.GamerOver('برنده')
            elif  self.step == 3:
                await self.GamerOver('بازنده')

            else:
                response = await self.Comparison(answer)
                await self.client.answer_callback_query(queryid,
                 """❌ جواب اشتباه بود دوباره امتحان کنید ❌ 
                 مرحله : %s 

                 %s
                 """ % (self.step, response), show_alert=True)
        except Exception:
            logger.error('Error : ', exc_info=True)

    async def Comparison(self, num)-> str:

        """Comparing the number of the robot with the number of the user"""

        try:
            if num > self.number:
                answer = 'عدد ربات از عدد شما کوچک تر است'
            else:
                answer = 'عدد ربات از عدد شما بزرگ تر است'
            return answer
        except Exception:
            logger.error('Error : ', exc_info=True)

    async def SendButtons(self):

        """To send buttons"""

        try:
            await self.message.edit_message_text(
                """
                ❓ ربات یه عدد در نظر گرفته است عدد را با دکمه هار زیر حدث بزنید ❓
                """ ,
                reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                    [
                        InlineKeyboardButton('1️⃣', '1'),
                        InlineKeyboardButton('2️⃣', '2'),
                        InlineKeyboardButton('3️⃣', '3'),
                        InlineKeyboardButton('4️⃣', '4'),
                        InlineKeyboardButton('5️⃣', '5')
                    ],
                    [
                        InlineKeyboardButton('6️⃣', '6'),
                        InlineKeyboardButton('7️⃣', '7'),
                        InlineKeyboardButton('8️⃣', '8'),
                        InlineKeyboardButton('9️⃣', '9'),
                        InlineKeyboardButton('🔟', '10')
                    ],
                    [
                        InlineKeyboardButton('Back', 'Back')
                    ]
                ])
            )
        except Exception:
            logger.error('Error : ', exc_info=True)
    
    async def GamerOver(self, status):

        """Finish the game"""

        try:
            await self.message.edit_message_text('بازی تمام شد شما %s شدید جواب : %s' % (status, self.number))
            await _Gamers.Remove(self.message.from_user.id)
        except Exception:
            logger.error('Error : ', exc_info=True )