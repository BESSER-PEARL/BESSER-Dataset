





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_StateMachine extends Behavior {






    private UML2WithID_BehavioredClassifier uml2withid_behavioredclassifier;




    private UML2WithID_StateMachine uml2withid_statemachine;




    private UML2WithID_BehavioredClassifier uml2withid_behavioredclassifier;




    private UML2WithID_State uml2withid_state;




    private List<UML2WithID_Pseudostate> uml2withid_pseudostates;




    private UML2WithID_Region uml2withid_region;




    private List<UML2WithID_Region> uml2withid_regions;


    public UML2WithID_StateMachine(
    ) {
        super(
        );
        this.uml2withid_pseudostates = new ArrayList<>();
        this.uml2withid_regions = new ArrayList<>();
    }

    public UML2WithID_StateMachine(
        ArrayList<UML2WithID_Pseudostate> uml2withid_pseudostates,        ArrayList<UML2WithID_Region> uml2withid_regions    ) {
        this.uml2withid_pseudostates = uml2withid_pseudostates;
        this.uml2withid_regions = uml2withid_regions;
    }


    public UML2WithID_BehavioredClassifier getUml2withid_behavioredclassifier() {
        return uml2withid_behavioredclassifier;
    }

    public void setUml2withid_behavioredclassifier(UML2WithID_BehavioredClassifier uml2withid_behavioredclassifier) {
        this.uml2withid_behavioredclassifier = uml2withid_behavioredclassifier;
    }
    public UML2WithID_StateMachine getUml2withid_statemachine() {
        return uml2withid_statemachine;
    }

    public void setUml2withid_statemachine(UML2WithID_StateMachine uml2withid_statemachine) {
        this.uml2withid_statemachine = uml2withid_statemachine;
    }
    public UML2WithID_BehavioredClassifier getUml2withid_behavioredclassifier() {
        return uml2withid_behavioredclassifier;
    }

    public void setUml2withid_behavioredclassifier(UML2WithID_BehavioredClassifier uml2withid_behavioredclassifier) {
        this.uml2withid_behavioredclassifier = uml2withid_behavioredclassifier;
    }
    public UML2WithID_State getUml2withid_state() {
        return uml2withid_state;
    }

    public void setUml2withid_state(UML2WithID_State uml2withid_state) {
        this.uml2withid_state = uml2withid_state;
    }
    public List<UML2WithID_Pseudostate> getUml2withid_pseudostates() {
        return uml2withid_pseudostates;
    }

    public void addUml2withid_pseudostate(Uml2withid_pseudostate uml2withid_pseudostate) {
        this.uml2withid_pseudostates.add(uml2withid_pseudostate);
    }
    public UML2WithID_Region getUml2withid_region() {
        return uml2withid_region;
    }

    public void setUml2withid_region(UML2WithID_Region uml2withid_region) {
        this.uml2withid_region = uml2withid_region;
    }
    public List<UML2WithID_Region> getUml2withid_regions() {
        return uml2withid_regions;
    }

    public void addUml2withid_region(Uml2withid_region uml2withid_region) {
        this.uml2withid_regions.add(uml2withid_region);
    }

}