





import java.util.List;
import java.util.ArrayList;

public class book_Article  {

    private String title;





    private List<book_Person> book_persons;




    private book_Person book_person;


    public book_Article(
        String title    ) {
        this.title = title;
        this.book_persons = new ArrayList<>();
    }

    public book_Article(
        String title        ArrayList<book_Person> book_persons    ) {
        this.title = title;
        this.book_persons = book_persons;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public List<book_Person> getBook_persons() {
        return book_persons;
    }

    public void addBook_person(Book_person book_person) {
        this.book_persons.add(book_person);
    }
    public book_Person getBook_person() {
        return book_person;
    }

    public void setBook_person(book_Person book_person) {
        this.book_person = book_person;
    }

}