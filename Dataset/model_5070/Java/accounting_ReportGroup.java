





import java.util.List;
import java.util.ArrayList;

public class accounting_ReportGroup  {

    private String name;





    private List<accounting_ReportGroup> accounting_reportgroups;




    private accounting_BalanceAccount accounting_balanceaccount;




    private List<accounting_BalanceAccount> accounting_balanceaccounts;


    public accounting_ReportGroup(
        String name    ) {
        this.name = name;
        this.accounting_reportgroups = new ArrayList<>();
        this.accounting_balanceaccounts = new ArrayList<>();
    }

    public accounting_ReportGroup(
        String name        ArrayList<accounting_ReportGroup> accounting_reportgroups,        ArrayList<accounting_BalanceAccount> accounting_balanceaccounts    ) {
        this.name = name;
        this.accounting_reportgroups = accounting_reportgroups;
        this.accounting_balanceaccounts = accounting_balanceaccounts;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<accounting_ReportGroup> getAccounting_reportgroups() {
        return accounting_reportgroups;
    }

    public void addAccounting_reportgroup(Accounting_reportgroup accounting_reportgroup) {
        this.accounting_reportgroups.add(accounting_reportgroup);
    }
    public accounting_BalanceAccount getAccounting_balanceaccount() {
        return accounting_balanceaccount;
    }

    public void setAccounting_balanceaccount(accounting_BalanceAccount accounting_balanceaccount) {
        this.accounting_balanceaccount = accounting_balanceaccount;
    }
    public List<accounting_BalanceAccount> getAccounting_balanceaccounts() {
        return accounting_balanceaccounts;
    }

    public void addAccounting_balanceaccount(Accounting_balanceaccount accounting_balanceaccount) {
        this.accounting_balanceaccounts.add(accounting_balanceaccount);
    }

}