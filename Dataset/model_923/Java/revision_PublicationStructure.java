





import java.util.List;
import java.util.ArrayList;

public class revision_PublicationStructure extends Named {






    private List<revision_Researcher> revision_researchers;




    private List<revision_Paper> revision_papers;


    public revision_PublicationStructure(
    ) {
        super(
        );
        this.revision_researchers = new ArrayList<>();
        this.revision_papers = new ArrayList<>();
    }

    public revision_PublicationStructure(
        ArrayList<revision_Researcher> revision_researchers,        ArrayList<revision_Paper> revision_papers    ) {
        this.revision_researchers = revision_researchers;
        this.revision_papers = revision_papers;
    }


    public List<revision_Researcher> getRevision_researchers() {
        return revision_researchers;
    }

    public void addRevision_researcher(Revision_researcher revision_researcher) {
        this.revision_researchers.add(revision_researcher);
    }
    public List<revision_Paper> getRevision_papers() {
        return revision_papers;
    }

    public void addRevision_paper(Revision_paper revision_paper) {
        this.revision_papers.add(revision_paper);
    }

}