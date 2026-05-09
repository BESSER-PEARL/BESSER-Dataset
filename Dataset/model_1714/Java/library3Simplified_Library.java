





import java.util.List;
import java.util.ArrayList;

public class library3Simplified_Library  {






    private List<library3Simplified_Book> library3simplified_books;




    private List<library3Simplified_Customer> library3simplified_customers;


    public library3Simplified_Library(
    ) {
        this.library3simplified_books = new ArrayList<>();
        this.library3simplified_customers = new ArrayList<>();
    }

    public library3Simplified_Library(
        ArrayList<library3Simplified_Book> library3simplified_books,        ArrayList<library3Simplified_Customer> library3simplified_customers    ) {
        this.library3simplified_books = library3simplified_books;
        this.library3simplified_customers = library3simplified_customers;
    }


    public List<library3Simplified_Book> getLibrary3simplified_books() {
        return library3simplified_books;
    }

    public void addLibrary3simplified_book(Library3simplified_book library3simplified_book) {
        this.library3simplified_books.add(library3simplified_book);
    }
    public List<library3Simplified_Customer> getLibrary3simplified_customers() {
        return library3simplified_customers;
    }

    public void addLibrary3simplified_customer(Library3simplified_customer library3simplified_customer) {
        this.library3simplified_customers.add(library3simplified_customer);
    }

}