





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Clause extends Element {






    private UML2WithID_Clause uml2withid_clause;




    private List<UML2WithID_Clause> uml2withid_clauses;




    private List<UML2WithID_ActivityNode> uml2withid_activitynodes;




    private List<UML2WithID_ActivityNode> uml2withid_activitynodes;


    public UML2WithID_Clause(
    ) {
        super(
        );
        this.uml2withid_clauses = new ArrayList<>();
        this.uml2withid_activitynodes = new ArrayList<>();
        this.uml2withid_activitynodes = new ArrayList<>();
    }

    public UML2WithID_Clause(
        ArrayList<UML2WithID_Clause> uml2withid_clauses,        ArrayList<UML2WithID_ActivityNode> uml2withid_activitynodes,        ArrayList<UML2WithID_ActivityNode> uml2withid_activitynodes    ) {
        this.uml2withid_clauses = uml2withid_clauses;
        this.uml2withid_activitynodes = uml2withid_activitynodes;
        this.uml2withid_activitynodes = uml2withid_activitynodes;
    }


    public UML2WithID_Clause getUml2withid_clause() {
        return uml2withid_clause;
    }

    public void setUml2withid_clause(UML2WithID_Clause uml2withid_clause) {
        this.uml2withid_clause = uml2withid_clause;
    }
    public List<UML2WithID_Clause> getUml2withid_clauses() {
        return uml2withid_clauses;
    }

    public void addUml2withid_clause(Uml2withid_clause uml2withid_clause) {
        this.uml2withid_clauses.add(uml2withid_clause);
    }
    public List<UML2WithID_ActivityNode> getUml2withid_activitynodes() {
        return uml2withid_activitynodes;
    }

    public void addUml2withid_activitynode(Uml2withid_activitynode uml2withid_activitynode) {
        this.uml2withid_activitynodes.add(uml2withid_activitynode);
    }
    public List<UML2WithID_ActivityNode> getUml2withid_activitynodes() {
        return uml2withid_activitynodes;
    }

    public void addUml2withid_activitynode(Uml2withid_activitynode uml2withid_activitynode) {
        this.uml2withid_activitynodes.add(uml2withid_activitynode);
    }

}