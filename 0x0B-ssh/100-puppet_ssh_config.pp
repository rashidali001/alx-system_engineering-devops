# Add client configuration

file_line { 'disable password':
	line    => 'PasswordAuthentication no',
	path    => '/etc/ssh/ssh_config',
	replace => true,
}

file_line { 'add Identity file':
	line    => 'IdentityFile ~/.ssh/school',
	path    => '/etc/ssh/ssh_config',
	replace => true,
}

