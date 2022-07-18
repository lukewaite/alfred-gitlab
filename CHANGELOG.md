# Release Notes for v1.x

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [v3.0.1] (2022-07-18)
* Remove URLEncoding of repo URLs are they appear to break opening in Alfred 5 ([#9ce14af](https://github.com/lukewaite/alfred-gitlab/commit/9ce14af))

## [v3.0.0] (2022-03-26)
* Upgrade to support python3 ([#28](https://github.com/lukewaite/alfred-gitlab/pull/28))
  Thanks to @TribuneX

### Upgrade notes
If you have already upgraded to MacOS 12.3 you will not be able to automatically upgrade.
Please download the latest released copy of the workflow from [releases](https://github.com/lukewaite/alfred-gitlab/releases) and re-install.

If you are not yet on 12.3, you can run `gl workflow:update` to update.

### Skipping 2.x
The PR with the fix for python3 came in tagged as 3.0.0. I'm going to skip straight to that tag so that anyone who's
upgraded to the fork in the meantime has the ability to pull updates in the future without having to "go back" to 2.x.

## [v1.6.0] (2019-02-02)
* Allow subpage navigation to be disabled

## [v1.5.0] (2019-01-27)
* adds a way to go directly to subpages of a repository (Overview, Merge Request,...)

## [v1.4.0] (2018-02-27)
* Update search to key off of name_with_namespace and path_with_namespace

## [v1.3.0] (2018-02-02)
* Add UID to workflow items so alfred can sort items

## [v1.2.3] (2018-01-16)
* Default to correct GitLab public API endpoint

## [v1.2.2] (2018-01-05)
* Correctly poll for updates on first run ([#ea3e49174](https://github.com/lukewaite/alfred-gitlab/commit/ea3e49174ac000649c692a064910b3c5c0c7834b))
* Do not show "updating" alert if data is cached and not filtered out

## [v1.2.1] (2017-10-23)
* Default to the gitlab.com public API

## [v1.2.0] (2017-10-20)

### Feature
* Notify if alfred-workflow detects a new version of alfred-gitlab

### Fixed
* Refresh after background updating of GitLab projects list

## [v1.1.0] (2017-10-20)
* Enable background updating of GitLab projects list

## [v1.0.2] (2017-10-20)
* Bump alfred-workflow to 1.28.1 to fix issues

## [v1.0.1] (2017-10-20)
* Fix readme reference to public GitLab API

## [v1.0.0] (2017-10-20)

* Initial implementaiton of alfred-gitlab workflow

[Unreleased]: https://github.com/lukewaite/alfred-gitlab/compare/v3.0.1...HEAD
[v3.0.0]: https://github.com/lukewaite/alfred-gitlab/compare/v3.0.0...v3.0.1
[v3.0.0]: https://github.com/lukewaite/alfred-gitlab/compare/v1.6.0...v3.0.0
[v1.6.0]: https://github.com/lukewaite/alfred-gitlab/compare/v1.5.0...v1.6.0
[v1.5.0]: https://github.com/lukewaite/alfred-gitlab/compare/v1.4.0...v1.5.0
[v1.4.0]: https://github.com/lukewaite/alfred-gitlab/compare/v1.3.0...v1.4.0
[v1.3.0]: https://github.com/lukewaite/alfred-gitlab/compare/v1.2.3...v1.3.0
[v1.2.3]: https://github.com/lukewaite/alfred-gitlab/compare/v1.2.2...v1.2.3
[v1.2.2]: https://github.com/lukewaite/alfred-gitlab/compare/v1.2.1...v1.2.2
[v1.2.1]: https://github.com/lukewaite/alfred-gitlab/compare/v1.2.0...v1.2.1
[v1.2.0]: https://github.com/lukewaite/alfred-gitlab/compare/v1.1.0...v1.2.0
[v1.1.0]: https://github.com/lukewaite/alfred-gitlab/compare/v1.0.2...v1.1.0
[v1.0.2]: https://github.com/lukewaite/alfred-gitlab/compare/v1.0.1...v1.0.2
[v1.0.1]: https://github.com/lukewaite/alfred-gitlab/compare/v1.0.0...v1.0.1
[v1.0.0]: https://github.com/lukewaite/alfred-gitlab/compare/90b63639ac1d06f9a52c37afd3f9c1da37d6ebd2...v1.0.0
