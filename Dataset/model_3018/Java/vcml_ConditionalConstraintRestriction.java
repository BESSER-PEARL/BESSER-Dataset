





import java.util.List;
import java.util.ArrayList;

public class vcml_ConditionalConstraintRestriction extends ConstraintRestriction {






    private vcml_ConstraintRestriction vcml_constraintrestriction;




    private vcml_Condition vcml_condition;


    public vcml_ConditionalConstraintRestriction(
    ) {
        super(
        );
    }



    public vcml_ConstraintRestriction getVcml_constraintrestriction() {
        return vcml_constraintrestriction;
    }

    public void setVcml_constraintrestriction(vcml_ConstraintRestriction vcml_constraintrestriction) {
        this.vcml_constraintrestriction = vcml_constraintrestriction;
    }
    public vcml_Condition getVcml_condition() {
        return vcml_condition;
    }

    public void setVcml_condition(vcml_Condition vcml_condition) {
        this.vcml_condition = vcml_condition;
    }

}