





import java.util.List;
import java.util.ArrayList;

public class accounting_AccountGroup  {

    private String name;





    private List<accounting_Account> accounting_accounts;


    public accounting_AccountGroup(
        String name    ) {
        this.name = name;
        this.accounting_accounts = new ArrayList<>();
    }

    public accounting_AccountGroup(
        String name        ArrayList<accounting_Account> accounting_accounts    ) {
        this.name = name;
        this.accounting_accounts = accounting_accounts;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<accounting_Account> getAccounting_accounts() {
        return accounting_accounts;
    }

    public void addAccounting_account(Accounting_account accounting_account) {
        this.accounting_accounts.add(accounting_account);
    }

}