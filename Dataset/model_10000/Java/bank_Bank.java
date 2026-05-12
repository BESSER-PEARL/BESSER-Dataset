





import java.util.List;
import java.util.ArrayList;

public class bank_Bank  {






    private List<bank_Client> bank_clients;




    private List<bank_Account> bank_accounts;


    public bank_Bank(
    ) {
        this.bank_clients = new ArrayList<>();
        this.bank_accounts = new ArrayList<>();
    }

    public bank_Bank(
        ArrayList<bank_Client> bank_clients,        ArrayList<bank_Account> bank_accounts    ) {
        this.bank_clients = bank_clients;
        this.bank_accounts = bank_accounts;
    }


    public List<bank_Client> getBank_clients() {
        return bank_clients;
    }

    public void addBank_client(Bank_client bank_client) {
        this.bank_clients.add(bank_client);
    }
    public List<bank_Account> getBank_accounts() {
        return bank_accounts;
    }

    public void addBank_account(Bank_account bank_account) {
        this.bank_accounts.add(bank_account);
    }

}