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
            server.sendmail(email_sa, email_addr, msg.as_string())
            server.quit()
        print('\t > SENT | STMPLIB.SMTP-SERVER SENDMAIL !')


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


def pull_format_message_string(filename):
    """ pull template string to format with args """
    with open(filename, 'r') as file:
        lines = file.read()
        file.close()
    formatted = lines.format(restaurant_choice=restaurant_choice, email_prompt=email_prompt)
    return formatted


if __name__ == '__main__':
    print('\n\n\t------------------------------------------------------------------')

    # CREDENTIALS
    config = json.load(open('./config.json', ))
    stage = config['environment'].upper()
    print('\t > DONE | CONFIG.JSON LOADED ...')

    try:
        if stage == 'DEV':
            # DEV
            test_creds = json.load(open('./secret/secret.json', ))
            email_sa = test_creds['ENV_ESA']
            email_sf = test_creds['ENV_ESF']
            email_k = test_creds['ENV_EK']
            email_c = test_creds['ENV_EC']
            email_b = test_creds['ENV_ESA']
            smtp_server = test_creds['ENV_E_H']
            smtp_port = test_creds['ENV_E_P']
            email_c_conv = email_c
            print('\t > DONE | SECRET.JSON LOADED ...')

        elif stage == 'PROD':
            # PROD
            email_sa = os.environ['ENV_ESA']
            email_sf = os.environ['ENV_ESF']
            email_k = os.environ['ENV_EK']
            email_c = os.environ['ENV_EC']
            email_b = os.environ['ENV_ESA']
            smtp_server = os.environ['ENV_E_H']
            smtp_port = os.environ['ENV_E_P']
            email_c_conv = json.loads(email_c)
            print('\t > DONE | GIT-SECRETS LOADED ...')

        else:
            # CANCEL
            raise Exception

        print('\t > DONE | CREDENTIALS CONFIRMED ...')

        # GRAB RESTAURANT CHOICE
        restaurant_list = './data/restaurants.json'
        restaurants = json.load(open(restaurant_list, 'rb'))
        restaurant_candidates = pull_lowest_score_dest(restaurants['restaurants'])
        restaurant_choice = restaurant_candidates[random.randint(0, len(restaurant_candidates) - 1)]
        print('\t > DONE | SELECTED RESTAURANT ...')

        # UPDATE GRUB SCORES
        push_update_score_tally(restaurant_choice, restaurants)
        print('\t > DONE | UPDATE TALLY SCORE ...')

        # MAKE MESSAGE
        if stage == 'PROD':
            # PROD
            email_prompts = open('./data/prompts.txt').readlines()
            email_prompt = email_prompts[random.randint(0, len(email_prompts) - 1)]
        else:
            # DEV
            email_prompt = '< THIS MESSAGE IS PART OF A TEST, PLEASE DISREGARD >'
        print('\t > DONE | PROMPT HAS BEEN SELECTED ...')

        # FORMAT MESSAGE TEMPLATE
        email_m = pull_format_message_string('./data/message_template.txt')
        email_e = email_m.encode('utf-8')
        print('\t > DONE | PARSE/FORMAT/AUTOFILL MESSAGE TEMPLATE ...')

        # SEND EMAIL
        send_email()
        print(f'\t > DONE | {str(len(email_c_conv))} EMAIL(S) SENT !')

    except Exception as err:
        if stage == 'DEV':
            # DEV
            print(f'\t > ERR | {err} ...')
        else:
            # PROD
            print(f'\t > ERR | EXCEPTION HAS BEEN THROWN. MUTED FOR SECURITY ...')

    print('\n\t------------------------------------------------------------------')
# FIN
