




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Account  {

    private boolean isClosed;
    private String billingAddress;
    private LocalDate closed;
    private LocalDate open;





    private Customer customer;




    private List<Payment> payments;




    private ShoppingCart shoppingcart;


    public Account(
        boolean isClosed,        String billingAddress,        LocalDate closed,        LocalDate open    ) {
        this.isClosed = isClosed;
        this.billingAddress = billingAddress;
        this.closed = closed;
        this.open = open;
        this.payments = new ArrayList<>();
    }

    public Account(
        boolean isClosed,        String billingAddress,        LocalDate closed,        LocalDate open        ArrayList<Payment> payments    ) {
        this.isClosed = isClosed;
        this.billingAddress = billingAddress;
        this.closed = closed;
        this.open = open;
        this.payments = payments;
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
    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}