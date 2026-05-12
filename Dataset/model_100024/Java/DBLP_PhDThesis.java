





import java.util.List;
import java.util.ArrayList;

public class DBLP_PhDThesis extends Record {

    private String month;
    private String title;
    private int year;



    public DBLP_PhDThesis(
        String month,        String title,        int year    ) {
        super(
        );
        this.month = month;
        this.title = title;
        this.year = year;
    }


    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
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


}