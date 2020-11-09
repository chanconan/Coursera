
import pandas as pd
import scipy.stats as stats

df = pd.read_csv('/Users/conanchan/Documents/Coursera/Python-Data_Analysis/IntroToDataSciPython/Week2/NISPUF17.csv',index_col=0)
df.columns = [x.lower().strip() for x in df.columns]
# Question 1
# def proportion_of_education():
#     df.columns = [x.lower().strip() for x in df.columns]
#     totalCount = len(df.index)
#     lessThanHighSchool = len(df[df["educ1"] == 1])/totalCount
#     highSchool = len(df[df["educ1"] == 2])/totalCount
#     notCollege = len(df[df["educ1"] == 3])/totalCount
#     college = len(df[df["educ1"] ==  4])/totalCount
#     proportion = {
#         "less than high school": lessThanHighSchool,
#         "high school": highSchool,
#         "more than high school but not college": notCollege,
#         "college": college
#     }
#     print(proportion)
#     return proportion

# assert type(proportion_of_education())==type({}), "You must return a dictionary."
# assert len(proportion_of_education()) == 4, "You have not returned a dictionary with four items in it."
# assert "less than high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
# assert "high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
# assert "more than high school but not college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
# assert "college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."

# Question 2
# Let's explore the relationship between being fed breastmilk as a child and getting a seasonal influenza vaccine from a healthcare provider. Return a tuple of the average number of influenza vaccines for those children we know received breastmilk as a child and those who know did not.
# This function should return a tuple in the form (use the correct numbers:
# (2.5, 0.1)

# df["CBF_01"] == 1 # Know received breastmilk 24261
# df["CBF_01"] == 2 # Know received breastmilk 4085
# df['P_NUMFLU'] # Number of seasonal vaccines doses

# def average_influenza_doses():
#     breastFed = df['p_numflu'].where(df['cbf_01'] == 1).dropna().mean()
#     notBreastFed = df['p_numflu'].where(df['cbf_01'] == 2).dropna().mean()
#     return (breastFed, notBreastFed)
# assert len(average_influenza_doses())==2, "Return two values in a tuple, the first for yes and the second for no."

# Question 3
# It would be interesting to see if there is any evidence of a link between vaccine effectiveness and sex of the child. 
# Calculate the ratio of the number of children who contracted chickenpox but were vaccinated against it (at least one varicella dose) 
# versus those who were vaccinated but did not contract chicken pox. Return results by sex.

# Vaccinated number will stay the same, change is sex and if had_cpox is 1 or 2.
# print(df[df['had_cpox'] == 1])
# print(df[df['p_numvrc'] > 0]) #only care about value exists, not amount (13995)
# print(df[df['sex'] < 1]) # 1 is male, 2 is female
# print(len(df[(df['p_numvrc'] > 0) & (df['had_cpox'] == 1) & (df['sex'] == 1)])) # 68 Male had cpox and vaccinated
# print(len(df[(df['p_numvrc'] > 0) & (df['had_cpox'] == 2) & (df['sex'] == 1)])) # 7028 Males did not get cpox and was vaccinated
# print(len(df[(df['p_numvrc'] > 0) & (df['had_cpox'] == 1) & (df['sex'] == 2)])) # 53 females had cpox and vaccinated
# print(len(df[(df['p_numvrc'] > 0) & (df['had_cpox'] == 2) & (df['sex'] == 2)])) # 6802 females did not get cpox and was vaccinated

def chickenpox_by_sex():
    hadCpoxMale = len(df[(df['p_numvrc'] > 0) & (df['had_cpox'] == 1) & (df['sex'] == 1)])
    noCpoxMale = len(df[(df['p_numvrc'] > 0) & (df['had_cpox'] == 2) & (df['sex'] == 1)])
    hadCpoxFemale = len(df[(df['p_numvrc'] > 0) & (df['had_cpox'] == 1) & (df['sex'] == 2)])
    noCpoxFemale = len(df[(df['p_numvrc'] > 0) & (df['had_cpox'] == 2) & (df['sex'] == 2)])
    chickenpox = {
        "male": hadCpoxMale/noCpoxMale,
        "female": hadCpoxFemale/noCpoxFemale
    }
    return chickenpox

assert len(chickenpox_by_sex())==2, "Return a dictionary with two items, the first for males and the second for females."

# Question 4
# A correlation is a statistical relationship between two variables. If we wanted to know if vaccines work, we might look at the correlation between the use of the vaccine and whether it results in prevention of the infection or disease [1]. In this question, you are to see if there is a correlation between having had the chicken pox and the number of chickenpox vaccine doses given (varicella).
# Some notes on interpreting the answer. The had_chickenpox_column is either 1 (for yes) or 2 (for no), and the num_chickenpox_vaccine_column is the number of doses a child has been given of the varicella vaccine. A positive correlation (e.g., corr > 0) means that an increase in had_chickenpox_column (which means more no’s) would also increase the values of num_chickenpox_vaccine_column (which means more doses of vaccine). If there is a negative correlation (e.g., corr < 0), it indicates that having had chickenpox is related to an increase in the number of vaccine doses.
# Also, pval is the probability that we observe a correlation between had_chickenpox_column and num_chickenpox_vaccine_column which is greater than or equal to a particular value occurred by chance. A small pval means that the observed correlation is highly unlikely to occur by chance. In this case, pval should be very small (will end in e-18 indicating a very small number).
# [1] This isn’t really the full picture, since we are not looking at when the dose was given. It’s possible that children had chickenpox and then their parents went to get them the vaccine. Does this dataset have the data we would need to investigate the timing of the dose?

# print(len(df[df['had_cpox'] == 2]) + len(df[df['had_cpox'] == 1])) #28357
# print(df[df['had_cpox'] > 2]) # 108
# print(len(df['had_cpox'])) # 28465
# new_df = df[(df['had_cpox'] == 1) | (df['had_cpox'] ==2)]
# # new_df = df[['had_cpox','p_numvrc']]
# print(new_df['p_numvrc'].dropna())
def corr_chickenpox():
    new_df = df[(df['had_cpox'] == 1) | (df['had_cpox'] ==2)]
    new_df = new_df[['had_cpox','p_numvrc']].dropna()
    corr2, pval2=stats.pearsonr(new_df['had_cpox'], new_df['p_numvrc'])
    return corr2, pval2
print(corr_chickenpox())
# assert -1<=corr_chickenpox()<=1, "You must return a float number between -1.0 and 1.0."
