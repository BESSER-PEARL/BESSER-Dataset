





import java.util.List;
import java.util.ArrayList;

public class elements_Writer  {

    private String name;





    private List<elements_Book> elements_books;




    private elements_Book elements_book;


    public elements_Writer(
        String name    ) {
        this.name = name;
        this.elements_books = new ArrayList<>();
    }

    public elements_Writer(
        String name        ArrayList<elements_Book> elements_books    ) {
        this.name = name;
        this.elements_books = elements_books;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<elements_Book> getElements_books() {
        return elements_books;
    }

    public void addElements_book(Elements_book elements_book) {
        this.elements_books.add(elements_book);
    }
    public elements_Book getElements_book() {
        return elements_book;
    }

    public void setElements_book(elements_Book elements_book) {
        this.elements_book = elements_book;
    }

}