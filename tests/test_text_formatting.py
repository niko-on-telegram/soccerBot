from src.utils import format_message

data = '''🔔 Dominator xG Alert

🌎 Copa Sudamericana (3rd vs 4th)
Nacional Potosi vs Sportivo Trinidense

Timer: 68'
Last Goal: Home at 68' (0 minutes ago)

Goals: 1 - 1
xG: 1.21 - 0.27
Corners: 7 - 1
Momentum: 51 - 39
Shots On Target: 5 - 2
Shots Off Target: 18 - 3
Attacks: 106 - 24
Dangerous Attacks: 57 - 10
Yellow Cards: 1 - 1
Red Cards: 0 - 0
Penalties: 0 - 0
Substitutions: 2 - 2
Possession %: 76 - 24
Crossing Accuracy %: 26 - 0
➕ Live Stats (https://inplayguru.com/inplay?caid=telegram_btn_inline#cURhRWVVUU1ZU009)

1X2 Pre-Match Odds:
1.40 5.00 7.00
1X2 Live Odds:
1.83 2.30 11.00
Over/Under 2.50 Odds:
1.44 2.63

📈 Matched: £233,652
⸻⸻⸻⸻⸻⸻
Powered by InPlayGuru (https://inplayguru.com/?mtm_campaign=telegram_banner)

✅ Hit
HT Score: 0-1
FT Score: 2-1'''

target = '''⚽️⚡️Dominator xG Alert
🌎 Copa Sudamericana
*Nacional Potosi vs Sportivo Trinidense*
Time: 68'
Score: 1 - 1
*xG: 1.21 - 0.27*'''


def test_format():
    res = format_message(data)
    assert res.text == target
    assert res.img_path == 'dominator.jpg'
