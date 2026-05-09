





import java.util.List;
import java.util.ArrayList;

public class publication_Researcher  {

    private String name;
    private String position;
    private String forName;





    private publication_PublicationStructure publication_publicationstructure;




    private publication_Paper publication_paper;




    private publication_PublicationPhase publication_publicationphase;




    private List<publication_Paper> publication_papers;




    private List<publication_PublicationPhase> publication_publicationphases;


    public publication_Researcher(
        String name,        String position,        String forName    ) {
        this.name = name;
        this.position = position;
        this.forName = forName;
        this.publication_papers = new ArrayList<>();
        this.publication_publicationphases = new ArrayList<>();
    }

    public publication_Researcher(
        String name,        String position,        String forName        ArrayList<publication_Paper> publication_papers,        ArrayList<publication_PublicationPhase> publication_publicationphases    ) {
        this.name = name;
        this.position = position;
        this.forName = forName;
        this.publication_papers = publication_papers;
        this.publication_publicationphases = publication_publicationphases;
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

    public publication_PublicationStructure getPublication_publicationstructure() {
        return publication_publicationstructure;
    }

    public void setPublication_publicationstructure(publication_PublicationStructure publication_publicationstructure) {
        this.publication_publicationstructure = publication_publicationstructure;
    }
    public publication_Paper getPublication_paper() {
        return publication_paper;
    }

    public void setPublication_paper(publication_Paper publication_paper) {
        this.publication_paper = publication_paper;
    }
    public publication_PublicationPhase getPublication_publicationphase() {
        return publication_publicationphase;
    }

    public void setPublication_publicationphase(publication_PublicationPhase publication_publicationphase) {
        this.publication_publicationphase = publication_publicationphase;
    }
    public List<publication_Paper> getPublication_papers() {
        return publication_papers;
    }

    public void addPublication_paper(Publication_paper publication_paper) {
        this.publication_papers.add(publication_paper);
    }
    public List<publication_PublicationPhase> getPublication_publicationphases() {
        return publication_publicationphases;
    }

    public void addPublication_publicationphase(Publication_publicationphase publication_publicationphase) {
        this.publication_publicationphases.add(publication_publicationphase);
    }

}