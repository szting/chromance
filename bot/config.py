import os
from dotenv import load_dotenv
from typing import Dict, List

load_dotenv()

# Bot Configuration
BOT_TOKEN = os.getenv('BOT_TOKEN')
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GIPHY_API_KEY = os.getenv('GIPHY_API_KEY')

# Rainbow Configuration
RAINBOW_COLORS = {
    'red': {'name': 'Red', 'emoji': '🔴', 'theme': 'Passion', 'points': 'spark'},
    'orange': {'name': 'Orange', 'emoji': '🟠', 'theme': 'Warmth', 'points': 'cozy'},
    'yellow': {'name': 'Yellow', 'emoji': '🟡', 'theme': 'Happiness', 'points': 'sunshine'},
    'green': {'name': 'Green', 'emoji': '🟢', 'theme': 'Peace', 'points': 'zen'},
    'blue': {'name': 'Blue', 'emoji': '🔵', 'theme': 'Trust', 'points': 'anchor'},
    'indigo': {'name': 'Indigo', 'emoji': '🟦', 'theme': 'Depth', 'points': 'sage'},
    'violet': {'name': 'Violet', 'emoji': '🟣', 'theme': 'Mystique', 'points': 'enigma'}
}

# Language Configuration
LANGUAGES = {
    'en': 'English',
    'zh': '中文'
}

# Achievement Badges
BADGES = {
    'rainbow_starter': {'name': 'Rainbow Starter', 'emoji': '🌈', 'requirement': 'Complete first challenge'},
    'peace_keeper': {'name': 'Peace Keeper', 'emoji': '🟢', 'requirement': 'Complete 5 green challenges'},
    'full_rainbow': {'name': 'Full Rainbow Achiever', 'emoji': '✨', 'requirement': 'Complete all 7 colors'},
    'streak_master': {'name': 'Streak Master', 'emoji': '🔥', 'requirement': '7 day streak'},
    'love_champion': {'name': 'Love Champion', 'emoji': '💖', 'requirement': '30 challenges completed'}
}

# Default Daily Schedule (in hours, 24-hour format)
DEFAULT_PROMPT_TIME = 9  # 9 AM local time
