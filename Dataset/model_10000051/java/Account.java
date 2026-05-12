




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Account  {

    private LocalDate open;
    private String billingAddress;
    private LocalDate closed;
    private boolean isClosed;





    private List<Payment> payments;




    private Customer customer;




    private ShoppingCart shoppingcart;


    public Account(
        LocalDate open,        String billingAddress,        LocalDate closed,        boolean isClosed    ) {
        this.open = open;
        this.billingAddress = billingAddress;
        this.closed = closed;
        this.isClosed = isClosed;
        this.payments = new ArrayList<>();
    }

    public Account(
        LocalDate open,        String billingAddress,        LocalDate closed,        boolean isClosed        ArrayList<Payment> payments    ) {
        this.open = open;
        this.billingAddress = billingAddress;
        this.closed = closed;
        this.isClosed = isClosed;
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