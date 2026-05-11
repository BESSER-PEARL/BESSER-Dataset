





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_Function extends ConfigurationStatement, Expression {

    private boolean all;





    private List<sqliteModel_Expression> sqlitemodel_expressions;




    private List<sqliteModel_FunctionArg> sqlitemodel_functionargs;




    private List<sqliteModel_DMLStatement> sqlitemodel_dmlstatements;


    public sqliteModel_Function(
        boolean all    ) {
        super(
        );
        this.all = all;
        this.sqlitemodel_expressions = new ArrayList<>();
        this.sqlitemodel_functionargs = new ArrayList<>();
        this.sqlitemodel_dmlstatements = new ArrayList<>();
    }

    public sqliteModel_Function(
        boolean all        ArrayList<sqliteModel_Expression> sqlitemodel_expressions,        ArrayList<sqliteModel_FunctionArg> sqlitemodel_functionargs,        ArrayList<sqliteModel_DMLStatement> sqlitemodel_dmlstatements    ) {
        this.all = all;
        this.sqlitemodel_expressions = sqlitemodel_expressions;
        this.sqlitemodel_functionargs = sqlitemodel_functionargs;
        this.sqlitemodel_dmlstatements = sqlitemodel_dmlstatements;
    }

    public boolean getAll() {
        return all;
    }

    public void setAll(boolean all) {
        this.all = all;
    }

    public List<sqliteModel_Expression> getSqlitemodel_expressions() {
        return sqlitemodel_expressions;
    }

    public void addSqlitemodel_expression(Sqlitemodel_expression sqlitemodel_expression) {
        this.sqlitemodel_expressions.add(sqlitemodel_expression);
    }
    public List<sqliteModel_FunctionArg> getSqlitemodel_functionargs() {
        return sqlitemodel_functionargs;
    }

    public void addSqlitemodel_functionarg(Sqlitemodel_functionarg sqlitemodel_functionarg) {
        this.sqlitemodel_functionargs.add(sqlitemodel_functionarg);
    }
    public List<sqliteModel_DMLStatement> getSqlitemodel_dmlstatements() {
        return sqlitemodel_dmlstatements;
    }

    public void addSqlitemodel_dmlstatement(Sqlitemodel_dmlstatement sqlitemodel_dmlstatement) {
        this.sqlitemodel_dmlstatements.add(sqlitemodel_dmlstatement);
    }

}