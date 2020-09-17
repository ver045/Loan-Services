# OVERVIEW
We identified a problem users face when applying for a loan through loan service companies. 
The problem is that when an applicant applies for a loan, part of the process is going through credit checking, or credit inquiries,
which ultimately affects the applicant's credit score. That being said, we came up with a solution by building a user-friendly service
that eliminates these credit inquiries in which a loan applicant simply inputs non-identifiable but relevant information to estimate 
their interest rate of that loan.

The information needed is:
- loan amount
- annual income
- credit score
- home ownership status (rent, own, mortgage status)
- loan terms (12, 24, 36 month repayment plan)


# PROCESS
We obtained our data from Lending Club, used AWS (Amazon Web Services) to store all the data, and used Google Colab as our notebook for data wrangling. Some of the tools used were Pandas and Pyspark to clean the data and store into dataframes, as well as data conversion, dropping null values and getting rid of any inconsistant data.

The next step was the feature engineering process, in which we had to extract and store our features into a new dataframe. This new dataframe made it much more easy to just focus on the data that was relevant so that we can start building our models. Once we built our models, we had to test and check for accuracy. After comparing models for best accuracy, we then deployed the final product using Flask app and ran it in our local server.

