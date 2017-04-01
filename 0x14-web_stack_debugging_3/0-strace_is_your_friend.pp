#Finds out why Apache returning a 500 error
exec { 'phpfix':
  command => "sed -ie 's/locale.phpp/locale.php/' /var/www/html/wp-settings.php",
  path    => '/bin',
}
