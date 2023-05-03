from bs4 import BeautifulSoup

def count_html_tags(filepath, tag_name):
    with open(filepath, 'r') as html_file:
        html_content = html_file.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        tag_list = soup.find_all(tag_name)
        count = 0
        for tag in tag_list:
            if len(tag.contents) > 0:
                count += 1
        return count

count = count_html_tags("index.html", "p")
print(count)