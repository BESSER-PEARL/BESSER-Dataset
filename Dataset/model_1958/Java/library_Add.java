





import java.util.List;
import java.util.ArrayList;

public class library_Add extends Command {

    private String isbn;
    private String year;
    private String title;



    public library_Add(
        String isbn,        String year,        String title    ) {
        super(
        );
        this.isbn = isbn;
        this.year = year;
        this.title = title;
    }


    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }
    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}