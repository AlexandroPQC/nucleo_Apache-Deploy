from fabric.api import run, sudo, put, env, task


@task
def install_apache():
	sudo("apt-get -y install apache2")

@task
def deploy():
	put("nucleo.tar.gz", "/home/alexandro/")
	run("tar -xzvf nucleo.tar.gz")
	sudo("rm -rf /home/alexandro/nucleo.tar.gz")
	sudo("chown -R www-data:www-data /home/alexandro/nucleo")
	put('000-nucleo.conf', '/etc/apache2/sites-available', use_sudo=True)
	sudo("echo '127.0.0.1	www.nucleognulinux.com' >> /etc/hosts")
	sudo("a2ensite 000-nucleo.conf")
	sudo("service apache2 reload")

@task
def undo():
	sudo("a2dissite 000-nucleo.conf")
	sudo("service apache2 reload")
	sudo("rm -rf /home/alexandro/nucleo")
	sudo("rm -f /etc/apache2/sites-available/000-nucleo.conf")
	sudo("rm -f /var/log/apache2/nucleo*")
	sudo("sed -i '$d' /etc/hosts")
