from flask import Flask, render_template, request
from markupsafe import Markup
app = Flask(__name__)

@app.route("/",methods=['POST', 'GET'])
def test():
    error_message = ''
    output1 = ''
    output2 = ''
    hightText = ''
    finalText = ''
    inputText = ''
    inputStart = ''
    inputEnd = ''
    if request.method == 'POST':
        inputText = request.form.get('inputText')
        inputStart = request.form.get('inputStart')
        inputEnd = request.form.get('inputEnd')
        flag = True
        if inputText == '':
            error_message = 'Input Text cannot be blank.'
            flag = False
        if inputStart == '' and flag:
            error_message = 'Start index cannot be blank.'
            flag = False
        if inputEnd == '' and flag:
            error_message = 'End index cannot be blank.'
            flag = False
        if not flag:
            return render_template('home.html',error_message=error_message,values={'inputText':inputText, 'inputStart':inputStart, 'inputEnd':inputEnd})
        else:
            startIndex = 0
            endIndex = 0
            try:
                startIndex = int(inputStart)
                endIndex = int(inputEnd)
            except ValueError:
                error_message = 'Start and End index has to be integers.'
                return render_template('home.html',error_message=error_message,values={'inputText':inputText, 'inputStart':inputStart, 'inputEnd':inputEnd})
            if startIndex<=0 or endIndex<=0:
                error_message = 'Start and end index have to be a positive integers.'
                return render_template('home.html',error_message=error_message,values={'inputText':inputText, 'inputStart':inputStart, 'inputEnd':inputEnd})
            if endIndex<startIndex:
                error_message = 'End index has to be greater than start index.'
                return render_template('home.html',error_message=error_message,values={'inputText':inputText, 'inputStart':inputStart, 'inputEnd':inputEnd})
            text_len = len(inputText)
            if startIndex>text_len or endIndex>text_len:
                error_message = 'Specified indices out of bound than given text.'
                return render_template('home.html',error_message=error_message,values={'inputText':inputText, 'inputStart':inputStart, 'inputEnd':inputEnd})
            startIndex = startIndex-1
            endIndex = endIndex-1
            output1,highText,output2 = inputText[:startIndex],inputText[startIndex:endIndex+1],inputText[endIndex+1:]
            finalText = Markup(output1+'<span class="highlight">'+highText+'</span>'+output2)

    return render_template('home.html',error_message=error_message,finalText=finalText, values={'inputText':inputText, 'inputStart':inputStart, 'inputEnd':inputEnd})

if __name__=='__main__':
    app.run()
