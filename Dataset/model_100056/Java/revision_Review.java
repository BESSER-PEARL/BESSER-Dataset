





import java.util.List;
import java.util.ArrayList;

public class revision_Review extends Labelled {






    private revision_Researcher revision_researcher;




    private revision_ReviewNote revision_reviewnote;


    public revision_Review(
    ) {
        super(
        );
    }



    public revision_Researcher getRevision_researcher() {
        return revision_researcher;
    }

    public void setRevision_researcher(revision_Researcher revision_researcher) {
        this.revision_researcher = revision_researcher;
    }
    public revision_ReviewNote getRevision_reviewnote() {
        return revision_reviewnote;
    }

    public void setRevision_reviewnote(revision_ReviewNote revision_reviewnote) {
        this.revision_reviewnote = revision_reviewnote;
    }

}