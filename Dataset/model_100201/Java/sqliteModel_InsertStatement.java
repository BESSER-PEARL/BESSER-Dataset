





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_InsertStatement extends DMLStatement {

    private String conflictResolution;





    private sqliteModel_SelectStatement sqlitemodel_selectstatement;


    public sqliteModel_InsertStatement(
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

    public sqliteModel_SelectStatement getSqlitemodel_selectstatement() {
        return sqlitemodel_selectstatement;
    }

    public void setSqlitemodel_selectstatement(sqliteModel_SelectStatement sqlitemodel_selectstatement) {
        this.sqlitemodel_selectstatement = sqlitemodel_selectstatement;
    }

}