




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Account  {

    private LocalDate open;
    private String billingAddress;
    private boolean isClosed;
    private LocalDate closed;





    private ShoppingCart shoppingcart;




    private List<Payment> payments;




    private Customer customer;


    public Account(
        LocalDate open,        String billingAddress,        boolean isClosed,        LocalDate closed    ) {
        this.open = open;
        this.billingAddress = billingAddress;
        this.isClosed = isClosed;
        this.closed = closed;
        this.payments = new ArrayList<>();
    }

    public Account(
        LocalDate open,        String billingAddress,        boolean isClosed,        LocalDate closed        ArrayList<Payment> payments    ) {
        this.open = open;
        this.billingAddress = billingAddress;
        this.isClosed = isClosed;
        this.closed = closed;
        this.payments = payments;
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
    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}