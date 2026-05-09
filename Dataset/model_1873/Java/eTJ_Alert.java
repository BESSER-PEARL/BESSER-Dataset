





import java.util.List;
import java.util.ArrayList;

public class eTJ_Alert  {

    private String level;





    private eTJ_JournalEntry etj_journalentry;


    public eTJ_Alert(
        String level    ) {
        this.level = level;
    }


    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }

    public eTJ_JournalEntry getEtj_journalentry() {
        return etj_journalentry;
    }

    public void setEtj_journalentry(eTJ_JournalEntry etj_journalentry) {
        this.etj_journalentry = etj_journalentry;
    }

}