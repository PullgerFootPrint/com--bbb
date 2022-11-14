from pullgerInternalControl import pIC_pFP


def get_search_result_list(session):
    issue_list = []
    list_group = session.find_xpath(xpath="//div[@class='stack stack-space-20']")

    inner_elements = list_group.finds_xpath(xpath="./child::div")
    for cur_inner_elements in inner_elements:
        element_class_name = cur_inner_elements.get_attribute("class")
        if element_class_name is not None:
            if element_class_name.find('MuiPaper-root') != -1:
                issue_list.append(cur_inner_elements)
    return issue_list


def pull_profile_id(web_element):
    profile_url_element = web_element.find_xpath(xpath=".//a[@class='css-1rni3ap eou9tt70']")
    url = profile_url_element.get_attribute("href")
    id_name_crude = url.split("/")[-1]
    id_name_profile = id_name_crude.split('?')[0]
    return id_name_profile


def pull_profile_city_keys(web_element):
    profile_url_element = web_element.find_xpath(xpath=".//a[@class='css-1rni3ap eou9tt70']")
    url = profile_url_element.get_attribute("href")
    url_split_call = url.split("//")
    url_split = url_split_call[-1].split("/")

    id_iso_country = url_split[1]
    id_iso_state = url_split[2]
    id_name_city = url_split[3]

    response = {
        'id_iso_country': id_iso_country,
        'id_iso_state': id_iso_state,
        'id_name_city': id_name_city
    }
    return response


def get_number_of_page_pagination(session):
    pagination_block = session.find_xpath(xpath="//div[@class='css-vdjz9q e170djn40']")
    page_number_pagination_block = pagination_block.find_xpath(xpath=".//span[@class='bbb__hideAt-xsDown']")
    split_test = page_number_pagination_block.text.split(" ")
    if split_test[0] == "PAGE":
        try:
            number_of_page = int(split_test[-1])
        except BaseException as e:
            pIC_pFP.ElementNotFound(
                msg="Incorrect information on pagination",
                level=40,
                exception=e
            )
    else:
        pIC_pFP.ElementNotFound(
            msg="Incorrect determine pagination number",
            level=40
        )
    return number_of_page


def get_page_number_on_pagination(session):
    pagination_block = session.find_xpath(xpath="//div[@class='css-vdjz9q e170djn40']")
    page_number_pagination_block = pagination_block.find_xpath(xpath=".//span[@class='bbb__hideAt-xsDown']")
    splitted_test = page_number_pagination_block.text.split(" ")
    if splitted_test[0] == "PAGE":
        return int(splitted_test[1])
    else:
        pIC_pFP.ElementNotFound(
            msg="Incorrect determine pagination number"
        )


def get_next_url(session):
    pagination_nav_block = session.find_xpath(xpath="//nav[@aria-label='pagination']")
    operation_list = pagination_nav_block.finds_xpath(xpath=".//li")
    if operation_list[-1].text == "Next":
        next_element = operation_list[-1].find_xpath(xpath=".//a")
        return next_element.get_attribute("href")
    else:
        pIC_pFP.ElementNotFound(
            msg="Incorrect determine Next element"
        )

