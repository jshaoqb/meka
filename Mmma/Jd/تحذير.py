import html

from jepthon import jepthon

from ..core.managers import edit_or_reply
from ..sql_helper import warns_sql as sql

plugin_category = "admin"


@jepthon.ar_cmd(
    pattern="تحذير(?:\s|$)([\s\S]*)",
    command=("تحذير", plugin_category),
    info={
        "header": "لتحذير المستخدم.",
        "description": "سيحذر المستخدم الذي تم الرد عليه.",
        "usage": "تحذير <السبب>",
    },
)
async def _(event):
    "لتحذير المستخدم"
    warn_reason = event.pattern_match.group(1)
    if not warn_reason:
        warn_reason = "- لا يوجد سبب ، 🗒"
    reply_message = await event.get_reply_message()
    limit, soft_warn = sql.get_warn_setting(event.chat_id)
    num_warns, reasons = sql.warn_user(
        reply_message.sender_id, event.chat_id, warn_reason
    )
    if num_warns >= limit:
        sql.reset_warns(reply_message.sender_id, event.chat_id)
        if soft_warn:
            logger.info("TODO: kick user")
            reply = "**▸┊بسبب تخطي التحذيرات الـ {} ، يجب طرد المستخدم! 🚷**".format(
                limit, reply_message.sender_id
            )
        else:
            logger.info("TODO: ban user")
            reply = "**▸┊بسبب تخطي التحذيرات الـ {} ، يجب حظر المستخدم! ⛔️**".format(
                limit, reply_message.sender_id
            )
    else:
        reply = "**▸┊[ المستخدم 👤](tg://user?id={}) **لديه {}/{} تحذيرات ، احذر!****".format(
            reply_message.sender_id, num_warns, limit
        )
        if warn_reason:
            reply += "\n**▸┊سبب التحذير الأخير **\n{}".format(html.escape(warn_reason))
    await edit_or_reply(event, reply)


@jepthon.ar_cmd(
    pattern="التحذيرات",
    command=("التحذيرات", plugin_category),
    info={
        "header": "للحصول على قائمة تحذيرات المستخدمين.",
        "usage": "التحذير <بالرد>",
    },
)
async def _(event):
    "للحصول على قائمة تحذيرات المستخدمين."
    reply_message = await event.get_reply_message()
    if not reply_message:
        return await edit_delete(
            event, "**▸┊قم بالرد ع المستخدم للحصول ع تحذيراته . ☻**"
        )
    result = sql.get_warns(reply_message.sender_id, event.chat_id)
    if not result or result[0] == 0:
        return await edit_or_reply(event, "__▸┊هذا المستخدم ليس لديه أي تحذير! ツ__")
    num_warns, reasons = result
    limit, soft_warn = sql.get_warn_setting(event.chat_id)
    if not reasons:
        return await edit_or_reply(
            event,
            "**▸┊[ المستخدم 👤](tg://user?id={}) **لديه {}/{} تحذيرات ، لكن لا توجد اسباب !**".format(
                num_warns, limit
            ),
        )

    text = "**▸┊[ المستخدم 👤](tg://user?id={}) **لديه {}/{} تحذيرات ، للأسباب : ↶**".format(
        num_warns, limit
    )
    text += "\r\n"
    text += reasons
    await event.edit(text)


@jepthon.ar_cmd(
    pattern="ح(ذف) ?التحذير$",
    command=("حذف التحذير", plugin_category),
    info={
        "header": "لحذف تحذيرات المستخدم الذي تم الرد عليه",
        "usage": [
            "{tr}ح التحذير",
            "{tr}حذف التحذير",
        ],
    },
)
async def _(event):
    "لحذف او اعادة تحذيرات المستخدم الذي تم الرد عليه"
    reply_message = await event.get_reply_message()
    sql.reset_warns(reply_message.sender_id, event.chat_id)
    await edit_or_reply(event, "**▸┊تم إعادة ضبط التحذيرات!**")
