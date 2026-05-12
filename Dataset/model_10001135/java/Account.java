




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Account  {

    private LocalDate openDate;
    private int id;
    private String billingAddress;





    private List<Payment> payments;




    private ShoppingCart shoppingcart;




    private Customer customer;


    public Account(
        LocalDate openDate,        int id,        String billingAddress    ) {
        this.openDate = openDate;
        this.id = id;
        this.billingAddress = billingAddress;
        this.payments = new ArrayList<>();
    }

    public Account(
        LocalDate openDate,        int id,        String billingAddress        ArrayList<Payment> payments    ) {
        this.openDate = openDate;
        this.id = id;
        this.billingAddress = billingAddress;
        this.payments = payments;
    }

    public LocalDate getOpendate() {
        return openDate;
    }

    public void setOpendate(LocalDate openDate) {
        this.openDate = openDate;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getBillingaddress() {
        return billingAddress;
    }

    public void setBillingaddress(String billingAddress) {
        this.billingAddress = billingAddress;
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