<?php
$command = "echo " . $argv[1] . " | cowsay -f " . $argv[2];
print(shell_exec($command));
?>
