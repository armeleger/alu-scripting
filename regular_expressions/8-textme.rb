#!/usr/bin/env ruby

<<<<<<< HEAD
input = ARGV[0]
match = input.match(/\[from:(.*?)\].*?\[to:(.*?)\].*?\[flags:(.*?)\]/)

if match
  sender = match[1]
  receiver = match[2]
  flags = match[3]
  puts "#{sender},#{receiver},#{flags}"
else
  puts "No match found"
end

=======
input = ARGV[0]
match = input.match(/\[from:(.*?)\].*?\[to:(.*?)\].*?\[flags:(.*?)\]/)

if match
  sender = match[1]
  receiver = match[2]
  flags = match[3]
  puts "#{sender},#{receiver},#{flags}"
else
  puts "No match found"
end
>>>>>>> 4bdfa1b6a304f78c4fa2dd56eeca0ab09ce803f0