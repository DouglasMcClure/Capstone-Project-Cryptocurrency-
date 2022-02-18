#!/usr/bin/perl
use DBI;
use strict;
use warnings FATAL => 'all';
use lib qw(..);
use JSON qw(  );

# create a new database in sqlite named people.
my $dsn = "DBI:SQLite:messario.sqlite";
my %attr = (PrintError=>0, RaiseError=>1);

# connect to the database
my $dbh = DBI->connect($dsn, \%attr);

# check if the database opened successfully or not;
print "Opened database successfully\n";

my $filename = 'DougOutput.json';
# connect to and open the json file
my $json_text = do {
   open(my $json_fh, "<:encoding(UTF-8)", $filename)
      or die("Can't open \$filename\": $!\n");
   local $/;
   <$json_fh>
};
# store the decoded json data in a variable ($data)
my $json = JSON->new;
my $data = $json->decode($json_text);