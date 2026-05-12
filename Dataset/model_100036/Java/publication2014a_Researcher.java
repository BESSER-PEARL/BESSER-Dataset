





import java.util.List;
import java.util.ArrayList;

public class publication2014a_Researcher  {

    private String forName;
    private String position;
    private String name;





    private publication2014a_PublicationStructure publication2014a_publicationstructure;




    private List<publication2014a_Write> publication2014a_writes;




    private publication2014a_Paper publication2014a_paper;




    private publication2014a_PublicationPhase publication2014a_publicationphase;




    private List<publication2014a_Review> publication2014a_reviews;




    private List<publication2014a_Paper> publication2014a_papers;




    private List<publication2014a_PublicationPhase> publication2014a_publicationphases;


    public publication2014a_Researcher(
        String forName,        String position,        String name    ) {
        this.forName = forName;
        this.position = position;
        this.name = name;
        this.publication2014a_writes = new ArrayList<>();
        this.publication2014a_reviews = new ArrayList<>();
        this.publication2014a_papers = new ArrayList<>();
        this.publication2014a_publicationphases = new ArrayList<>();
    }

    public publication2014a_Researcher(
        String forName,        String position,        String name        ArrayList<publication2014a_Write> publication2014a_writes,        ArrayList<publication2014a_Review> publication2014a_reviews,        ArrayList<publication2014a_Paper> publication2014a_papers,        ArrayList<publication2014a_PublicationPhase> publication2014a_publicationphases    ) {
        this.forName = forName;
        this.position = position;
        this.name = name;
        this.publication2014a_writes = publication2014a_writes;
        this.publication2014a_reviews = publication2014a_reviews;
        this.publication2014a_papers = publication2014a_papers;
        this.publication2014a_publicationphases = publication2014a_publicationphases;
    }

    public String getForname() {
        return forName;
    }

    public void setForname(String forName) {
        this.forName = forName;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public publication2014a_PublicationStructure getPublication2014a_publicationstructure() {
        return publication2014a_publicationstructure;
    }

    public void setPublication2014a_publicationstructure(publication2014a_PublicationStructure publication2014a_publicationstructure) {
        this.publication2014a_publicationstructure = publication2014a_publicationstructure;
    }
    public List<publication2014a_Write> getPublication2014a_writes() {
        return publication2014a_writes;
    }

    public void addPublication2014a_write(Publication2014a_write publication2014a_write) {
        this.publication2014a_writes.add(publication2014a_write);
    }
    public publication2014a_Paper getPublication2014a_paper() {
        return publication2014a_paper;
    }

    public void setPublication2014a_paper(publication2014a_Paper publication2014a_paper) {
        this.publication2014a_paper = publication2014a_paper;
    }
    public publication2014a_PublicationPhase getPublication2014a_publicationphase() {
        return publication2014a_publicationphase;
    }

    public void setPublication2014a_publicationphase(publication2014a_PublicationPhase publication2014a_publicationphase) {
        this.publication2014a_publicationphase = publication2014a_publicationphase;
    }
    public List<publication2014a_Review> getPublication2014a_reviews() {
        return publication2014a_reviews;
    }

    public void addPublication2014a_review(Publication2014a_review publication2014a_review) {
        this.publication2014a_reviews.add(publication2014a_review);
    }
    public List<publication2014a_Paper> getPublication2014a_papers() {
        return publication2014a_papers;
    }

    public void addPublication2014a_paper(Publication2014a_paper publication2014a_paper) {
        this.publication2014a_papers.add(publication2014a_paper);
    }
    public List<publication2014a_PublicationPhase> getPublication2014a_publicationphases() {
        return publication2014a_publicationphases;
    }

    public void addPublication2014a_publicationphase(Publication2014a_publicationphase publication2014a_publicationphase) {
        this.publication2014a_publicationphases.add(publication2014a_publicationphase);
    }

}