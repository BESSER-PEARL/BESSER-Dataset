





import java.util.List;
import java.util.ArrayList;

public class astm_sastm_RDBCheckConstraint extends RDBConstraint {

    private String RDBConstraintText;
    private String RDBConstraintType;



    public astm_sastm_RDBCheckConstraint(
        String RDBConstraintText,        String RDBConstraintType    ) {
        super(
        );
        this.RDBConstraintText = RDBConstraintText;
        this.RDBConstraintType = RDBConstraintType;
    }


    public String getRdbconstrainttext() {
        return RDBConstraintText;
    }

    public void setRdbconstrainttext(String RDBConstraintText) {
        this.RDBConstraintText = RDBConstraintText;
    }
    public String getRdbconstrainttype() {
        return RDBConstraintType;
    }

    public void setRdbconstrainttype(String RDBConstraintType) {
        this.RDBConstraintType = RDBConstraintType;
    }


}