





import java.util.List;
import java.util.ArrayList;

public class bookstore_Dvd extends Ent {

    private String title;





    private bookstore_Dvd bookstore_dvd;




    private List<bookstore_Person> bookstore_persons;




    private bookstore_Person bookstore_person;


    public bookstore_Dvd(
        String title    ) {
        super(
        );
        this.title = title;
        this.bookstore_persons = new ArrayList<>();
    }

    public bookstore_Dvd(
        String title        ArrayList<bookstore_Person> bookstore_persons    ) {
        this.title = title;
        this.bookstore_persons = bookstore_persons;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public bookstore_Dvd getBookstore_dvd() {
        return bookstore_dvd;
    }

    public void setBookstore_dvd(bookstore_Dvd bookstore_dvd) {
        this.bookstore_dvd = bookstore_dvd;
    }
    public List<bookstore_Person> getBookstore_persons() {
        return bookstore_persons;
    }

    public void addBookstore_person(Bookstore_person bookstore_person) {
        this.bookstore_persons.add(bookstore_person);
    }
    public bookstore_Person getBookstore_person() {
        return bookstore_person;
    }

    public void setBookstore_person(bookstore_Person bookstore_person) {
        this.bookstore_person = bookstore_person;
    }

}