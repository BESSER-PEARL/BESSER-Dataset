





import java.util.List;
import java.util.ArrayList;

public class BibTeX_Article extends AuthoredEntry, TitledEntry, DatedEntry {

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