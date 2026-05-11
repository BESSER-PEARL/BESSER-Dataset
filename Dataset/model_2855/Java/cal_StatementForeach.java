





import java.util.List;
import java.util.ArrayList;

public class cal_StatementForeach extends Statement {






    private List<cal_Statement> cal_statements;




    private cal_Variable cal_variable;




    private cal_AstExpression cal_astexpression;




    private cal_AstExpression cal_astexpression;


    public cal_StatementForeach(
    ) {
        super(
        );
        this.cal_statements = new ArrayList<>();
    }

    public cal_StatementForeach(
        ArrayList<cal_Statement> cal_statements    ) {
        this.cal_statements = cal_statements;
    }


    public List<cal_Statement> getCal_statements() {
        return cal_statements;
    }

    public void addCal_statement(Cal_statement cal_statement) {
        this.cal_statements.add(cal_statement);
    }
    public cal_Variable getCal_variable() {
        return cal_variable;
    }

    public void setCal_variable(cal_Variable cal_variable) {
        this.cal_variable = cal_variable;
    }
    public cal_AstExpression getCal_astexpression() {
        return cal_astexpression;
    }

    public void setCal_astexpression(cal_AstExpression cal_astexpression) {
        this.cal_astexpression = cal_astexpression;
    }
    public cal_AstExpression getCal_astexpression() {
        return cal_astexpression;
    }

    public void setCal_astexpression(cal_AstExpression cal_astexpression) {
        this.cal_astexpression = cal_astexpression;
    }

}