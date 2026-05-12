





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String creditCardDetails;
    private int orderID;
    private String orderNotes;
    private String date;
    private int time;





    private Customer customer;


    public Order(
        String creditCardDetails,        int orderID,        String orderNotes,        String date,        int time    ) {
        this.creditCardDetails = creditCardDetails;
        this.orderID = orderID;
        this.orderNotes = orderNotes;
        this.date = date;
        this.time = time;
    }


    public String getCreditcarddetails() {
        return creditCardDetails;
    }

    public void setCreditcarddetails(String creditCardDetails) {
        this.creditCardDetails = creditCardDetails;
    }
    public int getOrderid() {
        return orderID;
    }

    public void setOrderid(int orderID) {
        this.orderID = orderID;
    }
    public String getOrdernotes() {
        return orderNotes;
    }

    public void setOrdernotes(String orderNotes) {
        this.orderNotes = orderNotes;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}