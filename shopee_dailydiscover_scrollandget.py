import uiautomator2 as u2
import logging
from uiautomator2 import Direction


app = 'com.shopee.ph'
activity = 'com.shopee.app.ui.home.HomeActivity_'

def swipe_to_next():
    d.swipe_ext("up", scale=0.725)
    d.swipe_ext("up", scale=0.725)

def get_item_data():
    for element in d(textContains='₱'):
        log.info(element.sibling(className='android.widget.TextView')[0].get_text())
        if(element.sibling(className='android.widget.TextView')[2].exists(timeout=0.1)):
            log.info(element.sibling(className='android.widget.TextView')[2].get_text())
        else:
            log.info(element.sibling(className='android.widget.TextView')[1].get_text())


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')
log = logging.getLogger('shopee.bot')
d = u2.connect('V8GQDISCQOZHZXK7')
d.unlock()
d.app_start(package_name=app, activity=activity, stop=True)
d.xpath('//androidx.viewpager.widget.ViewPager/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[7]').click_exists(timeout=10)
log.info(d(textContains='Daily Discover'))
while((d(text ='DAILY DISCOVER')).exists(timeout=0.1) != True):
    d.swipe_ext(Direction.FORWARD)
    log.info(d(textContains='DAILY DISCOVER').exists(timeout=1))
    if((d(text ='DAILY DISCOVER')).exists(timeout=0.1) == True):
        d.swipe_ext(Direction.FORWARD)
        break #end loop to start scraping items from daily discover

for i in range(0,10):
    swipe_to_next()
    get_item_data()