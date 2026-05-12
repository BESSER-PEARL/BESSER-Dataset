




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ShoppingCart1  {

    private int itemCount;
    private int totalPrice;
    private boolean isClosed;
    private LocalDate closed;





    private ShoppingCart shoppingcart;




    private List<Payment> payments;


    public ShoppingCart1(
        int itemCount,        int totalPrice,        boolean isClosed,        LocalDate closed    ) {
        this.itemCount = itemCount;
        this.totalPrice = totalPrice;
        this.isClosed = isClosed;
        this.closed = closed;
        this.payments = new ArrayList<>();
    }

    public ShoppingCart1(
        int itemCount,        int totalPrice,        boolean isClosed,        LocalDate closed        ArrayList<Payment> payments    ) {
        this.itemCount = itemCount;
        this.totalPrice = totalPrice;
        this.isClosed = isClosed;
        this.closed = closed;
        this.payments = payments;
    }

    public int getItemcount() {
        return itemCount;
    }

    public void setItemcount(int itemCount) {
        this.itemCount = itemCount;
    }
    public int getTotalprice() {
        return totalPrice;
    }

    public void setTotalprice(int totalPrice) {
        this.totalPrice = totalPrice;
    }
    public boolean getIsclosed() {
        return isClosed;
    }

    public void setIsclosed(boolean isClosed) {
        this.isClosed = isClosed;
    }
    public LocalDate getClosed() {
        return closed;
    }

    public void setClosed(LocalDate closed) {
        this.closed = closed;
    }

    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }
    public List<Payment> getPayments() {
        return payments;
    }

    public void addPayment(Payment payment) {
        this.payments.add(payment);
    }

}