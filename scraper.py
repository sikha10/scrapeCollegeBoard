from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver = 'E:\selenium chromedriver\chromedriver.exe'

driver = webdriver.Chrome(chrome_driver)
driver.get("https://bigfuture.collegeboard.org/college-search/filters?aa=fafis&mc=Computer_Science")
driver.set_window_position(2000, 0)
driver.maximize_window()
driver.implicitly_wait(10)


college_count_div = driver.find_elements(By.CSS_SELECTOR, 'div[class="row no-gutters"]')

if len(college_count_div) == 28:
    college_count_container = college_count_div[-3].find_element(By.CSS_SELECTOR, 'div[id="cs-show-number-of-results"]')
    college_count = college_count_container.find_element(By.CSS_SELECTOR, 'span[class="cb-roboto-medium"]').get_attribute('innerHTML')
    print(college_count)

    colleges_container = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="cs-search-results-list"]')

    while True:
        all_colleges_containers = colleges_container.find_elements(By.CSS_SELECTOR, 'div[class="cs-college-card-outer-container"]')

        if len(all_colleges_containers) == int(college_count):
            break

        try:
            more_colleges_button_container = driver.find_element(By.CSS_SELECTOR, 'div[class="col-xs-8 offset-xs-2 col-md-6 offset-md-3 col-lg-4 offset-lg-4"]')
            more_colleges_button = more_colleges_button_container.find_element(By.CSS_SELECTOR, 'button[aria-label="Show More Colleges"]')
            driver.execute_script("arguments[0].click();", more_colleges_button)
        except:
            print('click error')
        
    count = 0
    all_colleges_lst = []

    for college in all_colleges_containers:
        link = college.find_element(By.TAG_NAME, 'a').get_attribute("href")
        all_info_div = college.find_element(By.CSS_SELECTOR, 'div[class="cs-college-card-details cb-white-bg"]')
        name_div = all_info_div.find_element(By.CSS_SELECTOR, 'div[class="cs-college-card-details-address cb-padding-bottom-16"]')
        name = name_div.find_element(By.CSS_SELECTOR, 'span[class="cs-college-card-college-name-link-text"]').get_attribute('innerHTML')

        more_info_div = all_info_div.find_element(By.CSS_SELECTOR, 'div[class="cs-college-card-details-profile cb-roboto-light"]')
        extra_info_div = more_info_div.find_element(By.CSS_SELECTOR, 'div[class="cb-no-padding"]')
        extra_info_ul = extra_info_div.find_element(By.TAG_NAME, 'ul')
        extra_info_li_lst = extra_info_ul.find_elements(By.TAG_NAME, 'li')
        extra_info_li_str = ''
        for extra_info_li in extra_info_li_lst:
            extra_info_li_str += extra_info_li.get_attribute('innerHTML') + "--"

        try:
            grad_rate_div = more_info_div.find_element(By.CSS_SELECTOR, 'div[data-testid="cs-college-card-details-profile-school-graduation-rate"]')
            grad_rate = grad_rate_div.find_element(By.TAG_NAME, 'strong').get_attribute('innerHTML')
        except:
            grad_rate = 'None'

        try:
            avg_cost_div = more_info_div.find_element(By.CSS_SELECTOR, 'div[data-testid="cs-college-card-details-profile-school-average-cost"]')
            avg_cost = avg_cost_div.find_element(By.TAG_NAME, 'strong').get_attribute('innerHTML')
        except:
            avg_cost = 'None'

        try:
            sat_score_div = more_info_div.find_element(By.CSS_SELECTOR, 'div[data-testid="cs-college-card-details-profile-school-sat-range"]')
            sat_score = sat_score_div.find_element(By.TAG_NAME, 'strong').get_attribute('innerHTML')
        except:
            sat_score = 'None'
        
        college_dict = {
            "name": name,
            "link": link,
            "info": extra_info_li_str,
            "grad_rate": grad_rate,
            "average cost per year after aid": avg_cost,
            "sat score": sat_score
        }

        all_colleges_lst.append(college_dict)
        count += 1
        print(college_dict)
        print(count)

    print(all_colleges_lst)

    print(count)
    print(len(all_colleges_lst))
        

else:
    print('not 28')

