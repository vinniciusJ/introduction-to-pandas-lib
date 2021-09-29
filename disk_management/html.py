import webbrowser
import os

def show_html(content):
    page_content = f'<html><head></head><body>{content}</body></html>'

    with open('index.html', 'w') as page:
        page.write('')
        page.write(page_content)
        page.close()

    filename = f'file:///{os.getcwd()}/index.html'
    webbrowser.open_new_tab(filename)