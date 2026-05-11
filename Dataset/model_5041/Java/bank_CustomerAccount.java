





import java.util.List;
import java.util.ArrayList;

public class bank_CustomerAccount extends Account {






    private bank_Product bank_product;




    private List<bank_Customer> bank_customers;




    private bank_Customer bank_customer;


    public bank_CustomerAccount(
    ) {
        super(
        );
        this.bank_customers = new ArrayList<>();
    }

    public bank_CustomerAccount(
        ArrayList<bank_Customer> bank_customers    ) {
        this.bank_customers = bank_customers;
    }


    public bank_Product getBank_product() {
        return bank_product;
    }

    public void setBank_product(bank_Product bank_product) {
        this.bank_product = bank_product;
    }
    public List<bank_Customer> getBank_customers() {
        return bank_customers;
    }

    public void addBank_customer(Bank_customer bank_customer) {
        this.bank_customers.add(bank_customer);
    }
    public bank_Customer getBank_customer() {
        return bank_customer;
    }

    public void setBank_customer(bank_Customer bank_customer) {
        this.bank_customer = bank_customer;
    }

}