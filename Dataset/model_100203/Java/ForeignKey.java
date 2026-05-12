





import java.util.List;
import java.util.ArrayList;

public class ForeignKey  {






    private sqlmodel_constraints_UniqueConstraint sqlmodel_constraints_uniqueconstraint;




    private sqlmodel_constraints_Index sqlmodel_constraints_index;




    private sqlmodel_tables_BaseTable sqlmodel_tables_basetable;


    public ForeignKey(
    ) {
    }



    public sqlmodel_constraints_UniqueConstraint getSqlmodel_constraints_uniqueconstraint() {
        return sqlmodel_constraints_uniqueconstraint;
    }

    public void setSqlmodel_constraints_uniqueconstraint(sqlmodel_constraints_UniqueConstraint sqlmodel_constraints_uniqueconstraint) {
        this.sqlmodel_constraints_uniqueconstraint = sqlmodel_constraints_uniqueconstraint;
    }
    public sqlmodel_constraints_Index getSqlmodel_constraints_index() {
        return sqlmodel_constraints_index;
    }

    public void setSqlmodel_constraints_index(sqlmodel_constraints_Index sqlmodel_constraints_index) {
        this.sqlmodel_constraints_index = sqlmodel_constraints_index;
    }
    public sqlmodel_tables_BaseTable getSqlmodel_tables_basetable() {
        return sqlmodel_tables_basetable;
    }

    public void setSqlmodel_tables_basetable(sqlmodel_tables_BaseTable sqlmodel_tables_basetable) {
        this.sqlmodel_tables_basetable = sqlmodel_tables_basetable;
    }

}