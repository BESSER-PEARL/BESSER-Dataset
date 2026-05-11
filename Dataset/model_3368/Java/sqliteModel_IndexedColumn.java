





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_IndexedColumn  {

    private boolean asc;
    private boolean desc;
    private String collationName;





    private sqliteModel_CreateIndexStatement sqlitemodel_createindexstatement;


    public sqliteModel_IndexedColumn(
        boolean asc,        boolean desc,        String collationName    ) {
        this.asc = asc;
        this.desc = desc;
        this.collationName = collationName;
    }


    public boolean getAsc() {
        return asc;
    }

    public void setAsc(boolean asc) {
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

    public sqliteModel_CreateIndexStatement getSqlitemodel_createindexstatement() {
        return sqlitemodel_createindexstatement;
    }

    public void setSqlitemodel_createindexstatement(sqliteModel_CreateIndexStatement sqlitemodel_createindexstatement) {
        this.sqlitemodel_createindexstatement = sqlitemodel_createindexstatement;
    }

}