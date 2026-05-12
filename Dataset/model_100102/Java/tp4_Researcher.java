





import java.util.List;
import java.util.ArrayList;

public class tp4_Researcher  {

    private String name;
    private String forName;





    private List<tp4_Skill> tp4_skills;




    private List<tp4_Write> tp4_writes;




    private List<tp4_Review> tp4_reviews;




    private List<tp4_Paper> tp4_papers;




    private tp4_PublicationStructure tp4_publicationstructure;




    private tp4_Position tp4_position;




    private tp4_Paper tp4_paper;


    public tp4_Researcher(
        String name,        String forName    ) {
        this.name = name;
        this.forName = forName;
        this.tp4_skills = new ArrayList<>();
        this.tp4_writes = new ArrayList<>();
        this.tp4_reviews = new ArrayList<>();
        this.tp4_papers = new ArrayList<>();
    }

    public tp4_Researcher(
        String name,        String forName        ArrayList<tp4_Skill> tp4_skills,        ArrayList<tp4_Write> tp4_writes,        ArrayList<tp4_Review> tp4_reviews,        ArrayList<tp4_Paper> tp4_papers    ) {
        this.name = name;
        this.forName = forName;
        this.tp4_skills = tp4_skills;
        this.tp4_writes = tp4_writes;
        this.tp4_reviews = tp4_reviews;
        this.tp4_papers = tp4_papers;
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

    public List<tp4_Skill> getTp4_skills() {
        return tp4_skills;
    }

    public void addTp4_skill(Tp4_skill tp4_skill) {
        this.tp4_skills.add(tp4_skill);
    }
    public List<tp4_Write> getTp4_writes() {
        return tp4_writes;
    }

    public void addTp4_write(Tp4_write tp4_write) {
        this.tp4_writes.add(tp4_write);
    }
    public List<tp4_Review> getTp4_reviews() {
        return tp4_reviews;
    }

    public void addTp4_review(Tp4_review tp4_review) {
        this.tp4_reviews.add(tp4_review);
    }
    public List<tp4_Paper> getTp4_papers() {
        return tp4_papers;
    }

    public void addTp4_paper(Tp4_paper tp4_paper) {
        this.tp4_papers.add(tp4_paper);
    }
    public tp4_PublicationStructure getTp4_publicationstructure() {
        return tp4_publicationstructure;
    }

    public void setTp4_publicationstructure(tp4_PublicationStructure tp4_publicationstructure) {
        this.tp4_publicationstructure = tp4_publicationstructure;
    }
    public tp4_Position getTp4_position() {
        return tp4_position;
    }

    public void setTp4_position(tp4_Position tp4_position) {
        this.tp4_position = tp4_position;
    }
    public tp4_Paper getTp4_paper() {
        return tp4_paper;
    }

    public void setTp4_paper(tp4_Paper tp4_paper) {
        this.tp4_paper = tp4_paper;
    }

}