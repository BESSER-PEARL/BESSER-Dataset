




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Account  {

    private String billingAddress;
    private boolean isClosed;
    private LocalDate open;
    private LocalDate closed;





    private Customer customer;




    private ShoppinCart shoppincart;




    private List<Payment> payments;


    public Account(
        String billingAddress,        boolean isClosed,        LocalDate open,        LocalDate closed    ) {
        this.billingAddress = billingAddress;
        this.isClosed = isClosed;
        this.open = open;
        this.closed = closed;
        this.payments = new ArrayList<>();
    }

    public Account(
        String billingAddress,        boolean isClosed,        LocalDate open,        LocalDate closed        ArrayList<Payment> payments    ) {
        this.billingAddress = billingAddress;
        this.isClosed = isClosed;
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
    public ShoppinCart getShoppincart() {
        return shoppincart;
    }

    public void setShoppincart(ShoppinCart shoppincart) {
        this.shoppincart = shoppincart;
    }
    public List<Payment> getPayments() {
        return payments;
    }

    public void addPayment(Payment payment) {
        this.payments.add(payment);
    }

}