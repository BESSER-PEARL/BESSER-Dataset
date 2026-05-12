





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String name;
    private String taxId;





    private List<Account> accounts;




    private Bank bank;


    public Customer(
        String name,        String taxId    ) {
        this.name = name;
        this.taxId = taxId;
        this.accounts = new ArrayList<>();
    }

    public Customer(
        String name,        String taxId        ArrayList<Account> accounts    ) {
        this.name = name;
        this.taxId = taxId;
        this.accounts = accounts;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTaxid() {
        return taxId;
    }

    public void setTaxid(String taxId) {
        this.taxId = taxId;
    }

    public List<Account> getAccounts() {
        return accounts;
    }

    public void addAccount(Account account) {
        this.accounts.add(account);
    }
    public Bank getBank() {
        return bank;
    }

    public void setBank(Bank bank) {
        this.bank = bank;
    }

}