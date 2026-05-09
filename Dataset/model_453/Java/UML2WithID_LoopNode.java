





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_LoopNode extends StructuredActivityNode {

    private boolean isTestedFirst;





    private List<UML2WithID_ActivityNode> uml2withid_activitynodes;




    private UML2WithID_OutputPin uml2withid_outputpin;




    private List<UML2WithID_OutputPin> uml2withid_outputpins;




    private List<UML2WithID_ActivityNode> uml2withid_activitynodes;




    private List<UML2WithID_ActivityNode> uml2withid_activitynodes;




    private List<UML2WithID_OutputPin> uml2withid_outputpins;




    private List<UML2WithID_OutputPin> uml2withid_outputpins;




    private List<UML2WithID_InputPin> uml2withid_inputpins;


    public UML2WithID_LoopNode(
        boolean isTestedFirst    ) {
        super(
        );
        this.isTestedFirst = isTestedFirst;
        this.uml2withid_activitynodes = new ArrayList<>();
        this.uml2withid_outputpins = new ArrayList<>();
        this.uml2withid_activitynodes = new ArrayList<>();
        this.uml2withid_activitynodes = new ArrayList<>();
        this.uml2withid_outputpins = new ArrayList<>();
        this.uml2withid_outputpins = new ArrayList<>();
        this.uml2withid_inputpins = new ArrayList<>();
    }

    public UML2WithID_LoopNode(
        boolean isTestedFirst        ArrayList<UML2WithID_ActivityNode> uml2withid_activitynodes,        ArrayList<UML2WithID_OutputPin> uml2withid_outputpins,        ArrayList<UML2WithID_ActivityNode> uml2withid_activitynodes,        ArrayList<UML2WithID_ActivityNode> uml2withid_activitynodes,        ArrayList<UML2WithID_OutputPin> uml2withid_outputpins,        ArrayList<UML2WithID_OutputPin> uml2withid_outputpins,        ArrayList<UML2WithID_InputPin> uml2withid_inputpins    ) {
        this.isTestedFirst = isTestedFirst;
        this.uml2withid_activitynodes = uml2withid_activitynodes;
        this.uml2withid_outputpins = uml2withid_outputpins;
        this.uml2withid_activitynodes = uml2withid_activitynodes;
        this.uml2withid_activitynodes = uml2withid_activitynodes;
        this.uml2withid_outputpins = uml2withid_outputpins;
        this.uml2withid_outputpins = uml2withid_outputpins;
        this.uml2withid_inputpins = uml2withid_inputpins;
    }

    public boolean getIstestedfirst() {
        return isTestedFirst;
    }

    public void setIstestedfirst(boolean isTestedFirst) {
        this.isTestedFirst = isTestedFirst;
    }

    public List<UML2WithID_ActivityNode> getUml2withid_activitynodes() {
        return uml2withid_activitynodes;
    }

    public void addUml2withid_activitynode(Uml2withid_activitynode uml2withid_activitynode) {
        this.uml2withid_activitynodes.add(uml2withid_activitynode);
    }
    public UML2WithID_OutputPin getUml2withid_outputpin() {
        return uml2withid_outputpin;
    }

    public void setUml2withid_outputpin(UML2WithID_OutputPin uml2withid_outputpin) {
        this.uml2withid_outputpin = uml2withid_outputpin;
    }
    public List<UML2WithID_OutputPin> getUml2withid_outputpins() {
        return uml2withid_outputpins;
    }

    public void addUml2withid_outputpin(Uml2withid_outputpin uml2withid_outputpin) {
        this.uml2withid_outputpins.add(uml2withid_outputpin);
    }
    public List<UML2WithID_ActivityNode> getUml2withid_activitynodes() {
        return uml2withid_activitynodes;
    }

    public void addUml2withid_activitynode(Uml2withid_activitynode uml2withid_activitynode) {
        this.uml2withid_activitynodes.add(uml2withid_activitynode);
    }
    public List<UML2WithID_ActivityNode> getUml2withid_activitynodes() {
        return uml2withid_activitynodes;
    }

    public void addUml2withid_activitynode(Uml2withid_activitynode uml2withid_activitynode) {
        this.uml2withid_activitynodes.add(uml2withid_activitynode);
    }
    public List<UML2WithID_OutputPin> getUml2withid_outputpins() {
        return uml2withid_outputpins;
    }

    public void addUml2withid_outputpin(Uml2withid_outputpin uml2withid_outputpin) {
        this.uml2withid_outputpins.add(uml2withid_outputpin);
    }
    public List<UML2WithID_OutputPin> getUml2withid_outputpins() {
        return uml2withid_outputpins;
    }

    public void addUml2withid_outputpin(Uml2withid_outputpin uml2withid_outputpin) {
        this.uml2withid_outputpins.add(uml2withid_outputpin);
    }
    public List<UML2WithID_InputPin> getUml2withid_inputpins() {
        return uml2withid_inputpins;
    }

    public void addUml2withid_inputpin(Uml2withid_inputpin uml2withid_inputpin) {
        this.uml2withid_inputpins.add(uml2withid_inputpin);
    }

}