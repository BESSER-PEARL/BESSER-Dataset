




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Account  {

    private boolean isClosed;
    private LocalDate closed;
    private LocalDate open;
    private String billingAddress;





    private ShoppingCart shoppingcart;




    private Customer customer;




    private List<Payment> payments;


    public Account(
        boolean isClosed,        LocalDate closed,        LocalDate open,        String billingAddress    ) {
        this.isClosed = isClosed;
        this.closed = closed;
        this.open = open;
        this.billingAddress = billingAddress;
        this.payments = new ArrayList<>();
    }

    public Account(
        boolean isClosed,        LocalDate closed,        LocalDate open,        String billingAddress        ArrayList<Payment> payments    ) {
        this.isClosed = isClosed;
        this.closed = closed;
        this.open = open;
        this.billingAddress = billingAddress;
        this.payments = payments;
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
    public LocalDate getOpen() {
        return open;
    }

    public void setOpen(LocalDate open) {
        this.open = open;
    }
    public String getBillingaddress() {
        return billingAddress;
    }

    public void setBillingaddress(String billingAddress) {
        this.billingAddress = billingAddress;
    }

    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }
    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public List<Payment> getPayments() {
        return payments;
    }

    public void addPayment(Payment payment) {
        this.payments.add(payment);
    }

}