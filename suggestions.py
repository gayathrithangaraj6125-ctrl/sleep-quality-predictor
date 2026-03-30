
def get_suggestions(stress, screen_time, exercise):

    tips = []

    if stress > 7:
        tips.append("Reduce stress using meditation or relaxation")

    if screen_time > 60:
        tips.append("Reduce screen time before sleep")

    if exercise < 20:
        tips.append("Increase daily exercise")

    if len(tips) == 0:
        tips.append("Your habits look good!")

    return tips