# ResuParser
An AI program that will parse through resumes and choose those that fit certain requirements

# Summary
Recruiters spend a lot of time skimming through resumes to find the best candidate for a job position. Since there can be hundreds of applications for a single position, this process has been automated in several ways — the most common is keyword matching. Resumes are shortlisted and read by the recruiters based on a set of keywords found in a candidates resume. Otherwise, the resume is discarded, and the candidate is rejected for the job. However, this screening process has many drawbacks. Candidates are aware of the keyword matching algorithm, and many of them insert as many keywords as possible into their resumes to get shortlisted by the company.

You can build a resume parser with the help of artificial intelligence and machine learning techniques that can skim through a candidate’s application and identify skilled candidates, filtering out people who fill their resume with unnecessary keywords.

You can use the Resume Dataset available on Kaggle to build this model. This dataset contains only two columns — job title and the candidate’s resume information.

The data is present in the form of text and needs to be pre-processed. You can use the NLTK Python library for this purpose. Then, you can build a clustering algorithm that groups closely related words and skills that a candidate should possess in each domain. Words that are similar in context (and not just keywords) should be considered. You can assign a final weightage score to each resume — from 0 (least favourable) to 10 (most favourable).
