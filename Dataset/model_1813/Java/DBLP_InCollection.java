





import java.util.List;
import java.util.ArrayList;

public class DBLP_InCollection extends Record {

    private String bookTitle;
    private int fromPage;
    private String title;
    private int year;
    private String month;
    private int toPage;



    public DBLP_InCollection(
        String bookTitle,        int fromPage,        String title,        int year,        String month,        int toPage    ) {
        super(
        );
        this.bookTitle = bookTitle;
        this.fromPage = fromPage;
        this.title = title;
        this.year = year;
        this.month = month;
        this.toPage = toPage;
    }


    public String getBooktitle() {
        return bookTitle;
    }

    public void setBooktitle(String bookTitle) {
        this.bookTitle = bookTitle;
    }
    public int getFrompage() {
        return fromPage;
    }

    public void setFrompage(int fromPage) {
        this.fromPage = fromPage;
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
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public int getTopage() {
        return toPage;
    }

    public void setTopage(int toPage) {
        this.toPage = toPage;
    }


}