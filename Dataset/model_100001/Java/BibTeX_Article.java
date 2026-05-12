





import java.util.List;
import java.util.ArrayList;

public class BibTeX_Article extends TitledEntry, DatedEntry, AuthoredEntry {

    private String journal;



    public BibTeX_Article(
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