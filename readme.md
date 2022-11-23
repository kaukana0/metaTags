# ?

This isn't your usual component that you'd import and use.

It's useful during preparing (assembling/packing...) a deployment.

It inserts meta-tags for social networks into a html file.

Since the URL under which the deployment can be reached changes from project to project, that URL must be given as (only) 
argument for "insertMetaTags.py".

insertMetaTags.py takes all other information by direct file access (e.g. translations, screenshot image dimensions).

Using this implicitly agrees with some suggested dir-structure of the code.
There's 4 variables at the top of the file that can be adapted to a different dir-structure.

Note:
insertMetaTags.py can be run anywhere there's python3 - that could be the development environment as well as the production environment.