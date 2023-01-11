# using Puppet to create file /tmp

file { '/tmp':
  path  => '/tmp/school',
  mode  => '0744',
  owner => 'www-data',
  group => 'www-data',
}

