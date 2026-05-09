





import java.util.List;
import java.util.ArrayList;

public class book_Book  {

    private int id;
    private String name;





    private book_BookCollection book_bookcollection;


    public book_Book(
        int id,        String name    ) {
        this.id = id;
        this.name = name;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public book_BookCollection getBook_bookcollection() {
        return book_bookcollection;
    }

    public void setBook_bookcollection(book_BookCollection book_bookcollection) {
        this.book_bookcollection = book_bookcollection;
    }

}