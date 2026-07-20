import discord
from discord import app_commands
from discord.ext import commands
import asyncio

# --- THE DARK CONFIG ---
TOKEN = 'BOT_TOKEN_HERE'
# -----------------------

class SpamBot(commands.Bot):
    def __init__(self):
        # Intents are required even for user apps to function properly
        intents = discord.Intents.default()
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        # Syncs the slash commands to the global scope
        await self.tree.sync()
        print("💌 [SYSTEM] Slash commands synced. Ready to msg.")

bot = SpamBot()

# --- THE TRIGGER BUTTON ---
class SpamButton(discord.ui.View):
    def __init__(self, message_text, amount):
        super().__init__(timeout=None)
        self.message_text = message_text
        self.amount = amount

    async def run_spam_task(self, interaction: discord.Interaction):
        """Background task to handle the loops smoothly without freezing the UI"""
        for i in range(self.amount):
            try:
                await interaction.followup.send(self.message_text)
                # Small sleep to avoid instant rate-limit ban
                await asyncio.sleep(0.6)
            except discord.HTTPException as e:
                print(f"⚠️ Rate limited by the gods: {e}")
                await asyncio.sleep(5) # Wait for the cooldown


    @discord.ui.button(label='Send', style=discord.ButtonStyle.danger)
    async def start_spam(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Acknowledge the interaction so it doesn't time out
        await interaction.response.send_message("🚀 Msg Sending...", ephemeral=True)

        # Pass the interaction object instead of the channel
        asyncio.create_task(self.run_spam_task(interaction))

# --- THE SLASH COMMAND ---
@bot.tree.command(
    name="spam",
    description="Set up a hidden spam trigger"
)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.default_permissions(send_messages=True)
@app_commands.describe(text="The filth to spam", amount="How many times to scream")
async def spam(interaction: discord.Interaction, text: str, amount: int):
    # ephemeral=True makes the message visible ONLY to you
    view = SpamButton(text, amount)
    await interaction.response.send_message(
        f"Target locked. Text: '{text}' | Amount: '{amount}'\nClick the button to send msg.",
        view=view,
        ephemeral=True
    )

bot.run(TOKEN)
