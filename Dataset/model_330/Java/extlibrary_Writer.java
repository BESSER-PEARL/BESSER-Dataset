





import java.util.List;
import java.util.ArrayList;

public class extlibrary_Writer extends Person {

    private String name;





    private List<extlibrary_Book> extlibrary_books;




    private extlibrary_Book extlibrary_book;


    public extlibrary_Writer(
        String name    ) {
        super(
        );
        this.name = name;
        this.extlibrary_books = new ArrayList<>();
    }

    public extlibrary_Writer(
        String name        ArrayList<extlibrary_Book> extlibrary_books    ) {
        this.name = name;
        this.extlibrary_books = extlibrary_books;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<extlibrary_Book> getExtlibrary_books() {
        return extlibrary_books;
    }

    public void addExtlibrary_book(Extlibrary_book extlibrary_book) {
        this.extlibrary_books.add(extlibrary_book);
    }
    public extlibrary_Book getExtlibrary_book() {
        return extlibrary_book;
    }

    public void setExtlibrary_book(extlibrary_Book extlibrary_book) {
        this.extlibrary_book = extlibrary_book;
    }

}