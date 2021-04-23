import uiautomator2 as u2
import logging
from uiautomator2 import Direction


app = 'com.shopee.ph'
activity = 'com.shopee.app.ui.home.HomeActivity_'

def search_item(item): #types the item in the search bar and press enter
    d.xpath('//androidx.viewpager.widget.ViewPager/\
        android.widget.LinearLayout[1]/\
            android.widget.FrameLayout[1]/\
                android.widget.FrameLayout[1]/\
                    android.view.ViewGroup[3]').child('android.widget.TextView').click()
    d.send_keys(str(item),clear=True)
    d.press('enter')

def swipe_to_next():
    d.swipe_ext("up", scale=0.725)
    d.swipe_ext("up", scale=0.725)

def get_item_data():
    for element in d(textContains='₱'):
        if('off' in element.sibling(className='android.widget.TextView')[0].get_text()): #has promo
            log.info(element.sibling(className='android.widget.TextView')[0].up(className='android.widget.TextView').get_text() + ' : ' + element.sibling(className='android.widget.TextView')[3].get_text())
        elif(element.sibling(className='android.widget.TextView')[3].exists(timeout=0.1) == False): #discounted
            log.info(element.sibling(className='android.widget.TextView')[0].get_text() + ' : ' + element.sibling(className='android.widget.TextView')[2].get_text())
        else: #no discounts or promo
            log.info(element.sibling(className='android.widget.TextView')[0].get_text() + ' : ' + element.sibling(className='android.widget.TextView')[1].get_text())


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')
log = logging.getLogger('shopee.bot')
d = u2.connect('V8GQDISCQOZHZXK7')
d.unlock()
d.app_start(package_name=app, activity=activity, stop=True)
d.xpath('//androidx.viewpager.widget.ViewPager/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[7]').click_exists(timeout=10)
search_item('sharpie')
d(textContains='sold').wait(timeout=10)
for i in range(0,2):
    if i==0:
        d.swipe_ext("up", 0.51)
        get_item_data()
    swipe_to_next()
    get_item_data()