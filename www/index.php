
<html>
<head>
<script src="static/sorttable.js"></script>

<style>
  .pokemon {
    float:left;
    width: 200px;
  }
  td {
	min-width: 30px;
	text-align: center;
  }

  table.sortable thead {
	background-color: #eee;
	color: #666;
	font-weight: bold;
	cursor: default;
  }
</style>

</head><body>
<h1>Pokemon Tools</h1>

<h2>Main maps:</h2>
<p><a href="map-nospawns.html">Only gyms and pokestops</a></p>
<p><a href="map.html">Spawn locations with spawn time indicators</a></p>
<p><a href="spawnlocation-heatmap.html">Spawn location heatmap</a></p>

<h2>Pokemon Statistics</h2>

<table class="sortable">
  <thead>
	<tr>
		<th>ID</th>
		<th>Image</th>
		<th>Seen</th>
		<th>Links</th>
	</tr>
  </thead>
<?php

$db =  new SQLite3('../pokemon.sqlite3');
for($i = 1; $i <= 151; $i++) {
	$id = sprintf("%03d", $i);

	print "<tr>\n";
	print "	<td>$id</td>\n";
	print "	<td><img src='static/pokemon/$id.png' /></td>\n";
	print " <td>" . $db->querySingle('SELECT COUNT(*) FROM pokemon WHERE pid=' . $i) . "</td>\n";
	print " <td style='text-align: left;'>
			<a href='heatmap.html?pid=$id'>Heatmap</a><br/>
			<a href='sightings.php?pid=$id'>Sightings table</a><br/>
		</td>";
	print "</tr>\n";
}

?>
