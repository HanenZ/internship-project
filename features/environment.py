from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from support.logger import logger
from app.application import Application


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """

    # ## CHROME Browser #
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    ##  FIREFOX Browser #
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    ## SAFARI Browser #
    # context.driver = webdriver.Safari()


    # HEADLESS MODE #
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument('--window--size=1920*1080')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )
    # recommended by Jeff in case test case fails with headless mode
    # driver.set_window_size(1920, 1080)


    ## BROWSERSTACK #|

    bs_user = 'hanenzoghlami_YcXQE1'
    bs_key = 'VGrJssvZYcgq7jaSCjwx'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    options = Options()
    bstack_options = {
        'os': 'OS X',
        'osVersion': 'Ventura',
        'browserName': 'Firefox',

        'sessionName': scenario_name
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.set_window_size(1920, 1080)
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)
    # context.driver.maximize_window()



def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    logger.info(f'Started step: {step}')
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        # Screenshot:
        # context.driver.save_screenshot(f'step_failed_{step}.png')
        print('\nStep failed: ', step)
        logger.error(f'Step failed: {step}')


def after_scenario(context, feature):
    context.driver.quit()