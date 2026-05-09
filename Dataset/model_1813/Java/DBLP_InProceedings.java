





import java.util.List;
import java.util.ArrayList;

public class DBLP_InProceedings extends Record {

    private int toPage;
    private int year;
    private String title;
    private String bootitle;
    private String month;
    private int fromPage;



    public DBLP_InProceedings(
        int toPage,        int year,        String title,        String bootitle,        String month,        int fromPage    ) {
        super(
        );
        this.toPage = toPage;
        this.year = year;
        this.title = title;
        this.bootitle = bootitle;
        this.month = month;
        this.fromPage = fromPage;
    }


    public int getTopage() {
        return toPage;
    }

    public void setTopage(int toPage) {
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
    public String getBootitle() {
        return bootitle;
    }

    public void setBootitle(String bootitle) {
        this.bootitle = bootitle;
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