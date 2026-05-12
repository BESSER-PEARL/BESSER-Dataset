





import java.util.List;
import java.util.ArrayList;

public class order  {

    private String order_status_;
    private int amount__;
    private int no_of_items_;





    private Account account;




    private Cart cart;


    public order(
        String order_status_,        int amount__,        int no_of_items_    ) {
        this.order_status_ = order_status_;
        this.amount__ = amount__;
        this.no_of_items_ = no_of_items_;
    }


    public String getOrder_status_() {
        return order_status_;
    }

    public void setOrder_status_(String order_status_) {
        this.order_status_ = order_status_;
    }
    public int getAmount__() {
        return amount__;
    }

    public void setAmount__(int amount__) {
        this.amount__ = amount__;
    }
    public int getNo_of_items_() {
        return no_of_items_;
    }

    public void setNo_of_items_(int no_of_items_) {
        this.no_of_items_ = no_of_items_;
    }

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }
    public Cart getCart() {
        return cart;
    }

    public void setCart(Cart cart) {
        this.cart = cart;
    }

}