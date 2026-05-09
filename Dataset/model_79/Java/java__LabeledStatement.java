





import java.util.List;
import java.util.ArrayList;

public class java__LabeledStatement extends Statement, NamedElement {






    private java__ContinueStatement java__continuestatement;




    private List<java__ContinueStatement> java__continuestatements;




    private java__BreakStatement java__breakstatement;




    private List<java__BreakStatement> java__breakstatements;




    private java__Statement java__statement;


    public java__LabeledStatement(
    ) {
        super(
        );
        this.java__continuestatements = new ArrayList<>();
        this.java__breakstatements = new ArrayList<>();
    }

    public java__LabeledStatement(
        ArrayList<java__ContinueStatement> java__continuestatements,        ArrayList<java__BreakStatement> java__breakstatements    ) {
        this.java__continuestatements = java__continuestatements;
        this.java__breakstatements = java__breakstatements;
    }


    public java__ContinueStatement getJava__continuestatement() {
        return java__continuestatement;
    }

    public void setJava__continuestatement(java__ContinueStatement java__continuestatement) {
        this.java__continuestatement = java__continuestatement;
    }
    public List<java__ContinueStatement> getJava__continuestatements() {
        return java__continuestatements;
    }

    public void addJava__continuestatement(Java__continuestatement java__continuestatement) {
        this.java__continuestatements.add(java__continuestatement);
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
    public java__Statement getJava__statement() {
        return java__statement;
    }

    public void setJava__statement(java__Statement java__statement) {
        this.java__statement = java__statement;
    }

}