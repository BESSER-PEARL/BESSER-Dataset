





import java.util.List;
import java.util.ArrayList;

public class DBLP_MastersThesis extends Record {

    private String title;
    private String month;
    private int year;



    public DBLP_MastersThesis(
        String title,        String month,        int year    ) {
        super(
        );
        this.title = title;
        this.month = month;
        this.year = year;
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


}