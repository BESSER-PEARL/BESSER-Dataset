





import java.util.List;
import java.util.ArrayList;

public class libraryinteractionmodel_Book  {

    private String title;
    private String isbn;



    public libraryinteractionmodel_Book(
        String title,        String isbn    ) {
        this.title = title;
        this.isbn = isbn;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }


}