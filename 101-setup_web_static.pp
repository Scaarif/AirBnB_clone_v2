# Script that configures Nginx server with some folders and files

# ensure nginx is installed
exec {'update apt':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install nginx'],
}

exec {'install nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['start nginx'],
}

exec {'start nginx':
  provider => shell,
  command  => 'sudo service nginx start',
  before   => Exec['data folders'],
}

# create all the necessary folders/repos (in /data/)
exec {'data folders':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
  before   => Exec['shared folder'],
}

exec {'shared folder':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/shared/',
  before   => Exec['index.html'],
}

# add a test file in /data/web_static/releases/test/
exec {'index.html':
  provider => shell,
  command  => 'echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html',
  before   => Exec['symbolic link'],
}

# craete a symbolic link to /data/web_static/releases/test/
exec {'symbolic link':
  provider => shell,
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  before   => Exec['location'],
}

# add location to match requests from https://domain/hbnb_static/...
exec {'location':
  provider => shell,
  command  => 'sudo sed -i \'40i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n\' /etc/nginx/sites-available/default',
  before   => Exec['restart nginx'],
}

# restart nginx once done with the configuration change / update
exec {'restart nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
  before   => File['/data/']
}

# change ownership of the /data/ repo to ubuntu (owner and group)
file {'/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}
