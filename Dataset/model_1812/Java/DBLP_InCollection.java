





import java.util.List;
import java.util.ArrayList;

public class DBLP_InCollection extends Record {

    private int toPage;
    private String title;
    private String bookTitle;
    private int year;
    private String month;
    private int fromPage;



    public DBLP_InCollection(
        int toPage,        String title,        String bookTitle,        int year,        String month,        int fromPage    ) {
        super(
        );
        this.toPage = toPage;
        this.title = title;
        this.bookTitle = bookTitle;
        this.year = year;
        this.month = month;
        this.fromPage = fromPage;
    }


    public int getTopage() {
        return toPage;
    }

    public void setTopage(int toPage) {
        this.toPage = toPage;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getBooktitle() {
        return bookTitle;
    }

    public void setBooktitle(String bookTitle) {
        this.bookTitle = bookTitle;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public int getFrompage() {
        return fromPage;
    }

    public void setFrompage(int fromPage) {
        this.fromPage = fromPage;
    }


}