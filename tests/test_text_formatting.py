from src.utils import format_message

data = '''🔔 Test 1

🇩🇪 Germany Regionalliga North (3rd vs 8th)
Phonix Lubeck vs Hamburg SV II

Timer: 10'
Last Goal: Home at 7' (3 minutes ago)

Goals: 1 - 0
Corners: 1 - 0
Momentum: 47 - 3
Shots On Target: 1 - 0
Shots Off Target: 0 - 0
Attacks: 15 - 4
Dangerous Attacks: 10 - 0
Yellow Cards: 0 - 1
Red Cards: 0 - 0
Penalties: 0 - 0
Substitutions: 0 - 0
Possession %: 86 - 14
➕ Live Stats (https://inplayguru.com/inplay?caid=telegram_btn_inline#cjNtekRxMnV2WVk9)

1X2 Pre-Match Odds:
1.75 4.00 3.80
1X2 Live Odds:
1.25 6.00 8.50
Over/Under 1.50 Odds:
1.01 15.00

📈 Matched: £144
⸻⸻⸻⸻⸻⸻
Powered by InPlayGuru (https://inplayguru.com/?mtm_campaign=telegram_banner)'''

target = '''🔔 GOAL ALERT
🇩🇪 Germany Regionalliga North (3rd vs 8th)
Phonix Lubeck vs Hamburg SV II

Match Time: 10'
Current Score: 1 - 0
Pre-Match Odds:
1.75 4.00 3.80
Current Live Market:
1.25 6.00 8.50
'''


def test_format():
    res = format_message(data)
    assert res == target
