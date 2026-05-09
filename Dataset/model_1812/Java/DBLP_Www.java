





import java.util.List;
import java.util.ArrayList;

public class DBLP_Www extends Record {

    private int year;
    private String title;
    private String month;



    public DBLP_Www(
        int year,        String title,        String month    ) {
        super(
        );
        this.year = year;
        this.title = title;
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
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }


}