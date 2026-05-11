





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_DropTableConstraint extends AlterTableAction {






    private ddlDsl_Constraint ddldsl_constraint;


    public ddlDsl_DropTableConstraint(
    ) {
        super(
        );
    }



    public ddlDsl_Constraint getDdldsl_constraint() {
        return ddldsl_constraint;
    }

    public void setDdldsl_constraint(ddlDsl_Constraint ddldsl_constraint) {
        this.ddldsl_constraint = ddldsl_constraint;
    }

}