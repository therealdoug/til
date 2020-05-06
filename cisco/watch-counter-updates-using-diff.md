# Watch Counter Updates Using Diff

diff is a great linux tool, command - in fact, I have a TIL just for it! ([`diff` The Output of Two Commands](linux/diff-the-output-of-two-commands.md))

Cisco NXOS lets you use the diff command to compare outputs or files stored locally (think log files or before/after upgrade config files).

Here are some great scenarios to put this command to use
- Comparing the routing/arp/mac table before and after a change or during tshoot
- Comparing interface output (great for easily seeing counters)
- When doing upgrades or changes save the running config, make the change, then compare with current running config

## How to use it

Basically, you just run the command you are interested in *twice*; with some amount of time in between.

For instance, if you want to watch counters on all interfaces to see which ones are incrementing, EASY:

` show interface | include ignore-case ^interface|description|crc|erorr|discard | diff`

<wait some amount of time>

hit `<UP><ENTER>` or ` show interface | include ignore-case ^interface|description|crc|erorr|discard | diff`