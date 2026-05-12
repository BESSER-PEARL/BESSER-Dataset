





import java.util.List;
import java.util.ArrayList;

public class PaymentMethod  {

    private String online;
    private String cashOnDelievery;
    private String paymentType;





    private Cart cart;


    public PaymentMethod(
        String online,        String cashOnDelievery,        String paymentType    ) {
        this.online = online;
        this.cashOnDelievery = cashOnDelievery;
        this.paymentType = paymentType;
    }


    public String getOnline() {
        return online;
    }

    public void setOnline(String online) {
        this.online = online;
    }
    public String getCashondelievery() {
        return cashOnDelievery;
    }

    public void setCashondelievery(String cashOnDelievery) {
        this.cashOnDelievery = cashOnDelievery;
    }
    public String getPaymenttype() {
        return paymentType;
    }

    public void setPaymenttype(String paymentType) {
        this.paymentType = paymentType;
    }

    public Cart getCart() {
        return cart;
    }

    public void setCart(Cart cart) {
        this.cart = cart;
    }

}