





import java.util.List;
import java.util.ArrayList;

public class DBLP_InProceedings extends Record {

    private String bootitle;
    private int fromPage;
    private String title;
    private String month;
    private int year;
    private int toPage;





    private DBLP_Publisher dblp_publisher;


    public DBLP_InProceedings(
        String bootitle,        int fromPage,        String title,        String month,        int year,        int toPage    ) {
        super(
        );
        this.bootitle = bootitle;
        this.fromPage = fromPage;
        this.title = title;
        this.month = month;
        this.year = year;
        this.toPage = toPage;
    }


    public String getBootitle() {
        return bootitle;
    }

    public void setBootitle(String bootitle) {
        this.bootitle = bootitle;
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

    public DBLP_Publisher getDblp_publisher() {
        return dblp_publisher;
    }

    public void setDblp_publisher(DBLP_Publisher dblp_publisher) {
        this.dblp_publisher = dblp_publisher;
    }

}