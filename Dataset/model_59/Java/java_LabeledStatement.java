





import java.util.List;
import java.util.ArrayList;

public class java_LabeledStatement extends NamedElement, Statement {






    private java_BreakStatement java_breakstatement;




    private List<java_BreakStatement> java_breakstatements;




    private java_Statement java_statement;


    public java_LabeledStatement(
    ) {
        super(
        );
        this.java_breakstatements = new ArrayList<>();
    }

    public java_LabeledStatement(
        ArrayList<java_BreakStatement> java_breakstatements    ) {
        this.java_breakstatements = java_breakstatements;
    }


    public java_BreakStatement getJava_breakstatement() {
        return java_breakstatement;
    }

    public void setJava_breakstatement(java_BreakStatement java_breakstatement) {
        this.java_breakstatement = java_breakstatement;
    }
    public List<java_BreakStatement> getJava_breakstatements() {
        return java_breakstatements;
    }

    public void addJava_breakstatement(Java_breakstatement java_breakstatement) {
        this.java_breakstatements.add(java_breakstatement);
    }
    public java_Statement getJava_statement() {
        return java_statement;
    }

    public void setJava_statement(java_Statement java_statement) {
        this.java_statement = java_statement;
    }

}