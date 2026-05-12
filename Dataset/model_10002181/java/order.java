





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int OrderID;
    private String date;
    private String attribute;
    private int Customerid;
    private String Dishname;



    public Order(
        int OrderID,        String date,        String attribute,        int Customerid,        String Dishname    ) {
        this.OrderID = OrderID;
        this.date = date;
        this.attribute = attribute;
        this.Customerid = Customerid;
        this.Dishname = Dishname;
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
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public int getCustomerid() {
        return Customerid;
    }

    public void setCustomerid(int Customerid) {
        this.Customerid = Customerid;
    }
    public String getDishname() {
        return Dishname;
    }

    public void setDishname(String Dishname) {
        this.Dishname = Dishname;
    }


}