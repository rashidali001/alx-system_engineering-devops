#  create a manifest that kills a process named killmenow.

exec { 'end killmenow process':
  command  => 'pkill -f killmenow',
  provider => 'shell',
}

