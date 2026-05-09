





import java.util.List;
import java.util.ArrayList;

public class publication2014b_Researcher  {

    private String name;
    private String position;
    private String forName;





    private publication2014b_Paper publication2014b_paper;




    private publication2014b_PublicationStructure publication2014b_publicationstructure;




    private List<publication2014b_Paper> publication2014b_papers;


    public publication2014b_Researcher(
        String name,        String position,        String forName    ) {
        this.name = name;
        this.position = position;
        this.forName = forName;
        this.publication2014b_papers = new ArrayList<>();
    }

    public publication2014b_Researcher(
        String name,        String position,        String forName        ArrayList<publication2014b_Paper> publication2014b_papers    ) {
        this.name = name;
        this.position = position;
        this.forName = forName;
        this.publication2014b_papers = publication2014b_papers;
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
    public String getForname() {
        return forName;
    }

    public void setForname(String forName) {
        this.forName = forName;
    }

    public publication2014b_Paper getPublication2014b_paper() {
        return publication2014b_paper;
    }

    public void setPublication2014b_paper(publication2014b_Paper publication2014b_paper) {
        this.publication2014b_paper = publication2014b_paper;
    }
    public publication2014b_PublicationStructure getPublication2014b_publicationstructure() {
        return publication2014b_publicationstructure;
    }

    public void setPublication2014b_publicationstructure(publication2014b_PublicationStructure publication2014b_publicationstructure) {
        this.publication2014b_publicationstructure = publication2014b_publicationstructure;
    }
    public List<publication2014b_Paper> getPublication2014b_papers() {
        return publication2014b_papers;
    }

    public void addPublication2014b_paper(Publication2014b_paper publication2014b_paper) {
        this.publication2014b_papers.add(publication2014b_paper);
    }

}