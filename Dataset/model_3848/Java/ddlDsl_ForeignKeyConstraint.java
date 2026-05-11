





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_ForeignKeyConstraint extends Constraint {






    private ddlDsl_ReferenceClause ddldsl_referenceclause;




    private List<ddlDsl_Column> ddldsl_columns;


    public ddlDsl_ForeignKeyConstraint(
    ) {
        super(
        );
        this.ddldsl_columns = new ArrayList<>();
    }

    public ddlDsl_ForeignKeyConstraint(
        ArrayList<ddlDsl_Column> ddldsl_columns    ) {
        this.ddldsl_columns = ddldsl_columns;
    }


    public ddlDsl_ReferenceClause getDdldsl_referenceclause() {
        return ddldsl_referenceclause;
    }

    public void setDdldsl_referenceclause(ddlDsl_ReferenceClause ddldsl_referenceclause) {
        this.ddldsl_referenceclause = ddldsl_referenceclause;
    }
    public List<ddlDsl_Column> getDdldsl_columns() {
        return ddldsl_columns;
    }

    public void addDdldsl_column(Ddldsl_column ddldsl_column) {
        this.ddldsl_columns.add(ddldsl_column);
    }

}