# create a file in /tmp

file { '/tmp/school':
  ensure  => 'file',      # Ensure that the file exists
  content => 'I love Puppet',  # Content of the file
  mode    => '0744',      # File permission
  owner   => 'www-data',  # File owner
  group   => 'www-data',  # File group
}

