document.getElementById('AboutMe').addEventListener('click', aboutme);
document.getElementById('Downloads').addEventListener('click', downloads);
document.getElementById('Links').addEventListener('click', links);
document.getElementById('Home').addEventListener('click', home);
var AboutMe = "<h1>about me</h1><p>I am very interested in coding and science! So have a look at the Downloads and have fun with them!</p>";
var Downloads = "<h1>Downloads</h1><ul><li><a href='Elementarteilchen.pyw' download>Elementarteilchen</a></li><li><a href='Homepage' download>Blue Bird</a></li></ul>"
var Links = "<h1>Links</h1><a href='grenzweg-wb.bplaced.net'>Grenzweg</a>"
var Home = "<h1>Home</h1><p>Welcome to my Homepage!<br/>Explore and have fun!</p>"
function aboutme()
{
    document.getElementById('Themefield').innerHTML = AboutMe;
}
function downloads()
{
    document.getElementById('Themefield').innerHTML = Downloads;    
}
function links()
{
    document.getElementById('Themefield').innerHTML = Links;
}
function home()
{
    document.getElementById('Themefield').innerHTML = Home;
}
