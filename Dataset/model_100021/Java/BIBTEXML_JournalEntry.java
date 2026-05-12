





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_JournalEntry extends Entry {

    private String journal;



    public BIBTEXML_JournalEntry(
        String journal    ) {
        super(
        );
        this.journal = journal;
    }


    public String getJournal() {
        return journal;
    }

    public void setJournal(String journal) {
        this.journal = journal;
    }


}