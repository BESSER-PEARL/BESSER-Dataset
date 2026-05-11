





import java.util.List;
import java.util.ArrayList;

public class accounting_JournalGroup  {

    private String name;





    private accounting_JournalGroup accounting_journalgroup;




    private accounting_Accounting accounting_accounting;


    public accounting_JournalGroup(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public accounting_JournalGroup getAccounting_journalgroup() {
        return accounting_journalgroup;
    }

    public void setAccounting_journalgroup(accounting_JournalGroup accounting_journalgroup) {
        this.accounting_journalgroup = accounting_journalgroup;
    }
    public accounting_Accounting getAccounting_accounting() {
        return accounting_accounting;
    }

    public void setAccounting_accounting(accounting_Accounting accounting_accounting) {
        this.accounting_accounting = accounting_accounting;
    }

}