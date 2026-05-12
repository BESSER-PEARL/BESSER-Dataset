





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private boolean Status;
    private int UserID;
    private int OrderCustomerID;
    private int ShopOnlineID;
    private String TotalDiscount;
    private int OrderID;
    private String OrderDate;
    private int ReceiveCustomerID;
    private String TotalPrice;





    private OnlineShop onlineshop;


    public Order(
        boolean Status,        int UserID,        int OrderCustomerID,        int ShopOnlineID,        String TotalDiscount,        int OrderID,        String OrderDate,        int ReceiveCustomerID,        String TotalPrice    ) {
        this.Status = Status;
        this.UserID = UserID;
        this.OrderCustomerID = OrderCustomerID;
        this.ShopOnlineID = ShopOnlineID;
        this.TotalDiscount = TotalDiscount;
        this.OrderID = OrderID;
        this.OrderDate = OrderDate;
        this.ReceiveCustomerID = ReceiveCustomerID;
        this.TotalPrice = TotalPrice;
    }


    public boolean getStatus() {
        return Status;
    }

    public void setStatus(boolean Status) {
        this.Status = Status;
    }
    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }
    public int getOrdercustomerid() {
        return OrderCustomerID;
    }

    public void setOrdercustomerid(int OrderCustomerID) {
        this.OrderCustomerID = OrderCustomerID;
    }
    public int getShoponlineid() {
        return ShopOnlineID;
    }

    public void setShoponlineid(int ShopOnlineID) {
        this.ShopOnlineID = ShopOnlineID;
    }
    public String getTotaldiscount() {
        return TotalDiscount;
    }

    public void setTotaldiscount(String TotalDiscount) {
        this.TotalDiscount = TotalDiscount;
    }
    public int getOrderid() {
        return OrderID;
    }

    public void setOrderid(int OrderID) {
        this.OrderID = OrderID;
    }
    public String getOrderdate() {
        return OrderDate;
    }

    public void setOrderdate(String OrderDate) {
        this.OrderDate = OrderDate;
    }
    public int getReceivecustomerid() {
        return ReceiveCustomerID;
    }

    public void setReceivecustomerid(int ReceiveCustomerID) {
        this.ReceiveCustomerID = ReceiveCustomerID;
    }
    public String getTotalprice() {
        return TotalPrice;
    }

    public void setTotalprice(String TotalPrice) {
        this.TotalPrice = TotalPrice;
    }

    public OnlineShop getOnlineshop() {
        return onlineshop;
    }

    public void setOnlineshop(OnlineShop onlineshop) {
        this.onlineshop = onlineshop;
    }

}