<?php
$received = file_get_contents('php://input');
$fileToWrite = "image_pau1.jpg";
file_put_contents($fileToWrite, $received);
