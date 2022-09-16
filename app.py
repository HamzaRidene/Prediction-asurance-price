import pandas as pd
import joblib
import streamlit as st

def main():
    st.title("Prédiction du prix d'assurance maladie avec ML")
#st.header()

    model=joblib.load("model_gr")

    p1=st.slider("Enter your age ",18,100)

    s1=st.selectbox('Sex',('Male','Femal'))
    if s1=="Male":
        p2=1
    else :
        p2=0

    p3=st.number_input("Enter your BMI value ")

    p4=st.slider("Enter your children number ",0,5)    

    s5=st.selectbox('Smoker',('Yes','No'))
    if s5=="Yes":
        p5=0
    else :
        p5=1

    p6=st.slider("Enter your region ",0,4) 

    if st.button("predict"):
        pred=model.predict([[p1,p2,p3,p4,p5,p6]])
        st.balloons()
        st.success("Your Insurance Coast is {}".format(round(pred[0],2)))

if __name__=='__main__':
    main()




