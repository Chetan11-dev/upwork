from string import Template
from greatawesomeutils.lang import *

def is_empty_string(x):
    return x.strip() == ''

if __name__ == "__main__":
    linkedin_lead_gen = '''$greeting$name,
I understand that you need a LinkedIn Lead Generation Expert who could provide you with high quality leads$industry.

I am a confident in my ability to provide you with 100% verified 📞 Phone and ✉️ Email.

Let me share with you 2 instances in which my LinkedIn Lead Generation Expertise helped generate Revenue for my Clients.

1. HealthCare 
Here we wanted to sell a Health Care system to Surgeons in the US. I was able to provide my Client with verified leads who were then 📞 called leading to successful conversions.

2. Marketing Services
Here we wanted to market Client's Shopify and Facebook Ad running skills. Here also, I provided my Clients with valuable leads which helped generate business for the Client.

I am attaching an image and excel sheet describing the result you will get as proof.

Also, I am ready to provide you with a free sample of 20 LinkedIn Leads so you may see quality of leads by yourself.
Let's Connect,

$thanks,
Chandan Kumar'''

    lead_gen1 = '''$greeting$name,
I understand that you need a Lead Generation Expert who could provide you with high quality leads __ONELINE_NEED__.

I am a Lead Generation Expert who is confident in his ability to provide you with 100% verified 📞 Phone Numbers and ✉️ Email.

Let me share with you 2 instances in which my Lead Generation Expertise helped generate Revenue for my Clients.

1. HealthCare 
Here we wanted to sell a Health Care system to Surgeons in the US. I was able to provide my Client with verified leads who were then 📞 called leading to successful conversions.

2. Marketing Services
Here we wanted to market Client's Shopify and Facebook Ad running skills. Here also, I provided my Clients with valuable leads which helped generate business for the Client.

I am attaching an image and excel sheet describing the result you will get as proof.

Also, I am ready to provide you with a free sample of 20 Leads so you may see quality of leads by yourself.
Let's Connect,

$thanks,
Chandan Kumar'''


    lead_gen2 = '''$greeting$name,
I understand that you need a list of high quality leads __ONELINE_NEED__.

I am GIVING YOU 25 LEADS FOR FREE so that you can understand my work and quality before hiring me.

MY PROCESS FOR FINDING LEADS:

Sources - My primary sources for data are LinkedIn. I have access to LinkedIn Sales Navigator, but if needed I can also use Inside view, CrunchBase Pro, AngelList, Google, Manta, Findthebest.com, Inc500, hoovers, jigsaw, find the company Zoom Info, Bigz, Data.com, twitter, yellow pages, Pipl.com, and other social networks to expand my searchability.

E-mail Finding Tools - I use many premium and free tools to find email addresses like Email Hunter, FTL, Lead 411, sell hack, emailgenerator.io, etc.

Verifying Emails - To verify Emails I use Rapportive, mailtester.com, validateemailaddress.org, verifyemailaddress.io, www.verifyemailaddress.org, email-checker.net, and a paid email verifier called Atom park to check for bounces. I only provide 100% verified Emails.

Let's jump on a quick call or chat and discuss this project in detail.

$thanks,
Chandan Kumar'''


    web_scraping = '''$greeting$name,
I understand that you need _ONELINE_ need.

I am very capable to create such a Bot for you with fast turnaround Time. 

Let me tell you about 2 of my 🤖 that I build to solve problems of my Upwork Clients.

1. G2 Scraper 🤖
This Scraper scrapes g2.com for valuable Product Informations. I had to use residential proxies and captcha solving solutions like 2captcha to scrape G2.

2. AngelList Scraper 🤖
This Scraper scrapes New Jobs posted on AngelList which is quite helpful to Jobseekers.

I have attached video demonstration of these bots so you may see them in Action :). 

Looking forward to helping you.
$thanks,
Chandan Kumar'''

    blank = '''$greeting$name,
I understand that you need a Lead Generation Expert who could __ONE_LINE_PROPSITION__.

I am a __STACK__ Expert who is confident in his ability to __CLIENT__TASK__

__GIVE_PROJECT_EXAMPLES__

I am attaching __WHAT__.
Let's Connect,

$thanks,
Chandan Kumar'''

    templates = {
        'Linkedin Lead Generation': linkedin_lead_gen,
        'Lead Generation 1': lead_gen1,
        'Lead Generation 2': lead_gen2,
        'Blank' : blank, 
        'Web Scraping' : web_scraping 
    }

    
    result = ''
    index = 1
    for i in templates:
        result += f'   {index}. {i}\n'
        index += 1

    result = result.strip()

    template_option = int(input(f'''Choose Template: 
   {result}
''').strip())

    key = list(templates.keys())[template_option - 1]
    template_data = templates[key]
    vars = {}

    if key == 'Linkedin Lead Generation':
        industry = input('Industry: ').strip()
        vars['industry'] = '' if is_empty_string(industry) else f' of {industry} Industry'

    name = input('Client Name: ').strip()
    country_code = input('Client Country Code (IN, FR, DE, IT, CN OR Leave Blank): ').strip().upper()


    vars['name'] = '' if is_empty_string(
        name) else f' {name}'

    if country_code == 'IN':
        greeting = '🙏 Namaste'
        thanks = 'Dhanyawad'
        final_name = vars['name']

        # if not is_empty_string(final_name):
        #     vars['name'] = f'{final_name} Ji' 
    elif country_code == 'FR':
        greeting = '👋 Bonjour Monsieur'
        thanks = 'Merci'
    elif country_code == 'DE':
        greeting = '👋 Hallo Herr'
        thanks = 'Vielen Dank'
    elif country_code == 'IT':
        greeting = '👋 Ciao Signore'
        thanks = 'Grazie'
    elif country_code == 'CN':
        greeting = '👋 Nǐ hǎo'
        thanks = 'Xièxiè nǐ'
    else:
        greeting = '👋 Sir'
        thanks = 'Thanks'
        
        # 
    vars['greeting'] = greeting
    vars['thanks'] = thanks


    form = Template(template_data)
    data = form.substitute(vars)
    write_file('working.md', data)
    
    print('REMEMBER TO ATTACH THE ATTACHMENTS, THE PROFILE IS IN ./working.md')
