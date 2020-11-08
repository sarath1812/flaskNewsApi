from flask import Flask ,render_template,request 

from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='18bb29c9b5f24cdc96c666adfad78411')

# /v2/top-headlines





apple = Flask(__name__) 
 
@apple.route("/")

def home ():
    return render_template('home.html',news='')

      
@apple.route('/results/',methods=['POST'])
def get_results(): 
    keyword = request.form['keyword']
    top_headlines = newsapi.get_top_headlines(q=keyword,language='en',country='in')
    data=top_headlines['articles']
    

    return render_template('home.html',news=data)





if __name__=="__main__":
    apple.run(debug=False)