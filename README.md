<img width="20%" src="./assets/logo_1.png">

# Grub Recommendation Bot (SMTP/SMS)

> A simple weekly restaurant suggestion bot service.

<a href="#"><img alt="Python" src="https://img.shields.io/badge/Python-4584b6.svg?logo=python&logoColor=ffcc00&style=for-the-badge"></a>
<a href="#"><img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub%20Actions-8d3f8d.svg?logo=github%20actions&logoColor=white&style=for-the-badge"></a>
<a href="#"><img alt="SMTP / SMS" src="https://custom-icon-badges.demolab.com/badge/SMTP%20/%20SMS-orange.svg?logo=server&logoColor=white&style=for-the-badge"></a>
<a href="#"><img alt="Cron" src="https://img.shields.io/badge/Cron-372923.svg?logo=ubuntu&logoColor=white&style=for-the-badge"></a>
<!--<a href="#"><img alt="discord.py" src="https://img.shields.io/badge/discord.py-4584b6.svg?logo=discord&logoColor=ffcc00&style=for-the-badge"></a>-->

## Overview
Utilizes GitHub Actions and Cronjob Scheduling with SMTP/Email and SMS messaging services.
- **GitHub Action Workflow** builds and runs the job every **Friday**, at **12:00PM**. `(00 12 * * 5)`
- A random Restaurant is selected from a list of available/nearby restaurants, that have the `lowest` visitation integer.
- A random message prompt is also determined, and is sent to multiple **Emails and Phone Numbers**.

> *Note: Phone Numbers, Emails, and Webhooks are stored for security through **Secrets** on the public repository.*

<br>

[![Run Grub-Bot-Pipeline](https://github.com/LordBramster/Grub-Recommendation-Bot-SMS-SMTP/actions/workflows/actions.yml/badge.svg)](https://github.com/LordBramster/Grub-Recommendation-Bot-SMS-SMTP/actions/workflows/actions.yml)

Future integrations will include: `Google Maps API`, `Discord Bot/Webhooks`

## SMS/SMTP Demo

Once the `Workflow Job` finishes, an SMS/SMTP message is sent to the available end-users.
- All Email Address and PHone Numbers on this Repo are safely stored as environment variables and GitHub secrets.
- When the `Workflow Job` executes, it will pull the Secret from the repo into a local environment var on the server instance.
- The script will ping each SMS/SMTP destination found within the converted list of Addresses.

<p align="center">
    <a href="#"><img width="50%" src="./assets/demo_1.png"></a>
</p>

## Resources
- https://www.verizon.com/about/news/vzw/2013/06/computer-to-phone-text-messaging  
