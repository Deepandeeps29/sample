class Library_Locator:
    # ! Register Page
    Url = "https://demoapps.qspiders.com/"
    UI_Test="//p[text()='UI Testing Concepts']/following-sibling::div"
    Practice_Session_Text = "//button[normalize-space(text())='Practice Session']"
    Text_Field_Button = "//section[normalize-space(text())='Text Field']"
    Register_Text = "//h1[normalize-space(text())='Register']"
    Signup_Name = "//input[@placeholder='Enter your name']"
    Signup_Email = "//input[@placeholder='Enter Your Email']"
    Signup_Password = "//input[@placeholder='Enter your password']"
    Signup_Submit_Button = "//button[@type='submit']"
    
    # ! Login Page
    
    Login_Url = "https://demoapps.qspiders.com/ui/login"
    Login_Page_Text = "//h1[normalize-space(text())='Login']"
    Login_Email = "//input[@type='email']"
    Login_Password = "(//label[normalize-space(text())='Password']/following::input)[1]"
    Login_Submit_Button = "//button[@type='submit']"
    
    
    # ! Button Page
    
    Button_Page = "//section[normalize-space(text())='Button']"
    Button_Page_Text = "//h3[normalize-space(text())='Feed Back On Shopping Registration']"
    Button_Page_Yes_Button = "//button[normalize-space(text())='Yes']"
    Button_Page_Yes_Button_Text = "//button[contains(@class,'active:bg-green-400 transition-all')]/following-sibling::span[1]"
    Button_Page_No_Button = "//button[normalize-space(text())='No']"
    Button_Page_No_Button_Text = "//button[contains(@class,'active:bg-green-400 transition-all')]/following-sibling::span[1]"
    
    
    # ! Check Box
    
    CheckBox_Button = "//section[normalize-space()='Check Box']"
    CheckBox_Button_Text = "//h1[normalize-space(text())='Checkout Page']"
    CheckBox_Select_Domain = "(//input[@name='Domain'])[1]"
    CheckBox_Select_mode = "(//span[normalize-space(text())='Sandals']/following::input)[1]"
    CheckBox_Submit_Button = "//input[@type='submit']"
    CheckBox_Select_mode_2 = "(//span[normalize-space(text())='Regarding the same product']/following::input)[1]"


    # ! Radio Button
    
    Radio_Button = "//section[normalize-space(text())='Radio Button']"
    Radio_Button_Title = "//h1[normalize-space(text())='Checkout Page']"
    Radio_Button_Payment_1 = "//input[@value='Upi']"
    Radio_Button_Payment_2 = "//input[@value='cod']"
    Radio_Button_Delivery = "//input[@value='home']"
    Radio_Button_Continue = "//button[normalize-space(text())='Continue']"
    
    
    
    
    
    
    
    
    