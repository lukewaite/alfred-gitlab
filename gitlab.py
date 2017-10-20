# encoding: utf-8

import sys
import argparse
from workflow import Workflow, ICON_WEB, ICON_WARNING, web, PasswordNotFound

log = None

def get_projects(api_key):
    """
    Parse all pages of projects
    :return: list
    """
    return get_project_page(api_key, 1, [])

def get_project_page(api_key, page, list):
    log.info("Calling API page {page}".format(page=page))
    url = 'https://git.intouchinsight.io/api/v4/projects'
    params = dict(private_token=api_key, per_page=100, page=page, membership='true')
    r = web.get(url, params)

    # throw an error if request failed
    # Workflow will catch this and show it to the user
    r.raise_for_status()

    # Parse the JSON returned by GitLab and extract the projects
    result = list + r.json()

    nextpage = r.headers.get('X-Next-Page')
    if nextpage:
        result = get_project_page(api_key, nextpage, result)

    return result


def search_for_project(project):
    """Generate a string search key for a project"""
    elements = []
    elements.append(project['name'])
    elements.append(project['namespace']['path'])
    return u' '.join(elements)

def main(wf):
    # build argument parser to parse script args and collect their
    # values
    parser = argparse.ArgumentParser()
    # add an optional (nargs='?') --setkey argument and save its
    # value to 'apikey' (dest). This will be called from a separate "Run Script"
    # action with the API key
    parser.add_argument('--setkey', dest='apikey', nargs='?', default=None)
    # add an optional query and save it to 'query'
    parser.add_argument('query', nargs='?', default=None)
    # parse the script's arguments
    args = parser.parse_args(wf.args)

    ####################################################################
    # Save the provided API key
    ####################################################################

    # decide what to do based on arguments
    if args.apikey:  # Script was passed an API key
        # save the key
        wf.save_password('gitlab_api_key', args.apikey)
        return 0  # 0 means script exited cleanly

    ####################################################################
    # Check that we have an API key saved
    ####################################################################

    try:
        api_key = wf.get_password('gitlab_api_key')
    except PasswordNotFound:  # API key has not yet been set
        wf.add_item('No API key set.',
                    'Please use glsetkey to set your GitLab API key.',
                    valid=False,
                    icon=ICON_WARNING)
        wf.send_feedback()
        return 0

    ####################################################################
    # View/filter GitLab Projects
    ####################################################################

    query = args.query

    def wrapper():
        return get_projects(api_key)

    projects = wf.cached_data('projects123', wrapper, max_age=3600)

    # If script was passed a query, use it to filter projects
    if query:
        projects = wf.filter(query, projects, key=search_for_project, min_score=20)

    if not projects:  # we have no data to show, so show a warning and stop
        wf.add_item('No projects found', icon=ICON_WARNING)
        wf.send_feedback()
        return 0

    # Loop through the returned posts and add an item for each to
    # the list of results for Alfred
    for project in projects:
        wf.add_item(title=project['name_with_namespace'],
                    subtitle=project['path_with_namespace'],
                    arg=project['web_url'],
                    valid=True,
                    icon=ICON_WEB)

    # Send the results to Alfred as XML
    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))