





import java.util.List;
import java.util.ArrayList;

public class cal_StatementWhile extends Statement {






    private List<cal_Statement> cal_statements;




    private cal_AstExpression cal_astexpression;


    public cal_StatementWhile(
    ) {
        super(
        );
        this.cal_statements = new ArrayList<>();
    }

    public cal_StatementWhile(
        ArrayList<cal_Statement> cal_statements    ) {
        this.cal_statements = cal_statements;
    }


    public List<cal_Statement> getCal_statements() {
        return cal_statements;
    }

    public void addCal_statement(Cal_statement cal_statement) {
        this.cal_statements.add(cal_statement);
    }
    public cal_AstExpression getCal_astexpression() {
        return cal_astexpression;
    }

    public void setCal_astexpression(cal_AstExpression cal_astexpression) {
        this.cal_astexpression = cal_astexpression;
    }

}