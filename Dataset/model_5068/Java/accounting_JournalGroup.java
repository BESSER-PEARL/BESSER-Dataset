





import java.util.List;
import java.util.ArrayList;

public class accounting_JournalGroup  {

    private String name;





    private List<accounting_JournalGroup> accounting_journalgroups;


    public accounting_JournalGroup(
        String name    ) {
        this.name = name;
        this.accounting_journalgroups = new ArrayList<>();
    }

    public accounting_JournalGroup(
        String name        ArrayList<accounting_JournalGroup> accounting_journalgroups    ) {
        this.name = name;
        this.accounting_journalgroups = accounting_journalgroups;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<accounting_JournalGroup> getAccounting_journalgroups() {
        return accounting_journalgroups;
    }

    public void addAccounting_journalgroup(Accounting_journalgroup accounting_journalgroup) {
        this.accounting_journalgroups.add(accounting_journalgroup);
    }

}