





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_GroupByExpressions  {






    private sqliteModel_SelectExpression sqlitemodel_selectexpression;




    private List<sqliteModel_Expression> sqlitemodel_expressions;


    public sqliteModel_GroupByExpressions(
    ) {
        this.sqlitemodel_expressions = new ArrayList<>();
    }

    public sqliteModel_GroupByExpressions(
        ArrayList<sqliteModel_Expression> sqlitemodel_expressions    ) {
        this.sqlitemodel_expressions = sqlitemodel_expressions;
    }


    public sqliteModel_SelectExpression getSqlitemodel_selectexpression() {
        return sqlitemodel_selectexpression;
    }

    public void setSqlitemodel_selectexpression(sqliteModel_SelectExpression sqlitemodel_selectexpression) {
        this.sqlitemodel_selectexpression = sqlitemodel_selectexpression;
    }
    public List<sqliteModel_Expression> getSqlitemodel_expressions() {
        return sqlitemodel_expressions;
    }

    public void addSqlitemodel_expression(Sqlitemodel_expression sqlitemodel_expression) {
        this.sqlitemodel_expressions.add(sqlitemodel_expression);
    }

}