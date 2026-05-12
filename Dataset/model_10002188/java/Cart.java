





import java.util.List;
import java.util.ArrayList;

public class Cart  {

    private int CartID;
    private String CartInfo;





    private User user;


    public Cart(
        int CartID,        String CartInfo    ) {
        this.CartID = CartID;
        this.CartInfo = CartInfo;
    }


    public int getCartid() {
        return CartID;
    }

    public void setCartid(int CartID) {
        this.CartID = CartID;
    }
    public String getCartinfo() {
        return CartInfo;
    }

    public void setCartinfo(String CartInfo) {
        this.CartInfo = CartInfo;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}