# install flask from pip3 using puppet

package { 'Flask':
  ensure   => '2.1.0',  # Ensure the specified version
  provider => 'pip3',   # Use the pip3 provider
}

