import re 
import asyncio
import discord
from discord.ext import commands
from utils.redditParse import RedditParse

class Poni(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sendChannels = { }


    @commands.command()
    async def send(self, ctx, url = None):
        if self.sendChannels.get(ctx.channel.id, False) == True:
            await ctx.send("данный канал уже задействован")
            return
        
        self.sendChannels[ctx.channel.id] = True

        if url == None :
            url ="https://www.reddit.com/r/AnimeWitches/"

        parse = RedditParse(url)
        while self.sendChannels.get(ctx.channel.id, False):
            try:
                pony = parse.next()
            except Exception as e:
                print(e)
                self.sendChannels.pop(ctx.channel.id)
                return await ctx.send(str(e))

            if pony is None:
                break

            embed = discord.Embed(
                colour = discord.Colour.from_rgb(0, 0, 0),
                description= f"{pony['title']}\n[ссылочка]({pony['url']})"
                )
            embed.set_image(url = pony['url'])

            await ctx.send(embed = embed)
        await ctx.send("конец")
        self.sendChannels.pop(ctx.channel.id)
        
    @commands.command()
    async def stop(self, ctx):
        if self.sendChannels.get(ctx.channel.id, False) == False:
            await ctx.send("данный канал не задействован")
            return
    
def setup(bot):
    bot.add_cog(Poni(bot))