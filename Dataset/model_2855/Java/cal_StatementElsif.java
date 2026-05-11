





import java.util.List;
import java.util.ArrayList;

public class cal_StatementElsif  {






    private List<cal_Statement> cal_statements;




    private cal_StatementIf cal_statementif;




    private cal_AstExpression cal_astexpression;


    public cal_StatementElsif(
    ) {
        this.cal_statements = new ArrayList<>();
    }

    public cal_StatementElsif(
        ArrayList<cal_Statement> cal_statements    ) {
        this.cal_statements = cal_statements;
    }


    public List<cal_Statement> getCal_statements() {
        return cal_statements;
    }

    public void addCal_statement(Cal_statement cal_statement) {
        this.cal_statements.add(cal_statement);
    }
    public cal_StatementIf getCal_statementif() {
        return cal_statementif;
    }

    public void setCal_statementif(cal_StatementIf cal_statementif) {
        this.cal_statementif = cal_statementif;
    }
    public cal_AstExpression getCal_astexpression() {
        return cal_astexpression;
    }

    public void setCal_astexpression(cal_AstExpression cal_astexpression) {
        this.cal_astexpression = cal_astexpression;
    }

}