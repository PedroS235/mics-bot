import nextcord
from nextcord.ext import commands
from nextcord import application_command, Interaction

from bics_bot.embeds.logger_embed import LoggerEmbed, LogLevel
from bics_bot.config.server_ids import (
    ROLE_INTRO_LIST,
)
from bics_bot.utils.file_manipulation import read_txt
from bics_bot.utils.server_utilities import retrieve_server_ids

from bics_bot.cogs.commands.birthday_cmd import (
    is_valid_birthday,
    store_birthday,
)


class IntroCmd(commands.Cog):
    """This class represents the command </intro>

    The `/intro` command is used for newcomers to get a student role,
    and change their server username to comply with the server format.
    Format Example: John Doe -> John D

    Attributes:
        client: Required by the API, not directly utilized.
    """

    def __init__(self, client):
        self.client = client

    @application_command.slash_command(
        description="Introduction",
    )
    async def intro(
        self,
        interaction: Interaction,
        name: str = nextcord.SlashOption(
            description="First Name", required=True
        ),
        surname: str = nextcord.SlashOption(
            description="Last Name", required=True
        ),
        year: str = nextcord.SlashOption(
            description="The year you will be in. In case you plan on joining the University choose **incoming**",
            choices=ROLE_INTRO_LIST,
        ),
        birthday: str = nextcord.SlashOption(
            description="(OPTIONAL) Your birthday in the format DD.MM.YYYY",
            required=False,
            default="",
        ),
    ) -> None:
        """
        The `/intro` command is used for newcomers to get a student role,
        and change their server username to comply with the server format.
        Format Example: John Doe -> John D

        Args:
            interaction: Required by the API. Gives meta information about
              the interaction.
            name: The first name of the student
            surname: The last name of the student.
            year: The promotion of the student.

        Returns:
            None
        """

        server_ids = retrieve_server_ids(interaction.guild)

        user = interaction.user
        server_roles = interaction.guild.roles

        if (
            len(user.roles) > 1
            and len(
                [
                    role
                    for role in user.roles
                    if role.name == "Moderator" or role.name == "Gamer"
                ]
            )
            == 0
        ):
            # User already used /intro once
            msg = f"You have already introduced yourself! Wrong name? Ping an <@&{server_ids['roles']['admin']}> or <@&{server_ids['roles']['moderator']}>"
            await interaction.response.send_message(
                embed=LoggerEmbed(msg, LogLevel.ERROR),
                ephemeral=True,
            )
            return

        print(birthday)

        # Check if entered birthday is valid
        if birthday != "" and not is_valid_birthday(birthday):
            msg = "You entered an invalid birthday. Please follow the format **DD.MM.YYYY**."
            await interaction.response.send_message(
                embed=LoggerEmbed(msg, LogLevel.WARNING),
                ephemeral=True,
            )
            return

        # Retrieving the roles
        roles = {
            "year-1": nextcord.utils.get(server_roles, name="Year 1"),
            "year-2": nextcord.utils.get(server_roles, name="Year 2"),
            "erasmus": nextcord.utils.get(server_roles, name="Erasmus"),
            "alumni": nextcord.utils.get(server_roles, name="Alumni"),
            "incoming": nextcord.utils.get(server_roles, name="Incoming"),
        }

        # Add role to the user
        await user.add_roles(roles[year])

        # Storing the user's birthday in JSON file
        if len(birthday) > 0:
            file_name = "./db/birthdays.json"
            store_birthday(file_name, birthday, user.id)

        # Changing the nickname to Name + Surname initial
        try:
            await user.edit(nick=f"{name.capitalize()} {surname[0].upper()}")
        except nextcord.Forbidden:
            await interaction.response.send_message(
                embed=LoggerEmbed(
                    "I don't have permission to change your nickname 😢",
                    LogLevel.ERROR,
                ),
                ephemeral=True,
            )
            return
        msg = f"""Welcome on board **{name.capitalize()} {surname.capitalize()}**!
            Your role has been updated and you are all set 😉.
            In case of any question, feel free to ping an <@&{server_ids['roles']['admin']}> or <@&{server_ids['roles']['moderator']}>\n\n"""

        if year == "incoming":
            msg = msg + read_txt("./bics_bot/texts/introduction_incoming.txt")
        else:
            msg = msg + read_txt("./bics_bot/texts/introduction.txt")

        await interaction.response.send_message(
            embed=LoggerEmbed(msg),
            ephemeral=True,
        )


def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(IntroCmd(client))
