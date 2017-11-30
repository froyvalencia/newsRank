# newsRank 
The development of News Rank was an extremely enjoyable and rewarding introduction to software engineering and project management. News Rank is a reliability site intended to provide users feedback on the accuracy of the news source, i.e. a solution to the controversial topic of fake news spread on social media. The inspiration for this project comes as sites like snapchat and twitter are curating news, while Facebook is now hiring thousands of support agents to manually reviews articles shared and relying on users to flag stories. The issue with these current solutions is that they are labor intensive. News Rank while not a perfect solution allows the user to filter out news on their own as opposed receiving curated news without the need for thousands of manual reviewers.
 
For the development of News Rank we followed SCRUM and agile software methodologies for development. The group of 5 was broken down into Product Owner (myself), Lead Developer (myself), Scrum Master (rotational), and development and design team. In our specific approach we broke down our development and design team into subgroups; I had 2 members work on Frontend UI and UX design, I worked on the backend implementation and implmenting the logic for the machine learning as well as feature selection. We had 1 members work on external and internal tools to interact with our application such as an managing the github repository, external search and setting up a hosting server (Heroku). This approached worked amazingly well as we were using the Model View Controller Framework Django which is known for being highly abstracted and allows for the functionality of the app to be modularized. 
 
In regards to the specific role of product owner for this project; some of the duties I was involved in included creating a prioritized wish list of product features (product backlog) and participated in sprint planning. During each sprint plan meeting, we select features from product backlog and decide how to implement as well as assign weights based on the work and effort required. I chose the tools to be used, as well as framework selection and assigning users to tasks based on their strengths. During development tools that we used included GitHub (version control), zube (scrum board, burnup, and burndown charts), and heroku (cloud hosting service).
 
During the process we encountered things that worked extremely well, a specific instance was our switch to pair programming in sprint 2. Pair programming is an agile software development technique that has two programmers work in unison at one computer. We did not use pair programming much during the first sprint and what we saw was that certain tasks for the frontend and backend tended to be inter-reliant on each other so it was difficult to test functionality. Another benefit was the team as a unit had a better understanding of the code base, where if in the issue came up one of 2 developers could help communicate or resolve the issue. A key benefit of pair programming was that it allowed me to assist some of the more junior developers on our team.

During the process, we also encountered things that did not work as efficiently as I would have liked. Some of these included our research phase taking longer than expected which caused a delay in starting development of our software. The delay was also in part due to our development teams steep learning curve as our the majority of the team had very little experience with the Django framework, the natural language toolkit, and machine learning classification algorithms. In regards to our scrum meetings and collaborative environment, we had one member who was using Skype for meetings as he lived 3 hours away; while this was an adequate solution for occasional meetings and communicating, his specific productivity during sprint 3 was much higher when we worked together side by side.
 
My favorite aspect of the scrum methodology was the collaborative environment it created for our development team. While being able to only meet 3 times a week for scrum we would additionally have daily scrums over slack. For a team of 5 members, we were surprisingly flexible in terms of scheduling meetings, we maintained a group calendar with everyone’s work, and time commitments blocked off. This allowed us to know when other members were available and set a meeting time easily as opposed to having to communicate to ask if they were available and then attempt to find a time slot which can be time-consuming.
 
The project as a whole was an extremely great experience in project management and full stack development. One great learning lesson I’d like to leave off on was a feature that I implemented that relied on topics gathered from our article text extraction was used to asynchronously gather sentiment analysis from Twitter users; we saw that this feature, in the long run, did not increase the reliability or accuracy of our main product and in terms it was better to maintain.
