#!/usr/bin/perl
use DBI;
use strict;
use warnings FATAL => 'all';
use lib qw(..);
use JSON qw(  );
use Data::Dumper;

# create a new database in sqlite named people.
my $dsn = "DBI:SQLite:messario.sqlite";
my %attr = (PrintError=>0, RaiseError=>1);

# connect to the database
my $dbh = DBI->connect($dsn, \%attr);

# check if the database opened successfully or not;
print "Opened database successfully\n";

my $filename = "Apifiles/Code/DougOutput.json";
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

$dbh->do('PRAGMA foreign_keys = ON');
$dbh->do('PRAGMA foreign_keys');

my @ddl = (
    'CREATE TABLE DATA (
        id varchar(255) ,
        title varchar(255),
        content TEXT,
        publish_at varchar(255),
        name varchar(255),
        tags varchar(255),
        url varchar(255),
        PRIMARY KEY (id)
    )'
);

for my $sql (@ddl) {
    $dbh->do($sql);
}

for ( @{$data->{data}} ) {
   print Dumper $data;
   my $data_id = $_->{id};
      my $query1 = "\"insert into news (id) values (?) \"";
      my $statement = $dbh->prepare($query1);
      $statement->execute($data_id);
   }