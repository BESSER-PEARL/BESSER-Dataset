





import java.util.List;
import java.util.ArrayList;

public class cascadenotall_Library  {

    private String name;





    private List<cascadenotall_Book> cascadenotall_books;




    private List<cascadenotall_Writer> cascadenotall_writers;


    public cascadenotall_Library(
        String name    ) {
        this.name = name;
        this.cascadenotall_books = new ArrayList<>();
        this.cascadenotall_writers = new ArrayList<>();
    }

    public cascadenotall_Library(
        String name        ArrayList<cascadenotall_Book> cascadenotall_books,        ArrayList<cascadenotall_Writer> cascadenotall_writers    ) {
        this.name = name;
        this.cascadenotall_books = cascadenotall_books;
        this.cascadenotall_writers = cascadenotall_writers;
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
    public List<cascadenotall_Writer> getCascadenotall_writers() {
        return cascadenotall_writers;
    }

    public void addCascadenotall_writer(Cascadenotall_writer cascadenotall_writer) {
        this.cascadenotall_writers.add(cascadenotall_writer);
    }

}