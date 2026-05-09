





import java.util.List;
import java.util.ArrayList;

public class publication101_Researcher  {

    private String name;
    private String forName;





    private List<publication101_Collaboration> publication101_collaborations;




    private publication101_PublicationStructure publication101_publicationstructure;




    private publication101_Position publication101_position;




    private publication101_Paper publication101_paper;




    private List<publication101_Paper> publication101_papers;




    private List<publication101_Skill> publication101_skills;


    public publication101_Researcher(
        String name,        String forName    ) {
        this.name = name;
        this.forName = forName;
        this.publication101_collaborations = new ArrayList<>();
        this.publication101_papers = new ArrayList<>();
        this.publication101_skills = new ArrayList<>();
    }

    public publication101_Researcher(
        String name,        String forName        ArrayList<publication101_Collaboration> publication101_collaborations,        ArrayList<publication101_Paper> publication101_papers,        ArrayList<publication101_Skill> publication101_skills    ) {
        this.name = name;
        this.forName = forName;
        this.publication101_collaborations = publication101_collaborations;
        this.publication101_papers = publication101_papers;
        this.publication101_skills = publication101_skills;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getForname() {
        return forName;
    }

    public void setForname(String forName) {
        this.forName = forName;
    }

    public List<publication101_Collaboration> getPublication101_collaborations() {
        return publication101_collaborations;
    }

    public void addPublication101_collaboration(Publication101_collaboration publication101_collaboration) {
        this.publication101_collaborations.add(publication101_collaboration);
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
    public publication101_Paper getPublication101_paper() {
        return publication101_paper;
    }

    public void setPublication101_paper(publication101_Paper publication101_paper) {
        this.publication101_paper = publication101_paper;
    }
    public List<publication101_Paper> getPublication101_papers() {
        return publication101_papers;
    }

    public void addPublication101_paper(Publication101_paper publication101_paper) {
        this.publication101_papers.add(publication101_paper);
    }
    public List<publication101_Skill> getPublication101_skills() {
        return publication101_skills;
    }

    public void addPublication101_skill(Publication101_skill publication101_skill) {
        this.publication101_skills.add(publication101_skill);
    }

}