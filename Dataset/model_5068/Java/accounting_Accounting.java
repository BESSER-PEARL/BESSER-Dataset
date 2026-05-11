





import java.util.List;
import java.util.ArrayList;

public class accounting_Accounting extends Serializable {

    private String name;





    private accounting_Report accounting_report;




    private accounting_BalanceAccount accounting_balanceaccount;




    private List<accounting_AccountGroup> accounting_accountgroups;




    private List<accounting_JournalGroup> accounting_journalgroups;


    public accounting_Accounting(
        String name    ) {
        super(
        );
        this.name = name;
        this.accounting_accountgroups = new ArrayList<>();
        this.accounting_journalgroups = new ArrayList<>();
    }

    public accounting_Accounting(
        String name        ArrayList<accounting_AccountGroup> accounting_accountgroups,        ArrayList<accounting_JournalGroup> accounting_journalgroups    ) {
        this.name = name;
        this.accounting_accountgroups = accounting_accountgroups;
        this.accounting_journalgroups = accounting_journalgroups;
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
    public accounting_BalanceAccount getAccounting_balanceaccount() {
        return accounting_balanceaccount;
    }

    public void setAccounting_balanceaccount(accounting_BalanceAccount accounting_balanceaccount) {
        this.accounting_balanceaccount = accounting_balanceaccount;
    }
    public List<accounting_AccountGroup> getAccounting_accountgroups() {
        return accounting_accountgroups;
    }

    public void addAccounting_accountgroup(Accounting_accountgroup accounting_accountgroup) {
        this.accounting_accountgroups.add(accounting_accountgroup);
    }
    public List<accounting_JournalGroup> getAccounting_journalgroups() {
        return accounting_journalgroups;
    }

    public void addAccounting_journalgroup(Accounting_journalgroup accounting_journalgroup) {
        this.accounting_journalgroups.add(accounting_journalgroup);
    }

}