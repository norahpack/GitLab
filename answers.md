# Quiz questions

This is only a "quiz" in the loosest sense that it's asking questions whose
answers will be part of your grade. Please use *any resources you want*, as
long as you list those resources (e.g. peers, websites, etc.)

## Navigating logs

1. What is the SHA for the last commit made by Prof. Xanda on the branch
xanda_0000_movie_processing?
(For this and future questions, the first 5 characters is plenty - neither
Git nor I need the whole SHA.)

9b257

2. What is the SHA for the last commit associated with line 9 of this file?

b2ed3

3. What did line 12 of this file say in commit d1d83?

"2. I should really finish writing this"

4. What changed between commit e474c and 82045?

In the process_movie_data.py file, 

gross_sort = lambda x : x["Gross"] 
became
gross_sort = lambda x : int(x["Gross"])

and 

top_five = rows[:-5:-1] 
became
top_five = rows[:-6:-1]

(which is good, because the new line actually gives us five values instead of four)

## Predicting merges

Assume at the start of each of these three questions that your
branch for switching to a top-10 list was called `top_ten`
and your branch generalizing to any number of movies was called `top_N`.
Predict the behavior of these three possible operations - you don't
have to provide a full `diff` but you should describe at a high level
what changes would happen.

These questions are supposed to be separate paths, not cumulative;
for example, you should *not* assume that the operations of 5 were run
before 6. When testing outcomes later in the lab, you should make sure to
revert back to the state of the branch before you started these questions.

5. What do you think would happen if you ran the following commands?
What branches would change, and how?
```
git checkout test
git merge top_N
```
Running git merge top_N when we are on the test branch will only affect the branch test. The changes that were made in top_N since it diverged from test will be merged into the branch test. Therefore, the process_movie_data.py file in the test branch will reflect the changes made to it in the top_N branch - that is, the process_movie_data.py file in the test branch will now have a find_top_N function that finds the top N grossing movies.

6. What do you think would happen if you ran the following commands?
What branches would change, and how?
```
git checkout top_ten
git merge test
```

Running git merge test when we are on the top_ten branch will only affect the top_ten branch. The changes that were made in test since it diverged from top_ten will be merged into the branch top_ten. This means that the process_movie_data.py file in the top_ten branch will NOT revert back to containing the find_top_5 function that finds the top 5 grossing movies since that change was made before top_ten and test diverted. However, the file that was named quiz.md in top_ten will now be named answers.md as it is named in the test branch.

7. What do you think would happen if you ran the following commands?
What branches would change, and how?
```
git checkout test
git rebase top_ten
git rebase top_N
```
used the resource https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase

Git rebase top_ten will move the top_ten branch to begin on the end (most recent commit) of the test branch. A new commit will be written onto the test branch for each commit in top_ten.

After this step, the process_movie_data.py file in the test branch will be changed to contain the find_top_10 function that finds the top 10 grossing movies. However, in the test branch, the answers.md file will not be renamed to quiz.md

Then, git rebase top_N will move the top_N branch to begin on the end (most recent commit) of the test branch after we rebased the top_ten branch. A new commit will be written onto the test branch for each commit in top_N.

After this step, the process_movie_data.py file in the test branch will contain the find_top_N function that finds the top N grossing movies, defaulting to 10 movies (which we set when resolving merge conflicts). Also, in the test branch, the quiz.md file will be still named answers.md.