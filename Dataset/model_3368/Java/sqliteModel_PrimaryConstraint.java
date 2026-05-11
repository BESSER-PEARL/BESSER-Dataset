





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_PrimaryConstraint extends TableConstraint {






    private List<sqliteModel_IndexedColumn> sqlitemodel_indexedcolumns;


    public sqliteModel_PrimaryConstraint(
    ) {
        super(
        );
        this.sqlitemodel_indexedcolumns = new ArrayList<>();
    }

    public sqliteModel_PrimaryConstraint(
        ArrayList<sqliteModel_IndexedColumn> sqlitemodel_indexedcolumns    ) {
        this.sqlitemodel_indexedcolumns = sqlitemodel_indexedcolumns;
    }


    public List<sqliteModel_IndexedColumn> getSqlitemodel_indexedcolumns() {
        return sqlitemodel_indexedcolumns;
    }

    public void addSqlitemodel_indexedcolumn(Sqlitemodel_indexedcolumn sqlitemodel_indexedcolumn) {
        this.sqlitemodel_indexedcolumns.add(sqlitemodel_indexedcolumn);
    }

}