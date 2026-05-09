





import java.util.List;
import java.util.ArrayList;

public class publication103_Researcher  {

    private String forName;
    private String name;





    private publication103_Paper publication103_paper;




    private publication103_PublicationStructure publication103_publicationstructure;




    private List<publication103_Write> publication103_writes;




    private publication103_Position publication103_position;




    private List<publication103_Skill> publication103_skills;




    private List<publication103_Review> publication103_reviews;




    private List<publication103_Collaboration> publication103_collaborations;




    private List<publication103_Paper> publication103_papers;


    public publication103_Researcher(
        String forName,        String name    ) {
        this.forName = forName;
        this.name = name;
        this.publication103_writes = new ArrayList<>();
        this.publication103_skills = new ArrayList<>();
        this.publication103_reviews = new ArrayList<>();
        this.publication103_collaborations = new ArrayList<>();
        this.publication103_papers = new ArrayList<>();
    }

    public publication103_Researcher(
        String forName,        String name        ArrayList<publication103_Write> publication103_writes,        ArrayList<publication103_Skill> publication103_skills,        ArrayList<publication103_Review> publication103_reviews,        ArrayList<publication103_Collaboration> publication103_collaborations,        ArrayList<publication103_Paper> publication103_papers    ) {
        this.forName = forName;
        this.name = name;
        this.publication103_writes = publication103_writes;
        this.publication103_skills = publication103_skills;
        this.publication103_reviews = publication103_reviews;
        this.publication103_collaborations = publication103_collaborations;
        this.publication103_papers = publication103_papers;
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

    public publication103_Paper getPublication103_paper() {
        return publication103_paper;
    }

    public void setPublication103_paper(publication103_Paper publication103_paper) {
        this.publication103_paper = publication103_paper;
    }
    public publication103_PublicationStructure getPublication103_publicationstructure() {
        return publication103_publicationstructure;
    }

    public void setPublication103_publicationstructure(publication103_PublicationStructure publication103_publicationstructure) {
        this.publication103_publicationstructure = publication103_publicationstructure;
    }
    public List<publication103_Write> getPublication103_writes() {
        return publication103_writes;
    }

    public void addPublication103_write(Publication103_write publication103_write) {
        this.publication103_writes.add(publication103_write);
    }
    public publication103_Position getPublication103_position() {
        return publication103_position;
    }

    public void setPublication103_position(publication103_Position publication103_position) {
        this.publication103_position = publication103_position;
    }
    public List<publication103_Skill> getPublication103_skills() {
        return publication103_skills;
    }

    public void addPublication103_skill(Publication103_skill publication103_skill) {
        this.publication103_skills.add(publication103_skill);
    }
    public List<publication103_Review> getPublication103_reviews() {
        return publication103_reviews;
    }

    public void addPublication103_review(Publication103_review publication103_review) {
        this.publication103_reviews.add(publication103_review);
    }
    public List<publication103_Collaboration> getPublication103_collaborations() {
        return publication103_collaborations;
    }

    public void addPublication103_collaboration(Publication103_collaboration publication103_collaboration) {
        this.publication103_collaborations.add(publication103_collaboration);
    }
    public List<publication103_Paper> getPublication103_papers() {
        return publication103_papers;
    }

    public void addPublication103_paper(Publication103_paper publication103_paper) {
        this.publication103_papers.add(publication103_paper);
    }

}