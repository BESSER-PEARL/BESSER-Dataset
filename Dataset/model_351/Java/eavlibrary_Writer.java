





import java.util.List;
import java.util.ArrayList;

public class eavlibrary_Writer  {

    private String name;





    private List<eavlibrary_Book> eavlibrary_books;




    private eavlibrary_Book eavlibrary_book;


    public eavlibrary_Writer(
        String name    ) {
        this.name = name;
        this.eavlibrary_books = new ArrayList<>();
    }

    public eavlibrary_Writer(
        String name        ArrayList<eavlibrary_Book> eavlibrary_books    ) {
        this.name = name;
        this.eavlibrary_books = eavlibrary_books;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<eavlibrary_Book> getEavlibrary_books() {
        return eavlibrary_books;
    }

    public void addEavlibrary_book(Eavlibrary_book eavlibrary_book) {
        this.eavlibrary_books.add(eavlibrary_book);
    }
    public eavlibrary_Book getEavlibrary_book() {
        return eavlibrary_book;
    }

    public void setEavlibrary_book(eavlibrary_Book eavlibrary_book) {
        this.eavlibrary_book = eavlibrary_book;
    }

}