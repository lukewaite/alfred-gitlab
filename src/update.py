# encoding: utf-8

from workflow import Workflow, PasswordNotFound
import mureq


def get_projects(api_key, url):
    return get_project_page(api_key, url, 1, [])


def get_project_page(api_key, url, page, stored_projects):
    log.info("Calling API page {page}".format(page=page))
    response = mureq.get(url, params=({'private_token': api_key, 'per_page': 100, 'page': page, 'membership': 'true'}))

    # throw an error if request failed
    # Workflow will catch this and show it to the user
    response.raise_for_status()

    # Parse the JSON returned by GitLab and extract the projects
    projects = stored_projects + response.json()

    next_page = response.headers.get('X-Next-Page')
    if next_page:
        projects = get_project_page(api_key, url, next_page, projects)

    return projects


def main(wf):
    try:
        # Get API key from Keychain
        api_key = wf.get_password('gitlab_api_key')
        api_url = wf.settings.get('api_url', 'https://gitlab.com/api/v4/projects')

        def fetch_gitlab_projects():
            return get_projects(api_key, api_url)

        projects = wf.cached_data('projects', fetch_gitlab_projects, max_age=3600)

        # Record our progress in the log file
        log.debug('{} gitlab projects cached'.format(len(projects)))

    except PasswordNotFound:  # API key has not yet been set
        # Nothing we can do about this, so just log it
        wf.logger.error('No API key saved')


if __name__ == "__main__":
    wf = Workflow()
    log = wf.logger
    wf.run(main)
