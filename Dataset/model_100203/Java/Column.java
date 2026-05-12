





import java.util.List;
import java.util.ArrayList;

public class Column  {






    private sqlmodel_constraints_IndexMember sqlmodel_constraints_indexmember;




    private sqlmodel_tables_Table sqlmodel_tables_table;




    private sqlmodel_tables_Trigger sqlmodel_tables_trigger;




    private sqlmodel_constraints_ReferenceConstraint sqlmodel_constraints_referenceconstraint;


    public Column(
    ) {
    }



    public sqlmodel_constraints_IndexMember getSqlmodel_constraints_indexmember() {
        return sqlmodel_constraints_indexmember;
    }

    public void setSqlmodel_constraints_indexmember(sqlmodel_constraints_IndexMember sqlmodel_constraints_indexmember) {
        this.sqlmodel_constraints_indexmember = sqlmodel_constraints_indexmember;
    }
    public sqlmodel_tables_Table getSqlmodel_tables_table() {
        return sqlmodel_tables_table;
    }

    public void setSqlmodel_tables_table(sqlmodel_tables_Table sqlmodel_tables_table) {
        this.sqlmodel_tables_table = sqlmodel_tables_table;
    }
    public sqlmodel_tables_Trigger getSqlmodel_tables_trigger() {
        return sqlmodel_tables_trigger;
    }

    public void setSqlmodel_tables_trigger(sqlmodel_tables_Trigger sqlmodel_tables_trigger) {
        this.sqlmodel_tables_trigger = sqlmodel_tables_trigger;
    }
    public sqlmodel_constraints_ReferenceConstraint getSqlmodel_constraints_referenceconstraint() {
        return sqlmodel_constraints_referenceconstraint;
    }

    public void setSqlmodel_constraints_referenceconstraint(sqlmodel_constraints_ReferenceConstraint sqlmodel_constraints_referenceconstraint) {
        this.sqlmodel_constraints_referenceconstraint = sqlmodel_constraints_referenceconstraint;
    }

}