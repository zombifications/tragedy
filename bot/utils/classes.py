from discord.ext import commands

def EmojiBool(bool: bool):
    switch = {
        True: ":white_check_mark:",
        False: ":x:",
    }
    return switch.get(bool, "N/A")

class NotVoter(commands.CheckFailure):
	pass

class WelcomeNotConfigured(commands.CheckFailure):
    pass

class NotGuildOwner(commands.CheckFailure):
    pass

class ShopItem(object):
    def __init__(self, item_name, item_price, item_emoji):
        self.name = item_name
        self.price = item_price
        self.emoji = item_emoji


class AutoModConfig(object):
    def __init__(self, profanity_filter: bool, invite_filter: bool, mention_filter: bool, mention_length: int, spam_filter: bool):
        self.profanity_filter = profanity_filter
        self.invite_filter = invite_filter
        self.mention_filter = mention_filter
        self.mention_length = mention_length
        self.spam_filter = spam_filter

    def __str__(self) -> str:
        return str("Profanity Filter - %s\nInvite Filter - %s\nMention Filter - %s\nMax Mentions - %d\nSpam Filter - %s\nSpam Ratio - %s" % (EmojiBool(self.profanity_filter), EmojiBool(self.invite_filter), EmojiBool(self.mention_filter), self.mention_length, EmojiBool(self.spam_filter), "5 per 2 seconds"))

    def __query__(self) -> str:
        return "INSERT INTO `auto-mod` (profanity_filter, invite_filter, mention_filter, mention_length, spam_filter) VALUES (%s, %s, %s, %s, %s)"

def query(config: AutoModConfig) -> str:
    return config.__query__()