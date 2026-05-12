





import java.util.List;
import java.util.ArrayList;

public class DBLP_InCollection extends Record {

    private String title;
    private int fromPage;
    private String month;
    private int year;
    private int toPage;
    private String bookTitle;





    private DBLP_Publisher dblp_publisher;


    public DBLP_InCollection(
        String title,        int fromPage,        String month,        int year,        int toPage,        String bookTitle    ) {
        super(
        );
        this.title = title;
        this.fromPage = fromPage;
        this.month = month;
        this.year = year;
        this.toPage = toPage;
        this.bookTitle = bookTitle;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getFrompage() {
        return fromPage;
    }

    public void setFrompage(int fromPage) {
        this.fromPage = fromPage;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }
    public int getTopage() {
        return toPage;
    }

    public void setTopage(int toPage) {
        this.toPage = toPage;
    }
    public String getBooktitle() {
        return bookTitle;
    }

    public void setBooktitle(String bookTitle) {
        this.bookTitle = bookTitle;
    }

    public DBLP_Publisher getDblp_publisher() {
        return dblp_publisher;
    }

    public void setDblp_publisher(DBLP_Publisher dblp_publisher) {
        this.dblp_publisher = dblp_publisher;
    }

}