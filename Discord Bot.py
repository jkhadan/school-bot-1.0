import discord
from discord.ext import commands
import asyncio
import datetime as dt
import pytz
import icalendar

intent = discord.Intents(messages=True, members=True, guilds=True)

bot = commands.Bot(command_prefix="pb$", intents=intent)

users = {}
# with open("users.csv", "r") as r:
#     for lines in r.readlines():


homework = {}


async def adduser():
    await bot.wait_until_ready()

    while not bot.is_closed():
        for guild in bot.guilds:
            for member in guild.members:
                if member.id not in users.keys():
                    users.update({member.id: []})
        with open("users.csv", "w") as f:
            for key in users.keys():
                f.write(f"{key},{users[key]}\n")
        await asyncio.sleep(10)


def checkday(arg, user=None, view=None):
    if arg == "":
        return False
    elif arg[0] == 'A':
        if user is not None:
            view = discord.Embed(
                description=user.mention,
                color=discord.Color.from_rgb(46, 48, 146)
            )
            view.set_author(name=f"{user.name}'s {arg[0]} Day Schedule",
                            icon_url=user.avatar_url)
            # A Schedule (1, 2, 3, 5, 6)
            view.add_field(name=f"Block {1}", value=users.get(user.id)[0], inline=False)
            view.add_field(name=f"Block {2}", value=users.get(user.id)[1], inline=False)
            view.add_field(name=f"Block {3}", value=users.get(user.id)[2], inline=False)
            view.add_field(name=f"Block {4}", value=users.get(user.id)[4], inline=False)
            view.add_field(name=f"Block {5}", value=users.get(user.id)[5], inline=False)
        else:
            return True
    elif arg[0] == 'B':
        if user is not None:
            view = discord.Embed(
                description=user.mention,
                color=discord.Color.from_rgb(46, 48, 146)
            )
            view.set_author(name=f"{user.name}'s {arg[0]} Day Schedule",
                            icon_url=user.avatar_url)
            # B Schedule (4, 1, 2, 7, 5)
            view.add_field(name=f"Block {1}", value=users.get(user.id)[3], inline=False)
            view.add_field(name=f"Block {2}", value=users.get(user.id)[0], inline=False)
            view.add_field(name=f"Block {3}", value=users.get(user.id)[1], inline=False)
            view.add_field(name=f"Block {4}", value=users.get(user.id)[6], inline=False)
            view.add_field(name=f"Block {5}", value=users.get(user.id)[4], inline=False)
        else:
            return True
    elif arg[0] == 'C':
        if user is not None:
            view = discord.Embed(
                description=user.mention,
                color=discord.Color.from_rgb(46, 48, 146)
            )
            view.set_author(name=f"{user.name}'s {arg[0]} Day Schedule",
                            icon_url=user.avatar_url)
            # C Schedule (3, 4, 1, 6, 7)
            view.add_field(name=f"Block {1}", value=users.get(user.id)[2], inline=False)
            view.add_field(name=f"Block {2}", value=users.get(user.id)[3], inline=False)
            view.add_field(name=f"Block {3}", value=users.get(user.id)[0], inline=False)
            view.add_field(name=f"Block {4}", value=users.get(user.id)[5], inline=False)
            view.add_field(name=f"Block {5}", value=users.get(user.id)[6], inline=False)
        else:
            return True
    elif arg[0] == 'D':
        if user is not None:
            view = discord.Embed(
                description=user.mention,
                color=discord.Color.from_rgb(46, 48, 146)
            )
            view.set_author(name=f"{user.name}'s {arg[0]} Day Schedule",
                            icon_url=user.avatar_url)
            # D Schedule (2, 3, 4, 5, 6)
            view.add_field(name=f"Block {1}", value=users.get(user.id)[1], inline=False)
            view.add_field(name=f"Block {2}", value=users.get(user.id)[2], inline=False)
            view.add_field(name=f"Block {3}", value=users.get(user.id)[3], inline=False)
            view.add_field(name=f"Block {4}", value=users.get(user.id)[4], inline=False)
            view.add_field(name=f"Block {5}", value=users.get(user.id)[5], inline=False)
        else:
            return True
    elif arg[0] == 'E':
        if user is not None:
            view = discord.Embed(
                description=user.mention,
                color=discord.Color.from_rgb(46, 48, 146)
            )
            view.set_author(name=f"{user.name}'s {arg[0]} Day Schedule",
                            icon_url=user.avatar_url)
            # E Schedule (1, 2, 3, 7, 5)
            view.add_field(name=f"Block {1}", value=users.get(user.id)[0], inline=False)
            view.add_field(name=f"Block {2}", value=users.get(user.id)[1], inline=False)
            view.add_field(name=f"Block {3}", value=users.get(user.id)[2], inline=False)
            view.add_field(name=f"Block {4}", value=users.get(user.id)[6], inline=False)
            view.add_field(name=f"Block {5}", value=users.get(user.id)[4], inline=False)
        else:
            return True
    elif arg[0] == 'F':
        if user is not None:
            view = discord.Embed(
                description=user.mention,
                color=discord.Color.from_rgb(46, 48, 146)
            )
            view.set_author(name=f"{user.name}'s {arg[0]} Day Schedule",
                            icon_url=user.avatar_url)
            # F Schedule (4, 1, 2, 6, 7)
            view.add_field(name=f"Block {1}", value=users.get(user.id)[3], inline=False)
            view.add_field(name=f"Block {2}", value=users.get(user.id)[0], inline=False)
            view.add_field(name=f"Block {3}", value=users.get(user.id)[1], inline=False)
            view.add_field(name=f"Block {4}", value=users.get(user.id)[5], inline=False)
            view.add_field(name=f"Block {5}", value=users.get(user.id)[6], inline=False)
        else:
            return True
    elif arg[0] == 'G':
        if user is not None:
            view = discord.Embed(
                description=user.mention,
                color=discord.Color.from_rgb(46, 48, 146)
            )
            view.set_author(name=f"{user.name}'s {arg[0]} Day Schedule",
                            icon_url=user.avatar_url)
            # G Schedule (3, 4, 7, 5, 6)
            view.add_field(name=f"Block {1}", value=users.get(user.id)[2], inline=False)
            view.add_field(name=f"Block {2}", value=users.get(user.id)[3], inline=False)
            view.add_field(name=f"Block {3}", value=users.get(user.id)[6], inline=False)
            view.add_field(name=f"Block {4}", value=users.get(user.id)[4], inline=False)
            view.add_field(name=f"Block {5}", value=users.get(user.id)[5], inline=False)
        else:
            return True
    return view


def blockEmbed(letter, block, user, embed=None):
    if letter == 'A':
        if block == 1:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[0]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 7:30-8:18", inline=True)
        elif block == 2:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[1]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 8:25-9:13", inline=True)
        elif block == 3:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[2]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 9:20-10:08", inline=True)
        elif block == 4:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[4]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 10:15-11:03", inline=True)
        elif block == 5:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[5]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 11:03-12:00", inline=True)
    elif letter == 'B':
        if block == 1:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[3]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 7:30-8:18", inline=True)
        elif block == 2:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[0]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 8:25-9:13", inline=True)
        elif block == 3:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[1]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 9:20-10:08", inline=True)
        elif block == 4:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[6]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 10:15-11:03", inline=True)
        elif block == 5:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[4]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 11:10-12:00", inline=True)
    elif letter == 'C':
        if block == 1:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[2]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 7:30-8:18", inline=True)
        elif block == 2:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[3]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 8:25-9:13", inline=True)
        elif block == 3:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[0]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 9:20-10:08", inline=True)
        elif block == 4:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[5]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 10:15-11:03", inline=True)
        elif block == 5:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[6]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 11:03-12:00", inline=True)
    elif letter == 'D':
        if block == 1:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[1]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 7:30-8:18", inline=True)
        elif block == 2:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[2]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 8:25-9:13", inline=True)
        elif block == 3:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[3]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 9:20-10:08", inline=True)
        elif block == 4:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[4]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 10:15-11:03", inline=True)
        elif block == 5:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[5]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 11:03-12:00", inline=True)
    elif letter == 'E':
        if block == 1:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[0]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 7:30-8:18", inline=True)
        elif block == 2:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[1]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 8:25-9:13", inline=True)
        elif block == 3:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[2]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 9:20-10:08", inline=True)
        elif block == 4:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[4]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 10:15-11:03", inline=True)
        elif block == 5:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[5]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 11:03-12:00", inline=True)
    elif letter == 'F':
        if block == 1:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[3]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 7:30-8:18", inline=True)
        elif block == 2:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[0]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 8:25-9:13", inline=True)
        elif block == 3:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[1]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 9:20-10:08", inline=True)
        elif block == 4:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[5]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 10:15-11:03", inline=True)
        elif block == 5:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[6]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 11:03-12:00", inline=True)
    elif letter == 'G':
        if block == 1:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[2]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 7:30-8:18", inline=True)
        elif block == 2:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[3]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 8:25-9:13", inline=True)
        elif block == 3:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[6]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 9:20-10:08", inline=True)
        elif block == 4:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[4]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 10:15-11:03", inline=True)
        elif block == 5:
            embed = discord.Embed(
                title=f"Time for {users.get(user.id)[5]}!",
                description=f"Block {block} has now started",
                color=discord.Color.from_rgb(46, 48, 146)
            )
            embed.add_field(name="Time span", value="This block will run from 11:03-12:00", inline=True)
    return embed


async def session():
    await bot.wait_until_ready()

    while not bot.is_closed():
        # Get the time
        today_utc = dt.datetime.now()
        today_est = today_utc.astimezone(pytz.timezone("US/Eastern"))

        calendar = open("SWCal.ics", "rb")
        iCal = icalendar.Calendar.from_ical(calendar.read())
        letterDay = ""
        event = "No Events for Today"

        # Read Calendar to see if there is school today, and what letter day it is if any
        for component in iCal.walk():
            if component.name == "VEVENT":
                if component.get("dtstart").dt == today_est.date():
                    if "Day: Block Schedule" in component.get("summary"):
                        letterDay = component.get("summary")
                    else:
                        event = component.get("summary")
        calendar.close()
        if checkday(letterDay):
            # Determine if 7:25 on a weekday
            if today_est.time().hour == 7 and today_est.time().minute == 25:

                # Checks if school is today to grab schedule
                for user in users.keys():
                    person = await bot.fetch_user(user)
                    if len(users.get(user)) == 7:
                        try:
                            await person.send(
                                "Good Morning! School Starts in 5 minutes. Here is your schedule for the day.")
                        except:
                            pass
                        view = checkday(letterDay, person)
                        view.add_field(name="Event", value=event)
                        await person.send(embed=view)
                    else:
                        try:
                            await person.send(
                                "It looks like you are in a server with me, but have not yet filled out a schedule. "
                                "In order to get your daily schedule, please go to the server which I am located, "
                                "and fill out your schedule with $setperiod")
                        except:
                            pass

            if today_est.time().hour == 7 and today_est.time().minute == 30:
                people = []
                for user in users.keys():
                    person = await bot.fetch_user(user)
                    if len(users.get(user)) == 7:
                        people.append(person)
                if letterDay[0] == 'A':
                    for user in people:
                        message = blockEmbed('A', 1, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('A', 2, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('A', 3, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('A', 4, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('A', 5, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)
                    for user in people:
                        try:
                            await user.send(
                                "School is now officially over! Enjoy the rest of your day, and don't forget your "
                                "homework! :)")
                        except:
                            pass
                elif letterDay[0] == 'B':
                    for user in people:
                        message = blockEmbed('B', 1, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('B', 2, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('B', 3, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('B', 4, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('B', 5, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)
                    for user in people:
                        try:
                            await user.send(
                                "School is now officially over! Enjoy the rest of your day, and don't forget your "
                                "homework! :)")
                        except:
                            pass
                elif letterDay[0] == 'C':
                    for user in people:
                        message = blockEmbed('C', 1, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('C', 2, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('C', 3, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('C', 4, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('C', 5, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)
                    for user in people:
                        try:
                            await user.send(
                                "School is now officially over! Enjoy the rest of your day, and don't forget your "
                                "homework! :)")
                        except:
                            pass
                elif letterDay[0] == 'D':
                    for user in people:
                        message = blockEmbed('D', 1, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('D', 2, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('D', 3, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('D', 4, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('D', 5, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)
                    for user in people:
                        try:
                            await user.send(
                                "School is now officially over! Enjoy the rest of your day, and don't forget your "
                                "homework! :)")
                        except:
                            pass
                elif letterDay[0] == 'E':
                    for user in people:
                        message = blockEmbed('E', 1, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('E', 2, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('E', 3, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('E', 4, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('E', 5, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)
                    for user in people:
                        try:
                            await user.send(
                                "School is now officially over! Enjoy the rest of your day, and don't forget your "
                                "homework! :)")
                        except:
                            pass
                elif letterDay[0] == 'F':
                    for user in people:
                        message = blockEmbed('F', 1, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('F', 2, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('F', 3, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('F', 4, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('F', 5, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)
                    for user in people:
                        try:
                            await user.send(
                                "School is now officially over! Enjoy the rest of your day, and don't forget your "
                                "homework! :)")
                        except:
                            pass
                elif letterDay[0] == 'G':
                    for user in people:
                        message = blockEmbed('G', 1, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('G', 2, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('G', 3, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('G', 4, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)

                    for user in people:
                        message = blockEmbed('G', 5, user)
                        try:
                            await user.send(embed=message)
                        except:
                            pass
                    await asyncio.sleep(2580)
                    for user in people:
                        try:
                            await user.send("Only 5 minutes left in class!")
                        except:
                            pass
                    await asyncio.sleep(720)
                    for user in people:
                        try:
                            await user.send(
                                "School is now officially over! Enjoy the rest of your day, and don't forget your "
                                "homework! :)")
                        except:
                            pass

        await asyncio.sleep(45)


@bot.event
async def on_ready():
    print("Bot is ready")


@bot.command(pass_context=True)
async def setperiod(ctx, *arg):
    if len(users.get(ctx.message.author.id)) < 7:
        output = ""
        for args in arg:
            output += args + " "
        if len(output) < 23:
            users.get(ctx.message.author.id).append(output[:len(output) - 1])
            await ctx.send(
                f"\nSuccess! Period `{len(users.get(ctx.message.author.id))}` has been set to "
                f"`{output[:len(output) - 1]}`")
        else:
            await ctx.send("I'm sorry, but the inputted name is too long.")
    else:
        await ctx.send("You already have your periods filled out! If you would like to view your schedule, "
                       "use $schedule, or to change one, use $changeperiod.")


@bot.command()
async def debug(ctx):
    print(users)


@bot.command(pass_context=True)
async def addhw(ctx, *args):
    today_utc = dt.datetime.now()
    today_est = today_utc.astimezone(pytz.timezone("US/Eastern"))
    block1 = today_est.replace(hour=8, minute=18, second=0, microsecond=0)
    block2 = today_est.replace(hour=9, minute=13, second=0, microsecond=0)
    block3 = today_est.replace(hour=10, minute=8, second=0, microsecond=0)
    block4 = today_est.replace(hour=10, minute=15, second=0, microsecond=0)
    block5 = today_est.replace(hour=12, minute=0, second=0, microsecond=0)
    if len(args) == 7:
        if today_est < block1:
            homework.get(ctx.message.author.id).append()
        elif today_est < block2:
            delta = block2 - today_est
            await ctx.send(
                f"There are {delta.total_seconds() // 60} minutes and {delta.total_seconds() % 60} seconds left in "
                f"Block 2")
        elif today_est < block3:
            delta = block3 - today_est
            await ctx.send(
                f"There are {delta.total_seconds() // 60} minutes and {delta.total_seconds() % 60} seconds left in "
                f"Block 3")
        elif today_est < block4:
            delta = block4 - today_est
            await ctx.send(
                f"There are {delta.total_seconds() // 60} minutes and {delta.total_seconds() % 60} seconds left in "
                f"Block 4")
        elif today_est < block5:
            delta = block5 - today_est
            await ctx.send(
                f"There are {delta.total_seconds() // 60} minutes and {delta.total_seconds() % 60} seconds left in "
                f"Block 5")

    else:
        ctx.send("You need to have a full schedule in order to add homework")


@bot.command(pass_context=True)
async def changeperiod(ctx, *arg):
    if len(arg) > 1:
        if int(arg[0]) <= len(users.get(ctx.message.author.id)) and int(arg[0]) < 8:
            output = ""
            for args in arg[1:]:
                output += args + " "
            if len(output) < 24:
                users.get(ctx.message.author.id)[int(arg[0]) - 1] = output[:len(output) - 1]
                await ctx.send(f"Success! Period `{arg[0]}` has been changed to `{output}`")
            else:
                await ctx.send("I'm sorry, but the inputted name is too long.")
        else:
            await ctx.send("Please fill out your schedule first before changing it")
    else:
        await ctx.send("Usage: <period #> <class name>")


@bot.command(pass_context=True)
async def timeleft(ctx):
    today_utc = dt.datetime.now()
    today_est = today_utc.astimezone(pytz.timezone("US/Eastern"))
    block1 = today_est.replace(hour=8, minute=18, second=0, microsecond=0)
    block2 = today_est.replace(hour=9, minute=13, second=0, microsecond=0)
    block3 = today_est.replace(hour=10, minute=8, second=0, microsecond=0)
    block4 = today_est.replace(hour=10, minute=15, second=0, microsecond=0)
    block5 = today_est.replace(hour=12, minute=0, second=0, microsecond=0)
    if today_est < block1:
        delta = block1 - today_est
        await ctx.send(
            f"There are {delta.total_seconds() // 60} minutes and {delta.total_seconds() % 60} seconds left in "
            f"Block 1")
    elif today_est < block2:
        delta = block2 - today_est
        await ctx.send(
            f"There are {delta.total_seconds() // 60} minutes and {delta.total_seconds() % 60} seconds left in "
            f"Block 2")
    elif today_est < block3:
        delta = block3 - today_est
        await ctx.send(
            f"There are {delta.total_seconds() // 60} minutes and {delta.total_seconds() % 60} seconds left in "
            f"Block 3")
    elif today_est < block4:
        delta = block4 - today_est
        await ctx.send(
            f"There are {delta.total_seconds() // 60} minutes and {delta.total_seconds() % 60} seconds left in "
            f"Block 4")
    elif today_est < block5:
        delta = block5 - today_est
        await ctx.send(
            f"There are {delta.total_seconds() // 60} minutes and {delta.total_seconds() % 60} seconds left in "
            f"Block 5")
    else:
        await ctx.send("Looks like you're not currently in class. This command is only used in class.")


@bot.command(pass_context=True)
async def schedule(ctx, arg=None):
    if arg is None:
        if len(users.get(ctx.message.author.id)) > 0:
            view = discord.Embed(
                description=ctx.message.author.mention,
                color=discord.Color.from_rgb(46, 48, 146)
            )
            view.set_author(name=f"{ctx.message.author.name}'s Schedule", icon_url=ctx.message.author.avatar_url)
            order = 1
            for classes in users.get(ctx.message.author.id):
                view.add_field(name=f"Period {order}", value=classes, inline=False)
                order += 1
            await ctx.send(embed=view)
        else:
            await ctx.send("You need to have something on your schedule in order to view it")
    else:
        try:
            argument = str(arg)

            numID = int(argument[3:len(argument) - 1])
            user = await bot.fetch_user(numID)

            if len(users.get(user.id)) > 0:
                view = discord.Embed(
                    description=user.mention,
                    color=discord.Color.from_rgb(46, 48, 146)
                )
                view.set_author(name=f"{user.name}'s Schedule", icon_url=user.avatar_url)
                order = 1
                for classes in users.get(user.id):
                    view.add_field(name=f"Period {order}", value=classes, inline=False)
                    order += 1
                await ctx.send(embed=view)
            else:
                await ctx.send("This person needs to have a schedule set up in order to view it")
        except:
            await ctx.send("Please either mention the user you want to view, or put nothing to view your own")


@bot.command(pass_context=True)
async def daysleft(ctx):
    today = dt.date.today()
    lastDay = dt.date(2021, 6, 23)
    delta = today - lastDay
    schoolDays = 0

    calendar = open("SWCal.ics", "rb")
    ical = icalendar.Calendar.from_ical(calendar.read())
    for component in ical.walk():
        if component.name == "VEVENT":
            if "Day: Block Schedule" in component.get("summary"):
                if component.get("dtstart").dt > today:
                    schoolDays += 1
            beginCal = component.get("dtstamp").dt

    daysfromstart = today - beginCal.date()
    delta = (daysfromstart - delta).days
    calendar.close()

    await ctx.send(f"There are `{delta}` days left until the last day of school, or `{schoolDays}` school days.")


bot.loop.create_task(session())
bot.loop.create_task(adduser())
bot.run("Key Goes Here")
