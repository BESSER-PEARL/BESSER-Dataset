





import java.util.List;
import java.util.ArrayList;

public class BookStorePackage_Book  {

    private String name;
    private int isbn;





    private BookStorePackage_BookStore bookstorepackage_bookstore;


    public BookStorePackage_Book(
        String name,        int isbn    ) {
        this.name = name;
        this.isbn = isbn;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getIsbn() {
        return isbn;
    }

    public void setIsbn(int isbn) {
        this.isbn = isbn;
    }

    public BookStorePackage_BookStore getBookstorepackage_bookstore() {
        return bookstorepackage_bookstore;
    }

    public void setBookstorepackage_bookstore(BookStorePackage_BookStore bookstorepackage_bookstore) {
        this.bookstorepackage_bookstore = bookstorepackage_bookstore;
    }

}