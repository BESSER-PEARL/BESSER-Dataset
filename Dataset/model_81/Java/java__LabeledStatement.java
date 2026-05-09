





import java.util.List;
import java.util.ArrayList;

public class java__LabeledStatement extends Statement, NamedElement {






    private List<java__ContinueStatement> java__continuestatements;




    private java__ContinueStatement java__continuestatement;




    private java__Statement java__statement;


    public java__LabeledStatement(
    ) {
        super(
        );
        this.java__continuestatements = new ArrayList<>();
    }

    public java__LabeledStatement(
        ArrayList<java__ContinueStatement> java__continuestatements    ) {
        this.java__continuestatements = java__continuestatements;
    }


    public List<java__ContinueStatement> getJava__continuestatements() {
        return java__continuestatements;
    }

    public void addJava__continuestatement(Java__continuestatement java__continuestatement) {
        this.java__continuestatements.add(java__continuestatement);
    }
    public java__ContinueStatement getJava__continuestatement() {
        return java__continuestatement;
    }

    public void setJava__continuestatement(java__ContinueStatement java__continuestatement) {
        this.java__continuestatement = java__continuestatement;
    }
    public java__Statement getJava__statement() {
        return java__statement;
    }

    public void setJava__statement(java__Statement java__statement) {
        this.java__statement = java__statement;
    }

}