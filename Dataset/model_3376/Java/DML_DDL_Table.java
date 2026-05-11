





import java.util.List;
import java.util.ArrayList;

public class DML_DDL_Table extends DataDefinition {

    private String commentTable;
    private String tableName;





    private DML_DDL_Pk dml_ddl_pk;




    private DML_DDL_Fk dml_ddl_fk;




    private List<DML_DDL_Fk> dml_ddl_fks;


    public DML_DDL_Table(
        String commentTable,        String tableName    ) {
        super(
        );
        this.commentTable = commentTable;
        this.tableName = tableName;
        this.dml_ddl_fks = new ArrayList<>();
    }

    public DML_DDL_Table(
        String commentTable,        String tableName        ArrayList<DML_DDL_Fk> dml_ddl_fks    ) {
        this.commentTable = commentTable;
        this.tableName = tableName;
        this.dml_ddl_fks = dml_ddl_fks;
    }

    public String getCommenttable() {
        return commentTable;
    }

    public void setCommenttable(String commentTable) {
        this.commentTable = commentTable;
    }
    public String getTablename() {
        return tableName;
    }

    public void setTablename(String tableName) {
        this.tableName = tableName;
    }

    public DML_DDL_Pk getDml_ddl_pk() {
        return dml_ddl_pk;
    }

    public void setDml_ddl_pk(DML_DDL_Pk dml_ddl_pk) {
        this.dml_ddl_pk = dml_ddl_pk;
    }
    public DML_DDL_Fk getDml_ddl_fk() {
        return dml_ddl_fk;
    }

    public void setDml_ddl_fk(DML_DDL_Fk dml_ddl_fk) {
        this.dml_ddl_fk = dml_ddl_fk;
    }
    public List<DML_DDL_Fk> getDml_ddl_fks() {
        return dml_ddl_fks;
    }

    public void addDml_ddl_fk(Dml_ddl_fk dml_ddl_fk) {
        this.dml_ddl_fks.add(dml_ddl_fk);
    }

}