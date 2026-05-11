





import java.util.List;
import java.util.ArrayList;

public class RandL_Date  {

    private String day;
    private String year;
    private String month;





    private RandL_Transaction randl_transaction;




    private RandL_Customer randl_customer;




    private RandL_Container_RandL randl_container_randl;


    public RandL_Date(
        String day,        String year,        String month    ) {
        this.day = day;
        this.year = year;
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
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }

    public RandL_Transaction getRandl_transaction() {
        return randl_transaction;
    }

    public void setRandl_transaction(RandL_Transaction randl_transaction) {
        this.randl_transaction = randl_transaction;
    }
    public RandL_Customer getRandl_customer() {
        return randl_customer;
    }

    public void setRandl_customer(RandL_Customer randl_customer) {
        this.randl_customer = randl_customer;
    }
    public RandL_Container_RandL getRandl_container_randl() {
        return randl_container_randl;
    }

    public void setRandl_container_randl(RandL_Container_RandL randl_container_randl) {
        this.randl_container_randl = randl_container_randl;
    }

}