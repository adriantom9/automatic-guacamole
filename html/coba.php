<?php
$received = file_get_contents('php://input');
$fileToWrite = "image.jpg";
file_put_contents($fileToWrite, $received);
