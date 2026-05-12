





import java.util.List;
import java.util.ArrayList;

public class Orders  {

    private String Customer_Id;
    private String Date_Created;
    private int Order_id;
    private String Date_Shipped;
    private String Status;





    private Customer customer;


    public Orders(
        String Customer_Id,        String Date_Created,        int Order_id,        String Date_Shipped,        String Status    ) {
        this.Customer_Id = Customer_Id;
        this.Date_Created = Date_Created;
        this.Order_id = Order_id;
        this.Date_Shipped = Date_Shipped;
        this.Status = Status;
    }


    public String getCustomer_id() {
        return Customer_Id;
    }

    public void setCustomer_id(String Customer_Id) {
        this.Customer_Id = Customer_Id;
    }
    public String getDate_created() {
        return Date_Created;
    }

    public void setDate_created(String Date_Created) {
        this.Date_Created = Date_Created;
    }
    public int getOrder_id() {
        return Order_id;
    }

    public void setOrder_id(int Order_id) {
        this.Order_id = Order_id;
    }
    public String getDate_shipped() {
        return Date_Shipped;
    }

    public void setDate_shipped(String Date_Shipped) {
        this.Date_Shipped = Date_Shipped;
    }
    public String getStatus() {
        return Status;
    }

    public void setStatus(String Status) {
        this.Status = Status;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}