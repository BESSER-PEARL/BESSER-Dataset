





import java.util.List;
import java.util.ArrayList;

public class Orders  {

    private String OrderInfo;
    private int OrderID;
    private String DeliInfo;
    private int UserID;





    private User user;


    public Orders(
        String OrderInfo,        int OrderID,        String DeliInfo,        int UserID    ) {
        this.OrderInfo = OrderInfo;
        this.OrderID = OrderID;
        this.DeliInfo = DeliInfo;
        this.UserID = UserID;
    }


    public String getOrderinfo() {
        return OrderInfo;
    }

    public void setOrderinfo(String OrderInfo) {
        this.OrderInfo = OrderInfo;
    }
    public int getOrderid() {
        return OrderID;
    }

    public void setOrderid(int OrderID) {
        this.OrderID = OrderID;
    }
    public String getDeliinfo() {
        return DeliInfo;
    }

    public void setDeliinfo(String DeliInfo) {
        this.DeliInfo = DeliInfo;
    }
    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}