





import java.util.List;
import java.util.ArrayList;

public class DBLP_InProceedings extends Record {

    private String title;
    private int fromPage;
    private int year;
    private String month;
    private int toPage;
    private String bootitle;



    public DBLP_InProceedings(
        String title,        int fromPage,        int year,        String month,        int toPage,        String bootitle    ) {
        super(
        );
        this.title = title;
        this.fromPage = fromPage;
        this.year = year;
        this.month = month;
        this.toPage = toPage;
        this.bootitle = bootitle;
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
    public String getBootitle() {
        return bootitle;
    }

    public void setBootitle(String bootitle) {
        this.bootitle = bootitle;
    }


}