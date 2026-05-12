





import java.util.List;
import java.util.ArrayList;

public class Order1  {

    private int Customerid;
    private String attribute;
    private int OrderID;
    private String date;
    private String Dishname;





    private Customer1 customer1;




    private Customer1 customer1;




    private Payment1 payment1;


    public Order1(
        int Customerid,        String attribute,        int OrderID,        String date,        String Dishname    ) {
        this.Customerid = Customerid;
        this.attribute = attribute;
        this.OrderID = OrderID;
        this.date = date;
        this.Dishname = Dishname;
    }


    public int getCustomerid() {
        return Customerid;
    }

    public void setCustomerid(int Customerid) {
        this.Customerid = Customerid;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public int getOrderid() {
        return OrderID;
    }

    public void setOrderid(int OrderID) {
        this.OrderID = OrderID;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getDishname() {
        return Dishname;
    }

    public void setDishname(String Dishname) {
        this.Dishname = Dishname;
    }

    public Customer1 getCustomer1() {
        return customer1;
    }

    public void setCustomer1(Customer1 customer1) {
        this.customer1 = customer1;
    }
    public Customer1 getCustomer1() {
        return customer1;
    }

    public void setCustomer1(Customer1 customer1) {
        this.customer1 = customer1;
    }
    public Payment1 getPayment1() {
        return payment1;
    }

    public void setPayment1(Payment1 payment1) {
        this.payment1 = payment1;
    }

}