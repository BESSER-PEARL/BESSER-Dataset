





import java.util.List;
import java.util.ArrayList;

public class bank_Client  {

    private String name;
    private int capacity;





    private bank_Account bank_account;




    private bank_Client bank_client;




    private List<bank_Account> bank_accounts;


    public bank_Client(
        String name,        int capacity    ) {
        this.name = name;
        this.capacity = capacity;
        this.bank_accounts = new ArrayList<>();
    }

    public bank_Client(
        String name,        int capacity        ArrayList<bank_Account> bank_accounts    ) {
        this.name = name;
        this.capacity = capacity;
        this.bank_accounts = bank_accounts;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }

    public bank_Account getBank_account() {
        return bank_account;
    }

    public void setBank_account(bank_Account bank_account) {
        this.bank_account = bank_account;
    }
    public bank_Client getBank_client() {
        return bank_client;
    }

    public void setBank_client(bank_Client bank_client) {
        this.bank_client = bank_client;
    }
    public List<bank_Account> getBank_accounts() {
        return bank_accounts;
    }

    public void addBank_account(Bank_account bank_account) {
        this.bank_accounts.add(bank_account);
    }

}