





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_IndexedColumn  {

    private boolean desc;
    private String collationName;
    private boolean asc;





    private sqliteModel_PrimaryConstraint sqlitemodel_primaryconstraint;




    private sqliteModel_UniqueTableConstraint sqlitemodel_uniquetableconstraint;




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

    public sqliteModel_PrimaryConstraint getSqlitemodel_primaryconstraint() {
        return sqlitemodel_primaryconstraint;
    }

    public void setSqlitemodel_primaryconstraint(sqliteModel_PrimaryConstraint sqlitemodel_primaryconstraint) {
        this.sqlitemodel_primaryconstraint = sqlitemodel_primaryconstraint;
    }
    public sqliteModel_UniqueTableConstraint getSqlitemodel_uniquetableconstraint() {
        return sqlitemodel_uniquetableconstraint;
    }

    public void setSqlitemodel_uniquetableconstraint(sqliteModel_UniqueTableConstraint sqlitemodel_uniquetableconstraint) {
        this.sqlitemodel_uniquetableconstraint = sqlitemodel_uniquetableconstraint;
    }
    public sqliteModel_CreateIndexStatement getSqlitemodel_createindexstatement() {
        return sqlitemodel_createindexstatement;
    }

    public void setSqlitemodel_createindexstatement(sqliteModel_CreateIndexStatement sqlitemodel_createindexstatement) {
        this.sqlitemodel_createindexstatement = sqlitemodel_createindexstatement;
    }

}