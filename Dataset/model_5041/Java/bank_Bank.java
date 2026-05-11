





import java.util.List;
import java.util.ArrayList;

public class bank_Bank extends Party {






    private List<bank_Customer> bank_customers;




    private List<bank_Banker> bank_bankers;




    private List<bank_Account> bank_accounts;




    private List<bank_Merchant> bank_merchants;




    private List<bank_Product> bank_products;


    public bank_Bank(
    ) {
        super(
        );
        this.bank_customers = new ArrayList<>();
        this.bank_bankers = new ArrayList<>();
        this.bank_accounts = new ArrayList<>();
        this.bank_merchants = new ArrayList<>();
        this.bank_products = new ArrayList<>();
    }

    public bank_Bank(
        ArrayList<bank_Customer> bank_customers,        ArrayList<bank_Banker> bank_bankers,        ArrayList<bank_Account> bank_accounts,        ArrayList<bank_Merchant> bank_merchants,        ArrayList<bank_Product> bank_products    ) {
        this.bank_customers = bank_customers;
        this.bank_bankers = bank_bankers;
        this.bank_accounts = bank_accounts;
        this.bank_merchants = bank_merchants;
        this.bank_products = bank_products;
    }


    public List<bank_Customer> getBank_customers() {
        return bank_customers;
    }

    public void addBank_customer(Bank_customer bank_customer) {
        this.bank_customers.add(bank_customer);
    }
    public List<bank_Banker> getBank_bankers() {
        return bank_bankers;
    }

    public void addBank_banker(Bank_banker bank_banker) {
        this.bank_bankers.add(bank_banker);
    }
    public List<bank_Account> getBank_accounts() {
        return bank_accounts;
    }

    public void addBank_account(Bank_account bank_account) {
        this.bank_accounts.add(bank_account);
    }
    public List<bank_Merchant> getBank_merchants() {
        return bank_merchants;
    }

    public void addBank_merchant(Bank_merchant bank_merchant) {
        this.bank_merchants.add(bank_merchant);
    }
    public List<bank_Product> getBank_products() {
        return bank_products;
    }

    public void addBank_product(Bank_product bank_product) {
        this.bank_products.add(bank_product);
    }

}