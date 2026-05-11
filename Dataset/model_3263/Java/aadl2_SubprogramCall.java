





import java.util.List;
import java.util.ArrayList;

public class aadl2_SubprogramCall extends Context, BehavioralFeature {






    private aadl2_CalledSubprogram aadl2_calledsubprogram;




    private aadl2_SubprogramCallSequence aadl2_subprogramcallsequence;


    public aadl2_SubprogramCall(
    ) {
        super(
        );
    }



    public aadl2_CalledSubprogram getAadl2_calledsubprogram() {
        return aadl2_calledsubprogram;
    }

    public void setAadl2_calledsubprogram(aadl2_CalledSubprogram aadl2_calledsubprogram) {
        this.aadl2_calledsubprogram = aadl2_calledsubprogram;
    }
    public aadl2_SubprogramCallSequence getAadl2_subprogramcallsequence() {
        return aadl2_subprogramcallsequence;
    }

    public void setAadl2_subprogramcallsequence(aadl2_SubprogramCallSequence aadl2_subprogramcallsequence) {
        this.aadl2_subprogramcallsequence = aadl2_subprogramcallsequence;
    }

}