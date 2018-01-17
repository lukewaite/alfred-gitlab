# encoding: utf-8

from workflow import web, Workflow, PasswordNotFound

def get_projects(api_key, url):
    """
    Parse all pages of projects
    :return: list
    """
    return get_project_page(api_key, url, 1, [])

def get_project_page(api_key, url, page, list):
    log.info("Calling API page {page}".format(page=page))
    params = dict(private_token=api_key, per_page=100, page=page, membership='true')
    r = web.get(url, params)

    # throw an error if request failed
    # Workflow will catch this and show it to the user
    r.raise_for_status()

    # Parse the JSON returned by GitLab and extract the projects
    result = list + r.json()

    nextpage = r.headers.get('X-Next-Page')
    if nextpage:
        result = get_project_page(api_key, url, nextpage, result)

    return result

def main(wf):
    try:
        # Get API key from Keychain
        api_key = wf.get_password('gitlab_api_key')
        api_url = wf.settings.get('api_url', 'https://gitlab.com/api/v4/projects')

        # Retrieve projects from cache if available and no more than 600
        # seconds old
        def wrapper():
            return get_projects(api_key, api_url)

        projects = wf.cached_data('projects', wrapper, max_age=3600)

        # Record our progress in the log file
        log.debug('{} gitlab projects cached'.format(len(projects)))

    except PasswordNotFound:  # API key has not yet been set
        # Nothing we can do about this, so just log it
        wf.logger.error('No API key saved')

if __name__ == u"__main__":
    wf = Workflow()
    log = wf.logger
    wf.run(main)