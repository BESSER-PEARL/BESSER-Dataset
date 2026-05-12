





import java.util.List;
import java.util.ArrayList;

public class Bank  {

    private int Account;
    private String Name;





    private List<Customer> customers;


    public Bank(
        int Account,        String Name    ) {
        this.Account = Account;
        this.Name = Name;
        this.customers = new ArrayList<>();
    }

    public Bank(
        int Account,        String Name        ArrayList<Customer> customers    ) {
        this.Account = Account;
        this.Name = Name;
        this.customers = customers;
    }

    public int getAccount() {
        return Account;
    }

    public void setAccount(int Account) {
        this.Account = Account;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<Customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }

}