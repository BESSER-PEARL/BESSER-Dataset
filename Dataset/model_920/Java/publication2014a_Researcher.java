





import java.util.List;
import java.util.ArrayList;

public class publication2014a_Researcher  {

    private String position;
    private String forName;
    private String name;





    private publication2014a_PublicationPhase publication2014a_publicationphase;




    private List<publication2014a_PublicationPhase> publication2014a_publicationphases;




    private publication2014a_PublicationStructure publication2014a_publicationstructure;




    private publication2014a_Paper publication2014a_paper;




    private List<publication2014a_Paper> publication2014a_papers;


    public publication2014a_Researcher(
        String position,        String forName,        String name    ) {
        this.position = position;
        this.forName = forName;
        this.name = name;
        this.publication2014a_publicationphases = new ArrayList<>();
        this.publication2014a_papers = new ArrayList<>();
    }

    public publication2014a_Researcher(
        String position,        String forName,        String name        ArrayList<publication2014a_PublicationPhase> publication2014a_publicationphases,        ArrayList<publication2014a_Paper> publication2014a_papers    ) {
        this.position = position;
        this.forName = forName;
        this.name = name;
        this.publication2014a_publicationphases = publication2014a_publicationphases;
        this.publication2014a_papers = publication2014a_papers;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public publication2014a_PublicationPhase getPublication2014a_publicationphase() {
        return publication2014a_publicationphase;
    }

    public void setPublication2014a_publicationphase(publication2014a_PublicationPhase publication2014a_publicationphase) {
        this.publication2014a_publicationphase = publication2014a_publicationphase;
    }
    public List<publication2014a_PublicationPhase> getPublication2014a_publicationphases() {
        return publication2014a_publicationphases;
    }

    public void addPublication2014a_publicationphase(Publication2014a_publicationphase publication2014a_publicationphase) {
        this.publication2014a_publicationphases.add(publication2014a_publicationphase);
    }
    public publication2014a_PublicationStructure getPublication2014a_publicationstructure() {
        return publication2014a_publicationstructure;
    }

    public void setPublication2014a_publicationstructure(publication2014a_PublicationStructure publication2014a_publicationstructure) {
        this.publication2014a_publicationstructure = publication2014a_publicationstructure;
    }
    public publication2014a_Paper getPublication2014a_paper() {
        return publication2014a_paper;
    }

    public void setPublication2014a_paper(publication2014a_Paper publication2014a_paper) {
        this.publication2014a_paper = publication2014a_paper;
    }
    public List<publication2014a_Paper> getPublication2014a_papers() {
        return publication2014a_papers;
    }

    public void addPublication2014a_paper(Publication2014a_paper publication2014a_paper) {
        this.publication2014a_papers.add(publication2014a_paper);
    }

}