





import java.util.List;
import java.util.ArrayList;

public class java__SwitchStatement extends Statement {






    private java__Expression java__expression;




    private List<java__Statement> java__statements;


    public java__SwitchStatement(
    ) {
        super(
        );
        this.java__statements = new ArrayList<>();
    }

    public java__SwitchStatement(
        ArrayList<java__Statement> java__statements    ) {
        this.java__statements = java__statements;
    }


    public java__Expression getJava__expression() {
        return java__expression;
    }

    public void setJava__expression(java__Expression java__expression) {
        this.java__expression = java__expression;
    }
    public List<java__Statement> getJava__statements() {
        return java__statements;
    }

    public void addJava__statement(Java__statement java__statement) {
        this.java__statements.add(java__statement);
    }

}