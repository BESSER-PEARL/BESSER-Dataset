





import java.util.List;
import java.util.ArrayList;

public class SearchCondition  {






    private sqlmodel_tables_Trigger sqlmodel_tables_trigger;




    private sqlmodel_constraints_Assertion sqlmodel_constraints_assertion;


    public SearchCondition(
    ) {
    }



    public sqlmodel_tables_Trigger getSqlmodel_tables_trigger() {
        return sqlmodel_tables_trigger;
    }

    public void setSqlmodel_tables_trigger(sqlmodel_tables_Trigger sqlmodel_tables_trigger) {
        this.sqlmodel_tables_trigger = sqlmodel_tables_trigger;
    }
    public sqlmodel_constraints_Assertion getSqlmodel_constraints_assertion() {
        return sqlmodel_constraints_assertion;
    }

    public void setSqlmodel_constraints_assertion(sqlmodel_constraints_Assertion sqlmodel_constraints_assertion) {
        this.sqlmodel_constraints_assertion = sqlmodel_constraints_assertion;
    }

}