<?php
$received = file_get_contents('php://input');
$fileToWrite = "image_lab1.jpg";
file_put_contents($fileToWrite, $received);
