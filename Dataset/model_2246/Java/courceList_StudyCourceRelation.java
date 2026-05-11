





import java.util.List;
import java.util.ArrayList;

public class courceList_StudyCourceRelation  {

    private String status;
    private int year;



    public courceList_StudyCourceRelation(
        String status,        int year    ) {
        this.status = status;
        this.year = year;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }


}