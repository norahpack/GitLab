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


Extra-credit question:
I chose to focus on the git command cherry pick. Cherry pick means we can choose any arbitrary commit from one branch and apply it to another. It lets us choose which of the changes we want to apply.

First, I created another branch off of test called applyTo, where I am going to cherry-pick a commit on another branch and apply it to the applyTo branch.

Then, I created another branch off of test called applyFrom, where I am going to cherry-pick a commit on applyFrom and apply it to the applyTo branch.

Then, once I checked out the applyFrom branch, I made the following changes to the survey.txt files and created the following commits:

1.  the commit "new commit 1" included the following changes:

- Survey question 1 answer was changed to "Norah Catherine" from "Norah Pack"
- Survey question 2 answer was changed to "I changed this in commit 1" from "Light Pink"
- Survey question 3 answer was changed to "Not Oranges" from "Pho"

- Survey question 4 answer remained "Argentina".

2. the commit "new commit 2" included the following changes:

- Survey question 1 answer was changed to "Norah Catherine Pack" from "Norah Catherine"
- Survey question 3 answer was changed back to "Pho" from "Not Oranges"
- Survey question 4 question was changed to "Which country's capital is Buenos Aires?"

- Survey question 2 answer remained "I changed this in commit 1"
- Survey question 4 answer remained "Argentina".

Then, I ran the command git log to find the SHA hashes of the last two commits.
SHA hash of new commit 2 starts with 5c772
SHA hash of new commit 1 starts with 488b9

Then, I checked out the branch applyTo (which, right now, is the same as test).

Then, I ran the cherry pick command.
I used https://git-scm.com/docs/git-cherry-pick for documentation
git cherry-pick applyFrom.

According to the documentation, this applies the commit at the tip of the applyFrom branch (new commit 2) to the applyTo branch and creates a new commit.

When I ran this command, I got a merge conflict:

merge conflict in survey.txt
...
after resolving the conflicts, mark them with "git add/rm <pathspec>" then run git cherry-pick --continue.

I opened survey.txt and saw this:

1. What is your name?
"<<<<<<< HEAD
Answer: Norah Pack
=======
Answer: Norah Catherine Pack
>>>>>>> 5c77273 (new commit 2)"

2. What is your favorite color?
Answer: Light pink

3. What is your favorite food?
Answer: Pho

4. Which country's capital is Buenos Aires?
Answer: Argentina

First, notice that the answer to question 2 remains Light pink, even though it was "I changed this in commit 1" in new commit 2. This is because the answer to question 2 was not changed in commit "new commit 2", so it was not applied when we cherry-picked this commit.

This is interesting - the question to question 4 was changed when compared to the applyTo branch, but that didn't have any merge conflicts and the change applied. However, the answer to question 1 was changed both in the new commit 1 of applyFrom and new commit 2 of applyFrom. My guess is that because the change in new commit 2 started from a different place ("Norah Catherine") than was expected based on the current state of the file in applyTo ("Norah Pack"), this is why we encountered the merge conflict.

I manually resolved the merge conflicts by selecting the answer to question 1 in the new commit 2 commit ("Norah Catherine Pack"). I saved these changes, ran "git add survey.txt" and ran "git cherry-pick --continue"

I was prompted to change the commit name, which I changed to "cherry-pick new commit 2".

I ran "git log" and saw that new commit 2 and new commit 1 were not in the git log, but cherry-pick new commit 2 was in the git log. Then, I ran "git push".

Now, the applyTo branch is on GitHub and survey.txt reads:

1. What is your name?
Answer: Norah Catherine Pack

2. What is your favorite color?
Answer: Light pink

3. What is your favorite food?
Answer: Pho

4. Which country's capital is Buenos Aires?
Answer: Argentina