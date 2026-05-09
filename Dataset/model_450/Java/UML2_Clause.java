





import java.util.List;
import java.util.ArrayList;

public class UML2_Clause extends Element {






    private List<UML2_OutputPin> uml2_outputpins;




    private List<UML2_Clause> uml2_clauses;




    private List<UML2_ActivityNode> uml2_activitynodes;




    private List<UML2_ActivityNode> uml2_activitynodes;




    private List<UML2_Clause> uml2_clauses;




    private UML2_OutputPin uml2_outputpin;




    private UML2_ConditionalNode uml2_conditionalnode;


    public UML2_Clause(
    ) {
        super(
        );
        this.uml2_outputpins = new ArrayList<>();
        this.uml2_clauses = new ArrayList<>();
        this.uml2_activitynodes = new ArrayList<>();
        this.uml2_activitynodes = new ArrayList<>();
        this.uml2_clauses = new ArrayList<>();
    }

    public UML2_Clause(
        ArrayList<UML2_OutputPin> uml2_outputpins,        ArrayList<UML2_Clause> uml2_clauses,        ArrayList<UML2_ActivityNode> uml2_activitynodes,        ArrayList<UML2_ActivityNode> uml2_activitynodes,        ArrayList<UML2_Clause> uml2_clauses    ) {
        this.uml2_outputpins = uml2_outputpins;
        this.uml2_clauses = uml2_clauses;
        this.uml2_activitynodes = uml2_activitynodes;
        this.uml2_activitynodes = uml2_activitynodes;
        this.uml2_clauses = uml2_clauses;
    }


    public List<UML2_OutputPin> getUml2_outputpins() {
        return uml2_outputpins;
    }

    public void addUml2_outputpin(Uml2_outputpin uml2_outputpin) {
        this.uml2_outputpins.add(uml2_outputpin);
    }
    public List<UML2_Clause> getUml2_clauses() {
        return uml2_clauses;
    }

    public void addUml2_clause(Uml2_clause uml2_clause) {
        this.uml2_clauses.add(uml2_clause);
    }
    public List<UML2_ActivityNode> getUml2_activitynodes() {
        return uml2_activitynodes;
    }

    public void addUml2_activitynode(Uml2_activitynode uml2_activitynode) {
        this.uml2_activitynodes.add(uml2_activitynode);
    }
    public List<UML2_ActivityNode> getUml2_activitynodes() {
        return uml2_activitynodes;
    }

    public void addUml2_activitynode(Uml2_activitynode uml2_activitynode) {
        this.uml2_activitynodes.add(uml2_activitynode);
    }
    public List<UML2_Clause> getUml2_clauses() {
        return uml2_clauses;
    }

    public void addUml2_clause(Uml2_clause uml2_clause) {
        this.uml2_clauses.add(uml2_clause);
    }
    public UML2_OutputPin getUml2_outputpin() {
        return uml2_outputpin;
    }

    public void setUml2_outputpin(UML2_OutputPin uml2_outputpin) {
        this.uml2_outputpin = uml2_outputpin;
    }
    public UML2_ConditionalNode getUml2_conditionalnode() {
        return uml2_conditionalnode;
    }

    public void setUml2_conditionalnode(UML2_ConditionalNode uml2_conditionalnode) {
        this.uml2_conditionalnode = uml2_conditionalnode;
    }

}