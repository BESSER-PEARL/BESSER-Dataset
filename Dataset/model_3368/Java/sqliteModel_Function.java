





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_Function extends Expression, ConfigurationStatement {

    private boolean all;





    private List<sqliteModel_Expression> sqlitemodel_expressions;




    private sqliteModel_SelectStatement sqlitemodel_selectstatement;




    private List<sqliteModel_FunctionArg> sqlitemodel_functionargs;


    public sqliteModel_Function(
        boolean all    ) {
        super(
        );
        this.all = all;
        this.sqlitemodel_expressions = new ArrayList<>();
        this.sqlitemodel_functionargs = new ArrayList<>();
    }

    public sqliteModel_Function(
        boolean all        ArrayList<sqliteModel_Expression> sqlitemodel_expressions,        ArrayList<sqliteModel_FunctionArg> sqlitemodel_functionargs    ) {
        this.all = all;
        this.sqlitemodel_expressions = sqlitemodel_expressions;
        this.sqlitemodel_functionargs = sqlitemodel_functionargs;
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
    public sqliteModel_SelectStatement getSqlitemodel_selectstatement() {
        return sqlitemodel_selectstatement;
    }

    public void setSqlitemodel_selectstatement(sqliteModel_SelectStatement sqlitemodel_selectstatement) {
        this.sqlitemodel_selectstatement = sqlitemodel_selectstatement;
    }
    public List<sqliteModel_FunctionArg> getSqlitemodel_functionargs() {
        return sqlitemodel_functionargs;
    }

    public void addSqlitemodel_functionarg(Sqlitemodel_functionarg sqlitemodel_functionarg) {
        this.sqlitemodel_functionargs.add(sqlitemodel_functionarg);
    }

}