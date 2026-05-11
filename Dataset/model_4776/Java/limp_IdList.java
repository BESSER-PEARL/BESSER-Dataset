





import java.util.List;
import java.util.ArrayList;

public class limp_IdList  {






    private List<limp_VariableRef> limp_variablerefs;




    private limp_AssignmentStatement limp_assignmentstatement;


    public limp_IdList(
    ) {
        this.limp_variablerefs = new ArrayList<>();
    }

    public limp_IdList(
        ArrayList<limp_VariableRef> limp_variablerefs    ) {
        this.limp_variablerefs = limp_variablerefs;
    }


    public List<limp_VariableRef> getLimp_variablerefs() {
        return limp_variablerefs;
    }

    public void addLimp_variableref(Limp_variableref limp_variableref) {
        this.limp_variablerefs.add(limp_variableref);
    }
    public limp_AssignmentStatement getLimp_assignmentstatement() {
        return limp_assignmentstatement;
    }

    public void setLimp_assignmentstatement(limp_AssignmentStatement limp_assignmentstatement) {
        this.limp_assignmentstatement = limp_assignmentstatement;
    }

}