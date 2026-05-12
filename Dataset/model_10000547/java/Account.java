




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Account  {

    private LocalDate closed;
    private String billingAddress;
    private LocalDate open;
    private boolean isClosed;





    private Customer customer;




    private List<Payment> payments;




    private ShoppingCart shoppingcart;


    public Account(
        LocalDate closed,        String billingAddress,        LocalDate open,        boolean isClosed    ) {
        this.closed = closed;
        this.billingAddress = billingAddress;
        this.open = open;
        this.isClosed = isClosed;
        this.payments = new ArrayList<>();
    }

    public Account(
        LocalDate closed,        String billingAddress,        LocalDate open,        boolean isClosed        ArrayList<Payment> payments    ) {
        this.closed = closed;
        this.billingAddress = billingAddress;
        this.open = open;
        this.isClosed = isClosed;
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