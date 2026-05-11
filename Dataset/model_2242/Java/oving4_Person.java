





import java.util.List;
import java.util.ArrayList;

public class oving4_Person  {

    private String last_name;
    private String first_name;
    private String name;
    private float studyCredits;





    private oving4_PersonRole oving4_personrole;




    private oving4_Evaluation oving4_evaluation;




    private List<oving4_PersonRole> oving4_personroles;




    private oving4_Root oving4_root;




    private List<oving4_Evaluation> oving4_evaluations;


    public oving4_Person(
        String last_name,        String first_name,        String name,        float studyCredits    ) {
        this.last_name = last_name;
        this.first_name = first_name;
        this.name = name;
        this.studyCredits = studyCredits;
        this.oving4_personroles = new ArrayList<>();
        this.oving4_evaluations = new ArrayList<>();
    }

    public oving4_Person(
        String last_name,        String first_name,        String name,        float studyCredits        ArrayList<oving4_PersonRole> oving4_personroles,        ArrayList<oving4_Evaluation> oving4_evaluations    ) {
        this.last_name = last_name;
        this.first_name = first_name;
        this.name = name;
        this.studyCredits = studyCredits;
        this.oving4_personroles = oving4_personroles;
        this.oving4_evaluations = oving4_evaluations;
    }

    public String getLast_name() {
        return last_name;
    }

    public void setLast_name(String last_name) {
        this.last_name = last_name;
    }
    public String getFirst_name() {
        return first_name;
    }

    public void setFirst_name(String first_name) {
        this.first_name = first_name;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getStudycredits() {
        return studyCredits;
    }

    public void setStudycredits(float studyCredits) {
        this.studyCredits = studyCredits;
    }

    public oving4_PersonRole getOving4_personrole() {
        return oving4_personrole;
    }

    public void setOving4_personrole(oving4_PersonRole oving4_personrole) {
        this.oving4_personrole = oving4_personrole;
    }
    public oving4_Evaluation getOving4_evaluation() {
        return oving4_evaluation;
    }

    public void setOving4_evaluation(oving4_Evaluation oving4_evaluation) {
        this.oving4_evaluation = oving4_evaluation;
    }
    public List<oving4_PersonRole> getOving4_personroles() {
        return oving4_personroles;
    }

    public void addOving4_personrole(Oving4_personrole oving4_personrole) {
        this.oving4_personroles.add(oving4_personrole);
    }
    public oving4_Root getOving4_root() {
        return oving4_root;
    }

    public void setOving4_root(oving4_Root oving4_root) {
        this.oving4_root = oving4_root;
    }
    public List<oving4_Evaluation> getOving4_evaluations() {
        return oving4_evaluations;
    }

    public void addOving4_evaluation(Oving4_evaluation oving4_evaluation) {
        this.oving4_evaluations.add(oving4_evaluation);
    }

}