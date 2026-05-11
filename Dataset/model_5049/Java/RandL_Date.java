





import java.util.List;
import java.util.ArrayList;

public class RandL_Date  {

    private String month;
    private String day;
    private String year;





    private RandL_Transaction randl_transaction;


    public RandL_Date(
        String month,        String day,        String year    ) {
        this.month = month;
        this.day = day;
        this.year = year;
    }


    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public String getDay() {
        return day;
    }

    public void setDay(String day) {
        this.day = day;
    }
    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }

    public RandL_Transaction getRandl_transaction() {
        return randl_transaction;
    }

    public void setRandl_transaction(RandL_Transaction randl_transaction) {
        this.randl_transaction = randl_transaction;
    }

}