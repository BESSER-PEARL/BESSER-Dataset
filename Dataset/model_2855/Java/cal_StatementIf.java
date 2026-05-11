





import java.util.List;
import java.util.ArrayList;

public class cal_StatementIf extends Statement {






    private cal_AstExpression cal_astexpression;




    private List<cal_Statement> cal_statements;




    private List<cal_Statement> cal_statements;


    public cal_StatementIf(
    ) {
        super(
        );
        this.cal_statements = new ArrayList<>();
        this.cal_statements = new ArrayList<>();
    }

    public cal_StatementIf(
        ArrayList<cal_Statement> cal_statements,        ArrayList<cal_Statement> cal_statements    ) {
        this.cal_statements = cal_statements;
        this.cal_statements = cal_statements;
    }


    public cal_AstExpression getCal_astexpression() {
        return cal_astexpression;
    }

    public void setCal_astexpression(cal_AstExpression cal_astexpression) {
        this.cal_astexpression = cal_astexpression;
    }
    public List<cal_Statement> getCal_statements() {
        return cal_statements;
    }

    public void addCal_statement(Cal_statement cal_statement) {
        this.cal_statements.add(cal_statement);
    }
    public List<cal_Statement> getCal_statements() {
        return cal_statements;
    }

    public void addCal_statement(Cal_statement cal_statement) {
        this.cal_statements.add(cal_statement);
    }

}