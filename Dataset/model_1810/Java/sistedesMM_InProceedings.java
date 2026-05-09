





import java.util.List;
import java.util.ArrayList;

public class sistedesMM_InProceedings extends Publication {

    private String fromPage;
    private String bookTitle;
    private int year;
    private String toPage;
    private String title;
    private String month;





    private sistedesMM_Publisher sistedesmm_publisher;


    public sistedesMM_InProceedings(
        String fromPage,        String bookTitle,        int year,        String toPage,        String title,        String month    ) {
        super(
        );
        this.fromPage = fromPage;
        this.bookTitle = bookTitle;
        this.year = year;
        this.toPage = toPage;
        this.title = title;
        this.month = month;
    }


    public String getFrompage() {
        return fromPage;
    }

    public void setFrompage(String fromPage) {
        this.fromPage = fromPage;
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
    public String getTopage() {
        return toPage;
    }

    public void setTopage(String toPage) {
        this.toPage = toPage;
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

    public sistedesMM_Publisher getSistedesmm_publisher() {
        return sistedesmm_publisher;
    }

    public void setSistedesmm_publisher(sistedesMM_Publisher sistedesmm_publisher) {
        this.sistedesmm_publisher = sistedesmm_publisher;
    }

}