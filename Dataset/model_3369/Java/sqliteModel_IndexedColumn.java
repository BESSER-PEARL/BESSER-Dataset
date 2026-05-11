





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_IndexedColumn  {

    private boolean desc;
    private String collationName;
    private boolean asc;





    private sqliteModel_ColumnDef sqlitemodel_columndef;




    private sqliteModel_CreateIndexStatement sqlitemodel_createindexstatement;


    public sqliteModel_IndexedColumn(
        boolean desc,        String collationName,        boolean asc    ) {
        this.desc = desc;
        this.collationName = collationName;
        this.asc = asc;
    }


    public boolean getDesc() {
        return desc;
    }

    public void setDesc(boolean desc) {
        this.desc = desc;
    }
    public String getCollationname() {
        return collationName;
    }

    public void setCollationname(String collationName) {
        this.collationName = collationName;
    }
    public boolean getAsc() {
        return asc;
    }

    public void setAsc(boolean asc) {
        this.asc = asc;
    }

    public sqliteModel_ColumnDef getSqlitemodel_columndef() {
        return sqlitemodel_columndef;
    }

    public void setSqlitemodel_columndef(sqliteModel_ColumnDef sqlitemodel_columndef) {
        this.sqlitemodel_columndef = sqlitemodel_columndef;
    }
    public sqliteModel_CreateIndexStatement getSqlitemodel_createindexstatement() {
        return sqlitemodel_createindexstatement;
    }

    public void setSqlitemodel_createindexstatement(sqliteModel_CreateIndexStatement sqlitemodel_createindexstatement) {
        this.sqlitemodel_createindexstatement = sqlitemodel_createindexstatement;
    }

}