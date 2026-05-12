





import java.util.List;
import java.util.ArrayList;

public class revision_Researcher  {

    private String forName;
    private String name;
    private String position;





    private revision_Paper revision_paper;




    private revision_PublicationStructure revision_publicationstructure;




    private List<revision_Paper> revision_papers;


    public revision_Researcher(
        String forName,        String name,        String position    ) {
        this.forName = forName;
        this.name = name;
        this.position = position;
        this.revision_papers = new ArrayList<>();
    }

    public revision_Researcher(
        String forName,        String name,        String position        ArrayList<revision_Paper> revision_papers    ) {
        this.forName = forName;
        this.name = name;
        this.position = position;
        this.revision_papers = revision_papers;
    }

    public String getForname() {
        return forName;
    }

    public void setForname(String forName) {
        this.forName = forName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }

    public revision_Paper getRevision_paper() {
        return revision_paper;
    }

    public void setRevision_paper(revision_Paper revision_paper) {
        this.revision_paper = revision_paper;
    }
    public revision_PublicationStructure getRevision_publicationstructure() {
        return revision_publicationstructure;
    }

    public void setRevision_publicationstructure(revision_PublicationStructure revision_publicationstructure) {
        this.revision_publicationstructure = revision_publicationstructure;
    }
    public List<revision_Paper> getRevision_papers() {
        return revision_papers;
    }

    public void addRevision_paper(Revision_paper revision_paper) {
        this.revision_papers.add(revision_paper);
    }

}