





import java.util.List;
import java.util.ArrayList;

public class tp5_Researcher  {

    private String name;
    private String forName;





    private List<tp5_Collaboration> tp5_collaborations;




    private List<tp5_Paper> tp5_papers;




    private List<tp5_Skill> tp5_skills;




    private tp5_Paper tp5_paper;




    private tp5_Position tp5_position;


    public tp5_Researcher(
        String name,        String forName    ) {
        this.name = name;
        this.forName = forName;
        this.tp5_collaborations = new ArrayList<>();
        this.tp5_papers = new ArrayList<>();
        this.tp5_skills = new ArrayList<>();
    }

    public tp5_Researcher(
        String name,        String forName        ArrayList<tp5_Collaboration> tp5_collaborations,        ArrayList<tp5_Paper> tp5_papers,        ArrayList<tp5_Skill> tp5_skills    ) {
        this.name = name;
        this.forName = forName;
        this.tp5_collaborations = tp5_collaborations;
        this.tp5_papers = tp5_papers;
        this.tp5_skills = tp5_skills;
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

    public List<tp5_Collaboration> getTp5_collaborations() {
        return tp5_collaborations;
    }

    public void addTp5_collaboration(Tp5_collaboration tp5_collaboration) {
        this.tp5_collaborations.add(tp5_collaboration);
    }
    public List<tp5_Paper> getTp5_papers() {
        return tp5_papers;
    }

    public void addTp5_paper(Tp5_paper tp5_paper) {
        this.tp5_papers.add(tp5_paper);
    }
    public List<tp5_Skill> getTp5_skills() {
        return tp5_skills;
    }

    public void addTp5_skill(Tp5_skill tp5_skill) {
        this.tp5_skills.add(tp5_skill);
    }
    public tp5_Paper getTp5_paper() {
        return tp5_paper;
    }

    public void setTp5_paper(tp5_Paper tp5_paper) {
        this.tp5_paper = tp5_paper;
    }
    public tp5_Position getTp5_position() {
        return tp5_position;
    }

    public void setTp5_position(tp5_Position tp5_position) {
        this.tp5_position = tp5_position;
    }

}