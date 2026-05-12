





import java.util.List;
import java.util.ArrayList;

public class sistedesMM_InProceedings extends Publication {

    private String toPage;
    private String fromPage;
    private String title;
    private String month;
    private String bookTitle;
    private int year;



    public sistedesMM_InProceedings(
        String toPage,        String fromPage,        String title,        String month,        String bookTitle,        int year    ) {
        super(
        );
        this.toPage = toPage;
        this.fromPage = fromPage;
        this.title = title;
        this.month = month;
        this.bookTitle = bookTitle;
        this.year = year;
    }


    public String getTopage() {
        return toPage;
    }

    public void setTopage(String toPage) {
        this.toPage = toPage;
    }
    public String getFrompage() {
        return fromPage;
    }

    public void setFrompage(String fromPage) {
        this.fromPage = fromPage;
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


}