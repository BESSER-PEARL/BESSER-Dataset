





import java.util.List;
import java.util.ArrayList;

public class bz242995_Library  {

    private String name;





    private List<bz242995_Book> bz242995_books;




    private List<bz242995_Writer> bz242995_writers;


    public bz242995_Library(
        String name    ) {
        this.name = name;
        this.bz242995_books = new ArrayList<>();
        this.bz242995_writers = new ArrayList<>();
    }

    public bz242995_Library(
        String name        ArrayList<bz242995_Book> bz242995_books,        ArrayList<bz242995_Writer> bz242995_writers    ) {
        this.name = name;
        this.bz242995_books = bz242995_books;
        this.bz242995_writers = bz242995_writers;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<bz242995_Book> getBz242995_books() {
        return bz242995_books;
    }

    public void addBz242995_book(Bz242995_book bz242995_book) {
        this.bz242995_books.add(bz242995_book);
    }
    public List<bz242995_Writer> getBz242995_writers() {
        return bz242995_writers;
    }

    public void addBz242995_writer(Bz242995_writer bz242995_writer) {
        this.bz242995_writers.add(bz242995_writer);
    }

}