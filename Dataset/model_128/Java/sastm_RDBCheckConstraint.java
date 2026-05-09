





import java.util.List;
import java.util.ArrayList;

public class sastm_RDBCheckConstraint extends RDBConstraint {

    private String RDBConstraintType;
    private String RDBConstraintText;



    public sastm_RDBCheckConstraint(
        String RDBConstraintType,        String RDBConstraintText    ) {
        super(
        );
        this.RDBConstraintType = RDBConstraintType;
        this.RDBConstraintText = RDBConstraintText;
    }


    public String getRdbconstrainttype() {
        return RDBConstraintType;
    }

    public void setRdbconstrainttype(String RDBConstraintType) {
        this.RDBConstraintType = RDBConstraintType;
    }
    public String getRdbconstrainttext() {
        return RDBConstraintText;
    }

    public void setRdbconstrainttext(String RDBConstraintText) {
        this.RDBConstraintText = RDBConstraintText;
    }


}