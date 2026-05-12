




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Account  {

    private LocalDate closed;
    private boolean isClosed;
    private LocalDate open;
    private String billingAddress;





    private List<Payment> payments;




    private Customer customer;




    private ShoppingCart shoppingcart;


    public Account(
        LocalDate closed,        boolean isClosed,        LocalDate open,        String billingAddress    ) {
        this.closed = closed;
        this.isClosed = isClosed;
        this.open = open;
        this.billingAddress = billingAddress;
        this.payments = new ArrayList<>();
    }

    public Account(
        LocalDate closed,        boolean isClosed,        LocalDate open,        String billingAddress        ArrayList<Payment> payments    ) {
        this.closed = closed;
        this.isClosed = isClosed;
        this.open = open;
        this.billingAddress = billingAddress;
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

    public List<Payment> getPayments() {
        return payments;
    }

    public void addPayment(Payment payment) {
        this.payments.add(payment);
    }
    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}