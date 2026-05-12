





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_InsertStatement extends DMLStatement {

    private String conflictResolution;





    private List<sqliteModel_ColumnDef> sqlitemodel_columndefs;




    private sqliteModel_TableDefinition sqlitemodel_tabledefinition;


    public sqliteModel_InsertStatement(
        String conflictResolution    ) {
        super(
        );
        this.conflictResolution = conflictResolution;
        this.sqlitemodel_columndefs = new ArrayList<>();
    }

    public sqliteModel_InsertStatement(
        String conflictResolution        ArrayList<sqliteModel_ColumnDef> sqlitemodel_columndefs    ) {
        this.conflictResolution = conflictResolution;
        this.sqlitemodel_columndefs = sqlitemodel_columndefs;
    }

    public String getConflictresolution() {
        return conflictResolution;
    }

    public void setConflictresolution(String conflictResolution) {
        this.conflictResolution = conflictResolution;
    }

    public List<sqliteModel_ColumnDef> getSqlitemodel_columndefs() {
        return sqlitemodel_columndefs;
    }

    public void addSqlitemodel_columndef(Sqlitemodel_columndef sqlitemodel_columndef) {
        this.sqlitemodel_columndefs.add(sqlitemodel_columndef);
    }
    public sqliteModel_TableDefinition getSqlitemodel_tabledefinition() {
        return sqlitemodel_tabledefinition;
    }

    public void setSqlitemodel_tabledefinition(sqliteModel_TableDefinition sqlitemodel_tabledefinition) {
        this.sqlitemodel_tabledefinition = sqlitemodel_tabledefinition;
    }

}