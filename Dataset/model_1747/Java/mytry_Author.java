





import java.util.List;
import java.util.ArrayList;

public class mytry_Author  {

    private String name;





    private List<mytry_Book> mytry_books;




    private mytry_Library mytry_library;




    private mytry_Book mytry_book;


    public mytry_Author(
        String name    ) {
        this.name = name;
        this.mytry_books = new ArrayList<>();
    }

    public mytry_Author(
        String name        ArrayList<mytry_Book> mytry_books    ) {
        this.name = name;
        this.mytry_books = mytry_books;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<mytry_Book> getMytry_books() {
        return mytry_books;
    }

    public void addMytry_book(Mytry_book mytry_book) {
        this.mytry_books.add(mytry_book);
    }
    public mytry_Library getMytry_library() {
        return mytry_library;
    }

    public void setMytry_library(mytry_Library mytry_library) {
        this.mytry_library = mytry_library;
    }
    public mytry_Book getMytry_book() {
        return mytry_book;
    }

    public void setMytry_book(mytry_Book mytry_book) {
        this.mytry_book = mytry_book;
    }

}