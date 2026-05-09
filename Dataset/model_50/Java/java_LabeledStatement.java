





import java.util.List;
import java.util.ArrayList;

public class java_LabeledStatement extends Statement, NamedElement {






    private java_Statement java_statement;




    private java_ContinueStatement java_continuestatement;




    private List<java_ContinueStatement> java_continuestatements;


    public java_LabeledStatement(
    ) {
        super(
        );
        this.java_continuestatements = new ArrayList<>();
    }

    public java_LabeledStatement(
        ArrayList<java_ContinueStatement> java_continuestatements    ) {
        this.java_continuestatements = java_continuestatements;
    }


    public java_Statement getJava_statement() {
        return java_statement;
    }

    public void setJava_statement(java_Statement java_statement) {
        this.java_statement = java_statement;
    }
    public java_ContinueStatement getJava_continuestatement() {
        return java_continuestatement;
    }

    public void setJava_continuestatement(java_ContinueStatement java_continuestatement) {
        this.java_continuestatement = java_continuestatement;
    }
    public List<java_ContinueStatement> getJava_continuestatements() {
        return java_continuestatements;
    }

    public void addJava_continuestatement(Java_continuestatement java_continuestatement) {
        this.java_continuestatements.add(java_continuestatement);
    }

}