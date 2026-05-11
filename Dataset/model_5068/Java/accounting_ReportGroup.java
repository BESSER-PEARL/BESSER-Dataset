





import java.util.List;
import java.util.ArrayList;

public class accounting_ReportGroup  {

    private String name;





    private accounting_Report accounting_report;




    private accounting_Report accounting_report;




    private accounting_BalanceAccount accounting_balanceaccount;




    private List<accounting_BalanceAccount> accounting_balanceaccounts;




    private accounting_ReportGroup accounting_reportgroup;


    public accounting_ReportGroup(
        String name    ) {
        this.name = name;
        this.accounting_balanceaccounts = new ArrayList<>();
    }

    public accounting_ReportGroup(
        String name        ArrayList<accounting_BalanceAccount> accounting_balanceaccounts    ) {
        this.name = name;
        this.accounting_balanceaccounts = accounting_balanceaccounts;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public accounting_Report getAccounting_report() {
        return accounting_report;
    }

    public void setAccounting_report(accounting_Report accounting_report) {
        this.accounting_report = accounting_report;
    }
    public accounting_Report getAccounting_report() {
        return accounting_report;
    }

    public void setAccounting_report(accounting_Report accounting_report) {
        this.accounting_report = accounting_report;
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
    public accounting_ReportGroup getAccounting_reportgroup() {
        return accounting_reportgroup;
    }

    public void setAccounting_reportgroup(accounting_ReportGroup accounting_reportgroup) {
        this.accounting_reportgroup = accounting_reportgroup;
    }

}