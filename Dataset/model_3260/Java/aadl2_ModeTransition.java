





import java.util.List;
import java.util.ArrayList;

public class aadl2_ModeTransition extends ModeFeature {






    private aadl2_Mode aadl2_mode;




    private List<aadl2_ModeTransitionTrigger> aadl2_modetransitiontriggers;




    private aadl2_ModalPath aadl2_modalpath;




    private aadl2_Mode aadl2_mode;


    public aadl2_ModeTransition(
    ) {
        super(
        );
        this.aadl2_modetransitiontriggers = new ArrayList<>();
    }

    public aadl2_ModeTransition(
        ArrayList<aadl2_ModeTransitionTrigger> aadl2_modetransitiontriggers    ) {
        this.aadl2_modetransitiontriggers = aadl2_modetransitiontriggers;
    }


    public aadl2_Mode getAadl2_mode() {
        return aadl2_mode;
    }

    public void setAadl2_mode(aadl2_Mode aadl2_mode) {
        this.aadl2_mode = aadl2_mode;
    }
    public List<aadl2_ModeTransitionTrigger> getAadl2_modetransitiontriggers() {
        return aadl2_modetransitiontriggers;
    }

    public void addAadl2_modetransitiontrigger(Aadl2_modetransitiontrigger aadl2_modetransitiontrigger) {
        this.aadl2_modetransitiontriggers.add(aadl2_modetransitiontrigger);
    }
    public aadl2_ModalPath getAadl2_modalpath() {
        return aadl2_modalpath;
    }

    public void setAadl2_modalpath(aadl2_ModalPath aadl2_modalpath) {
        this.aadl2_modalpath = aadl2_modalpath;
    }
    public aadl2_Mode getAadl2_mode() {
        return aadl2_mode;
    }

    public void setAadl2_mode(aadl2_Mode aadl2_mode) {
        this.aadl2_mode = aadl2_mode;
    }

}