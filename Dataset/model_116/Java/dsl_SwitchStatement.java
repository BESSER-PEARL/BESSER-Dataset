





import java.util.List;
import java.util.ArrayList;

public class dsl_SwitchStatement  {






    private dsl_Statement dsl_statement;




    private List<dsl_BlockStatement> dsl_blockstatements;




    private dsl_Expression dsl_expression;


    public dsl_SwitchStatement(
    ) {
        this.dsl_blockstatements = new ArrayList<>();
    }

    public dsl_SwitchStatement(
        ArrayList<dsl_BlockStatement> dsl_blockstatements    ) {
        this.dsl_blockstatements = dsl_blockstatements;
    }


    public dsl_Statement getDsl_statement() {
        return dsl_statement;
    }

    public void setDsl_statement(dsl_Statement dsl_statement) {
        this.dsl_statement = dsl_statement;
    }
    public List<dsl_BlockStatement> getDsl_blockstatements() {
        return dsl_blockstatements;
    }

    public void addDsl_blockstatement(Dsl_blockstatement dsl_blockstatement) {
        this.dsl_blockstatements.add(dsl_blockstatement);
    }
    public dsl_Expression getDsl_expression() {
        return dsl_expression;
    }

    public void setDsl_expression(dsl_Expression dsl_expression) {
        this.dsl_expression = dsl_expression;
    }

}