# Change the OS configuration so that it is possible to
# login with the holberton user and open a file without
# any error message.

exec {'Remove hard and soft file limit configs':
  command => 'sed -i "s/holberton/# holberton/g" /etc/security/limits.conf',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}
