





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String TimeStamp;
    private int Customer_id;
    private String Status;
    private String Customer_name;
    private int Table_id;



    public Customer(
        String TimeStamp,        int Customer_id,        String Status,        String Customer_name,        int Table_id    ) {
        this.TimeStamp = TimeStamp;
        this.Customer_id = Customer_id;
        this.Status = Status;
        this.Customer_name = Customer_name;
        this.Table_id = Table_id;
    }


    public String getTimestamp() {
        return TimeStamp;
    }

    public void setTimestamp(String TimeStamp) {
        this.TimeStamp = TimeStamp;
    }
    public int getCustomer_id() {
        return Customer_id;
    }

    public void setCustomer_id(int Customer_id) {
        this.Customer_id = Customer_id;
    }
    public String getStatus() {
        return Status;
    }

    public void setStatus(String Status) {
        this.Status = Status;
    }
    public String getCustomer_name() {
        return Customer_name;
    }

    public void setCustomer_name(String Customer_name) {
        this.Customer_name = Customer_name;
    }
    public int getTable_id() {
        return Table_id;
    }

    public void setTable_id(int Table_id) {
        this.Table_id = Table_id;
    }


}