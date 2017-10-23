# Alfred Gitlab

Quickly navigate to GitLab projects in [Alfred 3][alfred].

![][sample]

## Setup and Usage
* Generate a GitLab personal access token (https://gitlab.com/profile/personal_access_tokens) then run `glsetkey <yourkey>`
* (Optionally) Tell it where the GitLab API you want to connect to is by running `glseturl https://<host>/api/v4/projects`
  * Defaults to GitLab.com's public API
* search for projects with `gl <search>`

## Notes
By default, we will only show projects which you are a member of.

## TODOs
* Optionally, allow you to search for non-membership repos
* Add alfred-workflow updater notifications
* Clean up 

# Thanks, License, Copyright

- The [Alfred-Workflow][alfred-workflow] library is used heavily, and it's wonderful documentation was key in building the plugin.
- The GitLab icon is used, care of GitLab.

All other code/media are released under the [MIT Licence][license].

[alfred]: http://www.alfredapp.com/
[alfred-workflow]: http://www.deanishe.net/alfred-workflow/
[license]: src/LICENSE.txt
[sample]: https://raw.github.com/lukewaite/alfred-gitlab/master/docs/sample.png