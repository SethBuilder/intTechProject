<?php
if (isset($_POST['send'])) {
    
	$to = 'moghrabi@gmail.com'; // Use your own email address
     $subject = 'Feedback from my site';
	
	
	$message = 'Name: ' . $_POST['name'] . "\r\n\r\n";
	
	$message .= 'Email: ' . $_POST['email'] . "\r\n\r\n";
	$message .= 'Comments: ' . $_POST['comments'];

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
<h1>Thank You!</h1>
<p>Your message has been received and we'll respons very soon.</p>
<?php } else { ?>
<h1>Oops!</h1>
<p>Sorry, there was a problem sending your message.</p>
<?php } ?>
</body>
</html>

