"""Role testing files using testinfra."""


def test_hosts_file(host):
	"""Validate /etc/hosts file."""
	f = host.file('/etc/hosts')

	assert f.exists
	assert f.user == 'root'
	assert f.group == 'root'


def test_util(host):
	v = host.package("vim")
	n = host.package("nethogs")
	c = host.package("cockpit")

	assert v.is_installed
	assert n.is_installed
	assert c.is_installed


def test_regolith(host):
	p = host.package("regolith-desktop")
	assert p.is_installed


def test_gpg(host):
	o = host.run("su toni -c \"gpg --list-keys FC745865826D935D52E089583AF2DB499DD9D2A0\"")
	assert o.succeeded


def test_git(host):
	f = host.file("/home/toni/.gitconfig")
	p = host.package("git")

	assert f.is_file
	assert f.contains("User Name")
	assert p.is_installed


def test_virtualbox(host):
	v = host.package("virtualbox")

	assert v.is_installed


def test_phpbrew(host):
	cmd = host.run("phpbrew --version")

	assert cmd.succeeded

