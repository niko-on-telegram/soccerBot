from src.utils import format_message

data = '''🔔 Second Half Goal Signal [Beta]

🇧🇷 Brazil Serie A (2nd vs 11th)
Palmeiras vs EC Juventude

Timer: Half Time
Last Goal: None

Goals: 0 - 0
xG: 0.83 - 0.22
Corners: 6 - 2
Momentum: 38 - 46
Shots On Target: 3 - 3
Shots Off Target: 10 - 5
Attacks: 63 - 36
Dangerous Attacks: 41 - 14
Yellow Cards: 0 - 1
Red Cards: 0 - 0
Penalties: 0 - 0
Substitutions: 0 - 0
Possession %: 61 - 39
Crossing Accuracy %: 30 - 20
➕ Live Stats

1X2 Pre-Match Odds:
1.40 4.33 9.00
1X2 Live Odds:
1.67 3.00 8.00
Over/Under 0.50 Odds:
1.25 4.00

📈 Matched: £937,524
⸻⸻⸻⸻⸻⸻
Powered by InPlayGuru

✅ Hit
HT Score: 0-0
FT Score: 3-1'''

target = '''⚽️⚡️Second Half Goal Signal
🇧🇷 Brazil Serie A
*Palmeiras vs EC Juventude*
Match Time: Half Time
Current Score: 0 - 0'''


def test_format():
    res = format_message(data)
    assert res.text == target
    assert res.img_path == 'second_half_goal.jpg'
