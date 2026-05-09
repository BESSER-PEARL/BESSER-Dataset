





import java.util.List;
import java.util.ArrayList;

public class research101_Researcher  {

    private String name;
    private String forName;





    private research101_Paper research101_paper;




    private List<research101_Paper> research101_papers;




    private List<research101_Review> research101_reviews;




    private research101_PublicationStructure research101_publicationstructure;




    private List<research101_Skill> research101_skills;




    private research101_Position research101_position;




    private List<research101_Collaboration> research101_collaborations;




    private List<research101_Write> research101_writes;


    public research101_Researcher(
        String name,        String forName    ) {
        this.name = name;
        this.forName = forName;
        this.research101_papers = new ArrayList<>();
        this.research101_reviews = new ArrayList<>();
        this.research101_skills = new ArrayList<>();
        this.research101_collaborations = new ArrayList<>();
        this.research101_writes = new ArrayList<>();
    }

    public research101_Researcher(
        String name,        String forName        ArrayList<research101_Paper> research101_papers,        ArrayList<research101_Review> research101_reviews,        ArrayList<research101_Skill> research101_skills,        ArrayList<research101_Collaboration> research101_collaborations,        ArrayList<research101_Write> research101_writes    ) {
        this.name = name;
        this.forName = forName;
        this.research101_papers = research101_papers;
        this.research101_reviews = research101_reviews;
        this.research101_skills = research101_skills;
        this.research101_collaborations = research101_collaborations;
        this.research101_writes = research101_writes;
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

    public research101_Paper getResearch101_paper() {
        return research101_paper;
    }

    public void setResearch101_paper(research101_Paper research101_paper) {
        this.research101_paper = research101_paper;
    }
    public List<research101_Paper> getResearch101_papers() {
        return research101_papers;
    }

    public void addResearch101_paper(Research101_paper research101_paper) {
        this.research101_papers.add(research101_paper);
    }
    public List<research101_Review> getResearch101_reviews() {
        return research101_reviews;
    }

    public void addResearch101_review(Research101_review research101_review) {
        this.research101_reviews.add(research101_review);
    }
    public research101_PublicationStructure getResearch101_publicationstructure() {
        return research101_publicationstructure;
    }

    public void setResearch101_publicationstructure(research101_PublicationStructure research101_publicationstructure) {
        this.research101_publicationstructure = research101_publicationstructure;
    }
    public List<research101_Skill> getResearch101_skills() {
        return research101_skills;
    }

    public void addResearch101_skill(Research101_skill research101_skill) {
        this.research101_skills.add(research101_skill);
    }
    public research101_Position getResearch101_position() {
        return research101_position;
    }

    public void setResearch101_position(research101_Position research101_position) {
        this.research101_position = research101_position;
    }
    public List<research101_Collaboration> getResearch101_collaborations() {
        return research101_collaborations;
    }

    public void addResearch101_collaboration(Research101_collaboration research101_collaboration) {
        this.research101_collaborations.add(research101_collaboration);
    }
    public List<research101_Write> getResearch101_writes() {
        return research101_writes;
    }

    public void addResearch101_write(Research101_write research101_write) {
        this.research101_writes.add(research101_write);
    }

}