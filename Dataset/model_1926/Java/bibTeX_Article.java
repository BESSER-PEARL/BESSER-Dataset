





import java.util.List;
import java.util.ArrayList;

public class bibTeX_Article extends DatedEntry, TitledEntry, AuthoredEntry {

    private String journal;



    public bibTeX_Article(
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