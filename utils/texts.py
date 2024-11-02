def user_info(**kwargs):
    info=''
    info += f"first_name-{kwargs['first_name']}\n"
    info += f"username-@{kwargs['username']}\n"
    info += f"user_id-<code>{kwargs['user_id']}</code>\n"
    info += f"is_bot-{kwargs['is_bot']}\n"
    info += f"Message-{kwargs['text']}\n"

    return info