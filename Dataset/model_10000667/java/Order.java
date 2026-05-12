




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int MenuItem;
    private int OrderID;
    private LocalDate OrderDate;
    private String ItemName;
    private int CustNumber;



    public Order(
        int MenuItem,        int OrderID,        LocalDate OrderDate,        String ItemName,        int CustNumber    ) {
        this.MenuItem = MenuItem;
        this.OrderID = OrderID;
        this.OrderDate = OrderDate;
        this.ItemName = ItemName;
        this.CustNumber = CustNumber;
    }


    public int getMenuitem() {
        return MenuItem;
    }

    public void setMenuitem(int MenuItem) {
        this.MenuItem = MenuItem;
    }
    public int getOrderid() {
        return OrderID;
    }

    public void setOrderid(int OrderID) {
        this.OrderID = OrderID;
    }
    public LocalDate getOrderdate() {
        return OrderDate;
    }

    public void setOrderdate(LocalDate OrderDate) {
        this.OrderDate = OrderDate;
    }
    public String getItemname() {
        return ItemName;
    }

    public void setItemname(String ItemName) {
        this.ItemName = ItemName;
    }
    public int getCustnumber() {
        return CustNumber;
    }

    public void setCustnumber(int CustNumber) {
        this.CustNumber = CustNumber;
    }


}