# create a new database in sqlite named people.
my $dsn = "DBI:SQLite:people.sqlite";
my %attr = (PrintError=>0, RaiseError=>1);
# connect to the database
my $dbh = DBI->connect($dsn, \%attr);
# check if the database opened successfully or not;
print "Opened database successfully\n";
