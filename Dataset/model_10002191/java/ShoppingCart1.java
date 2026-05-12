




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ShoppingCart1  {

    private LocalDate closed;
    private boolean isClosed;
    private int totalPrice;
    private int itemCount;





    private ShoppingCart shoppingcart;




    private List<Payment> payments;


    public ShoppingCart1(
        LocalDate closed,        boolean isClosed,        int totalPrice,        int itemCount    ) {
        this.closed = closed;
        this.isClosed = isClosed;
        this.totalPrice = totalPrice;
        this.itemCount = itemCount;
        this.payments = new ArrayList<>();
    }

    public ShoppingCart1(
        LocalDate closed,        boolean isClosed,        int totalPrice,        int itemCount        ArrayList<Payment> payments    ) {
        this.closed = closed;
        this.isClosed = isClosed;
        this.totalPrice = totalPrice;
        this.itemCount = itemCount;
        this.payments = payments;
    }

    public LocalDate getClosed() {
        return closed;
    }

    public void setClosed(LocalDate closed) {
        this.closed = closed;
    }
    public boolean getIsclosed() {
        return isClosed;
    }

    public void setIsclosed(boolean isClosed) {
        this.isClosed = isClosed;
    }
    public int getTotalprice() {
        return totalPrice;
    }

    public void setTotalprice(int totalPrice) {
        this.totalPrice = totalPrice;
    }
    public int getItemcount() {
        return itemCount;
    }

    public void setItemcount(int itemCount) {
        this.itemCount = itemCount;
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