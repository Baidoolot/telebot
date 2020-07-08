from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram.utils.exceptions import MessageTextIsEmpty
from peewee import DoesNotExist 

from misc import dp
from db.models import *
import keyboards


class Univer(StatesGroup):
    univer = State()
    faculty = State()
    specialty = State()
    contacts = State()
    ort = State()


@dp.message_handler(commands=['start'], state = '*')
async def process_start_command(message: types.Message):
    await message.answer('Привет, я помогу тебе поступить.)', reply_markup=keyboards.menu())
    await Univer.faculty.set()
    await Univer.univer.set()


@dp.message_handler(state=Univer.univer, content_types=types.ContentTypes.ANY)
async def menu(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Поиск универиситета':
            await message.answer('Выбери город куда хочешь поступить', reply_markup=keyboards.city())
            await Univer.univer.set()        
        elif message.text == 'Меню':
            await message.answer('menu', reply_markup=keyboards.menu())
        elif message.text == 'Поиск факультета':
            await message.answer('Отправьте ID университета факультеты которой вы хотите увидеть')
            await Univer.faculty.set()
        elif message.text == 'Поиск специальности':
            await message.answer('Отправьте ID факультета специальность которой вы хотите найти')
            await Univer.specialty.set()
        elif message.text == 'Контакты':
            await message.answer('Отправьте ID университета контакты которой вы хотите получить')
            await Univer.contacts.set()
        elif message.text == 'Предметы для ОРТ':
            await message.answer('Отправьте ID факультета для получения инофмации об ОРТ.')
            await Univer.ort.set()
        

        table = University.select().where(University.city == message.text)
        id_ = None
        title = None
        text1 = []
        for x in table:
            id_ = x.id
            title = x.title
            text = f'{id_}. {title}'
            text1.append(text)
        await message.answer('\n'.join(text1))
   
    except MessageTextIsEmpty:
        pass




@dp.message_handler(state=Univer.faculty, content_types=types.ContentTypes.ANY)
async def search_faculty(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Поиск факультета':
            await message.answer('Отправьте id университета факультеты которой вы хотите увидеть')        
        univer = University.get(id=message.text)
        faculties = univer.faculties
        text = []
        for x in faculties:
            text1 = f'{x.id}. {x.title}'
            text.append(text1)
        await message.answer('\n'.join(text))
        await Univer.faculty.set()
    except DoesNotExist:
        await Univer.univer.set()
        return await message.answer('Попробуйте ещё раз.')
    except MessageTextIsEmpty:
        return await message.answer('Попробуйте ещё раз.')

@dp.message_handler(state=Univer.specialty, content_types=types.ContentTypes.ANY)
async def search_specialty(message: types.Message, state: FSMContext):
    try:
        faculty = Faculty.get(id=message.text)
        specialties = faculty.specialties
        for x in specialties:
            await message.answer(x.title)
            await Univer.univer.set()
    except DoesNotExist:
        return await Univer.univer.set()
        return await message.answer('Попробуйте ещё раз.')
    except MessageTextIsEmpty:
        return await message.answer('Попробуйте ещё раз.')


@dp.message_handler(state=Univer.contacts, content_types=types.ContentTypes.ANY)
async def contacts(message: types.Message, state: FSMContext):
    try:
        university = University.get(id=message.text)
        contacts = university.contacts
        for x in contacts:
            await message.answer(x.body)
            # await Univer.univer.set()
    except DoesNotExist:
        return await Univer.univer.set()
        return await message.answer('Попробуйте ещё раз.')
    except MessageTextIsEmpty:
        return await message.answer('Попробуйте ещё раз.')

@dp.message_handler(state=Univer.ort, content_types=types.ContentTypes.ANY)
async def ort(message: types.Message, state: FSMContext):
    try:
        faculty = Faculty.get(id=message.text)
        ort = faculty.ort
        for x in ort:
            await message.answer(x.body)
            await Univer.univer.set()
    except DoesNotExist:
        return await Univer.univer.set()
        return await message.answer('Попробуйте ещё раз.')
    except MessageTextIsEmpty:
        return await message.answer('Попробуйте ещё раз.')