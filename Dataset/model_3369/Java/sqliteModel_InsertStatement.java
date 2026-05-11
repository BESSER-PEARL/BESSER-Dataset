





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_InsertStatement extends DMLStatement {

    private String conflictResolution;





    private sqliteModel_SelectStatement sqlitemodel_selectstatement;




    private List<sqliteModel_Expression> sqlitemodel_expressions;


    public sqliteModel_InsertStatement(
        String conflictResolution    ) {
        super(
        );
        this.conflictResolution = conflictResolution;
        this.sqlitemodel_expressions = new ArrayList<>();
    }

    public sqliteModel_InsertStatement(
        String conflictResolution        ArrayList<sqliteModel_Expression> sqlitemodel_expressions    ) {
        this.conflictResolution = conflictResolution;
        this.sqlitemodel_expressions = sqlitemodel_expressions;
    }

    public String getConflictresolution() {
        return conflictResolution;
    }

    public void setConflictresolution(String conflictResolution) {
        this.conflictResolution = conflictResolution;
    }

    public sqliteModel_SelectStatement getSqlitemodel_selectstatement() {
        return sqlitemodel_selectstatement;
    }

    public void setSqlitemodel_selectstatement(sqliteModel_SelectStatement sqlitemodel_selectstatement) {
        this.sqlitemodel_selectstatement = sqlitemodel_selectstatement;
    }
    public List<sqliteModel_Expression> getSqlitemodel_expressions() {
        return sqlitemodel_expressions;
    }

    public void addSqlitemodel_expression(Sqlitemodel_expression sqlitemodel_expression) {
        this.sqlitemodel_expressions.add(sqlitemodel_expression);
    }

}