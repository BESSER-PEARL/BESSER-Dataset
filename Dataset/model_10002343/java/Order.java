





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int quantity;
    private None price;





    private Account account;


    public Order(
        int quantity,        None price    ) {
        this.quantity = quantity;
        this.price = price;
    }


    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public None getPrice() {
        return price;
    }

    public void setPrice(None price) {
        this.price = price;
    }

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

}