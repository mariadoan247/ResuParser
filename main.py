import pandas as pd

resumes = pd.read_csv("UpdatedResumeDataSet.csv")

for i in range(len(resumes)):
    info = resumes.iloc[i][1]
    yes = abs(info[i].count('d'))
    if yes > 0:
        print(f'{i} is a good resume')
    else:
        print(f'{i} is a bad resume')


# category = input("""
# Choose Category:
# 1. Data Science
# 2. HR
# """)
#
# if category == 1:
#     print("Data Science")
# else:
#     print("hi")

# if __name__ == '__main__':
#     print("Hello World! This is ResuParser!")