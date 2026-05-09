





import java.util.List;
import java.util.ArrayList;

public class publication2014_Researcher  {

    private String forName;
    private String name;
    private String position;





    private publication2014_PublicationStructure publication2014_publicationstructure;




    private publication2014_Paper publication2014_paper;




    private publication2014_PublicationPhase publication2014_publicationphase;




    private List<publication2014_PublicationPhase> publication2014_publicationphases;




    private List<publication2014_Paper> publication2014_papers;


    public publication2014_Researcher(
        String forName,        String name,        String position    ) {
        this.forName = forName;
        this.name = name;
        this.position = position;
        this.publication2014_publicationphases = new ArrayList<>();
        this.publication2014_papers = new ArrayList<>();
    }

    public publication2014_Researcher(
        String forName,        String name,        String position        ArrayList<publication2014_PublicationPhase> publication2014_publicationphases,        ArrayList<publication2014_Paper> publication2014_papers    ) {
        this.forName = forName;
        this.name = name;
        this.position = position;
        this.publication2014_publicationphases = publication2014_publicationphases;
        this.publication2014_papers = publication2014_papers;
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

    public publication2014_PublicationStructure getPublication2014_publicationstructure() {
        return publication2014_publicationstructure;
    }

    public void setPublication2014_publicationstructure(publication2014_PublicationStructure publication2014_publicationstructure) {
        this.publication2014_publicationstructure = publication2014_publicationstructure;
    }
    public publication2014_Paper getPublication2014_paper() {
        return publication2014_paper;
    }

    public void setPublication2014_paper(publication2014_Paper publication2014_paper) {
        this.publication2014_paper = publication2014_paper;
    }
    public publication2014_PublicationPhase getPublication2014_publicationphase() {
        return publication2014_publicationphase;
    }

    public void setPublication2014_publicationphase(publication2014_PublicationPhase publication2014_publicationphase) {
        this.publication2014_publicationphase = publication2014_publicationphase;
    }
    public List<publication2014_PublicationPhase> getPublication2014_publicationphases() {
        return publication2014_publicationphases;
    }

    public void addPublication2014_publicationphase(Publication2014_publicationphase publication2014_publicationphase) {
        this.publication2014_publicationphases.add(publication2014_publicationphase);
    }
    public List<publication2014_Paper> getPublication2014_papers() {
        return publication2014_papers;
    }

    public void addPublication2014_paper(Publication2014_paper publication2014_paper) {
        this.publication2014_papers.add(publication2014_paper);
    }

}