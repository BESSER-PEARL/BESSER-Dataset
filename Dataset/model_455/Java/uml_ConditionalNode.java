





import java.util.List;
import java.util.ArrayList;

public class uml_ConditionalNode extends StructuredActivityNode {

    private String isAssured;
    private String isDeterminate;





    private List<uml_Clause> uml_clauses;




    private List<uml_OutputPin> uml_outputpins;


    public uml_ConditionalNode(
        String isAssured,        String isDeterminate    ) {
        super(
        );
        this.isAssured = isAssured;
        this.isDeterminate = isDeterminate;
        this.uml_clauses = new ArrayList<>();
        this.uml_outputpins = new ArrayList<>();
    }

    public uml_ConditionalNode(
        String isAssured,        String isDeterminate        ArrayList<uml_Clause> uml_clauses,        ArrayList<uml_OutputPin> uml_outputpins    ) {
        this.isAssured = isAssured;
        this.isDeterminate = isDeterminate;
        this.uml_clauses = uml_clauses;
        this.uml_outputpins = uml_outputpins;
    }

    public String getIsassured() {
        return isAssured;
    }

    public void setIsassured(String isAssured) {
        this.isAssured = isAssured;
    }
    public String getIsdeterminate() {
        return isDeterminate;
    }

    public void setIsdeterminate(String isDeterminate) {
        this.isDeterminate = isDeterminate;
    }

    public List<uml_Clause> getUml_clauses() {
        return uml_clauses;
    }

    public void addUml_clause(Uml_clause uml_clause) {
        this.uml_clauses.add(uml_clause);
    }
    public List<uml_OutputPin> getUml_outputpins() {
        return uml_outputpins;
    }

    public void addUml_outputpin(Uml_outputpin uml_outputpin) {
        this.uml_outputpins.add(uml_outputpin);
    }

}