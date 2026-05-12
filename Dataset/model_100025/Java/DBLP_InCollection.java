





import java.util.List;
import java.util.ArrayList;

public class DBLP_InCollection extends Record {

    private int year;
    private String title;
    private int fromPage;
    private String month;
    private String bookTitle;
    private int toPage;



    public DBLP_InCollection(
        int year,        String title,        int fromPage,        String month,        String bookTitle,        int toPage    ) {
        super(
        );
        this.year = year;
        this.title = title;
        this.fromPage = fromPage;
        this.month = month;
        this.bookTitle = bookTitle;
        this.toPage = toPage;
    }


    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
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
    public String getBooktitle() {
        return bookTitle;
    }

    public void setBooktitle(String bookTitle) {
        this.bookTitle = bookTitle;
    }
    public int getTopage() {
        return toPage;
    }

    public void setTopage(int toPage) {
        this.toPage = toPage;
    }


}