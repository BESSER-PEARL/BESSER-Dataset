




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Account  {

    private boolean isClosed;
    private LocalDate open;
    private String billingAddress;
    private LocalDate closed;





    private List<Payment> payments;




    private ShoppingCart shoppingcart;




    private Customer customer;


    public Account(
        boolean isClosed,        LocalDate open,        String billingAddress,        LocalDate closed    ) {
        this.isClosed = isClosed;
        this.open = open;
        this.billingAddress = billingAddress;
        this.closed = closed;
        this.payments = new ArrayList<>();
    }

    public Account(
        boolean isClosed,        LocalDate open,        String billingAddress,        LocalDate closed        ArrayList<Payment> payments    ) {
        this.isClosed = isClosed;
        this.open = open;
        this.billingAddress = billingAddress;
        this.closed = closed;
        this.payments = payments;
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
    public LocalDate getClosed() {
        return closed;
    }

    public void setClosed(LocalDate closed) {
        this.closed = closed;
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
    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}