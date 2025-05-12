#!/usr/bin/env ruby

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

