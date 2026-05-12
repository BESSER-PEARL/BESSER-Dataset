





import java.util.List;
import java.util.ArrayList;

public class Library  {

    private int LibraryID;
    private String Address;





    private List<Person> persons;




    private List<Book> books;


    public Library(
        int LibraryID,        String Address    ) {
        this.LibraryID = LibraryID;
        this.Address = Address;
        this.persons = new ArrayList<>();
        this.books = new ArrayList<>();
    }

    public Library(
        int LibraryID,        String Address        ArrayList<Person> persons,        ArrayList<Book> books    ) {
        this.LibraryID = LibraryID;
        this.Address = Address;
        this.persons = persons;
        this.books = books;
    }

    public int getLibraryid() {
        return LibraryID;
    }

    public void setLibraryid(int LibraryID) {
        this.LibraryID = LibraryID;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }

    public List<Person> getPersons() {
        return persons;
    }

    public void addPerson(Person person) {
        this.persons.add(person);
    }
    public List<Book> getBooks() {
        return books;
    }

    public void addBook(Book book) {
        this.books.add(book);
    }

}