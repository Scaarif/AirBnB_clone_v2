# Setup web servers for 'web_static' deployment (task 0 using puppet)

# ensure nginx is installed
exec { 'update apt':
  command => 'sudo apt-get -y update',
  before  => Exec['install nginx']
}

exec { 'install nginx':
  command => 'sudo apt-get -y install nginx',
  before  => File['/data/']
}

# create the /data/ folders if they don't already exist (/data/web_static/releases/test/ /shared/)
file { '/data':
  ensure => 'directory'
}
file { '/data/web_static':
  ensure => 'directory'
}
file { '/data/web_static/releases':
  ensure => 'directory'
}
file { '/data/web_static/releases/test':
  ensure => 'directory'
}
file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => 'Holberton School'
}
file { '/data/web_static/shared':
  ensure => 'directory'
}
# always create a symbolic link to /data/web_static/releases/test/ folder (/data/web_static/current)
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test'
}
# give ownership of the /data/ folder to ubuntu (owner and group)
file { '/data/':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true
}
# update Nginx configuration to serve content of /data/web_static/current to 'hbnb_static' requests (use alias)
exec { 'add location':
  command => 'sudo sed -i \'40i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n\' /etc/nginx/sites-available/default',
  before  => Exec['restart nginx']
}
# update/restart Nginx after the configuration
exec { 'restart nginx':
  command => 'sudo service nginx restart',
}
