





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private None price;
    private int quantity;





    private Account account;


    public Order(
        None price,        int quantity    ) {
        this.price = price;
        this.quantity = quantity;
    }


    public None getPrice() {
        return price;
    }

    public void setPrice(None price) {
        this.price = price;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

}