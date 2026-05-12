





import java.util.List;
import java.util.ArrayList;

public class research18_Researcher  {

    private String forName;
    private String name;





    private List<research18_Collaboration> research18_collaborations;




    private research18_Paper research18_paper;




    private List<research18_Review> research18_reviews;




    private List<research18_Paper> research18_papers;




    private research18_Position research18_position;




    private research18_PublicationStructure research18_publicationstructure;




    private List<research18_Skill> research18_skills;


    public research18_Researcher(
        String forName,        String name    ) {
        this.forName = forName;
        this.name = name;
        this.research18_collaborations = new ArrayList<>();
        this.research18_reviews = new ArrayList<>();
        this.research18_papers = new ArrayList<>();
        this.research18_skills = new ArrayList<>();
    }

    public research18_Researcher(
        String forName,        String name        ArrayList<research18_Collaboration> research18_collaborations,        ArrayList<research18_Review> research18_reviews,        ArrayList<research18_Paper> research18_papers,        ArrayList<research18_Skill> research18_skills    ) {
        this.forName = forName;
        this.name = name;
        this.research18_collaborations = research18_collaborations;
        this.research18_reviews = research18_reviews;
        this.research18_papers = research18_papers;
        this.research18_skills = research18_skills;
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

    public List<research18_Collaboration> getResearch18_collaborations() {
        return research18_collaborations;
    }

    public void addResearch18_collaboration(Research18_collaboration research18_collaboration) {
        this.research18_collaborations.add(research18_collaboration);
    }
    public research18_Paper getResearch18_paper() {
        return research18_paper;
    }

    public void setResearch18_paper(research18_Paper research18_paper) {
        this.research18_paper = research18_paper;
    }
    public List<research18_Review> getResearch18_reviews() {
        return research18_reviews;
    }

    public void addResearch18_review(Research18_review research18_review) {
        this.research18_reviews.add(research18_review);
    }
    public List<research18_Paper> getResearch18_papers() {
        return research18_papers;
    }

    public void addResearch18_paper(Research18_paper research18_paper) {
        this.research18_papers.add(research18_paper);
    }
    public research18_Position getResearch18_position() {
        return research18_position;
    }

    public void setResearch18_position(research18_Position research18_position) {
        this.research18_position = research18_position;
    }
    public research18_PublicationStructure getResearch18_publicationstructure() {
        return research18_publicationstructure;
    }

    public void setResearch18_publicationstructure(research18_PublicationStructure research18_publicationstructure) {
        this.research18_publicationstructure = research18_publicationstructure;
    }
    public List<research18_Skill> getResearch18_skills() {
        return research18_skills;
    }

    public void addResearch18_skill(Research18_skill research18_skill) {
        this.research18_skills.add(research18_skill);
    }

}