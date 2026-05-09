





import java.util.List;
import java.util.ArrayList;

public class cascadenotall_Writer  {

    private String name;





    private List<cascadenotall_Book> cascadenotall_books;




    private cascadenotall_Book cascadenotall_book;


    public cascadenotall_Writer(
        String name    ) {
        this.name = name;
        this.cascadenotall_books = new ArrayList<>();
    }

    public cascadenotall_Writer(
        String name        ArrayList<cascadenotall_Book> cascadenotall_books    ) {
        this.name = name;
        this.cascadenotall_books = cascadenotall_books;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<cascadenotall_Book> getCascadenotall_books() {
        return cascadenotall_books;
    }

    public void addCascadenotall_book(Cascadenotall_book cascadenotall_book) {
        this.cascadenotall_books.add(cascadenotall_book);
    }
    public cascadenotall_Book getCascadenotall_book() {
        return cascadenotall_book;
    }

    public void setCascadenotall_book(cascadenotall_Book cascadenotall_book) {
        this.cascadenotall_book = cascadenotall_book;
    }

}