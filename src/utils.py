from aiogram import md

from models import FormattedMsg

template = """⚽️⚡️{alert_name}
{league}
{rivals}
Match Time: {timer_value}
Current Score: {score}"""

img_dict = {
    'First Half Goal Signal': 'first_half_goal.jpg',
    'Late Goal Signal': 'late_goal.jpg',
    'Second Half Goal Signal': 'second_half_goal.jpg',
    'Lay The Draw Signal': 'lay_the_draw.jpg',
}


def format_message(text: str) -> FormattedMsg:
    xs = text.split("\n")
    alert_name = xs[0].split(' ', 1)[1]
    if alert_name.endswith('[Beta]'):
        alert_name = alert_name.removesuffix('[Beta]').strip()

    league = xs[2].split(' (')[0]
    rivals = xs[3]
    timer_line = xs[5]
    timer_value = timer_line.removeprefix('Timer: ')
    score_line = xs[8]
    score = score_line.removeprefix("Goals: ")
    formatted_msg = template.format(
        alert_name=alert_name,
        league=league,
        rivals=md.bold(rivals),
        timer_value=timer_value,
        score=score,
    )
    return FormattedMsg(text=formatted_msg, img_path=img_dict[alert_name])
