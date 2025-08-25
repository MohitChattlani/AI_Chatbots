import requests
from bs4 import BeautifulSoup

# The page you want to scrape
url = "https://teslaberry.in/"

pages = [
    "https://teslaberry.in/contest.php",
    "https://teslaberry.in/index.php",
    "https://teslaberry.in/privacy_policy.php",
    "https://teslaberry.in/podcasts.php",
    "https://teslaberry.in/advertise.php",
    "https://teslaberry.in/form.php",
    "https://teslaberry.in/featured_section.php",
    "https://teslaberry.in/featured_section_submit.php",
    "https://teslaberry.in/featured_section_list.php?category=blog",
    "https://teslaberry.in/featured_section_list.php?category=question",
    "https://teslaberry.in/featured_section_list.php?category=short",
    "https://teslaberry.in/iq_test.php",
    "https://teslaberry.in/iq_test_attempt.php?category=test1",
    "https://teslaberry.in/iq_test_attempt.php?category=test2",
    "https://teslaberry.in/iq_test_attempt.php?category=test4",
    "https://teslaberry.in/iq_test_attempt.php?category=test5",
    "https://teslaberry.in/iq_test_attempt.php?category=test6",
    "https://teslaberry.in/iq_test_attempt.php?category=test7",
    "https://teslaberry.in/iq_test_attempt.php?category=test8",
    "https://teslaberry.in/iq_test_attempt.php?category=test9",
    "https://teslaberry.in/iq_test_attempt.php?category=test10",
    "https://teslaberry.in/subject_test.php",
    "https://teslaberry.in/iq_test_attempt.php?category=test3",
    "https://teslaberry.in/display_puzzles.php",
    "https://teslaberry.in/lateral_showlevels.php",
    "https://teslaberry.in/read.php",
    "https://teslaberry.in/about.php",
    "https://teslaberry.in/connect.php"
]

all_content = ""

for url in pages:
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    texts = soup.stripped_strings
    all_content += f"\n\n--- Page: {url} ---\n" + "\n".join(texts)

with open("teslaberry_content_final.txt", "w", encoding="utf-8") as f:
    f.write(all_content)

