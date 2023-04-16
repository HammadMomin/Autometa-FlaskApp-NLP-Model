#####LATEST#########

from flask import Flask, request
import papermill as pm


app = Flask(__name__)

##################################################

@app.route('/', methods=['POST'])
def run_notebook():
    data = request.get_json()
    text = data.get('text')
    question = data.get('question')
    
    output_file = 'QAS_output.ipynb'
    ans_file = 'QAS_ans.txt'
    pm.execute_notebook(
        'QAS.ipynb',
        output_file,
        parameters=dict(text=text , question=question , ans_file = ans_file)
    )
    with open(ans_file, 'r') as f:
        output_text = f.read()
    return output_text
    


if __name__ == '__main__':
   app.run()




