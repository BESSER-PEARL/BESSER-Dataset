





import java.util.List;
import java.util.ArrayList;

public class tp6_Researcher  {

    private String name;
    private String forName;





    private List<tp6_Paper> tp6_papers;




    private List<tp6_Skill> tp6_skills;




    private tp6_Paper tp6_paper;




    private tp6_Position tp6_position;




    private List<tp6_Collaboration> tp6_collaborations;


    public tp6_Researcher(
        String name,        String forName    ) {
        this.name = name;
        this.forName = forName;
        this.tp6_papers = new ArrayList<>();
        this.tp6_skills = new ArrayList<>();
        this.tp6_collaborations = new ArrayList<>();
    }

    public tp6_Researcher(
        String name,        String forName        ArrayList<tp6_Paper> tp6_papers,        ArrayList<tp6_Skill> tp6_skills,        ArrayList<tp6_Collaboration> tp6_collaborations    ) {
        this.name = name;
        this.forName = forName;
        this.tp6_papers = tp6_papers;
        this.tp6_skills = tp6_skills;
        this.tp6_collaborations = tp6_collaborations;
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

    public List<tp6_Paper> getTp6_papers() {
        return tp6_papers;
    }

    public void addTp6_paper(Tp6_paper tp6_paper) {
        this.tp6_papers.add(tp6_paper);
    }
    public List<tp6_Skill> getTp6_skills() {
        return tp6_skills;
    }

    public void addTp6_skill(Tp6_skill tp6_skill) {
        this.tp6_skills.add(tp6_skill);
    }
    public tp6_Paper getTp6_paper() {
        return tp6_paper;
    }

    public void setTp6_paper(tp6_Paper tp6_paper) {
        this.tp6_paper = tp6_paper;
    }
    public tp6_Position getTp6_position() {
        return tp6_position;
    }

    public void setTp6_position(tp6_Position tp6_position) {
        this.tp6_position = tp6_position;
    }
    public List<tp6_Collaboration> getTp6_collaborations() {
        return tp6_collaborations;
    }

    public void addTp6_collaboration(Tp6_collaboration tp6_collaboration) {
        this.tp6_collaborations.add(tp6_collaboration);
    }

}