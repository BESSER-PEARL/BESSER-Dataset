





import java.util.List;
import java.util.ArrayList;

public class research15_Researcher  {

    private String name;
    private String forName;





    private research15_Paper research15_paper;




    private List<research15_Collaboration> research15_collaborations;




    private List<research15_Review> research15_reviews;




    private research15_PublicationStructure research15_publicationstructure;




    private List<research15_Paper> research15_papers;




    private List<research15_Skill> research15_skills;




    private research15_Position research15_position;


    public research15_Researcher(
        String name,        String forName    ) {
        this.name = name;
        this.forName = forName;
        this.research15_collaborations = new ArrayList<>();
        this.research15_reviews = new ArrayList<>();
        this.research15_papers = new ArrayList<>();
        this.research15_skills = new ArrayList<>();
    }

    public research15_Researcher(
        String name,        String forName        ArrayList<research15_Collaboration> research15_collaborations,        ArrayList<research15_Review> research15_reviews,        ArrayList<research15_Paper> research15_papers,        ArrayList<research15_Skill> research15_skills    ) {
        this.name = name;
        this.forName = forName;
        this.research15_collaborations = research15_collaborations;
        this.research15_reviews = research15_reviews;
        this.research15_papers = research15_papers;
        this.research15_skills = research15_skills;
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

    public research15_Paper getResearch15_paper() {
        return research15_paper;
    }

    public void setResearch15_paper(research15_Paper research15_paper) {
        this.research15_paper = research15_paper;
    }
    public List<research15_Collaboration> getResearch15_collaborations() {
        return research15_collaborations;
    }

    public void addResearch15_collaboration(Research15_collaboration research15_collaboration) {
        this.research15_collaborations.add(research15_collaboration);
    }
    public List<research15_Review> getResearch15_reviews() {
        return research15_reviews;
    }

    public void addResearch15_review(Research15_review research15_review) {
        this.research15_reviews.add(research15_review);
    }
    public research15_PublicationStructure getResearch15_publicationstructure() {
        return research15_publicationstructure;
    }

    public void setResearch15_publicationstructure(research15_PublicationStructure research15_publicationstructure) {
        this.research15_publicationstructure = research15_publicationstructure;
    }
    public List<research15_Paper> getResearch15_papers() {
        return research15_papers;
    }

    public void addResearch15_paper(Research15_paper research15_paper) {
        this.research15_papers.add(research15_paper);
    }
    public List<research15_Skill> getResearch15_skills() {
        return research15_skills;
    }

    public void addResearch15_skill(Research15_skill research15_skill) {
        this.research15_skills.add(research15_skill);
    }
    public research15_Position getResearch15_position() {
        return research15_position;
    }

    public void setResearch15_position(research15_Position research15_position) {
        this.research15_position = research15_position;
    }

}