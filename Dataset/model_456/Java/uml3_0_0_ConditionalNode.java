





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_ConditionalNode extends StructuredActivityNode {

    private String isDeterminate;
    private String isAssured;





    private List<uml3_0_0_Clause> uml3_0_0_clauses;


    public uml3_0_0_ConditionalNode(
        String isDeterminate,        String isAssured    ) {
        super(
        );
        this.isDeterminate = isDeterminate;
        this.isAssured = isAssured;
        this.uml3_0_0_clauses = new ArrayList<>();
    }

    public uml3_0_0_ConditionalNode(
        String isDeterminate,        String isAssured        ArrayList<uml3_0_0_Clause> uml3_0_0_clauses    ) {
        this.isDeterminate = isDeterminate;
        this.isAssured = isAssured;
        this.uml3_0_0_clauses = uml3_0_0_clauses;
    }

    public String getIsdeterminate() {
        return isDeterminate;
    }

    public void setIsdeterminate(String isDeterminate) {
        this.isDeterminate = isDeterminate;
    }
    public String getIsassured() {
        return isAssured;
    }

    public void setIsassured(String isAssured) {
        this.isAssured = isAssured;
    }

    public List<uml3_0_0_Clause> getUml3_0_0_clauses() {
        return uml3_0_0_clauses;
    }

    public void addUml3_0_0_clause(Uml3_0_0_clause uml3_0_0_clause) {
        this.uml3_0_0_clauses.add(uml3_0_0_clause);
    }

}