





import java.util.List;
import java.util.ArrayList;

public class model_MappedLibrary  {

    private String books;





    private List<model_Book> model_books;




    private model_Location model_location;




    private List<model_Book> model_books;


    public model_MappedLibrary(
        String books    ) {
        this.books = books;
        this.model_books = new ArrayList<>();
        this.model_books = new ArrayList<>();
    }

    public model_MappedLibrary(
        String books        ArrayList<model_Book> model_books,        ArrayList<model_Book> model_books    ) {
        this.books = books;
        this.model_books = model_books;
        this.model_books = model_books;
    }

    public String getBooks() {
        return books;
    }

    public void setBooks(String books) {
        this.books = books;
    }

    public List<model_Book> getModel_books() {
        return model_books;
    }

    public void addModel_book(Model_book model_book) {
        this.model_books.add(model_book);
    }
    public model_Location getModel_location() {
        return model_location;
    }

    public void setModel_location(model_Location model_location) {
        this.model_location = model_location;
    }
    public List<model_Book> getModel_books() {
        return model_books;
    }

    public void addModel_book(Model_book model_book) {
        this.model_books.add(model_book);
    }

}