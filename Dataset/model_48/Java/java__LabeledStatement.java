





import java.util.List;
import java.util.ArrayList;

public class java__LabeledStatement extends Statement, NamedElement {






    private java__Statement java__statement;




    private java__BreakStatement java__breakstatement;




    private List<java__BreakStatement> java__breakstatements;


    public java__LabeledStatement(
    ) {
        super(
        );
        this.java__breakstatements = new ArrayList<>();
    }

    public java__LabeledStatement(
        ArrayList<java__BreakStatement> java__breakstatements    ) {
        this.java__breakstatements = java__breakstatements;
    }


    public java__Statement getJava__statement() {
        return java__statement;
    }

    public void setJava__statement(java__Statement java__statement) {
        this.java__statement = java__statement;
    }
    public java__BreakStatement getJava__breakstatement() {
        return java__breakstatement;
    }

    public void setJava__breakstatement(java__BreakStatement java__breakstatement) {
        this.java__breakstatement = java__breakstatement;
    }
    public List<java__BreakStatement> getJava__breakstatements() {
        return java__breakstatements;
    }

    public void addJava__breakstatement(Java__breakstatement java__breakstatement) {
        this.java__breakstatements.add(java__breakstatement);
    }

}