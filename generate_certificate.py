import os

from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
from bs4 import BeautifulSoup


org_profile_url = os.environ('org_profile_url')
repo_name = "awesome-notebooks"
date_of_contribution = "04/10/2022"
contributor_name = "Suhas B"
issue_name = "Pillow - Generate a certificate template #1212"
issue_id = "1212"
pr_name = os.environ['pr_name']

# These are accessed later by few functions
template_path = "certificate-template.png"
default_font_path = "Roboto-Regular.ttf"
content_font_path = "AnonymousPro-Regular.ttf"

print("PR name:", pr_name)
print("ORG url:", )