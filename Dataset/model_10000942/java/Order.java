




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int UserID;
    private int OrderID;
    private int DicountLvl;
    private LocalDate Date;
    private float Total;





    private Table table;




    private Users users;


    public Order(
        int UserID,        int OrderID,        int DicountLvl,        LocalDate Date,        float Total    ) {
        this.UserID = UserID;
        this.OrderID = OrderID;
        this.DicountLvl = DicountLvl;
        this.Date = Date;
        this.Total = Total;
    }


    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }
    public int getOrderid() {
        return OrderID;
    }

    public void setOrderid(int OrderID) {
        this.OrderID = OrderID;
    }
    public int getDicountlvl() {
        return DicountLvl;
    }

    public void setDicountlvl(int DicountLvl) {
        this.DicountLvl = DicountLvl;
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
    public Users getUsers() {
        return users;
    }

    public void setUsers(Users users) {
        this.users = users;
    }

}