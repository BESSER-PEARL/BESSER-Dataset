





import java.util.List;
import java.util.ArrayList;

public class revision_Paper extends Named {






    private revision_Researcher revision_researcher;




    private List<revision_Researcher> revision_researchers;


    public revision_Paper(
    ) {
        super(
        );
        this.revision_researchers = new ArrayList<>();
    }

    public revision_Paper(
        ArrayList<revision_Researcher> revision_researchers    ) {
        this.revision_researchers = revision_researchers;
    }


    public revision_Researcher getRevision_researcher() {
        return revision_researcher;
    }

    public void setRevision_researcher(revision_Researcher revision_researcher) {
        this.revision_researcher = revision_researcher;
    }
    public List<revision_Researcher> getRevision_researchers() {
        return revision_researchers;
    }

    public void addRevision_researcher(Revision_researcher revision_researcher) {
        this.revision_researchers.add(revision_researcher);
    }

}