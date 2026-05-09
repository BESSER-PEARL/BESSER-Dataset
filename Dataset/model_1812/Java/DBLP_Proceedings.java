





import java.util.List;
import java.util.ArrayList;

public class DBLP_Proceedings extends Record {

    private String title;
    private String month;
    private String isbn;
    private int year;



    public DBLP_Proceedings(
        String title,        String month,        String isbn,        int year    ) {
        super(
        );
        this.title = title;
        this.month = month;
        this.isbn = isbn;
        this.year = year;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
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