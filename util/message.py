import discord


async def get_message_reference(message: discord.Message) -> discord.Message:
    if message.reference.cached_message is not None:
        return message.reference.cached_message
    else:
        return await message.channel.fetch_message(message.reference.message_id)
