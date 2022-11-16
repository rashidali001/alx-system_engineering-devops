#!/usr/bin/env ruby
puts ARGV[0].scan(/from:([+]?[[:alnum:]]*).*to:([+]?[[:alnum:]]*).*flags:((?:-?[0-9]:?){5})/).join(',')
