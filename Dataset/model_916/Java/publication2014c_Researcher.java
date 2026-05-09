





import java.util.List;
import java.util.ArrayList;

public class publication2014c_Researcher  {

    private String forName;
    private String name;
    private String position;





    private publication2014c_PublicationStructure publication2014c_publicationstructure;




    private List<publication2014c_Review> publication2014c_reviews;




    private List<publication2014c_Write> publication2014c_writes;




    private List<publication2014c_PublicationPhase> publication2014c_publicationphases;




    private List<publication2014c_Paper> publication2014c_papers;




    private publication2014c_PublicationPhase publication2014c_publicationphase;




    private publication2014c_Paper publication2014c_paper;


    public publication2014c_Researcher(
        String forName,        String name,        String position    ) {
        this.forName = forName;
        this.name = name;
        this.position = position;
        this.publication2014c_reviews = new ArrayList<>();
        this.publication2014c_writes = new ArrayList<>();
        this.publication2014c_publicationphases = new ArrayList<>();
        this.publication2014c_papers = new ArrayList<>();
    }

    public publication2014c_Researcher(
        String forName,        String name,        String position        ArrayList<publication2014c_Review> publication2014c_reviews,        ArrayList<publication2014c_Write> publication2014c_writes,        ArrayList<publication2014c_PublicationPhase> publication2014c_publicationphases,        ArrayList<publication2014c_Paper> publication2014c_papers    ) {
        this.forName = forName;
        this.name = name;
        this.position = position;
        this.publication2014c_reviews = publication2014c_reviews;
        this.publication2014c_writes = publication2014c_writes;
        this.publication2014c_publicationphases = publication2014c_publicationphases;
        this.publication2014c_papers = publication2014c_papers;
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

    public publication2014c_PublicationStructure getPublication2014c_publicationstructure() {
        return publication2014c_publicationstructure;
    }

    public void setPublication2014c_publicationstructure(publication2014c_PublicationStructure publication2014c_publicationstructure) {
        this.publication2014c_publicationstructure = publication2014c_publicationstructure;
    }
    public List<publication2014c_Review> getPublication2014c_reviews() {
        return publication2014c_reviews;
    }

    public void addPublication2014c_review(Publication2014c_review publication2014c_review) {
        this.publication2014c_reviews.add(publication2014c_review);
    }
    public List<publication2014c_Write> getPublication2014c_writes() {
        return publication2014c_writes;
    }

    public void addPublication2014c_write(Publication2014c_write publication2014c_write) {
        this.publication2014c_writes.add(publication2014c_write);
    }
    public List<publication2014c_PublicationPhase> getPublication2014c_publicationphases() {
        return publication2014c_publicationphases;
    }

    public void addPublication2014c_publicationphase(Publication2014c_publicationphase publication2014c_publicationphase) {
        this.publication2014c_publicationphases.add(publication2014c_publicationphase);
    }
    public List<publication2014c_Paper> getPublication2014c_papers() {
        return publication2014c_papers;
    }

    public void addPublication2014c_paper(Publication2014c_paper publication2014c_paper) {
        this.publication2014c_papers.add(publication2014c_paper);
    }
    public publication2014c_PublicationPhase getPublication2014c_publicationphase() {
        return publication2014c_publicationphase;
    }

    public void setPublication2014c_publicationphase(publication2014c_PublicationPhase publication2014c_publicationphase) {
        this.publication2014c_publicationphase = publication2014c_publicationphase;
    }
    public publication2014c_Paper getPublication2014c_paper() {
        return publication2014c_paper;
    }

    public void setPublication2014c_paper(publication2014c_Paper publication2014c_paper) {
        this.publication2014c_paper = publication2014c_paper;
    }

}