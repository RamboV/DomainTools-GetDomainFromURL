import tldextract


def extract_domain(url):
    extract_result = tldextract.extract(url)
    domain = f'{extract_result.domain}.{extract_result.suffix}'
    return domain