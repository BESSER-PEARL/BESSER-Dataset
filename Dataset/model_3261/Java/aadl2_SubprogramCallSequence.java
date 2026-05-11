





import java.util.List;
import java.util.ArrayList;

public class aadl2_SubprogramCallSequence extends ModalElement, BehavioralFeature {






    private aadl2_BehavioredImplementation aadl2_behavioredimplementation;




    private List<aadl2_CallSpecification> aadl2_callspecifications;


    public aadl2_SubprogramCallSequence(
    ) {
        super(
        );
        this.aadl2_callspecifications = new ArrayList<>();
    }

    public aadl2_SubprogramCallSequence(
        ArrayList<aadl2_CallSpecification> aadl2_callspecifications    ) {
        this.aadl2_callspecifications = aadl2_callspecifications;
    }


    public aadl2_BehavioredImplementation getAadl2_behavioredimplementation() {
        return aadl2_behavioredimplementation;
    }

    public void setAadl2_behavioredimplementation(aadl2_BehavioredImplementation aadl2_behavioredimplementation) {
        this.aadl2_behavioredimplementation = aadl2_behavioredimplementation;
    }
    public List<aadl2_CallSpecification> getAadl2_callspecifications() {
        return aadl2_callspecifications;
    }

    public void addAadl2_callspecification(Aadl2_callspecification aadl2_callspecification) {
        this.aadl2_callspecifications.add(aadl2_callspecification);
    }

}