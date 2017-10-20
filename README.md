# Alfred Gitlab

Quickly navigate to GitLab projects in [Alfred 3][alfred].

## Setup and Usage
* Generate a GitLab personal access token (https://gitlab.com/profile/personal_access_tokens) then run `glsetkey <yourkey>`
* Tell it where our API is by running `glseturl https://git.intouchinsight.io/api/v4/projects`
* search for projects with `gl <search>`

## Notes
By default, we will only show projects which you are a member of.

# Thanks, License, Copyright

- The [Alfred-Workflow][alfred-workflow] library is used heavily, and it's wonderful documentation was key in building the plugin.
- The GitLab icon is used, care of GitLab.

All other code/media are released under the [MIT Licence][license].

[alfred]: http://www.alfredapp.com/
[alfred-workflow]: http://www.deanishe.net/alfred-workflow/
[license]: src/LICENSE.txt