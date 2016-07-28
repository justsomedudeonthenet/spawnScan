<html>
<head>
	<style>
		table, th, td {border: 1px solid black; border-collapse: collapse;}
		th { background-color: #eee;}
	</style>

</head>

<body>
<?php
print "<h1>Sightings of " . $_GET['pid'] . "</h1>";
print "<table>
	<thead>
		<tr>
			<th>Time</th>
			<th>Latitude</th>
			<th>Longitude</th>
		</tr>
	</thead>
	<tbody>";

$db =  new SQLite3('../pokemon.sqlite3');
$stmt = $db->prepare('SELECT time,lat,lng FROM pokemon WHERE pid=:pid ORDER BY time desc');
$stmt->bindValue(':pid', intval($_GET['pid']), SQLITE3_INTEGER);

$result = $stmt->execute();
while($res = $result->fetchArray(SQLITE3_ASSOC)) {
	print "<tr>";
	print "	<td>" . date("Y-m-d H:i:s", $res['time']/1000) . "</td>";
	print "	<td>" . $res['lat'] . "</td>";
	print "	<td>" . $res['lng'] . "</td>";
	print "</tr>";
}

print "</tbody>";
print "</table>";
?>
</body>
</html>
