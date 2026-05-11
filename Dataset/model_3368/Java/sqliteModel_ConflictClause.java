





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_ConflictClause  {

    private String resolution;





    private sqliteModel_UniqueTableConstraint sqlitemodel_uniquetableconstraint;




    private sqliteModel_PrimaryConstraint sqlitemodel_primaryconstraint;


    public sqliteModel_ConflictClause(
        String resolution    ) {
        this.resolution = resolution;
    }


    public String getResolution() {
        return resolution;
    }

    public void setResolution(String resolution) {
        this.resolution = resolution;
    }

    public sqliteModel_UniqueTableConstraint getSqlitemodel_uniquetableconstraint() {
        return sqlitemodel_uniquetableconstraint;
    }

    public void setSqlitemodel_uniquetableconstraint(sqliteModel_UniqueTableConstraint sqlitemodel_uniquetableconstraint) {
        this.sqlitemodel_uniquetableconstraint = sqlitemodel_uniquetableconstraint;
    }
    public sqliteModel_PrimaryConstraint getSqlitemodel_primaryconstraint() {
        return sqlitemodel_primaryconstraint;
    }

    public void setSqlitemodel_primaryconstraint(sqliteModel_PrimaryConstraint sqlitemodel_primaryconstraint) {
        this.sqlitemodel_primaryconstraint = sqlitemodel_primaryconstraint;
    }

}