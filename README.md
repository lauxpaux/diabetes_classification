# Diabetes Classification

## Processes and tools:
* Exploratory data analysis: Notebook documenting variable correlations and processes that lead to data processing functions

## Models: 
* K Nearest Neighbor: https://github.com/lauxpaux/diabetes_classification/blob/main/01-k-nearest-neighbors.py.ipynb
* Support Vector Classifer: https://github.com/lauxpaux/diabetes_classification/blob/main/02-support-vector-classification.py.ipynb
* Decision Tree Classifier: https://github.com/lauxpaux/diabetes_classification/blob/main/03-decision-tree-classifier.py.ipynb
* Random Forest Classifier: https://github.com/lauxpaux/diabetes_classification/blob/main/04-random-forest-classifier.py.ipynb
* Logistic Regression Classifier: https://github.com/lauxpaux/diabetes_classification/blob/main/05-logistic-regression-classifier.py.ipynb



## Motivations:
Diabetes is a chronic disease that interferes with the body's ability to digest sugar, causing sugar levels to build up in the blood stream. When left untreated, a build up of sugar in the blood stream can cause blockage in the arteries, block bloodflow to the extremities, and eyes. Further complications from the blockages may cause heart disease/heart attacks, loss of extremities and/or vision loss.

There are three different types of diabetes:

Type 1: Also known as Juvenile diabetes, is chronic and occurs to younger patients due to the pancreas not being able to produce any or enough insulin.
Type 2: Happens to predominantly adult patients, onset from lifestyle habits such as poor diet, or sedentary lifestyle. In type 2, the body makes less insulin or becomes resistant to insulin.
Gestational: Occurs when women aren't able to produce enough insulin during pregnancy.
To prevent complications from diabetes, patients must monitor sugar levels in the blood through bi/annual or annual A1C tests and daily pricks, adapt better diet and lifestyle habits to manage weight, and use the hormone insulin to digest sugar if their bodies stop producing it or don't produce enough.

Why is this a problem? Currently, diabetes affects 37 million people a year, and costs the US $327 million dollars in healthcare costs, and loss of time costs. In addition, Diabetes is the 7th leading cause of death in the United States and it could become an even bigger problem as obesity rates increase. Diabetes can be difficult to manage but it is not impossible.

How can this project help? This project uses healthcare data to train a KNN model to classify diabetes outcome in patients based on other health outcomes. In many healthcare settings, existing patient data can be used to help prioritize at-risk patients with the preventative care that they need. For example, patients that the model identifies as diabetic can be given priority lab appointments to confirm their A1Cs, or have priority for nutritional counceling appointments.

## Data:
The dataset for this project was obtained from Kaggle. It was sourced from the National Institute of Diabetes and Digestive and Kidney Diseases, and it consists of female patients that are 21 years or older and of Pima Indian descent.

This dataset is interesting because it captures diabetes and health outcomes of minority women of color, a group that has a long and complicated history with modern healthcare practices, from being victims of unethical practices in the United States, as was the case with the birth control trials on unsuspecting Puerto Rican women in the 1930s , to lacking the resources to access modern healthcare [4]. Healthcare needs of women are different from men, and as the FemTech industry continues to grow, it is not only important to research how to improve womens' health outcomes, but it is also more profitable since women have higher needs of care [5], [6], [7]. Furthermore, women's health is one of the biggest determinants of population health, and currently infant mortality rate is one of the strongest measures of a country's well being [8]. Still, infant mortality rates in the United States are the worst among minority women of color [9].

While this project focuses on identifying diabetes among women to improve health outcomes and administer early intervention efforts, it is also a commentary on the healthcare system's need to gain the trust of women of color, and adapt to the needs of minority women.

The data columns are:
Pregnancy
Glucose
Blood Pressure
SkinThickness
Insulin
BMI
DiabetesPedigreeFunction
Age
Outcome
We'll be using the other columns to predict feature 9: Diabetes diagnoses (0, 1) where 0 = No, 1 = Yes


## Conclusion:
<img width="393" alt="image" src="https://user-images.githubusercontent.com/40530704/232136579-db761d30-da32-4ba2-aec4-2e24335a8613.png">
As shown in the confusion matrix, and classification report above, we managed to increase recall from 80% to 95%, while keeping precision for positive cases at around 84%, and the f1-score at 85%. As we mentioned earlier, our goal was to aim for a higher recall for harm reduction, even if it meant losing a little bit of precision.

What this means for our project is that our model has gotten better at identifying positive diabetic patients in the whole dataset, even if those positive classifications weren't all true positive (diabetic) patients. We would rather have a few patients turn out to not be diabetic, than have a higher number of patients believe that they don't have diabetes when they in fact do.

We have succesfully achieved our goal of building a model that can help us identify diabetic patients!

This concludes our Diabetes Classification with KNN project. Some of the ways that we can expand on this project are:

Finding or sourcing data on different health outcomes for women in the United States, to broaden patient outreach and model usability.
Further analysis into the 3 different types of diabetes, including measuring our model's ability to predict based on Type 1, Type 2 and Gestational diabetes.
Evaluate patient outcomes for children of women who had gestational diabetes thus incorporating family history into the dataset somehow. Are individuals born to mothers who had gestational diabetes more likely to develop Type 1, or Type 2 diabetes in their lifetime?
