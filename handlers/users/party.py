from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp


@dp.message_handler(text="Ближайшая туса")
async def info(message: types.Message):
    await message.answer("*02.01.2022 17:00 - 03.01.2022 13:00*", parse_mode= "Markdown")

@dp.message_handler(text="Правила мероприятия")
async def info(message: types.Message):
    await message.answer("1.ПРОНОСИТЬ СВОЙ АЛКОГОЛЬ( хотите выпить пейте в коттедже или до него)\n"
"\n2.НАРКОТИЧЕСКИЕ ВЕЩЕСТВА НЕ ПРИВЕТСТВУЮТСЯ( если есть необходимость, делайте все до того как войдёте в дом)\n"
"\n3.ОПЛАТА ПРОВОДИТСЯ ЗА ДВЕ НЕДЕЛИ ДО ТУСОВКИ\n"
"\n4.ЛИЧНЫЕ ВЕЩИ ДОЛЖНЫ БЫТЬ ПРИ ВАС(АДМИНЫ ОТВЕТСТВЕННОСТИ НЕ НЕСУТ)\n"
"\n5.НЕ УСУГУБЛЯТЬ СИТУАЦИЮ, ЕСЛИ У ВАС НЕТ ВОЗМОЖНОСТИ ПОСЕТИТЬ МЕРОПРИЯТИЕ(взрослые там не нужны)\n"
"\n6.ПРЕДУПРЕЖДАЙТЕ АДМИНОВ ЗАРАНЕЕ ПРИ НАЛИЧИИ КАКИХ-ТО ИЗМЕНЕНИЙ\n"
"\n7.ЗАПРЕЩАЕТСЯ ПРОНОСИТЬ ОРУЖИЕ, СРЕДСТВО САМОЗАЩИТЫ, ОСТРЫЕ ПРЕДМЕТЫ И ТЕ ВЕЩИ КОТОРЫЕ МОГУТ НАВРЕДИТЬ НЕ ТОЛЬКО ВАМ, НО И ДРУГИМ ЛЮДЯМ.\n"
"\n8.ПРИ НЕ СОБЛЮДЕНИИ ПРАВИЛ ИЛИ ПОРЧЕ ИМУЩЕСТВА ПОЛНОСТЬЮ ВСЯ ОТВЕТСТВЕННОСТЬ ЛЕЖИТ НА ВАС.\n"
"\n9.В КАЖДОМ ДОМЕ СВОИ ПРАВИЛА, АДМИНЫ ОГЛАШАЮТ ИХ ЗАРАНЕЕ\n"
"\n10.Просим вас указывать ТОЛЬКО реальные данные в личном кабинете бота. Если вы ввели ФИО с ошибкой, то помощь - вам будет отказана.\n"
"\nПросьба:\n"
"Не создавать конфликт и прислушиваться.\n"
"\nСПАСИБО ЗА ВНИМАНИЕ!\nБудем рады вас видеть!"
"\nЕсли вы состоите в каналах Royal Party, то вы ознакомлены с правилами.")