





import java.util.List;
import java.util.ArrayList;

public class dbl_SwitchCase  {






    private dbl_Expression dbl_expression;




    private dbl_SwitchStatement dbl_switchstatement;




    private dbl_SwitchStatement dbl_switchstatement;




    private List<dbl_Statement> dbl_statements;


    public dbl_SwitchCase(
    ) {
        this.dbl_statements = new ArrayList<>();
    }

    public dbl_SwitchCase(
        ArrayList<dbl_Statement> dbl_statements    ) {
        this.dbl_statements = dbl_statements;
    }


    public dbl_Expression getDbl_expression() {
        return dbl_expression;
    }

    public void setDbl_expression(dbl_Expression dbl_expression) {
        this.dbl_expression = dbl_expression;
    }
    public dbl_SwitchStatement getDbl_switchstatement() {
        return dbl_switchstatement;
    }

    public void setDbl_switchstatement(dbl_SwitchStatement dbl_switchstatement) {
        this.dbl_switchstatement = dbl_switchstatement;
    }
    public dbl_SwitchStatement getDbl_switchstatement() {
        return dbl_switchstatement;
    }

    public void setDbl_switchstatement(dbl_SwitchStatement dbl_switchstatement) {
        this.dbl_switchstatement = dbl_switchstatement;
    }
    public List<dbl_Statement> getDbl_statements() {
        return dbl_statements;
    }

    public void addDbl_statement(Dbl_statement dbl_statement) {
        this.dbl_statements.add(dbl_statement);
    }

}