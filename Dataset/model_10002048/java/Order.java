





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int OrderID;
    private int CusID;
    private String DateCreated;





    private Customer customer;


    public Order(
        int OrderID,        int CusID,        String DateCreated    ) {
        this.OrderID = OrderID;
        this.CusID = CusID;
        this.DateCreated = DateCreated;
    }


    public int getOrderid() {
        return OrderID;
    }

    public void setOrderid(int OrderID) {
        this.OrderID = OrderID;
    }
    public int getCusid() {
        return CusID;
    }

    public void setCusid(int CusID) {
        this.CusID = CusID;
    }
    public String getDatecreated() {
        return DateCreated;
    }

    public void setDatecreated(String DateCreated) {
        this.DateCreated = DateCreated;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}