





import java.util.List;
import java.util.ArrayList;

public class jointPackage_SrcArticle extends SrcDatedEntry, SrcAuthoredEntry, SrcTitledEntry {

    private String journal;



    public jointPackage_SrcArticle(
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