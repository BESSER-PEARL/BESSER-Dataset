




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int UserID;
    private int DicountLvl;
    private int OrderID;
    private LocalDate Date;
    private float Total;





    private Table table;


    public Order(
        int UserID,        int DicountLvl,        int OrderID,        LocalDate Date,        float Total    ) {
        this.UserID = UserID;
        this.DicountLvl = DicountLvl;
        this.OrderID = OrderID;
        this.Date = Date;
        this.Total = Total;
    }


    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }
    public int getDicountlvl() {
        return DicountLvl;
    }

    public void setDicountlvl(int DicountLvl) {
        this.DicountLvl = DicountLvl;
    }
    public int getOrderid() {
        return OrderID;
    }

    public void setOrderid(int OrderID) {
        this.OrderID = OrderID;
    }
    public LocalDate getDate() {
        return Date;
    }

    public void setDate(LocalDate Date) {
        this.Date = Date;
    }
    public float getTotal() {
        return Total;
    }

    public void setTotal(float Total) {
        this.Total = Total;
    }

    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }

}