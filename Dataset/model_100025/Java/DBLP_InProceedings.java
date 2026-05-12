





import java.util.List;
import java.util.ArrayList;

public class DBLP_InProceedings extends Record {

    private String month;
    private int year;
    private int fromPage;
    private String title;
    private String bootitle;
    private int toPage;



    public DBLP_InProceedings(
        String month,        int year,        int fromPage,        String title,        String bootitle,        int toPage    ) {
        super(
        );
        this.month = month;
        this.year = year;
        this.fromPage = fromPage;
        this.title = title;
        this.bootitle = bootitle;
        this.toPage = toPage;
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
    public String getBootitle() {
        return bootitle;
    }

    public void setBootitle(String bootitle) {
        this.bootitle = bootitle;
    }
    public int getTopage() {
        return toPage;
    }

    public void setTopage(int toPage) {
        this.toPage = toPage;
    }


}