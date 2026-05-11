





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_UpdateStatement extends DMLStatement {

    private String conflictResolution;





    private sqliteModel_Expression sqlitemodel_expression;


    public sqliteModel_UpdateStatement(
        String conflictResolution    ) {
        super(
        );
        this.conflictResolution = conflictResolution;
    }


    public String getConflictresolution() {
        return conflictResolution;
    }

    public void setConflictresolution(String conflictResolution) {
        this.conflictResolution = conflictResolution;
    }

    public sqliteModel_Expression getSqlitemodel_expression() {
        return sqlitemodel_expression;
    }

    public void setSqlitemodel_expression(sqliteModel_Expression sqlitemodel_expression) {
        this.sqlitemodel_expression = sqlitemodel_expression;
    }

}