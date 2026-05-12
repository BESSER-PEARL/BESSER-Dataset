





import java.util.List;
import java.util.ArrayList;

public class Bank  {






    private List<Account> accounts;


    public Bank(
    ) {
        this.accounts = new ArrayList<>();
    }

    public Bank(
        ArrayList<Account> accounts    ) {
        this.accounts = accounts;
    }


    public List<Account> getAccounts() {
        return accounts;
    }

    public void addAccount(Account account) {
        this.accounts.add(account);
    }

}