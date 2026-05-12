





import java.util.List;
import java.util.ArrayList;

public class ShoppingCart  {

    private None Promo;
    private int ShoppingCartID;
    private int Quantity;
    private int OrderID;
    private String UserID;
    private String Total;
    private int ProductID;





    private User_Account user_account;


    public ShoppingCart(
        None Promo,        int ShoppingCartID,        int Quantity,        int OrderID,        String UserID,        String Total,        int ProductID    ) {
        this.Promo = Promo;
        this.ShoppingCartID = ShoppingCartID;
        this.Quantity = Quantity;
        this.OrderID = OrderID;
        this.UserID = UserID;
        this.Total = Total;
        this.ProductID = ProductID;
    }


    public None getPromo() {
        return Promo;
    }

    public void setPromo(None Promo) {
        this.Promo = Promo;
    }
    public int getShoppingcartid() {
        return ShoppingCartID;
    }

    public void setShoppingcartid(int ShoppingCartID) {
        this.ShoppingCartID = ShoppingCartID;
    }
    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int Quantity) {
        this.Quantity = Quantity;
    }
    public int getOrderid() {
        return OrderID;
    }

    public void setOrderid(int OrderID) {
        this.OrderID = OrderID;
    }
    public String getUserid() {
        return UserID;
    }

    public void setUserid(String UserID) {
        this.UserID = UserID;
    }
    public String getTotal() {
        return Total;
    }

    public void setTotal(String Total) {
        this.Total = Total;
    }
    public int getProductid() {
        return ProductID;
    }

    public void setProductid(int ProductID) {
        this.ProductID = ProductID;
    }

    public User_Account getUser_account() {
        return user_account;
    }

    public void setUser_account(User_Account user_account) {
        this.user_account = user_account;
    }

}