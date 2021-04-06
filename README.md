# BookmarkAPI

This is API version of Bookmark project.

Computer Vision tab

Implementation through machine learning models.
Implementation through deep learning models.
Implementation through artificial intelligence models.

API & Web Tab

Implementation through python.
Implementation through javascript.

MAJOR NEXT STEP IN API PROJECT:

1) Add security to user_profile and core app as done in recipe app api.
Desc -> only token authenticated users are able to do CRUD of all app. Add tests.
2) Implement other features taken frsom bookmark project in this api.
Desc -> add machine learning, deep learning and ai in data science tab. add project feature. add API tab feature.
3) Make Front end for this api.
Desc -> Make it minimalist and fast.

THINK ON:

1) Content Creation
2) Coloring
3) Project Creator
4) Tagging
5) Segregating Viewsets
6) Models and its features
7) Slug
8) Messaging
9) Add money making feature (usp for investor)
10) Speed of website and storage requirements
11) Sponsor, RSS, Subscribe


Apps :

Core : single point of models for Full project
User Profile : All thing related to user like comment promote and share, except posts. Plan it later
Post : All thing related to posts for profile or on other apps. Plan it later
Datascience : For Data Science related functionality (Tutorial and Articles) Current
Fullstack : For Full Stack related functionality (Tutorial and Articles) Next
<!-- Design : For design of all types e.g. game, automobile, buildings, software & content, hardware etc. -->
Project : Plan it later
Article : All authenticated user can make a project but only reputed user(usp for my client) are able to make articles.Integrate & Plan later

""" MODEL DETAILS """
User Model is used for managing authenticated users. Think about profile relation with this model later.

Post Model is used for posting on my profile, other profiles, other posts and other projects and its comment. Three types : Profile Post, Project Post, Status / Personal Post. Utilize Django 2.1/2.2 Old Course Project's Post model.

Project Model is used for getting user project details and for content for datascience and fullstack models. Need a good post submission editor. Tagging here has to be precise here.

Datascience Model is used for listing out datascience projects(filtered based on tag of full stack or datascience). Provision for injection of admin side content is needed. Link to user projects on this page.

Fullstack Model is used for listing out fullstack projects(filtered based on tag of full stack or datascience). Provision for injection of admin side content is needed. Link to user projects on this page.


I need to update project for Django >3. Porting pending.
