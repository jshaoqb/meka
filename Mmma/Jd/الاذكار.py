import random
from telethon import events
import random, re

from jepthon.utils import admin_cmd

import asyncio
from jepthon import jepthon
from JepIQ.razan._islam import *
from ..core.managers import edit_or_reply

plugin_category = "extra" 

#by ~ @et_40
@et_40.ar_cmd(
    pattern="اذكار الصباح",
    command=("اذكار الصباح", plugin_category),)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
           roze = random.choice(razan)
           return await event.edit(f"{roze}")
#by ~ @et_40
@et_40.ar_cmd(
    pattern="اذكار المساء$",
    command=("اذكار المساء", plugin_category),)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
           ror = random.choice(roz)
           return await event.edit(f"{ror}")
            
#by ~ @et_40
@et_40.ar_cmd(
    pattern="احاديث$",
    command=("احاديث", plugin_category),)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
           me = random.choice(roza)
           return await event.edit(f"{me}")

@et_40.ar_cmd(
    pattern="اذكار الاستيقاظ$",
    command=("اذكار الاستيقاظ", plugin_category),)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
           az = random.choice(rozan)
           return await event.edit(f"{az}")
                     
@et_40.ar_cmd(
    pattern="اذكار النوم$",
    command=("اذكار النوم", plugin_category),)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
           rr = random.choice(rozmuh)
           return await event.edit(f"{rr}")
           
@et_40.ar_cmd(
    pattern="اذكار الصلاة$",
    command=("اذكار الصلاة", plugin_category),)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
           rm = random.choice(rzane)
           return await event.edit(f"{rm}")


@et_40.ar_cmd(
    pattern="اوامر الاذكار$",
    command=("اوامر الاذكار", plugin_category),)
async def _(event):
    await event.edit(
    "قائمة اوامر الاذكار :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اذكار الصباح` ) \n- ( `.اذكار المساء` )   \n- (`.اذكار النوم`)\n- ( `.اذكار الصلاة`) \n- ( `.اذكار الاستيقاظ` ) \n- ( `.احاديث` )\n- ( `.اذكار` )\n- ( `.اذكار عشر` )\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @et_40"
            )           
