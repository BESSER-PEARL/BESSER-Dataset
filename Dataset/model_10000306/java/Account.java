




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Account  {

    private LocalDate closed;
    private boolean isClosed;
    private String billingAddress;
    private LocalDate open;





    private ShoppingCart shoppingcart;




    private List<Payment> payments;




    private Customer customer;


    public Account(
        LocalDate closed,        boolean isClosed,        String billingAddress,        LocalDate open    ) {
        this.closed = closed;
        this.isClosed = isClosed;
        this.billingAddress = billingAddress;
        this.open = open;
        this.payments = new ArrayList<>();
    }

    public Account(
        LocalDate closed,        boolean isClosed,        String billingAddress,        LocalDate open        ArrayList<Payment> payments    ) {
        this.closed = closed;
        this.isClosed = isClosed;
        this.billingAddress = billingAddress;
        this.open = open;
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
    public String getBillingaddress() {
        return billingAddress;
    }

    public void setBillingaddress(String billingAddress) {
        this.billingAddress = billingAddress;
    }
    public LocalDate getOpen() {
        return open;
    }

    public void setOpen(LocalDate open) {
        this.open = open;
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
    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}