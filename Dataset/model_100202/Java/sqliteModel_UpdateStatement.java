





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_UpdateStatement extends DMLStatement {

    private String conflictResolution;





    private sqliteModel_TableDefinition sqlitemodel_tabledefinition;


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

    public sqliteModel_TableDefinition getSqlitemodel_tabledefinition() {
        return sqlitemodel_tabledefinition;
    }

    public void setSqlitemodel_tabledefinition(sqliteModel_TableDefinition sqlitemodel_tabledefinition) {
        this.sqlitemodel_tabledefinition = sqlitemodel_tabledefinition;
    }

}