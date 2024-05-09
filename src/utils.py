template = """🔔 GOAL ALERT
{league}
{rivals}

Match Time: {timer_value}
Current Score: {score}
Pre-Match Odds:
{pre_match_odds}
Current Live Market:
{current_live_market}
"""


def format_message(text: str):
    xs = text.split("\n")
    league = xs[2]
    rivals = xs[3]
    timer_line = xs[5]
    timer_value = timer_line.removeprefix('Timer: ')
    score_line = xs[8]
    score = score_line.removeprefix("Goals: ")
    pre_odds_title_idx = xs.index('1X2 Pre-Match Odds:')
    pre_match_odds = xs[pre_odds_title_idx + 1]
    current_live_market = xs[pre_odds_title_idx + 3]
    formatted_msg = template.format(
        league=league,
        rivals=rivals,
        timer_value=timer_value,
        score=score,
        pre_match_odds=pre_match_odds,
        current_live_market=current_live_market,
    )
    return formatted_msg
