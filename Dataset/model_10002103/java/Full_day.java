





import java.util.List;
import java.util.ArrayList;

public class Full_day  {

    private int end_date;
    private int start_date;



    public Full_day(
        int end_date,        int start_date    ) {
        this.end_date = end_date;
        this.start_date = start_date;
    }


    public int getEnd_date() {
        return end_date;
    }

    public void setEnd_date(int end_date) {
        this.end_date = end_date;
    }
    public int getStart_date() {
        return start_date;
    }

    public void setStart_date(int start_date) {
        this.start_date = start_date;
    }


}