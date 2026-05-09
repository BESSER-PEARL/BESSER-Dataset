





import java.util.List;
import java.util.ArrayList;

public class bz242995_Writer  {

    private String name;





    private bz242995_Book bz242995_book;




    private List<bz242995_Book> bz242995_books;


    public bz242995_Writer(
        String name    ) {
        this.name = name;
        this.bz242995_books = new ArrayList<>();
    }

    public bz242995_Writer(
        String name        ArrayList<bz242995_Book> bz242995_books    ) {
        this.name = name;
        this.bz242995_books = bz242995_books;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bz242995_Book getBz242995_book() {
        return bz242995_book;
    }

    public void setBz242995_book(bz242995_Book bz242995_book) {
        this.bz242995_book = bz242995_book;
    }
    public List<bz242995_Book> getBz242995_books() {
        return bz242995_books;
    }

    public void addBz242995_book(Bz242995_book bz242995_book) {
        this.bz242995_books.add(bz242995_book);
    }

}