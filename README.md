# Node
Skoleprosjekt

Prosess for å hente nyeste endringer fra filer, gjøre endringer,
og å legge den til i git igjen:

Basic bruk av git: 

1. git pull 

2. Arbeide med

3. git add filnavn.py (eller "." istedetfor filnavn.py for å legge til alt)

4. git commit -m "din kommentar"

5. git push origin master (eller navnet på branch)

	Når du pusher og får en merge conflict:

	* Kjør en git pull for å merge filene

	* Åpne filene og fiks alle steder som inneholder konflikter. Fjern git linjer osv.

	* Push filen når den er ordnet i. Git klarer å se at du har arbeidet med en fil som har vært i konflikt og vil derfor laste opp filen din uten problem etter å ha endret feil i en merge conflict.

Vi burde sette oss inn i git og hvordan vi arbeider med det i praksis. Google stikkord som 'git fork', 'git branches', 'pull request' og 'git merge'.


Linux Terminal Commands:

cat test.txt (shows the file)

echo "This is a test file." > test.txt (creates a new file with content

touch test.txt (creates new file)

ls (list objects)

mkdir (make directory)

ls *.py (henter alle python filer)

ls ex*

mv filnavn directory 

mv filnavn filnavn

sudo (work as superuser)

rm -r filnavn  (delete)

