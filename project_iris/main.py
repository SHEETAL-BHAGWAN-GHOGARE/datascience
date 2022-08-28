from flask import Flask,render_template,request,jsonify

my_app = Flask(__name__)

@my_app.route('/')   ### Default API
def index():
    return render_template('index.html')

# @my_app.route('/get_data')  ### Default GET Method 
# def get_data():
#     data = request.form['var']
#     data1 = request.form['var1']
#     print(f"{data=},{data1=}")
    
#     return "Data Receieved"



# @my_app.route('/get_data', methods = ['GET','POST'])  ### Default GET Method 
# def get_data():
#     data = request.form['var']
#     data1 = request.form['var1']
#     print(f"{data=},{data1=}")
    
#     return "Data Receieved"


# @my_app.route('/get_data', methods = ['GET','POST'])  ### Default GET Method 
# def get_data():
#     if request.method == 'POST':
#         data = request.form['var']
#         data1 = request.form['var1']
#         print(f"{data=},{data1=}")
#     else:
#         var = request.form['var']
#         print(f"{var=}")
#         print("POST method not used")


# @my_app.route('/get_data', methods = ['POST'])  ### Default GET Method 
# def get_data():
#     if request.method == 'POST':
#         data = request.form['var']
#         data1 = request.form['var1']
#         print(f"{data=},{data1=}")
#     else:
#         var = request.form['var']
#         print(f"{var=}")
#         print("POST method not used")
    
#     return "Data Receieved"

# @my_app.route('/get_data', methods = ['GET','POST'])  ### Default GET Method 
# def get_data():
#     data = request.form
    
#     print(f"{data=}")
#     print(type(data))
#     data_from_imm = data['var1']
#     print(data_from_imm)
    
#     return jsonify(data)

@my_app.route('/get_data', methods = ['GET','POST'])  ### Default GET Method 
def get_data():
    data = request.get_json() ### DATA in form in dict
    
    print(f"{data=}")
    print(type(data))
    data_from_imm = data['var1']
    print(data_from_imm)
    
    return jsonify(data)

@my_app.route('/getdata', methods = ['GET','POST'])  ### Default GET Method 
def getdata():
    data = request.json ### DATA in form in dict
    
    print(f"{data=}")
    print(type(data))
    data_from_imm = data['var1']
    print(data_from_imm)
    
    return jsonify(data)


@my_app.route('/data', methods=['GET','POST'])
def data():
    var = request.args #### This for query params 
    print(var)
    print(type(var))

    return jsonify(var)


if __name__ == "__main__":
    my_app.run(debug=True)
