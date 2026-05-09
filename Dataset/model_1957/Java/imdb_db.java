





import java.util.List;
import java.util.ArrayList;

public class imdb_db  {

    private String bestOf2014;





    private List<imdb_Person> imdb_persons;




    private List<imdb_Movie> imdb_movies;




    private List<imdb_Person> imdb_persons;




    private List<imdb_Person> imdb_persons;




    private List<imdb_User> imdb_users;




    private List<imdb_StaffList> imdb_stafflists;


    public imdb_db(
        String bestOf2014    ) {
        this.bestOf2014 = bestOf2014;
        this.imdb_persons = new ArrayList<>();
        this.imdb_movies = new ArrayList<>();
        this.imdb_persons = new ArrayList<>();
        this.imdb_persons = new ArrayList<>();
        this.imdb_users = new ArrayList<>();
        this.imdb_stafflists = new ArrayList<>();
    }

    public imdb_db(
        String bestOf2014        ArrayList<imdb_Person> imdb_persons,        ArrayList<imdb_Movie> imdb_movies,        ArrayList<imdb_Person> imdb_persons,        ArrayList<imdb_Person> imdb_persons,        ArrayList<imdb_User> imdb_users,        ArrayList<imdb_StaffList> imdb_stafflists    ) {
        this.bestOf2014 = bestOf2014;
        this.imdb_persons = imdb_persons;
        this.imdb_movies = imdb_movies;
        this.imdb_persons = imdb_persons;
        this.imdb_persons = imdb_persons;
        this.imdb_users = imdb_users;
        this.imdb_stafflists = imdb_stafflists;
    }

    public String getBestof2014() {
        return bestOf2014;
    }

    public void setBestof2014(String bestOf2014) {
        this.bestOf2014 = bestOf2014;
    }

    public List<imdb_Person> getImdb_persons() {
        return imdb_persons;
    }

    public void addImdb_person(Imdb_person imdb_person) {
        this.imdb_persons.add(imdb_person);
    }
    public List<imdb_Movie> getImdb_movies() {
        return imdb_movies;
    }

    public void addImdb_movie(Imdb_movie imdb_movie) {
        this.imdb_movies.add(imdb_movie);
    }
    public List<imdb_Person> getImdb_persons() {
        return imdb_persons;
    }

    public void addImdb_person(Imdb_person imdb_person) {
        this.imdb_persons.add(imdb_person);
    }
    public List<imdb_Person> getImdb_persons() {
        return imdb_persons;
    }

    public void addImdb_person(Imdb_person imdb_person) {
        this.imdb_persons.add(imdb_person);
    }
    public List<imdb_User> getImdb_users() {
        return imdb_users;
    }

    public void addImdb_user(Imdb_user imdb_user) {
        this.imdb_users.add(imdb_user);
    }
    public List<imdb_StaffList> getImdb_stafflists() {
        return imdb_stafflists;
    }

    public void addImdb_stafflist(Imdb_stafflist imdb_stafflist) {
        this.imdb_stafflists.add(imdb_stafflist);
    }

}