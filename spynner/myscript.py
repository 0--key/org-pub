from time import sleep
from spynner import browser
br = browser.Browser(
#    debug_level=4
)
br.load('http://pypi.python.org/pypi')
br.create_webview()
br.show()

br.wk_fill('input[id=term]', 'spynner')
br.wk_click("input[id=submit]", wait_load=True, timeout=5)
print("Noticed the search")
sleep(3)

anchors = br.webframe.findAllElements('#menu ul.level-two a')
anchor = [a for a in anchors if 'Browse' in a.toPlainText()][0]
br.wk_click_element_link(anchor, timeout=10)
print("Noticed the click on the browse")
sleep(3)
