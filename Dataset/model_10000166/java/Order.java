




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int UserID;
    private LocalDate Date;
    private float Total;
    private int DicountLvl;
    private int OrderID;





    private Table table;




    private Users users;


    public Order(
        int UserID,        LocalDate Date,        float Total,        int DicountLvl,        int OrderID    ) {
        this.UserID = UserID;
        this.Date = Date;
        this.Total = Total;
        this.DicountLvl = DicountLvl;
        this.OrderID = OrderID;
    }


    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
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

    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }
    public Users getUsers() {
        return users;
    }

    public void setUsers(Users users) {
        this.users = users;
    }

}