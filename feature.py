from flask import Flask,render_template
FAI=Flask(__name__)

@FAI.route('/send_html')
def send_html():
    return render_template('send_html.html',name='LOKESH CHATTA')


@FAI.route('/Properties')
def Properties():
    return render_template('Properties.html')

if __name__ == '__main__':
    FAI.run(debug=True)