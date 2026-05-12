





import java.util.List;
import java.util.ArrayList;

public class DBLP_Proceedings extends Record {

    private String title;
    private int year;
    private String isbn;
    private String month;





    private DBLP_Publisher dblp_publisher;


    public DBLP_Proceedings(
        String title,        int year,        String isbn,        String month    ) {
        super(
        );
        this.title = title;
        this.year = year;
        this.isbn = isbn;
        this.month = month;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }
    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }

    public DBLP_Publisher getDblp_publisher() {
        return dblp_publisher;
    }

    public void setDblp_publisher(DBLP_Publisher dblp_publisher) {
        this.dblp_publisher = dblp_publisher;
    }

}