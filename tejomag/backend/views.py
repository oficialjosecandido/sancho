from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup

def teste():
    pass

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def get_news_details(request, link=None):
    try:
        # Test URL if none provided
        link = link or 'https://www.noticiasaominuto.com/pais/2759910/conselho-de-ministros-ou-campanha-no-bolhao-partidos-criticam-governo'

        # Fetch and parse page
        r = requests.get(link, headers=headers)
        r.raise_for_status()
        soup = BeautifulSoup(r.content, 'html.parser')

        # Extract content
        title = soup.find('h1', class_='lg:text-headline').text.strip()
        lead = soup.find('h2', class_='lg:text-lead').text.strip()
        source = soup.find('div', class_='text-darkgray').find('p', class_='font-thin').text.strip()

        # Paraphrase content
        paraphrased_lead = lead 

        # Get body content (first 3 paragraphs for demo)
        body_paragraphs = soup.find('div', class_='article-content').find_all('p')[:3]
        original_body = '\n'.join(p.text.strip() for p in body_paragraphs)
        paraphrased_body = original_body

        return JsonResponse({
            "title": title,
            "original_lead": lead,
            "paraphrased_lead": paraphrased_lead,
            "source": source,
            "original_body": original_body,
            "paraphrased_body": paraphrased_body,
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)