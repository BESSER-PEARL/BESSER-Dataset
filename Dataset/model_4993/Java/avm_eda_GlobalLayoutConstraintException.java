





import java.util.List;
import java.util.ArrayList;

public class avm_eda_GlobalLayoutConstraintException extends PcbLayoutConstraint {

    private String Constraint;



    public avm_eda_GlobalLayoutConstraintException(
        String Constraint    ) {
        super(
        );
        this.Constraint = Constraint;
    }


    public String getConstraint() {
        return Constraint;
    }

    public void setConstraint(String Constraint) {
        this.Constraint = Constraint;
    }


}