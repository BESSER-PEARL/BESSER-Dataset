





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_State extends Vertex, RedefinableElement, Namespace {

    private boolean isComposite;
    private boolean isSubmachineState;
    private boolean isSimple;
    private boolean isOrthogonal;





    private UML2WithID_State uml2withid_state;




    private UML2WithID_Region uml2withid_region;




    private List<UML2WithID_Region> uml2withid_regions;


    public UML2WithID_State(
        boolean isComposite,        boolean isSubmachineState,        boolean isSimple,        boolean isOrthogonal    ) {
        super(
        );
        this.isComposite = isComposite;
        this.isSubmachineState = isSubmachineState;
        this.isSimple = isSimple;
        this.isOrthogonal = isOrthogonal;
        this.uml2withid_regions = new ArrayList<>();
    }

    public UML2WithID_State(
        boolean isComposite,        boolean isSubmachineState,        boolean isSimple,        boolean isOrthogonal        ArrayList<UML2WithID_Region> uml2withid_regions    ) {
        this.isComposite = isComposite;
        this.isSubmachineState = isSubmachineState;
        this.isSimple = isSimple;
        this.isOrthogonal = isOrthogonal;
        this.uml2withid_regions = uml2withid_regions;
    }

    public boolean getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(boolean isComposite) {
        this.isComposite = isComposite;
    }
    public boolean getIssubmachinestate() {
        return isSubmachineState;
    }

    public void setIssubmachinestate(boolean isSubmachineState) {
        this.isSubmachineState = isSubmachineState;
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

    public UML2WithID_State getUml2withid_state() {
        return uml2withid_state;
    }

    public void setUml2withid_state(UML2WithID_State uml2withid_state) {
        this.uml2withid_state = uml2withid_state;
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