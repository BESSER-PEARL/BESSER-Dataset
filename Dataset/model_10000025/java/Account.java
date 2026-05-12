




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Account  {

    private String billingAddress;
    private LocalDate open;
    private LocalDate closed;





    private ShoppingCart shoppingcart;




    private List<Payment> payments;




    private Customer customer;


    public Account(
        String billingAddress,        LocalDate open,        LocalDate closed    ) {
        this.billingAddress = billingAddress;
        this.open = open;
        this.closed = closed;
        this.payments = new ArrayList<>();
    }

    public Account(
        String billingAddress,        LocalDate open,        LocalDate closed        ArrayList<Payment> payments    ) {
        this.billingAddress = billingAddress;
        this.open = open;
        this.closed = closed;
        this.payments = payments;
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