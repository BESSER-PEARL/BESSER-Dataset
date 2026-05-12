





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_IndexedColumn  {

    private boolean desc;
    private boolean asc;
    private String collationName;





    private sqliteModel_PrimaryConstraint sqlitemodel_primaryconstraint;




    private sqliteModel_CreateIndexStatement sqlitemodel_createindexstatement;


    public sqliteModel_IndexedColumn(
        boolean desc,        boolean asc,        String collationName    ) {
        this.desc = desc;
        this.asc = asc;
        this.collationName = collationName;
    }


    public boolean getDesc() {
        return desc;
    }

    public void setDesc(boolean desc) {
        this.desc = desc;
    }
    public boolean getAsc() {
        return asc;
    }

    public void setAsc(boolean asc) {
        this.asc = asc;
    }
    public String getCollationname() {
        return collationName;
    }

    public void setCollationname(String collationName) {
        this.collationName = collationName;
    }

    public sqliteModel_PrimaryConstraint getSqlitemodel_primaryconstraint() {
        return sqlitemodel_primaryconstraint;
    }

    public void setSqlitemodel_primaryconstraint(sqliteModel_PrimaryConstraint sqlitemodel_primaryconstraint) {
        this.sqlitemodel_primaryconstraint = sqlitemodel_primaryconstraint;
    }
    public sqliteModel_CreateIndexStatement getSqlitemodel_createindexstatement() {
        return sqlitemodel_createindexstatement;
    }

    public void setSqlitemodel_createindexstatement(sqliteModel_CreateIndexStatement sqlitemodel_createindexstatement) {
        this.sqlitemodel_createindexstatement = sqlitemodel_createindexstatement;
    }

}