





import java.util.List;
import java.util.ArrayList;

public class Orders  {

    private String dateOrdered;
    private String status;
    private String dateFinished;
    private int OrderID;





    private Customer customer;


    public Orders(
        String dateOrdered,        String status,        String dateFinished,        int OrderID    ) {
        this.dateOrdered = dateOrdered;
        this.status = status;
        this.dateFinished = dateFinished;
        this.OrderID = OrderID;
    }


    public String getDateordered() {
        return dateOrdered;
    }

    public void setDateordered(String dateOrdered) {
        this.dateOrdered = dateOrdered;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getDatefinished() {
        return dateFinished;
    }

    public void setDatefinished(String dateFinished) {
        this.dateFinished = dateFinished;
    }
    public int getOrderid() {
        return OrderID;
    }

    public void setOrderid(int OrderID) {
        this.OrderID = OrderID;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}