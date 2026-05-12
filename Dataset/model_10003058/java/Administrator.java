





import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private String Account;
    private String Fullname;





    private List<Customer> customers;


    public Administrator(
        String Account,        String Fullname    ) {
        this.Account = Account;
        this.Fullname = Fullname;
        this.customers = new ArrayList<>();
    }

    public Administrator(
        String Account,        String Fullname        ArrayList<Customer> customers    ) {
        this.Account = Account;
        this.Fullname = Fullname;
        this.customers = customers;
    }

    public String getAccount() {
        return Account;
    }

    public void setAccount(String Account) {
        this.Account = Account;
    }
    public String getFullname() {
        return Fullname;
    }

    public void setFullname(String Fullname) {
        this.Fullname = Fullname;
    }

    public List<Customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }

}