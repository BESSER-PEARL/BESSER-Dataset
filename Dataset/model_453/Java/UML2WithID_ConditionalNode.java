





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_ConditionalNode extends StructuredActivityNode {

    private boolean isAssured;
    private boolean isDeterminate;





    private List<UML2WithID_OutputPin> uml2withid_outputpins;




    private List<UML2WithID_Clause> uml2withid_clauses;


    public UML2WithID_ConditionalNode(
        boolean isAssured,        boolean isDeterminate    ) {
        super(
        );
        this.isAssured = isAssured;
        this.isDeterminate = isDeterminate;
        this.uml2withid_outputpins = new ArrayList<>();
        this.uml2withid_clauses = new ArrayList<>();
    }

    public UML2WithID_ConditionalNode(
        boolean isAssured,        boolean isDeterminate        ArrayList<UML2WithID_OutputPin> uml2withid_outputpins,        ArrayList<UML2WithID_Clause> uml2withid_clauses    ) {
        this.isAssured = isAssured;
        this.isDeterminate = isDeterminate;
        this.uml2withid_outputpins = uml2withid_outputpins;
        this.uml2withid_clauses = uml2withid_clauses;
    }

    public boolean getIsassured() {
        return isAssured;
    }

    public void setIsassured(boolean isAssured) {
        this.isAssured = isAssured;
    }
    public boolean getIsdeterminate() {
        return isDeterminate;
    }

    public void setIsdeterminate(boolean isDeterminate) {
        this.isDeterminate = isDeterminate;
    }

    public List<UML2WithID_OutputPin> getUml2withid_outputpins() {
        return uml2withid_outputpins;
    }

    public void addUml2withid_outputpin(Uml2withid_outputpin uml2withid_outputpin) {
        this.uml2withid_outputpins.add(uml2withid_outputpin);
    }
    public List<UML2WithID_Clause> getUml2withid_clauses() {
        return uml2withid_clauses;
    }

    public void addUml2withid_clause(Uml2withid_clause uml2withid_clause) {
        this.uml2withid_clauses.add(uml2withid_clause);
    }

}