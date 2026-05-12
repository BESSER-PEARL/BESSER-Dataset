





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String Date;
    private int UserID;
    private int Completed;
    private int OrderID;





    private Table table;




    private Users users;


    public Order(
        String Date,        int UserID,        int Completed,        int OrderID    ) {
        this.Date = Date;
        this.UserID = UserID;
        this.Completed = Completed;
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
    public int getCompleted() {
        return Completed;
    }

    public void setCompleted(int Completed) {
        this.Completed = Completed;
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