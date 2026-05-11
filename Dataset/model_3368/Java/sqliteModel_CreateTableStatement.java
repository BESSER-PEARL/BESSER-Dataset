





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_CreateTableStatement extends TableDefinition {

    private boolean temporary;





    private List<sqliteModel_ColumnSource> sqlitemodel_columnsources;




    private List<sqliteModel_TableConstraint> sqlitemodel_tableconstraints;


    public sqliteModel_CreateTableStatement(
        boolean temporary    ) {
        super(
        );
        this.temporary = temporary;
        this.sqlitemodel_columnsources = new ArrayList<>();
        this.sqlitemodel_tableconstraints = new ArrayList<>();
    }

    public sqliteModel_CreateTableStatement(
        boolean temporary        ArrayList<sqliteModel_ColumnSource> sqlitemodel_columnsources,        ArrayList<sqliteModel_TableConstraint> sqlitemodel_tableconstraints    ) {
        this.temporary = temporary;
        this.sqlitemodel_columnsources = sqlitemodel_columnsources;
        this.sqlitemodel_tableconstraints = sqlitemodel_tableconstraints;
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
    public List<sqliteModel_TableConstraint> getSqlitemodel_tableconstraints() {
        return sqlitemodel_tableconstraints;
    }

    public void addSqlitemodel_tableconstraint(Sqlitemodel_tableconstraint sqlitemodel_tableconstraint) {
        this.sqlitemodel_tableconstraints.add(sqlitemodel_tableconstraint);
    }

}