





import java.util.List;
import java.util.ArrayList;

public class BankingSystem_Financial_Representative extends Employee {






    private BankingSystem_Customer bankingsystem_customer;




    private List<BankingSystem_Customer> bankingsystem_customers;


    public BankingSystem_Financial_Representative(
    ) {
        super(
        );
        this.bankingsystem_customers = new ArrayList<>();
    }

    public BankingSystem_Financial_Representative(
        ArrayList<BankingSystem_Customer> bankingsystem_customers    ) {
        this.bankingsystem_customers = bankingsystem_customers;
    }


    public BankingSystem_Customer getBankingsystem_customer() {
        return bankingsystem_customer;
    }

    public void setBankingsystem_customer(BankingSystem_Customer bankingsystem_customer) {
        this.bankingsystem_customer = bankingsystem_customer;
    }
    public List<BankingSystem_Customer> getBankingsystem_customers() {
        return bankingsystem_customers;
    }

    public void addBankingsystem_customer(Bankingsystem_customer bankingsystem_customer) {
        this.bankingsystem_customers.add(bankingsystem_customer);
    }

}