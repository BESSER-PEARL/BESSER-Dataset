





import java.util.List;
import java.util.ArrayList;

public class Customer_Payment1  {

    private None ID;
    private boolean Auth__;
    private String PayBill__;





    private List<Customer_Customer1> customer_customer1s;


    public Customer_Payment1(
        None ID,        boolean Auth__,        String PayBill__    ) {
        this.ID = ID;
        this.Auth__ = Auth__;
        this.PayBill__ = PayBill__;
        this.customer_customer1s = new ArrayList<>();
    }

    public Customer_Payment1(
        None ID,        boolean Auth__,        String PayBill__        ArrayList<Customer_Customer1> customer_customer1s    ) {
        this.ID = ID;
        this.Auth__ = Auth__;
        this.PayBill__ = PayBill__;
        this.customer_customer1s = customer_customer1s;
    }

    public None getId() {
        return ID;
    }

    public void setId(None ID) {
        this.ID = ID;
    }
    public boolean getAuth__() {
        return Auth__;
    }

    public void setAuth__(boolean Auth__) {
        this.Auth__ = Auth__;
    }
    public String getPaybill__() {
        return PayBill__;
    }

    public void setPaybill__(String PayBill__) {
        this.PayBill__ = PayBill__;
    }

    public List<Customer_Customer1> getCustomer_customer1s() {
        return customer_customer1s;
    }

    public void addCustomer_customer1(Customer_customer1 customer_customer1) {
        this.customer_customer1s.add(customer_customer1);
    }

}