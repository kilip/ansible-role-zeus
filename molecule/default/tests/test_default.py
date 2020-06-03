"""Role testing files using testinfra."""


def test_hosts_file(host):
	"""Validate /etc/hosts file."""
	f = host.file('/etc/hosts')

	assert f.exists
	assert f.user == 'root'
	assert f.group == 'root'


def test_regolith(host):
	p = host.package("regolith-desktop")
	assert p.is_installed


def test_gpg(host):
	o = host.run("gpg --list-keys FC745865826D935D52E089583AF2DB499DD9D2A0")
	assert o.succeeded
