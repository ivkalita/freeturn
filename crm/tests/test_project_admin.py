import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_action(admin_app,
                      project):
    assert project.state == 'requested'
    url = reverse('crm_project_modeladmin_index')
    r = admin_app.get(url)
    r = r.click("Drop")
    inputs = r.lxml.xpath(".//*[@id='id_notes']")
    assert len(inputs) == 1

    r = r.forms[1].submit().follow()
    assert r.status_code == 200

    project.refresh_from_db()
    assert project.state == 'stopped'
    assert len(r.context['messages']) == 1


@pytest.mark.django_db
def test_inspect(admin_app,
                 project):
    url = reverse('crm_project_modeladmin_inspect', kwargs={'instance_pk': project.pk})
    r = admin_app.get(url)
    assert r.status_code == 200


@pytest.mark.django_db
def test_inspect_blank(admin_app, project_factory):
    project = project_factory.create(
        project_page=None,
        start_date=None,
        end_date=None,
        daily_rate=None
    )
    url = reverse('crm_project_modeladmin_inspect', kwargs={'instance_pk': project.pk})
    r = admin_app.get(url)
    assert r.status_code == 200
