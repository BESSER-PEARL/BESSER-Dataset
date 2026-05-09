





import java.util.List;
import java.util.ArrayList;

public class java_LabeledStatement extends Statement, NamedElement {






    private java_BreakStatement java_breakstatement;




    private java_Statement java_statement;


    public java_LabeledStatement(
    ) {
        super(
        );
    }



    public java_BreakStatement getJava_breakstatement() {
        return java_breakstatement;
    }

    public void setJava_breakstatement(java_BreakStatement java_breakstatement) {
        this.java_breakstatement = java_breakstatement;
    }
    public java_Statement getJava_statement() {
        return java_statement;
    }

    public void setJava_statement(java_Statement java_statement) {
        this.java_statement = java_statement;
    }

}