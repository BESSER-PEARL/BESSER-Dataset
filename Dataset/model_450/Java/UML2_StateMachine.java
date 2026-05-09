





import java.util.List;
import java.util.ArrayList;

public class UML2_StateMachine extends Behavior {






    private List<UML2_Region> uml2_regions;




    private UML2_StateMachine uml2_statemachine;




    private UML2_BehavioredClassifier uml2_behavioredclassifier;




    private UML2_BehavioredClassifier uml2_behavioredclassifier;




    private UML2_Region uml2_region;




    private UML2_State uml2_state;


    public UML2_StateMachine(
    ) {
        super(
        );
        this.uml2_regions = new ArrayList<>();
    }

    public UML2_StateMachine(
        ArrayList<UML2_Region> uml2_regions    ) {
        this.uml2_regions = uml2_regions;
    }


    public List<UML2_Region> getUml2_regions() {
        return uml2_regions;
    }

    public void addUml2_region(Uml2_region uml2_region) {
        this.uml2_regions.add(uml2_region);
    }
    public UML2_StateMachine getUml2_statemachine() {
        return uml2_statemachine;
    }

    public void setUml2_statemachine(UML2_StateMachine uml2_statemachine) {
        this.uml2_statemachine = uml2_statemachine;
    }
    public UML2_BehavioredClassifier getUml2_behavioredclassifier() {
        return uml2_behavioredclassifier;
    }

    public void setUml2_behavioredclassifier(UML2_BehavioredClassifier uml2_behavioredclassifier) {
        this.uml2_behavioredclassifier = uml2_behavioredclassifier;
    }
    public UML2_BehavioredClassifier getUml2_behavioredclassifier() {
        return uml2_behavioredclassifier;
    }

    public void setUml2_behavioredclassifier(UML2_BehavioredClassifier uml2_behavioredclassifier) {
        this.uml2_behavioredclassifier = uml2_behavioredclassifier;
    }
    public UML2_Region getUml2_region() {
        return uml2_region;
    }

    public void setUml2_region(UML2_Region uml2_region) {
        this.uml2_region = uml2_region;
    }
    public UML2_State getUml2_state() {
        return uml2_state;
    }

    public void setUml2_state(UML2_State uml2_state) {
        this.uml2_state = uml2_state;
    }

}