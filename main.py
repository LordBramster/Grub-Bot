import json
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


def send_email():
    """ send email to each address provided """
    for email_addr in email_c_conv:
        msg = MIMEMultipart()
        msg['From'] = email_sa
        msg['To'] = email_addr
        msg['Subject'] = email_b
        msg.attach(MIMEText(email_m, 'plain'))
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email_sf, email_k)
            server.sendmail(email_sf, email_addr, msg.as_string())
            server.quit()


def pull_random_food_category(food_types):
    """ pull_random_food_category(restaurants['restaurants'].keys()) """
    food_types_all = list(food_types)
    return food_types_all[random.randint(0, len(food_types_all) - 1)]


def pull_lowest_score_dest(restaurants):
    """ lowest_score = str(min(restaurants.values())) """
    min_scores = [place_name for place_name, x in restaurants.items() if not any(y < x for y in restaurants.values())]
    return min_scores


def push_update_score_tally(restaurant_selection, restaurant_dict):
    """ update restaurant scores (JSON) with new tally """
    restaurant_score = restaurant_dict['restaurants'][restaurant_selection]
    restaurant_score += 1
    restaurant_dict['restaurants'][restaurant_selection] = restaurant_score
    json.dump(restaurant_dict, open(restaurant_list, "w"))


if __name__ == '__main__':
    print('\n\n------------------------------------------------------------------')

    # PULL EMAIL DATA
    email_sa = os.environ['ENV_ESA']
    email_sf = os.environ['ENV_ESF']
    email_k = os.environ['ENV_EK']
    email_c = os.environ['ENV_EC']
    email_b = os.environ['ENV_ESA']
    smtp_server = os.environ['ENV_E_H']
    smtp_port = os.environ['ENV_E_P']

    # PROCESS EMAIL DATA
    email_c_conv = json.loads(email_c)

    print('PROCESSED ENV VARS FOR EMAIL CREDS ... [PASSED]')

    # GRAB RESTAURANT CHOICE
    restaurant_list = './data/restaurants.json'
    restaurants = json.load(open(restaurant_list, 'rb'))
    restaurant_candidates = pull_lowest_score_dest(restaurants['restaurants'])
    restaurant_choice = restaurant_candidates[random.randint(0, len(restaurant_candidates) - 1)]
    print('SELECTED RESTAURANT FOR WEEK ... [PASSED]')
    push_update_score_tally(restaurant_choice, restaurants)
    print('PUSH SCORE TALLY UPDATE ... [PASSED]')

    # MAKE MESSAGE
    email_prompts = open('./data/prompts.txt').readlines()
    email_prompt = email_prompts[random.randint(0, len(email_prompts) - 1)]
    print('EMAIL RAND PROMPT SELECTED ... [PASSED]')
    email_m = f"🍽️ Here is your weekend grub of interest:" \
              f"\n{restaurant_choice}!" \
              f"\n{email_prompt}" \
              f"\t- {email_b}"
    email_e = email_m.encode('utf-8')

    # SEND EMAIL
    print(f'\n{email_m}\n')
    send_email()
    print('EMAIL(S) SENT ... [PASSED]')
    print('\n------------------------------------------------------------------')
# FIN
