from aiogram import md

from models import FormattedMsg

template = """⚽️⚡️{alert_name}
{league}
{rivals}
Time: {timer_value}
Score: {score}
{xg_line}"""

img_dict = {
    'Lay The Leader xG Alert': 'lay_the_leader.jpg',
    'Drifter xG Alert': 'drifterScreen.png',
    'Dominator xG Alert': 'dominator.jpg',
    '+1 xG Alert': 'plus_one.jpg',
    'LTD xG Alert': 'lay_the_draw.jpg',
    'HotDog xG Alert': 'hot_dog.jpg',
    '+2 xG Alert': 'plus_two.jpg',
}


def format_message(text: str) -> FormattedMsg:
    xs = text.split("\n")
    alert_name = xs[0].split(' ', 1)[1]
    league = xs[2].split(' (')[0]
    rivals = xs[3]
    timer_line = xs[5]
    timer_value = timer_line.removeprefix('Timer: ')
    score_line = xs[8]
    score = score_line.removeprefix("Goals: ")
    xg_line = ''
    if 'xG' in xs[9]:
        xg_line = xs[9]
    formatted_msg = template.format(
        alert_name=alert_name,
        league=league,
        rivals=md.bold(rivals),
        timer_value=timer_value,
        score=score,
        xg_line=md.bold(xg_line),
    )
    return FormattedMsg(text=formatted_msg, img_path=img_dict[alert_name])
