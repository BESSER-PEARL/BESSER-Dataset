





import java.util.List;
import java.util.ArrayList;

public class DDL_CreateTable extends DataDefinition {

    private String tableName;
    private String commentTable;





    private DDL_CreatePk ddl_createpk;




    private List<DDL_CreateFk> ddl_createfks;




    private DDL_CreateFk ddl_createfk;


    public DDL_CreateTable(
        String tableName,        String commentTable    ) {
        super(
        );
        this.tableName = tableName;
        this.commentTable = commentTable;
        this.ddl_createfks = new ArrayList<>();
    }

    public DDL_CreateTable(
        String tableName,        String commentTable        ArrayList<DDL_CreateFk> ddl_createfks    ) {
        this.tableName = tableName;
        this.commentTable = commentTable;
        this.ddl_createfks = ddl_createfks;
    }

    public String getTablename() {
        return tableName;
    }

    public void setTablename(String tableName) {
        this.tableName = tableName;
    }
    public String getCommenttable() {
        return commentTable;
    }

    public void setCommenttable(String commentTable) {
        this.commentTable = commentTable;
    }

    public DDL_CreatePk getDdl_createpk() {
        return ddl_createpk;
    }

    public void setDdl_createpk(DDL_CreatePk ddl_createpk) {
        this.ddl_createpk = ddl_createpk;
    }
    public List<DDL_CreateFk> getDdl_createfks() {
        return ddl_createfks;
    }

    public void addDdl_createfk(Ddl_createfk ddl_createfk) {
        this.ddl_createfks.add(ddl_createfk);
    }
    public DDL_CreateFk getDdl_createfk() {
        return ddl_createfk;
    }

    public void setDdl_createfk(DDL_CreateFk ddl_createfk) {
        this.ddl_createfk = ddl_createfk;
    }

}