




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Account  {

    private boolean isClosed;
    private String billingAddress;
    private LocalDate open;
    private LocalDate closed;





    private Customer customer;




    private List<Payment> payments;




    private ShoppinCart shoppincart;


    public Account(
        boolean isClosed,        String billingAddress,        LocalDate open,        LocalDate closed    ) {
        this.isClosed = isClosed;
        this.billingAddress = billingAddress;
        this.open = open;
        this.closed = closed;
        this.payments = new ArrayList<>();
    }

    public Account(
        boolean isClosed,        String billingAddress,        LocalDate open,        LocalDate closed        ArrayList<Payment> payments    ) {
        this.isClosed = isClosed;
        this.billingAddress = billingAddress;
        this.open = open;
        this.closed = closed;
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
    public ShoppinCart getShoppincart() {
        return shoppincart;
    }

    public void setShoppincart(ShoppinCart shoppincart) {
        this.shoppincart = shoppincart;
    }

}