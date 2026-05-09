





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_State extends Namespace, Vertex, RedefinableElement {

    private String isSimple;
    private String isOrthogonal;
    private String isComposite;
    private String isSubmachineState;





    private uml3_0_0_State uml3_0_0_state;




    private List<uml3_0_0_Region> uml3_0_0_regions;




    private uml3_0_0_Region uml3_0_0_region;


    public uml3_0_0_State(
        String isSimple,        String isOrthogonal,        String isComposite,        String isSubmachineState    ) {
        super(
        );
        this.isSimple = isSimple;
        this.isOrthogonal = isOrthogonal;
        this.isComposite = isComposite;
        this.isSubmachineState = isSubmachineState;
        this.uml3_0_0_regions = new ArrayList<>();
    }

    public uml3_0_0_State(
        String isSimple,        String isOrthogonal,        String isComposite,        String isSubmachineState        ArrayList<uml3_0_0_Region> uml3_0_0_regions    ) {
        this.isSimple = isSimple;
        this.isOrthogonal = isOrthogonal;
        this.isComposite = isComposite;
        this.isSubmachineState = isSubmachineState;
        this.uml3_0_0_regions = uml3_0_0_regions;
    }

    public String getIssimple() {
        return isSimple;
    }

    public void setIssimple(String isSimple) {
        this.isSimple = isSimple;
    }
    public String getIsorthogonal() {
        return isOrthogonal;
    }

    public void setIsorthogonal(String isOrthogonal) {
        this.isOrthogonal = isOrthogonal;
    }
    public String getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(String isComposite) {
        this.isComposite = isComposite;
    }
    public String getIssubmachinestate() {
        return isSubmachineState;
    }

    public void setIssubmachinestate(String isSubmachineState) {
        this.isSubmachineState = isSubmachineState;
    }

    public uml3_0_0_State getUml3_0_0_state() {
        return uml3_0_0_state;
    }

    public void setUml3_0_0_state(uml3_0_0_State uml3_0_0_state) {
        this.uml3_0_0_state = uml3_0_0_state;
    }
    public List<uml3_0_0_Region> getUml3_0_0_regions() {
        return uml3_0_0_regions;
    }

    public void addUml3_0_0_region(Uml3_0_0_region uml3_0_0_region) {
        this.uml3_0_0_regions.add(uml3_0_0_region);
    }
    public uml3_0_0_Region getUml3_0_0_region() {
        return uml3_0_0_region;
    }

    public void setUml3_0_0_region(uml3_0_0_Region uml3_0_0_region) {
        this.uml3_0_0_region = uml3_0_0_region;
    }

}