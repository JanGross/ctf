<?php
$contact = replace("..", "", $_POST["contact"]);
$recipient = $_POST['mail'];
$msg  = "Thank you for contacting LoremCorp.\n<br>";
$msg .= "The contact you selected will get back to you as sool as possible.\n<br>";
$msg .= "A response can take up to 7 work days.\n<br>";
$msg .= "\n<br>";
$msg .= "In the case of an emergency, refer to the contact details below:\n<br>";
$msg .= file_get_contents($contact.".txt");

// use wordwrap() if lines are longer than 70 characters
$msg = wordwrap($msg,70);
$headers = "";
$headers .= "From: Lorem Corp <noreply@loremcorp.local> \r\n";
$headers .= "Reply-To: noreply@loremcorp.local\r\n" ."X-Mailer: PHP/" . phpversion();
$headers .= 'MIME-Version: 1.0' . "\r\n";
$headers .= 'Content-type: text/html; charset=iso-8859-1' . "\r\n";  // send email
mail($recipient,"We have received your email!",$msg, $headers);
?>
<style>
    #thanks {
        margin: 25%;
        font-size: 25px;
    }
    </style>
<div id="thanks">You will receive a confirmation E-Mail shortly. <br>
Thank you for contacting us!<br>
<a href="/index.html">Return to our homepage</a></div>