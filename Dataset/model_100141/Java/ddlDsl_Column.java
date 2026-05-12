





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_Column extends TableProperty {

    private String default;
    private boolean sorted;





    private ddlDsl_ColumnComment ddldsl_columncomment;




    private ddlDsl_Constraint ddldsl_constraint;


    public ddlDsl_Column(
        String default,        boolean sorted    ) {
        super(
        );
        this.default = default;
        this.sorted = sorted;
    }


    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public boolean getSorted() {
        return sorted;
    }

    public void setSorted(boolean sorted) {
        this.sorted = sorted;
    }

    public ddlDsl_ColumnComment getDdldsl_columncomment() {
        return ddldsl_columncomment;
    }

    public void setDdldsl_columncomment(ddlDsl_ColumnComment ddldsl_columncomment) {
        this.ddldsl_columncomment = ddldsl_columncomment;
    }
    public ddlDsl_Constraint getDdldsl_constraint() {
        return ddldsl_constraint;
    }

    public void setDdldsl_constraint(ddlDsl_Constraint ddldsl_constraint) {
        this.ddldsl_constraint = ddldsl_constraint;
    }

}