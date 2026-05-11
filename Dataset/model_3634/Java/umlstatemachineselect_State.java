





import java.util.List;
import java.util.ArrayList;

public class umlstatemachineselect_State extends Vertex {

    private boolean isComposite;
    private boolean isSimple;
    private boolean isOrthogonal;
    private boolean isSubmachineState;





    private umlstatemachineselect_StateMachine umlstatemachineselect_statemachine;




    private umlstatemachineselect_StateMachine umlstatemachineselect_statemachine;




    private umlstatemachineselect_Region umlstatemachineselect_region;




    private List<umlstatemachineselect_Region> umlstatemachineselect_regions;


    public umlstatemachineselect_State(
        boolean isComposite,        boolean isSimple,        boolean isOrthogonal,        boolean isSubmachineState    ) {
        super(
        );
        this.isComposite = isComposite;
        this.isSimple = isSimple;
        this.isOrthogonal = isOrthogonal;
        this.isSubmachineState = isSubmachineState;
        this.umlstatemachineselect_regions = new ArrayList<>();
    }

    public umlstatemachineselect_State(
        boolean isComposite,        boolean isSimple,        boolean isOrthogonal,        boolean isSubmachineState        ArrayList<umlstatemachineselect_Region> umlstatemachineselect_regions    ) {
        this.isComposite = isComposite;
        this.isSimple = isSimple;
        this.isOrthogonal = isOrthogonal;
        this.isSubmachineState = isSubmachineState;
        this.umlstatemachineselect_regions = umlstatemachineselect_regions;
    }

    public boolean getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(boolean isComposite) {
        this.isComposite = isComposite;
    }
    public boolean getIssimple() {
        return isSimple;
    }

    public void setIssimple(boolean isSimple) {
        this.isSimple = isSimple;
    }
    public boolean getIsorthogonal() {
        return isOrthogonal;
    }

    public void setIsorthogonal(boolean isOrthogonal) {
        this.isOrthogonal = isOrthogonal;
    }
    public boolean getIssubmachinestate() {
        return isSubmachineState;
    }

    public void setIssubmachinestate(boolean isSubmachineState) {
        this.isSubmachineState = isSubmachineState;
    }

    public umlstatemachineselect_StateMachine getUmlstatemachineselect_statemachine() {
        return umlstatemachineselect_statemachine;
    }

    public void setUmlstatemachineselect_statemachine(umlstatemachineselect_StateMachine umlstatemachineselect_statemachine) {
        this.umlstatemachineselect_statemachine = umlstatemachineselect_statemachine;
    }
    public umlstatemachineselect_StateMachine getUmlstatemachineselect_statemachine() {
        return umlstatemachineselect_statemachine;
    }

    public void setUmlstatemachineselect_statemachine(umlstatemachineselect_StateMachine umlstatemachineselect_statemachine) {
        this.umlstatemachineselect_statemachine = umlstatemachineselect_statemachine;
    }
    public umlstatemachineselect_Region getUmlstatemachineselect_region() {
        return umlstatemachineselect_region;
    }

    public void setUmlstatemachineselect_region(umlstatemachineselect_Region umlstatemachineselect_region) {
        this.umlstatemachineselect_region = umlstatemachineselect_region;
    }
    public List<umlstatemachineselect_Region> getUmlstatemachineselect_regions() {
        return umlstatemachineselect_regions;
    }

    public void addUmlstatemachineselect_region(Umlstatemachineselect_region umlstatemachineselect_region) {
        this.umlstatemachineselect_regions.add(umlstatemachineselect_region);
    }

}