<?php
if (isset($_POST['send'])) {
    
	$to = 'moghrabi@gmail.com'; // Use your own email address
     $subject = 'New Guide!';
	
	
	$message = 'First Name: ' . $_POST['firstname'] . "\r\n\r\n";
	$message .= 'Last Name: ' . $_POST['lastname'] . "\r\n\r\n";
	$message .= 'Email: ' . $_POST['email'] . "\r\n\r\n";
	$message .= 'Form of ID: ' . $_POST['iddoc'] . "\r\n\r\n";
	$message .= 'Tour Name: ' . $_POST['tourname'] . "\r\n\r\n";
	$message .= 'City: ' . $_POST['city'] . "\r\n\r\n";
	$message .= 'Country: ' . $_POST['country'] . "\r\n\r\n";
	$message .= 'Itenirary: ' . $_POST['itenirary'] . "\r\n\r\n";
	$message .= 'Location: ' . $_POST['location'] . "\r\n\r\n";
	$message .= 'Time: ' . $_POST['time'] . "\r\n\r\n";
	$message .= 'Date: ' . $_POST['date'] . "\r\n\r\n";
	$message .= 'Cost: ' . $_POST['cost'];

	
	
	

	$success = mail($to, $subject, $message);
}
?>

<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Message Received</title>
</head>

<body>


<?php if (isset($success) && $success) { ?>
<h1>Done!</h1>
<p>Your tour will go live very soon.</p>
<?php } else { ?>
<h1>Oops!</h1>
<p>Sorry, there was a problem sending your message.</p>
<?php } ?>
</body>
</html>

