





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_ColumnDef extends ColumnSource {

    private String type;





    private List<sqliteModel_ColumnConstraint> sqlitemodel_columnconstraints;




    private sqliteModel_IndexedColumn sqlitemodel_indexedcolumn;




    private sqliteModel_InsertStatement sqlitemodel_insertstatement;


    public sqliteModel_ColumnDef(
        String type    ) {
        super(
        );
        this.type = type;
        this.sqlitemodel_columnconstraints = new ArrayList<>();
    }

    public sqliteModel_ColumnDef(
        String type        ArrayList<sqliteModel_ColumnConstraint> sqlitemodel_columnconstraints    ) {
        this.type = type;
        this.sqlitemodel_columnconstraints = sqlitemodel_columnconstraints;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<sqliteModel_ColumnConstraint> getSqlitemodel_columnconstraints() {
        return sqlitemodel_columnconstraints;
    }

    public void addSqlitemodel_columnconstraint(Sqlitemodel_columnconstraint sqlitemodel_columnconstraint) {
        this.sqlitemodel_columnconstraints.add(sqlitemodel_columnconstraint);
    }
    public sqliteModel_IndexedColumn getSqlitemodel_indexedcolumn() {
        return sqlitemodel_indexedcolumn;
    }

    public void setSqlitemodel_indexedcolumn(sqliteModel_IndexedColumn sqlitemodel_indexedcolumn) {
        this.sqlitemodel_indexedcolumn = sqlitemodel_indexedcolumn;
    }
    public sqliteModel_InsertStatement getSqlitemodel_insertstatement() {
        return sqlitemodel_insertstatement;
    }

    public void setSqlitemodel_insertstatement(sqliteModel_InsertStatement sqlitemodel_insertstatement) {
        this.sqlitemodel_insertstatement = sqlitemodel_insertstatement;
    }

}