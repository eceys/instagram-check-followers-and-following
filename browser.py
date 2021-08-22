from selenium import webdriver
import time
import infoUserPanel as info

listFollows = []
listFollowers = []

class Browser:

    def __init__(self, link):
        self.link = link
        self.browser = webdriver.Chrome()
        Browser.goLink(self)

    def goLink(self):
        self.browser.get(self.link)
        time.sleep(3)
        Browser.login(self)
        followersList = Browser.getFollowers(self)
        time.sleep(4)
        Browser.goHomePage(self)
        time.sleep(2)
        followingList = Browser.getFollowing(self)
        time.sleep(4)
        Browser.check(self)
        time.sleep(2)
        Browser.goHomePage(self)



    def getFollowers(self):
        self.browser.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(4)

        Browser.scrollDown(self)

        followersList = self.browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")

        for follower in followersList:
            print(follower.text)
            listFollowers.append(follower.text)

        return followersList

    def getFollowing(self):
        self.browser.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[3]/a").click()
        time.sleep(4)

        Browser.scrollDown(self)

        followingList = self.browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
        print("Follow ------------------")
        for follow in followingList:
            print(follow.text)
            listFollows.append(follow.text)

        return followingList


    def scrollDown(self):
        jsCommand = """
    		page = document.querySelector(".isgrP");
    		page.scrollTo(0,page.scrollHeight);
    		var pageEnd = page.scrollHeight;
    		return pageEnd;
    		"""
        pageEnd = self.browser.execute_script(jsCommand)
        while True:
            end = pageEnd
            time.sleep(1)
            pageEnd = self.browser.execute_script(jsCommand)
            if end == pageEnd:
                break


    def login(self):
        username = self.browser.find_element_by_name("username")
        password = self.browser.find_element_by_name("password")

        username.send_keys(info.usurname)
        password.send_keys(info.password)

        time.sleep(4)

        loginButton = self.browser.find_element_by_xpath("//*[@id=\"loginForm\"]/div/div[3]")
        loginButton.click()
        time.sleep(5) # ifyou have a phone verification make this here 25 seconds e.g. time.sleep(25)

        Browser.goHomePage(self)

    def goHomePage(self):
        self.browser.get(self.link + "/" + info.usurname)
        time.sleep(3)

    def check(self):
        print("\nYou are following but he/she not following you : ")
        for follow in listFollows:
            check = 0
            for follower in listFollowers:
                if follow == follower:
                    check = 2
                    break
                else:
                    check = 1
            if check == 1:
                print(follow)


