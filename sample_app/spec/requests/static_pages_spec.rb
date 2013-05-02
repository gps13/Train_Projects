require 'spec_helper'

describe "Static pages" do

  describe "Home page" do #we describing the Home page, this is string!!! can be anything!!!!

#when you visit home @/static_pages/home content should have words "Sample App"
    it "should have the content 'Sample App'" do	#what goes inside the quote marks is irrelevant to RSpec, and is intended to be descriptive to human readers.
      visit '/static_pages/home'					# uses the Capybara function visit to simulate visiting the URI /static_pages/home in a browser
      page.should have_content('Sample App')	#uses the page variable (also provided by Capybara) to test that the resulting page has the right content
    end
  end

  describe "Help page" do #we describing the Help page, this is string!!! can be anything!!!!

#when you visit home @/static_pages/help content should have words "Help"
    it "should have the content 'Help'" do	#what goes inside the quote marks is irrelevant to RSpec, and is intended to be descriptive to human readers.
      visit '/static_pages/help'					# uses the Capybara function visit to simulate visiting the URI /static_pages/help in a browser
      page.should have_content('Help')	#uses the page variable (also provided by Capybara) to test that the resulting page has the right content
    end
  end
  
  describe "About page" do #we describing the About page, this is string!!! can be anything!!!!
#when you visit home @/static_pages/about content should have words "About Us"
    it "should have the content 'About Us'" do	#what goes inside the quote marks is irrelevant to RSpec, and is intended to be descriptive to human readers.
      visit '/static_pages/about'					# uses the Capybara function visit to simulate visiting the URI /static_pages/help in a browser
      page.should have_content('About Us')	#uses the page variable (also provided by Capybara) to test that the resulting page has the right content
    end
  end

end