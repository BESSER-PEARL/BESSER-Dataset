




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Account  {

    private LocalDate closed;
    private String billingAddress;
    private boolean isClosed;
    private LocalDate open;





    private Customer customer;




    private ShoppingCart shoppingcart;




    private List<Payment> payments;


    public Account(
        LocalDate closed,        String billingAddress,        boolean isClosed,        LocalDate open    ) {
        this.closed = closed;
        this.billingAddress = billingAddress;
        this.isClosed = isClosed;
        this.open = open;
        this.payments = new ArrayList<>();
    }

    public Account(
        LocalDate closed,        String billingAddress,        boolean isClosed,        LocalDate open        ArrayList<Payment> payments    ) {
        this.closed = closed;
        this.billingAddress = billingAddress;
        this.isClosed = isClosed;
        this.open = open;
        this.payments = payments;
    }

    public LocalDate getClosed() {
        return closed;
    }

    public void setClosed(LocalDate closed) {
        this.closed = closed;
    }
    public String getBillingaddress() {
        return billingAddress;
    }

    public void setBillingaddress(String billingAddress) {
        this.billingAddress = billingAddress;
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
    public List<Payment> getPayments() {
        return payments;
    }

    public void addPayment(Payment payment) {
        this.payments.add(payment);
    }

}