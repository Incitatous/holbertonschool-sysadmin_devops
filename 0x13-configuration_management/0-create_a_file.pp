file { '/tmp/holberton':
  ensure  => file,
  replace => 'no',
  content => 'I love Puppet',
  path    => '/tmp/holberton',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
