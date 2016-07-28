<?php

$db =  new SQLite3('../pokemon.sqlite3');
$stmt = $db->prepare('SELECT lat,lng FROM pokemon WHERE pid=:pid');
$stmt->bindValue(':pid', intval($_GET['pid']), SQLITE3_INTEGER);

$result = $stmt->execute();
$spawns = array();
while($res = $result->fetchArray(SQLITE3_ASSOC)) {
  $spawns[] = $res;
}

print json_encode($spawns);
?>
