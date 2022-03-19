import discord
from discord.ext import commands

frames_fixed = ""
frames = ""

class Karuta(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')

    """
    # Commands
    @commands.command()
    async def dave(self, ctx):
        await ctx.send('fucker')
    """

    @commands.command()
    async def clear(self, ctx):
        await ctx.channel.purge(check = None)

    """
    This method does an action when a user reacts
    with a certain emoji on the user "Karuta"'s
    message that is also of a certain type
    """
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):

        # make sure that it is from karuta bot
        if reaction.message.author.id == 646937666251915264:

            embeds = reaction.message.embeds

            # check for the type of message
            for embed in embeds:
                type = embed.to_dict()

            # do actions
            if type['title'] == 'Inventory':

                if reaction.emoji == '🖼️':
                    await reaction.message.channel.send("It works")

                # list down all your frames
                elif reaction.emoji == '⚙️':

                    # call function that lists it down
                    reset()
                    processFrames(type['description'])

                    # await reaction.message.channel.send(text)

                    pass
        
        # check reaction on bot message for type of frame to be printed
        if reaction.message.author.id == 947564414691844126 and \
            reaction.message.content.startswith("All Frames ["):

            try:

                if reaction.emoji == '👍':
                    await reaction.message.channel.send(frames)
                elif reaction.emoji == '👎':
                    await reaction.message.channel.send(filterBasicFrames())
                elif reaction.emoji == '👌':
                    await reaction.message.channel.send(filterSpecialFrames())
                elif reaction.emoji == '😔':
                    await reaction.message.channel.send(filterNoBasicFrames())
            except discord.errors.HTTPException:
                await reaction.message.channel.send('No frames found')

        pass

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):

        embeds = after.embeds

        reacts = after.reactions

        for react in reacts:
            if hash('⚙️') == hash(react):

                for embed in embeds:

                    type = embed.to_dict()
                    processFrames(type['description'])


    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):

        global frames

        if reaction.emoji == '⚙️':
            await reaction.message.channel.send("All Frames [👍] / Basic Frames [👎] / Special Frames [👌] / Basic Frames You Don't Have [😔]")
        pass

    @commands.Cog.listener()
    async def on_message(self, message):

        mentions = message.mentions

        if len(mentions) == 0:
            return

        for user in mentions:

            if user.id == 431469710375256094:
                await message.channel.send("big fucker")
                return

        pass


def processFrames(raw_text):

    global frames

    for line in raw_text.split('\n'):
        
        # if frame, print it out
        if "frame" in line:
            frames += line + "\n"

    return frames

def filterBasicFrames():

    global frames
    filteredFrames = ""

    # check the frames if they're in the txt file
    # put in a set
    #basicframes = open("basicframes.txt", "r", encoding = "utf-8").readlines()
    basicframes = [line.rstrip() for line in open('basicframes.txt')]

    basicframes_set = set(basicframes)

    for line in frames.split('\n'):

        split_line = line.split(' · ')
        
        try:
            split_line = split_line[2].replace("*", "")

            if split_line[7:] in basicframes_set:
                
                filteredFrames += line + '\n'
        except IndexError:
            pass

    return filteredFrames

def filterSpecialFrames():

    global frames
    filteredFrames = ""

    # check the frames if they're in the txt file
    # put in a set
    #basicframes = open("basicframes.txt", "r", encoding = "utf-8").readlines()
    basicframes = [line.rstrip() for line in open('basicframes.txt')]

    basicframes_set = set(basicframes)

    for line in frames.split('\n'):

        split_line = line.split(' · ')
        
        try:
            split_line = split_line[2].replace("*", "")

            if split_line[7:] not in basicframes_set:
                
                filteredFrames += line + '\n'
                
        except IndexError:
            pass

    return filteredFrames

def filterNoBasicFrames():

    owned = filterBasicFrames()

    basicframes = [line.rstrip() for line in open('basicframes.txt')]
    basicframes_set = set(basicframes)

    for line in owned.split('\n'):

        testCase = []
        split_line = line.split(' · ')
        
        try:
            split_line = split_line[2].replace("*", "")

            testCase.append(split_line[7:])

            basicframes_set -= set(testCase)

        except IndexError:
            pass

    if len(basicframes_set) == 0:
        return "You own all the bit frames"
        
    return basicframes_set

def getNotOwned():

    basicframes = [line.rstrip() for line in open('basicframes.txt')]
    basicframes_set = set(basicframes)

    
    pass

def reset():
    global frames
    frames = ""

def setup(client):
    client.add_cog(Karuta(client))
