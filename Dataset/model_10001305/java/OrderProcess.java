





import java.util.List;
import java.util.ArrayList;

public class OrderProcess  {

    private int UserID;
    private int OrderPickUp;
    private String Total;
    private int OrderID;
    private int MemberShipPayment;
    private String PromoCode;
    private int IsMember;





    private User_Account user_account;




    private ShoppingCart shoppingcart;


    public OrderProcess(
        int UserID,        int OrderPickUp,        String Total,        int OrderID,        int MemberShipPayment,        String PromoCode,        int IsMember    ) {
        this.UserID = UserID;
        this.OrderPickUp = OrderPickUp;
        this.Total = Total;
        this.OrderID = OrderID;
        this.MemberShipPayment = MemberShipPayment;
        this.PromoCode = PromoCode;
        this.IsMember = IsMember;
    }


    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }
    public int getOrderpickup() {
        return OrderPickUp;
    }

    public void setOrderpickup(int OrderPickUp) {
        this.OrderPickUp = OrderPickUp;
    }
    public String getTotal() {
        return Total;
    }

    public void setTotal(String Total) {
        this.Total = Total;
    }
    public int getOrderid() {
        return OrderID;
    }

    public void setOrderid(int OrderID) {
        this.OrderID = OrderID;
    }
    public int getMembershippayment() {
        return MemberShipPayment;
    }

    public void setMembershippayment(int MemberShipPayment) {
        this.MemberShipPayment = MemberShipPayment;
    }
    public String getPromocode() {
        return PromoCode;
    }

    public void setPromocode(String PromoCode) {
        this.PromoCode = PromoCode;
    }
    public int getIsmember() {
        return IsMember;
    }

    public void setIsmember(int IsMember) {
        this.IsMember = IsMember;
    }

    public User_Account getUser_account() {
        return user_account;
    }

    public void setUser_account(User_Account user_account) {
        this.user_account = user_account;
    }
    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}