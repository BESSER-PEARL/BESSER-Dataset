





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_CreateTableStatement extends TableDefinition {

    private boolean temporary;





    private List<sqliteModel_ColumnSource> sqlitemodel_columnsources;


    public sqliteModel_CreateTableStatement(
        boolean temporary    ) {
        super(
        );
        this.temporary = temporary;
        this.sqlitemodel_columnsources = new ArrayList<>();
    }

    public sqliteModel_CreateTableStatement(
        boolean temporary        ArrayList<sqliteModel_ColumnSource> sqlitemodel_columnsources    ) {
        this.temporary = temporary;
        this.sqlitemodel_columnsources = sqlitemodel_columnsources;
    }

    public boolean getTemporary() {
        return temporary;
    }

    public void setTemporary(boolean temporary) {
        this.temporary = temporary;
    }

    public List<sqliteModel_ColumnSource> getSqlitemodel_columnsources() {
        return sqlitemodel_columnsources;
    }

    public void addSqlitemodel_columnsource(Sqlitemodel_columnsource sqlitemodel_columnsource) {
        this.sqlitemodel_columnsources.add(sqlitemodel_columnsource);
    }

}