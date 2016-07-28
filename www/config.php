<?php
# Returns the scanned areas so squares can be drawn around them.
# This avoids exposing the config file.

$file = file_get_contents('../config.json');
$json = json_decode($file, true);
$areas = $json['work'];
$bounds = array();
foreach($areas as $area) {
	$bounds[] = array("north" => $area[0], "south" => $area[2], "east" => $area[3], "west" => $area[1]);
}

print json_encode($bounds);


?>
