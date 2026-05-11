





import java.util.List;
import java.util.ArrayList;

public class accounting_Accounting extends Serializable {

    private String name;





    private List<accounting_AccountGroup> accounting_accountgroups;




    private accounting_BalanceAccount accounting_balanceaccount;


    public accounting_Accounting(
        String name    ) {
        super(
        );
        this.name = name;
        this.accounting_accountgroups = new ArrayList<>();
    }

    public accounting_Accounting(
        String name        ArrayList<accounting_AccountGroup> accounting_accountgroups    ) {
        this.name = name;
        this.accounting_accountgroups = accounting_accountgroups;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<accounting_AccountGroup> getAccounting_accountgroups() {
        return accounting_accountgroups;
    }

    public void addAccounting_accountgroup(Accounting_accountgroup accounting_accountgroup) {
        this.accounting_accountgroups.add(accounting_accountgroup);
    }
    public accounting_BalanceAccount getAccounting_balanceaccount() {
        return accounting_balanceaccount;
    }

    public void setAccounting_balanceaccount(accounting_BalanceAccount accounting_balanceaccount) {
        this.accounting_balanceaccount = accounting_balanceaccount;
    }

}