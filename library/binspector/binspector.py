"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class binspector(ShutItModule):

	def is_installed(self, shutit):
		return False

	def build(self, shutit):
		shutit.install('curl')
		shutit.install('git')
		shutit.install('python2.7-minimal')
		shutit.install('libc6')
		shutit.install('mlocate')
		shutit.send('updatedb')
		# TODO: Make exports part of llvm
		shutit.send('export LIBRARY_PATH=:/usr/lib/x86_64-linux-gnu')
		shutit.send('export CPATH=/usr/include/c++/4.8:/usr/include/x86_64-linux-gnu/c++/4.8')
		# Hack to make clang use libstdc++ rather than c++
		shutit.send('ln -s /usr/lib/gcc/x86_64-linux-gnu/4.8/libstdc++.so /usr/lib/gcc/x86_64-linux-gnu/4.8/libc++.so')
		shutit.send('pushd /opt')
		shutit.send('git clone https://github.com/binspector/binspector.git')
		shutit.send('popd')
		shutit.send('pushd /opt/binspector')

		shutit.send('./configure.sh')
		shutit.send('./build.sh')
		shutit.send('./smoke_test.sh')
		shutit.send('popd')
		return True

def module():
	return binspector(
		'shutit.tk.binspector.binspector', 0.3132235246,
		description='binary inspector',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.setup','shutit.tk.llvm.llvm']
	)

