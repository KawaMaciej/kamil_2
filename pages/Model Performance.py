import streamlit as st
import pandas as pd
import json
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

##############################################
with open("model_information.json", "r") as f:
    model_information = json.load(f)  

model_names = model_information["Unique_names"]
model_scalers = model_information["Scaling_method"]
model_confusion_matrices = model_information["Confusion_Matrix"]
model_predictions = model_information["Predictions"]
model_accuracy = model_information["Accuracy"]

unique_model_names = model_names
unique_model_scalers = list(set(model_scalers))

with open("data_information.json", "r") as f:
    data_information = json.load(f)

X_train = data_information["training_set"]
X_test = data_information["test_set"]
Y_train = data_information["train_actual"]
Y_test = data_information["test_actual"]

##############################################
def roc_curve_plot(y, x):
    fpr, tpr, thresholds = roc_curve(y, x)
    roc_auc = auc(fpr, tpr)

    fig, ax = plt.subplots()
    ax.plot(fpr, tpr, color='blue', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
    ax.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.set_xlabel('False Positive Rate')
    ax.set_ylabel('True Positive Rate')
    ax.set_title('Receiver Operating Characteristic')
    ax.legend(loc="lower right")
    return fig
##############################################

st.title("Streamlit App for classification models")


tabs = st.tabs(unique_model_names)

for index, tab in enumerate(tabs):
    with tab:
        with st.spinner(f'Processing please wait...'):
            selected_option = st.radio("Scaling", unique_model_scalers, key = index, horizontal=True)
        if selected_option == "MinMaxScaler":
            st.write(f"Accuracy Score: {model_accuracy[index]}")
            st.write("Below is the confusion matrix for the given true and predicted labels:")
            cm_df = pd.DataFrame(model_confusion_matrices[index], 
                                 index=['Actual 0', 'Actual 1'], 
                                 columns=['Predicted 0', 'Predicted 1'])
            st.table(cm_df)
            fig = roc_curve_plot(Y_test, model_predictions[index])
            st.success(f'Processing of {selected_option} is complete!')
            st.title("ROC Curve")
            st.pyplot(fig)
        if selected_option == "StandardScaler":
            st.write(f"Accuracy Score: {model_accuracy[index+9]}")
            st.write("Below is the confusion matrix for the given true and predicted labels:")
            cm_df = pd.DataFrame(model_confusion_matrices[index+9], 
                                 index=['Actual 0', 'Actual 1'], 
                                 columns=['Predicted 0', 'Predicted 1'])
            st.table(cm_df)

            fig = roc_curve_plot(Y_test, model_predictions[index+9])
            st.success(f'Processing of {selected_option} is complete!')
            st.title("ROC Curve")
            st.pyplot(fig)

        if selected_option == "RobustScaler":
            st.write(f"Accuracy Score: {model_accuracy[index+18]}")
            st.write("Below is the confusion matrix for the given true and predicted labels:")
            cm_df = pd.DataFrame(model_confusion_matrices[index+18], 
                                 index=['Actual 0', 'Actual 1'], 
                                 columns=['Predicted 0', 'Predicted 1'])
            st.table(cm_df)

            fig = roc_curve_plot(Y_test, model_predictions[index+18])
            st.success(f'Processing of {selected_option} is complete!')
            st.title("ROC Curve")
            st.pyplot(fig)

        



