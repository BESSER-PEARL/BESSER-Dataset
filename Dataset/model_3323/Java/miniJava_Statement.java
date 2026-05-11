





import java.util.List;
import java.util.ArrayList;

public class miniJava_Statement  {

    private boolean isArrayElementAssignment;
    private String statementType;





    private List<miniJava_Statement> minijava_statements;




    private miniJava_MainMethod minijava_mainmethod;




    private miniJava_Method minijava_method;


    public miniJava_Statement(
        boolean isArrayElementAssignment,        String statementType    ) {
        this.isArrayElementAssignment = isArrayElementAssignment;
        this.statementType = statementType;
        this.minijava_statements = new ArrayList<>();
    }

    public miniJava_Statement(
        boolean isArrayElementAssignment,        String statementType        ArrayList<miniJava_Statement> minijava_statements    ) {
        this.isArrayElementAssignment = isArrayElementAssignment;
        this.statementType = statementType;
        this.minijava_statements = minijava_statements;
    }

    public boolean getIsarrayelementassignment() {
        return isArrayElementAssignment;
    }

    public void setIsarrayelementassignment(boolean isArrayElementAssignment) {
        this.isArrayElementAssignment = isArrayElementAssignment;
    }
    public String getStatementtype() {
        return statementType;
    }

    public void setStatementtype(String statementType) {
        this.statementType = statementType;
    }

    public List<miniJava_Statement> getMinijava_statements() {
        return minijava_statements;
    }

    public void addMinijava_statement(Minijava_statement minijava_statement) {
        this.minijava_statements.add(minijava_statement);
    }
    public miniJava_MainMethod getMinijava_mainmethod() {
        return minijava_mainmethod;
    }

    public void setMinijava_mainmethod(miniJava_MainMethod minijava_mainmethod) {
        this.minijava_mainmethod = minijava_mainmethod;
    }
    public miniJava_Method getMinijava_method() {
        return minijava_method;
    }

    public void setMinijava_method(miniJava_Method minijava_method) {
        this.minijava_method = minijava_method;
    }

}