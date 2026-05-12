





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_SelectStatement extends DMLStatement {






    private sqliteModel_SelectStatementExpression sqlitemodel_selectstatementexpression;




    private sqliteModel_Expression sqlitemodel_expression;




    private sqliteModel_Function sqlitemodel_function;




    private sqliteModel_Expression sqlitemodel_expression;




    private sqliteModel_InsertStatement sqlitemodel_insertstatement;




    private sqliteModel_SingleSourceSelectStatement sqlitemodel_singlesourceselectstatement;




    private sqliteModel_CreateViewStatement sqlitemodel_createviewstatement;


    public sqliteModel_SelectStatement(
    ) {
        super(
        );
    }



    public sqliteModel_SelectStatementExpression getSqlitemodel_selectstatementexpression() {
        return sqlitemodel_selectstatementexpression;
    }

    public void setSqlitemodel_selectstatementexpression(sqliteModel_SelectStatementExpression sqlitemodel_selectstatementexpression) {
        this.sqlitemodel_selectstatementexpression = sqlitemodel_selectstatementexpression;
    }
    public sqliteModel_Expression getSqlitemodel_expression() {
        return sqlitemodel_expression;
    }

    public void setSqlitemodel_expression(sqliteModel_Expression sqlitemodel_expression) {
        this.sqlitemodel_expression = sqlitemodel_expression;
    }
    public sqliteModel_Function getSqlitemodel_function() {
        return sqlitemodel_function;
    }

    public void setSqlitemodel_function(sqliteModel_Function sqlitemodel_function) {
        this.sqlitemodel_function = sqlitemodel_function;
    }
    public sqliteModel_Expression getSqlitemodel_expression() {
        return sqlitemodel_expression;
    }

    public void setSqlitemodel_expression(sqliteModel_Expression sqlitemodel_expression) {
        this.sqlitemodel_expression = sqlitemodel_expression;
    }
    public sqliteModel_InsertStatement getSqlitemodel_insertstatement() {
        return sqlitemodel_insertstatement;
    }

    public void setSqlitemodel_insertstatement(sqliteModel_InsertStatement sqlitemodel_insertstatement) {
        this.sqlitemodel_insertstatement = sqlitemodel_insertstatement;
    }
    public sqliteModel_SingleSourceSelectStatement getSqlitemodel_singlesourceselectstatement() {
        return sqlitemodel_singlesourceselectstatement;
    }

    public void setSqlitemodel_singlesourceselectstatement(sqliteModel_SingleSourceSelectStatement sqlitemodel_singlesourceselectstatement) {
        this.sqlitemodel_singlesourceselectstatement = sqlitemodel_singlesourceselectstatement;
    }
    public sqliteModel_CreateViewStatement getSqlitemodel_createviewstatement() {
        return sqlitemodel_createviewstatement;
    }

    public void setSqlitemodel_createviewstatement(sqliteModel_CreateViewStatement sqlitemodel_createviewstatement) {
        this.sqlitemodel_createviewstatement = sqlitemodel_createviewstatement;
    }

}