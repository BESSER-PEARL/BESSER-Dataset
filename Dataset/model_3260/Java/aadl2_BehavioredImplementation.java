





import java.util.List;
import java.util.ArrayList;

public class aadl2_BehavioredImplementation extends ComponentImplementation {






    private List<aadl2_SubprogramCallSequence> aadl2_subprogramcallsequences;


    public aadl2_BehavioredImplementation(
    ) {
        super(
        );
        this.aadl2_subprogramcallsequences = new ArrayList<>();
    }

    public aadl2_BehavioredImplementation(
        ArrayList<aadl2_SubprogramCallSequence> aadl2_subprogramcallsequences    ) {
        this.aadl2_subprogramcallsequences = aadl2_subprogramcallsequences;
    }


    public List<aadl2_SubprogramCallSequence> getAadl2_subprogramcallsequences() {
        return aadl2_subprogramcallsequences;
    }

    public void addAadl2_subprogramcallsequence(Aadl2_subprogramcallsequence aadl2_subprogramcallsequence) {
        this.aadl2_subprogramcallsequences.add(aadl2_subprogramcallsequence);
    }

}