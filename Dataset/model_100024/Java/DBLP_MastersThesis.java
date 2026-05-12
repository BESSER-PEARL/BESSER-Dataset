





import java.util.List;
import java.util.ArrayList;

public class DBLP_MastersThesis extends Record {

    private int year;
    private String month;
    private String title;



    public DBLP_MastersThesis(
        int year,        String month,        String title    ) {
        super(
        );
        this.year = year;
        this.month = month;
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
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}