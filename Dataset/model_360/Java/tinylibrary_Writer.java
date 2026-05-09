





import java.util.List;
import java.util.ArrayList;

public class tinylibrary_Writer extends Person {






    private List<tinylibrary_Book> tinylibrary_books;




    private tinylibrary_Book tinylibrary_book;




    private tinylibrary_Library tinylibrary_library;


    public tinylibrary_Writer(
    ) {
        super(
        );
        this.tinylibrary_books = new ArrayList<>();
    }

    public tinylibrary_Writer(
        ArrayList<tinylibrary_Book> tinylibrary_books    ) {
        this.tinylibrary_books = tinylibrary_books;
    }


    public List<tinylibrary_Book> getTinylibrary_books() {
        return tinylibrary_books;
    }

    public void addTinylibrary_book(Tinylibrary_book tinylibrary_book) {
        this.tinylibrary_books.add(tinylibrary_book);
    }
    public tinylibrary_Book getTinylibrary_book() {
        return tinylibrary_book;
    }

    public void setTinylibrary_book(tinylibrary_Book tinylibrary_book) {
        this.tinylibrary_book = tinylibrary_book;
    }
    public tinylibrary_Library getTinylibrary_library() {
        return tinylibrary_library;
    }

    public void setTinylibrary_library(tinylibrary_Library tinylibrary_library) {
        this.tinylibrary_library = tinylibrary_library;
    }

}