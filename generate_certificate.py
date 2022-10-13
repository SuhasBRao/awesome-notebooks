import os

from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
from bs4 import BeautifulSoup


org_profile_url = os.environ["org_profile_url"]
repo_name = os.environ["repo_name"]
date_of_contribution = os.environ["date"]
contributor_name = os.environ["contributor_name"]
issue_name = os.environ["issue_title"]
issue_id = "1212"
pr_name = os.environ["pr_name"]

# These are accessed later by few functions
template_path = "certificate-template.png"
default_font_path = "Roboto-Regular.ttf"
content_font_path = "AnonymousPro-Regular.ttf"

print("Inside Python:")
print("PR name:", pr_name)
print("ORG url:", org_profile_url)
print("Repo name", repo_name)
