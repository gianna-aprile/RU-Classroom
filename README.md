# RU Classroom
Our goal was to create a website where Rutgers students could easily find open classrooms to study in.

- **[RU Classroom](https://ruclassroom.herokuapp.com/)**


## How We Scraped the Course Data

- In order to determine which rooms are empty we first used Selenium to scrape the Rutgers schedule of classes (Link [Here](https://sis.rutgers.edu/soc/#subjects?semester=12019&campus=NB&level=U)). This is all done in the courseScraper.py file. This python prorgram is run once per semester and will scrape all of that semesters class data and store it in a txt file.

- To replicate this process there are a few lines that need to be changes to run per user.
  
    1. On line 9 the user name must be changed from my computers name to your own. This gets the driver for selenium to control the browser. We used Chrome but there are other drivers which can be found online if you use a different browser.
   
    ```
    driver_path = "/Users/kylelitton/FinalProject/chromedriver"
    ```
    
    2. On line 10 be sure to update the link with the correct semester's schedule of classes. This will change each semester.
    
    ```
    browser.get("https://sis.rutgers.edu/soc/#subjects?semester=12019&campus=NB&level=U")
    ```
    
    3. The last change you may need to make is line 11, this names the text file and should be changed for the corresponding text file.
    
    ```
    f = open("spring2019.txt", "w+")
    ```
    
   
## How We Used The Data

- The next step was creating the search.py file. This used the data from the semester.txt file and the input that comes from the user in app.py (Such as Campus, Time, and Weekday). In this program we had to filter out the rooms that did not fit the provided times slot.

- Once we were able to get the list of rooms that are open during this time, we decided it would be best to let the user know how much longer the room is open for. We did by going through the data once again, this time looking for the next time the class is occupied.

- We wanted the users to be able to find the resulting rooms as easily as possible. To simplify this we used Selenium again to scrape [The Rutgers Map Website](https://maps.rutgers.edu/#/?lat=40.2488462127653&lng=-74.70583984375003&sidebar=true&zoom=8). This code can be found in CreateRoomInfo.py. We searched the building codes that were in the resulting list from search.py and returned the buildings location that is used in a hyperlink on out website.

## The Website and Hosting

- Neither of us ever have had the chance to build a website before. For this project we decided to use Flask to create our website, and Heroku to host it.

- While neither of us had experiance with Flask or HTML, this project provided an opportunity to learn as much as we can. We were able to create a user friendly website that displays the desired information in clear way. 

- Note: if you want to run app.py to view the website localy, be sure to uncomment 
  
  ```
     #app.run(debug = True)
  ```
  Then comment out the following line, this is left for production deployment only
  
  ```
     app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
     ```

- **[RU Classroom](https://ruclassroom.herokuapp.com/)**


   
