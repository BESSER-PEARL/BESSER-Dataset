





import java.util.List;
import java.util.ArrayList;

public class DBLP_Www extends Record {

    private String month;
    private int year;
    private String title;



    public DBLP_Www(
        String month,        int year,        String title    ) {
        super(
        );
        this.month = month;
        this.year = year;
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
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}