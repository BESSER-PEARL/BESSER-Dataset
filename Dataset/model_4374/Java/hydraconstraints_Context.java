





import java.util.List;
import java.util.ArrayList;

public class hydraconstraints_Context extends BoolOperandChoices, NumOperandChoices {






    private hydraconstraints_MultipleFeature hydraconstraints_multiplefeature;




    private hydraconstraints_Constraint hydraconstraints_constraint;


    public hydraconstraints_Context(
    ) {
        super(
        );
    }



    public hydraconstraints_MultipleFeature getHydraconstraints_multiplefeature() {
        return hydraconstraints_multiplefeature;
    }

    public void setHydraconstraints_multiplefeature(hydraconstraints_MultipleFeature hydraconstraints_multiplefeature) {
        this.hydraconstraints_multiplefeature = hydraconstraints_multiplefeature;
    }
    public hydraconstraints_Constraint getHydraconstraints_constraint() {
        return hydraconstraints_constraint;
    }

    public void setHydraconstraints_constraint(hydraconstraints_Constraint hydraconstraints_constraint) {
        this.hydraconstraints_constraint = hydraconstraints_constraint;
    }

}