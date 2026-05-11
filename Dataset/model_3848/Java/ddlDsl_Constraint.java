





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_Constraint extends TableProperty {






    private ddlDsl_AlterTableAction ddldsl_altertableaction;




    private ddlDsl_Column ddldsl_column;


    public ddlDsl_Constraint(
    ) {
        super(
        );
    }



    public ddlDsl_AlterTableAction getDdldsl_altertableaction() {
        return ddldsl_altertableaction;
    }

    public void setDdldsl_altertableaction(ddlDsl_AlterTableAction ddldsl_altertableaction) {
        this.ddldsl_altertableaction = ddldsl_altertableaction;
    }
    public ddlDsl_Column getDdldsl_column() {
        return ddldsl_column;
    }

    public void setDdldsl_column(ddlDsl_Column ddldsl_column) {
        this.ddldsl_column = ddldsl_column;
    }

}