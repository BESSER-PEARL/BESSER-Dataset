





import java.util.List;
import java.util.ArrayList;

public class Account  {

    private String openDate;
    private String MAX_HOLDERS;
    private String accId;
    private String accNumber;
    private String balance;





    private Bank bank;




    private List<Customer> customers;


    public Account(
        String openDate,        String MAX_HOLDERS,        String accId,        String accNumber,        String balance    ) {
        this.openDate = openDate;
        this.MAX_HOLDERS = MAX_HOLDERS;
        this.accId = accId;
        this.accNumber = accNumber;
        this.balance = balance;
        this.customers = new ArrayList<>();
    }

    public Account(
        String openDate,        String MAX_HOLDERS,        String accId,        String accNumber,        String balance        ArrayList<Customer> customers    ) {
        this.openDate = openDate;
        this.MAX_HOLDERS = MAX_HOLDERS;
        this.accId = accId;
        this.accNumber = accNumber;
        this.balance = balance;
        this.customers = customers;
    }

    public String getOpendate() {
        return openDate;
    }

    public void setOpendate(String openDate) {
        this.openDate = openDate;
    }
    public String getMax_holders() {
        return MAX_HOLDERS;
    }

    public void setMax_holders(String MAX_HOLDERS) {
        this.MAX_HOLDERS = MAX_HOLDERS;
    }
    public String getAccid() {
        return accId;
    }

    public void setAccid(String accId) {
        this.accId = accId;
    }
    public String getAccnumber() {
        return accNumber;
    }

    public void setAccnumber(String accNumber) {
        this.accNumber = accNumber;
    }
    public String getBalance() {
        return balance;
    }

    public void setBalance(String balance) {
        this.balance = balance;
    }

    public Bank getBank() {
        return bank;
    }

    public void setBank(Bank bank) {
        this.bank = bank;
    }
    public List<Customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }

}