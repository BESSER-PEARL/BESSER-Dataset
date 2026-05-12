





import java.util.List;
import java.util.ArrayList;

public class publication_Researcher  {

    private String name;
    private String position;
    private String forName;





    private publication_PublicationPhase publication_publicationphase;




    private List<publication_Write> publication_writes;




    private List<publication_PublicationPhase> publication_publicationphases;




    private publication_PublicationStructure publication_publicationstructure;




    private List<publication_Review> publication_reviews;




    private publication_Paper publication_paper;




    private List<publication_Paper> publication_papers;


    public publication_Researcher(
        String name,        String position,        String forName    ) {
        this.name = name;
        this.position = position;
        this.forName = forName;
        this.publication_writes = new ArrayList<>();
        this.publication_publicationphases = new ArrayList<>();
        this.publication_reviews = new ArrayList<>();
        this.publication_papers = new ArrayList<>();
    }

    public publication_Researcher(
        String name,        String position,        String forName        ArrayList<publication_Write> publication_writes,        ArrayList<publication_PublicationPhase> publication_publicationphases,        ArrayList<publication_Review> publication_reviews,        ArrayList<publication_Paper> publication_papers    ) {
        this.name = name;
        this.position = position;
        this.forName = forName;
        this.publication_writes = publication_writes;
        this.publication_publicationphases = publication_publicationphases;
        this.publication_reviews = publication_reviews;
        this.publication_papers = publication_papers;
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

    public publication_PublicationPhase getPublication_publicationphase() {
        return publication_publicationphase;
    }

    public void setPublication_publicationphase(publication_PublicationPhase publication_publicationphase) {
        this.publication_publicationphase = publication_publicationphase;
    }
    public List<publication_Write> getPublication_writes() {
        return publication_writes;
    }

    public void addPublication_write(Publication_write publication_write) {
        this.publication_writes.add(publication_write);
    }
    public List<publication_PublicationPhase> getPublication_publicationphases() {
        return publication_publicationphases;
    }

    public void addPublication_publicationphase(Publication_publicationphase publication_publicationphase) {
        this.publication_publicationphases.add(publication_publicationphase);
    }
    public publication_PublicationStructure getPublication_publicationstructure() {
        return publication_publicationstructure;
    }

    public void setPublication_publicationstructure(publication_PublicationStructure publication_publicationstructure) {
        this.publication_publicationstructure = publication_publicationstructure;
    }
    public List<publication_Review> getPublication_reviews() {
        return publication_reviews;
    }

    public void addPublication_review(Publication_review publication_review) {
        this.publication_reviews.add(publication_review);
    }
    public publication_Paper getPublication_paper() {
        return publication_paper;
    }

    public void setPublication_paper(publication_Paper publication_paper) {
        this.publication_paper = publication_paper;
    }
    public List<publication_Paper> getPublication_papers() {
        return publication_papers;
    }

    public void addPublication_paper(Publication_paper publication_paper) {
        this.publication_papers.add(publication_paper);
    }

}