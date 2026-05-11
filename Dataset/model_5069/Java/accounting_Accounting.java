





import java.util.List;
import java.util.ArrayList;

public class accounting_Accounting  {

    private String name;





    private List<accounting_AccountGroup> accounting_accountgroups;


    public accounting_Accounting(
        String name    ) {
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

}