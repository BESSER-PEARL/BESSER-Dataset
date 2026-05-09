





import java.util.List;
import java.util.ArrayList;

public class eavlibrary_Library  {

    private String name;





    private List<eavlibrary_Writer> eavlibrary_writers;




    private List<eavlibrary_Book> eavlibrary_books;


    public eavlibrary_Library(
        String name    ) {
        this.name = name;
        this.eavlibrary_writers = new ArrayList<>();
        this.eavlibrary_books = new ArrayList<>();
    }

    public eavlibrary_Library(
        String name        ArrayList<eavlibrary_Writer> eavlibrary_writers,        ArrayList<eavlibrary_Book> eavlibrary_books    ) {
        this.name = name;
        this.eavlibrary_writers = eavlibrary_writers;
        this.eavlibrary_books = eavlibrary_books;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<eavlibrary_Writer> getEavlibrary_writers() {
        return eavlibrary_writers;
    }

    public void addEavlibrary_writer(Eavlibrary_writer eavlibrary_writer) {
        this.eavlibrary_writers.add(eavlibrary_writer);
    }
    public List<eavlibrary_Book> getEavlibrary_books() {
        return eavlibrary_books;
    }

    public void addEavlibrary_book(Eavlibrary_book eavlibrary_book) {
        this.eavlibrary_books.add(eavlibrary_book);
    }

}