import ConfigParser
import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup
import html2text
# what is this? imports bring in pre-written code you want to use

# this is a script. there's no hard and fast definition of a script.
# i tend to think of it as code that does everything in one go,
# like this one which does everything in the 'main' function
def main():

	# first, let's get your username and password using ConfigParser, more here:
	# https://wiki.python.org/moin/ConfigParserExamples
	# how did i figure out how to do this? i googled how to add a python config
	# and followed the example!
	conf = ConfigParser.ConfigParser()
	conf.read('config.ini')

	# i can print things out anytime to see what they really are,
	# but sometimes i have to convert them to a string to read them,
	# hence the str() part. how do i know to use str? well, i didn't use
	# it the first time, and python complained that it couldn't print this,
	# so i added it. try changing str(conf.sections()) to just conf.sections()
	# and running this script again, and you'll see what i mean
	print 'Here are the config sections: ' + str(conf.sections())

	username = conf.get('LinkedInCredentials', 'username')
	password = conf.get('LinkedInCredentials', 'password')

	# did i successfully get the username and password? let's see...
	print username + ": " + password

	# now we need to log in and get a 'cookie' from LinkedIn that says
	# we're ok to look at stuff. mmmmmmm cookies!!!
	#	            .---. .---. 
	#               :     : o   :    me want cookie!
	#           _..-:   o :     :-.._    /
	#       .-''  '  `---' `---' "   ``-.    
	#     .'   "   '  "  .    "  . '  "  `.  
	#    :   '.---.,,.,...,.,.,.,..---.  ' ;
	#    `. " `.                     .' " .'
	#     `.  '`.                   .' ' .'
	#      `.    `-._           _.-' "  .'  .----.
	#        `. "    '"--...--"'  . ' .'  .'  o   `.
	#        .'`-._'    " .     " _.-'`. :       o  :
	#      .'      ```--.....--'''    ' `:_ o       :
	#    .'    "     '         "     "   ; `.;";";";'
	#   ;         '       "       '     . ; .' ; ; ;
	#  ;     '         '       '   "    .'      .-'
	#  '  "     "   '      "           "    _.-'
	# i googled this to figure it out too, and used this 
	# http://stackoverflow.com/questions/20039643/how-to-scrape-a-website-that-requires-login-first-with-python
	# wait, what are cookies again? 
	# https://en.wikipedia.org/wiki/HTTP_cookie
	
	# Browser
	br = mechanize.Browser()

	# Cookie Jar
	cj = cookielib.LWPCookieJar()
	br.set_cookiejar(cj)

	# Browser options
	br.set_handle_equiv(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

	br.addheaders = [('User-agent', 'Chrome')]

	# The site we will navigate into, handling it's session
	br.open('https://www.linkedin.com/uas/login?goback=&trk=hb_signin')

	# on this LinkedIn site, there's only 1 form. select the first form 
	# by saying it's form number ZERO, because computers start counting
	# at zero, not one like pesky humans.
	br.select_form(nr=0)

	# User credentials
	br.form['session_key'] = username
	br.form['session_password'] = password

	# Login
	br.submit()

	print(br.open('https://www.linkedin.com/messaging').read())

	# enter LinkedIn search terms at the command line

	# get the main search results page(s)

	# scrape email addresses

	# stick into a CSV file

	

if __name__ == "__main__":
	main()
