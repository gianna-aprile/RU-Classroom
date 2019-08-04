from flask import Flask, render_template, request, flash
from search import checkTime


app = Flask(__name__)

app.secret_key = "o=*nqy39b+3v^4n80l$ysa^52sskccgf216#yt95t!5m9+gr$o"

@app.route('/')
def getForm():
   return render_template('my-form.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      campus = request.form['campus']

      day = request.form['day']
      
      hour = request.form['hour']

      minutes = request.form['minutes']

      try:
         amOrPm = request.form['amOrPm']         
      except:
         flash("ERROR: Select AM or PM")
         return render_template('my-form.html') 

      # Cast hour and minutes to ints for the search method
      # Convert to military time
      if amOrPm == "am" or hour == "12":
         newHour = int(hour)
      else:
         newHour = int(hour) + 12

      newMinutes = int(minutes)

      roomsAndLinks = checkTime(campus, day, newHour, newMinutes)
   
      return render_template("result.html",campus = campus, day = day, hour = hour, minutes = minutes, amOrPm = amOrPm, list = roomsAndLinks)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
   #app.run(debug = True)