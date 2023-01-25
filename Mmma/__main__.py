import sys

import jepthon
from jepthon import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID

from .Config import Config
from .core.logger import logging
from .core.session import jepthon
from .utils import (
    add_bot_to_logger_group,
    ipchange,
    load_plugins,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
    saves,
)

LOGS = logging.getLogger("JepThon")

print("Jepthon ar ©")

cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info("Starting jepthon")
    jepthon.loop.run_until_complete(setup_bot())
    LOGS.info("TG Bot Startup Completed")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()


class CatCheck:
    def __init__(self):
        self.sucess = True


Catcheck = CatCheck()


async def startup_process():
    check = await ipchange()
    if check is not None:
        Catcheck.sucess = False
        return
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print("⌯︙بـوت جـيبثون يعـمل بـنجاح ")
    print(
        f"يجـب تفـعيل وضع الأنلايـن ثم أرسـل {cmdhr}فحص لـرؤيـة اذا كـان البوت شـغال\
        \nللمسـاعدة تواصـل  https://t.me/JepthonSupport"
    )
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    await verifyLoggerGroup()
    await saves()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    Catcheck.sucess = True
    return



jepthon.loop.run_until_complete(startup_process())

if len(sys.argv) not in (1, 3, 4):
    jepthon.disconnect()
elif not Catcheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        jepthon.run_until_disconnected()
    except ConnectionError:
        pass
