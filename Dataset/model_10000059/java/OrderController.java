





import java.util.List;
import java.util.ArrayList;

public class OrderController  {

    private String Date;
    private int UserID;
    private String OrderTotal;
    private int OrderID;





    private Table table;


    public OrderController(
        String Date,        int UserID,        String OrderTotal,        int OrderID    ) {
        this.Date = Date;
        this.UserID = UserID;
        this.OrderTotal = OrderTotal;
        this.OrderID = OrderID;
    }


    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }
    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }
    public String getOrdertotal() {
        return OrderTotal;
    }

    public void setOrdertotal(String OrderTotal) {
        this.OrderTotal = OrderTotal;
    }
    public int getOrderid() {
        return OrderID;
    }

    public void setOrderid(int OrderID) {
        this.OrderID = OrderID;
    }

    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }

}