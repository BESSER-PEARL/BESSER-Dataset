





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_PrimaryKeyConstraint extends Constraint {






    private List<ddlDsl_Column> ddldsl_columns;


    public ddlDsl_PrimaryKeyConstraint(
    ) {
        super(
        );
        this.ddldsl_columns = new ArrayList<>();
    }

    public ddlDsl_PrimaryKeyConstraint(
        ArrayList<ddlDsl_Column> ddldsl_columns    ) {
        this.ddldsl_columns = ddldsl_columns;
    }


    public List<ddlDsl_Column> getDdldsl_columns() {
        return ddldsl_columns;
    }

    public void addDdldsl_column(Ddldsl_column ddldsl_column) {
        this.ddldsl_columns.add(ddldsl_column);
    }

}