





import java.util.List;
import java.util.ArrayList;

public class DBLP_Proceedings extends Record {

    private String month;
    private String title;
    private String isbn;
    private int year;



    public DBLP_Proceedings(
        String month,        String title,        String isbn,        int year    ) {
        super(
        );
        this.month = month;
        this.title = title;
        this.isbn = isbn;
        this.year = year;
    }


    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
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
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }


}