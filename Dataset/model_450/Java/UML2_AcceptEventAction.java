





import java.util.List;
import java.util.ArrayList;

public class UML2_AcceptEventAction extends Action {






    private List<UML2_Trigger> uml2_triggers;




    private List<UML2_OutputPin> uml2_outputpins;


    public UML2_AcceptEventAction(
    ) {
        super(
        );
        this.uml2_triggers = new ArrayList<>();
        this.uml2_outputpins = new ArrayList<>();
    }

    public UML2_AcceptEventAction(
        ArrayList<UML2_Trigger> uml2_triggers,        ArrayList<UML2_OutputPin> uml2_outputpins    ) {
        this.uml2_triggers = uml2_triggers;
        this.uml2_outputpins = uml2_outputpins;
    }


    public List<UML2_Trigger> getUml2_triggers() {
        return uml2_triggers;
    }

    public void addUml2_trigger(Uml2_trigger uml2_trigger) {
        this.uml2_triggers.add(uml2_trigger);
    }
    public List<UML2_OutputPin> getUml2_outputpins() {
        return uml2_outputpins;
    }

    public void addUml2_outputpin(Uml2_outputpin uml2_outputpin) {
        this.uml2_outputpins.add(uml2_outputpin);
    }

}