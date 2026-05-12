





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private int ID;
    private None Customer;
    private String Details;
    private int Amount;





    private Customer1 customer1;


    public Payment(
        int ID,        None Customer,        String Details,        int Amount    ) {
        this.ID = ID;
        this.Customer = Customer;
        this.Details = Details;
        this.Amount = Amount;
    }


    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public None getCustomer() {
        return Customer;
    }

    public void setCustomer(None Customer) {
        this.Customer = Customer;
    }
    public String getDetails() {
        return Details;
    }

    public void setDetails(String Details) {
        this.Details = Details;
    }
    public int getAmount() {
        return Amount;
    }

    public void setAmount(int Amount) {
        this.Amount = Amount;
    }

    public Customer1 getCustomer1() {
        return customer1;
    }

    public void setCustomer1(Customer1 customer1) {
        this.customer1 = customer1;
    }

}