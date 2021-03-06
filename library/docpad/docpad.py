
# Created from dockerfile: /space/git/dockerfiles_repos/dockerfile-examples/docpad/Dockerfile
from shutit_module import ShutItModule

class docpad(ShutItModule):

	def is_installed(self, shutit):
		return False

	def build(self, shutit):
		shutit.install('software-properties-common')
		# No add-apt-repository available on
		shutit.send('add-apt-repository -y ppa:chris-lea/node.js')
		shutit.send('echo "deb http://us.archive.ubuntu.com/ubuntu/ precise universe" >> /etc/apt/sources.list')
		shutit.send('apt-get update')
		shutit.install('python-software-properties')
		shutit.install('python')
		shutit.install('nodejs')
		#shutit.install('git')
		shutit.send('npm install -g docpad@6.44 && echo ""')
		return True

	def finalize(self, shutit):
		return True

	def test(self, shutit):
		return True

	def is_installed(self, shutit):
		return False

	def get_config(self, shutit):
		return True

def module():
	return docpad(
		'shutit.tk.docpad.docpad', 0.1258925,
		depends=['shutit.tk.setup']
	)
