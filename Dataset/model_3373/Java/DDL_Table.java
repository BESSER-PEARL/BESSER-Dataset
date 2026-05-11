





import java.util.List;
import java.util.ArrayList;

public class DDL_Table extends DataDefinition {

    private String commentTable;
    private String tableName;





    private DDL_Pk ddl_pk;




    private List<DDL_Fk> ddl_fks;




    private DDL_Fk ddl_fk;


    public DDL_Table(
        String commentTable,        String tableName    ) {
        super(
        );
        this.commentTable = commentTable;
        this.tableName = tableName;
        this.ddl_fks = new ArrayList<>();
    }

    public DDL_Table(
        String commentTable,        String tableName        ArrayList<DDL_Fk> ddl_fks    ) {
        this.commentTable = commentTable;
        this.tableName = tableName;
        this.ddl_fks = ddl_fks;
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

    public DDL_Pk getDdl_pk() {
        return ddl_pk;
    }

    public void setDdl_pk(DDL_Pk ddl_pk) {
        this.ddl_pk = ddl_pk;
    }
    public List<DDL_Fk> getDdl_fks() {
        return ddl_fks;
    }

    public void addDdl_fk(Ddl_fk ddl_fk) {
        this.ddl_fks.add(ddl_fk);
    }
    public DDL_Fk getDdl_fk() {
        return ddl_fk;
    }

    public void setDdl_fk(DDL_Fk ddl_fk) {
        this.ddl_fk = ddl_fk;
    }

}