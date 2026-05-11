





import java.util.List;
import java.util.ArrayList;

public class aadl2_SubprogramCallSequence extends ModalElement, BehavioralFeature {






    private List<aadl2_SubprogramCall> aadl2_subprogramcalls;


    public aadl2_SubprogramCallSequence(
    ) {
        super(
        );
        this.aadl2_subprogramcalls = new ArrayList<>();
    }

    public aadl2_SubprogramCallSequence(
        ArrayList<aadl2_SubprogramCall> aadl2_subprogramcalls    ) {
        this.aadl2_subprogramcalls = aadl2_subprogramcalls;
    }


    public List<aadl2_SubprogramCall> getAadl2_subprogramcalls() {
        return aadl2_subprogramcalls;
    }

    public void addAadl2_subprogramcall(Aadl2_subprogramcall aadl2_subprogramcall) {
        this.aadl2_subprogramcalls.add(aadl2_subprogramcall);
    }

}