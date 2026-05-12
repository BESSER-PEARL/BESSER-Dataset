




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Account  {

    private String billingAddress;
    private LocalDate closed;
    private LocalDate open;
    private boolean isClosed;





    private ShoppingCart shoppingcart;




    private List<Payment> payments;


    public Account(
        String billingAddress,        LocalDate closed,        LocalDate open,        boolean isClosed    ) {
        this.billingAddress = billingAddress;
        this.closed = closed;
        this.open = open;
        this.isClosed = isClosed;
        this.payments = new ArrayList<>();
    }

    public Account(
        String billingAddress,        LocalDate closed,        LocalDate open,        boolean isClosed        ArrayList<Payment> payments    ) {
        this.billingAddress = billingAddress;
        this.closed = closed;
        this.open = open;
        this.isClosed = isClosed;
        this.payments = payments;
    }

    public String getBillingaddress() {
        return billingAddress;
    }

    public void setBillingaddress(String billingAddress) {
        this.billingAddress = billingAddress;
    }
    public LocalDate getClosed() {
        return closed;
    }

    public void setClosed(LocalDate closed) {
        this.closed = closed;
    }
    public LocalDate getOpen() {
        return open;
    }

    public void setOpen(LocalDate open) {
        this.open = open;
    }
    public boolean getIsclosed() {
        return isClosed;
    }

    public void setIsclosed(boolean isClosed) {
        this.isClosed = isClosed;
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