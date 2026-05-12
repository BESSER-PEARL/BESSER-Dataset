





import java.util.List;
import java.util.ArrayList;

public class UML2_ConditionalNode extends StructuredActivityNode {

    private boolean isDeterminate;
    private boolean isAssured;





    private List<UML2_OutputPin> uml2_outputpins;




    private List<UML2_Clause> uml2_clauses;


    public UML2_ConditionalNode(
        boolean isDeterminate,        boolean isAssured    ) {
        super(
        );
        this.isDeterminate = isDeterminate;
        this.isAssured = isAssured;
        this.uml2_outputpins = new ArrayList<>();
        this.uml2_clauses = new ArrayList<>();
    }

    public UML2_ConditionalNode(
        boolean isDeterminate,        boolean isAssured        ArrayList<UML2_OutputPin> uml2_outputpins,        ArrayList<UML2_Clause> uml2_clauses    ) {
        this.isDeterminate = isDeterminate;
        this.isAssured = isAssured;
        this.uml2_outputpins = uml2_outputpins;
        this.uml2_clauses = uml2_clauses;
    }

    public boolean getIsdeterminate() {
        return isDeterminate;
    }

    public void setIsdeterminate(boolean isDeterminate) {
        this.isDeterminate = isDeterminate;
    }
    public boolean getIsassured() {
        return isAssured;
    }

    public void setIsassured(boolean isAssured) {
        this.isAssured = isAssured;
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

}