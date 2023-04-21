# Autometa Flask App (NLP Model)

Below Are the Steps to Run This Application On your System
--------------------------------------------------------------------
<ins>**Step 1:**</ins> To clone the repository, use the following command:
```
git clone https://github.com/HammadMomin/Autometa-FlaskApp-NLP-Model.git
```
<ins>**Step 2:**</ins> Go to project directory folder and run this Command.
```
python -m venv venv
```
This Above Command will create a virtual environment named as "venv" in the Project Directory. This Command Will Not Work If You don't have Python in Your Machine. If Not then install it from https://www.python.org/downloads/ and Include this in your System Environment Variables Inside the Path. After This You are Good to run the above command for creating the virtual environment. 

<ins>**Step 3:**</ins> To Activate your virtual environemnt i.e venv. Run the Following Command. 
```
venv\Scripts\activate.bat
```
This Will Activate the Virtual And You Can See Something Like This On your Terminal.

![venv terminal](https://user-images.githubusercontent.com/99894207/233696776-a7000a45-14b3-4d53-b95d-cf4bd6ef1966.png)

<ins>**Step 4:**</ins> To Install All the Packages And Libraries Used In the Project. Run the Following Command. <ins>**NOTE:**</ins> Only Run this Command after Activating the virtual environment as Shown in above Step 
```
pip install -r requirements.txt
```
<ins>**Step 5:**</ins> To run the Pyhton Script. Execute the Following Command.
```
python app.py
```
Now You Can See Your Flask Applicaton Is Running at Port http://127.0.0.1:5000.

![Flask Terminal](https://user-images.githubusercontent.com/99894207/233700006-5de2facb-4b43-4fa8-8c97-70551201e55a.gif)

--------------------------------------------------------------------------------------------------------------------------------

* After This Your Flask Application is Ready To take 2 Variables as "text" and "questions" from nodeJs application (https://github.com/HammadMomin/Autometa-Web-App.git) with the help of axios.post method And Serve it to the Jupyter Notebook i.e "QAS.ipynb" as a input varibales by using papermill library. After Execution it Gernerates Output Notebook i.e "QAS_outuput.ipynb" and output.txt 

* From the output.txt file we are extracting the output and send it back to nodeJS (To Display it to the Frontend Of the Web Application) 

* Below is Shown that when the axios.post request get hitted from nodeJS then it will Act as API and Execute the Notebook And Send the Output Back. 

![2023-04-21 23-52-04](https://user-images.githubusercontent.com/99894207/233710529-aa34bece-1dcd-40d6-8be5-0fbaf36eb72a.gif)

------------------------------------------------------------------------------------------------------------------------------
If You May Have Any Queries, You Can Reach me Out At `mohdhammad.momin@gmail.com`


 

