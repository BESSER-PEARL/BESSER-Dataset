





import java.util.List;
import java.util.ArrayList;

public class publication101_Researcher  {

    private String forName;
    private String name;





    private publication101_PublicationStructure publication101_publicationstructure;




    private publication101_Position publication101_position;




    private List<publication101_Paper> publication101_papers;




    private publication101_Paper publication101_paper;


    public publication101_Researcher(
        String forName,        String name    ) {
        this.forName = forName;
        this.name = name;
        this.publication101_papers = new ArrayList<>();
    }

    public publication101_Researcher(
        String forName,        String name        ArrayList<publication101_Paper> publication101_papers    ) {
        this.forName = forName;
        this.name = name;
        this.publication101_papers = publication101_papers;
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

    public publication101_PublicationStructure getPublication101_publicationstructure() {
        return publication101_publicationstructure;
    }

    public void setPublication101_publicationstructure(publication101_PublicationStructure publication101_publicationstructure) {
        this.publication101_publicationstructure = publication101_publicationstructure;
    }
    public publication101_Position getPublication101_position() {
        return publication101_position;
    }

    public void setPublication101_position(publication101_Position publication101_position) {
        this.publication101_position = publication101_position;
    }
    public List<publication101_Paper> getPublication101_papers() {
        return publication101_papers;
    }

    public void addPublication101_paper(Publication101_paper publication101_paper) {
        this.publication101_papers.add(publication101_paper);
    }
    public publication101_Paper getPublication101_paper() {
        return publication101_paper;
    }

    public void setPublication101_paper(publication101_Paper publication101_paper) {
        this.publication101_paper = publication101_paper;
    }

}