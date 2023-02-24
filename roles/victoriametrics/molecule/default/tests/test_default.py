from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os
import yaml
import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

@pytest.fixture()
def AnsibleDefaults():
    with open("defaults/main.yml", 'r') as stream:
        return yaml.full_load(stream)


@pytest.mark.parametrize("dirs", [
    "/var/lib/victoria-metrics"
])
def test_directories(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists

@pytest.mark.parametrize("files", [
    "/usr/local/bin/victoria-metrics-prod",
    "/usr/local/bin/vmagent-prod",
    "/usr/local/bin/vmalert-prod",
    "/usr/local/bin/vmauth-prod",
    "/usr/local/bin/vmbackup-prod",
    "/usr/local/bin/vmrestore-prod",
])
def test_files(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file

def test_user(host):
    assert host.group("victoriametrics").exists
    assert host.user("victoriametrics").exists

def test_service(host):
    s = host.service("victoriametrics")
    assert s.is_running

def test_socket(host):
    s = host.socket("tcp://0.0.0.0:8428")
    assert s.is_listening

def test_version(host):
    run = host.run("victoria-metrics-prod --version")
    out = run.stdout + run.stderr
    assert "victoria-metrics" in out
