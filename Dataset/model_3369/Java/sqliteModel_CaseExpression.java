





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_CaseExpression extends Expression {






    private sqliteModel_Expression sqlitemodel_expression;




    private List<sqliteModel_Case> sqlitemodel_cases;




    private sqliteModel_Expression sqlitemodel_expression;


    public sqliteModel_CaseExpression(
    ) {
        super(
        );
        this.sqlitemodel_cases = new ArrayList<>();
    }

    public sqliteModel_CaseExpression(
        ArrayList<sqliteModel_Case> sqlitemodel_cases    ) {
        this.sqlitemodel_cases = sqlitemodel_cases;
    }


    public sqliteModel_Expression getSqlitemodel_expression() {
        return sqlitemodel_expression;
    }

    public void setSqlitemodel_expression(sqliteModel_Expression sqlitemodel_expression) {
        this.sqlitemodel_expression = sqlitemodel_expression;
    }
    public List<sqliteModel_Case> getSqlitemodel_cases() {
        return sqlitemodel_cases;
    }

    public void addSqlitemodel_case(Sqlitemodel_case sqlitemodel_case) {
        this.sqlitemodel_cases.add(sqlitemodel_case);
    }
    public sqliteModel_Expression getSqlitemodel_expression() {
        return sqlitemodel_expression;
    }

    public void setSqlitemodel_expression(sqliteModel_Expression sqlitemodel_expression) {
        this.sqlitemodel_expression = sqlitemodel_expression;
    }

}