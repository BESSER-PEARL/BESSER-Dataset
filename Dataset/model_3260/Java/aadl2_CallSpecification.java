





import java.util.List;
import java.util.ArrayList;

public class aadl2_CallSpecification extends BehavioralFeature {






    private aadl2_SubprogramCallSequence aadl2_subprogramcallsequence;




    private aadl2_BehavioredImplementation aadl2_behavioredimplementation;


    public aadl2_CallSpecification(
    ) {
        super(
        );
    }



    public aadl2_SubprogramCallSequence getAadl2_subprogramcallsequence() {
        return aadl2_subprogramcallsequence;
    }

    public void setAadl2_subprogramcallsequence(aadl2_SubprogramCallSequence aadl2_subprogramcallsequence) {
        this.aadl2_subprogramcallsequence = aadl2_subprogramcallsequence;
    }
    public aadl2_BehavioredImplementation getAadl2_behavioredimplementation() {
        return aadl2_behavioredimplementation;
    }

    public void setAadl2_behavioredimplementation(aadl2_BehavioredImplementation aadl2_behavioredimplementation) {
        this.aadl2_behavioredimplementation = aadl2_behavioredimplementation;
    }

}