# Top216 Promo Code API & Homepage Banner

This Django project implements a promo code validation API and a simple homepage banner for the Top216 global awards platform, as part of the Alatree Ventures tech assessment.

---

## Features

- **POST `/api/apply-promo/`**  
  Validates promo codes and tiers, returns JSON with discounted price or error message.  
  Supported promo codes (example): `FLASH7`, `SUMMER20`, `WELCOME10`.

- **Homepage Banner**  
  Clean, modern banner following brand guidelines with teal and lime colors, Montserrat and Roboto fonts, and a call-to-action button.

---

## Getting Started

### Prerequisites

- Python 3.x
- Django

### Installation

```bash
git clone <your-repo-url>
cd <repo-folder>
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
pip install django
python manage.py migrate
python manage.py runserver
