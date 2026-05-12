




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int UserID;
    private int DicountLvl;
    private float Total;
    private int OrderID;
    private LocalDate Date;





    private Table table;




    private Users users;


    public Order(
        int UserID,        int DicountLvl,        float Total,        int OrderID,        LocalDate Date    ) {
        this.UserID = UserID;
        this.DicountLvl = DicountLvl;
        this.Total = Total;
        this.OrderID = OrderID;
        this.Date = Date;
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
    public float getTotal() {
        return Total;
    }

    public void setTotal(float Total) {
        this.Total = Total;
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