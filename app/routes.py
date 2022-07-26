from app import app
from flask import render_template

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/favorite_5')
def favorite():
    top5 = [
    {'name':'Takato Yamamoto', 'img':'https://files2.theloop.com.au/534723_Uncoloured-small.jpg?t=project-image'},
    {'name':'Audrey Kawasaki', 'img':'https://images.squarespace-cdn.com/content/v1/5a33fcb7914e6bb1202a2e0b/1513738860731-I3EWX0G4CKHM0LMUGJLI/self02.jpg?format=1500w'},
    {'name':'Michael Turner', 'img':'https://dennisupkins.files.wordpress.com/2017/05/8949772_orig.jpg?resize=700%2C445'},
    {'name':'Wayne Barlowe', 'img':'https://i0.wp.com/waynebarlowe.com/wp-content/uploads/2011/03/73984_171712942857723_100000570543852_476593_4385088_n1.jpg?resize=300%2C201'},
    {'name':'Shepard Fairey', 'img':'https://www.thoughtco.com/thmb/hsQFYlP_6GLLqwZXLxZxou2HIgY=/2667x2000/smart/filters:no_upscale()/obey-x-levi-s-collection-launch-92536927-5b847c22c9e77c0050540d86.jpg'}
    ]
    return render_template('favorite_5.html', artists = top5)