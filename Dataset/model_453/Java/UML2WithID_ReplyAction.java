





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_ReplyAction extends Action {






    private UML2WithID_InputPin uml2withid_inputpin;




    private List<UML2WithID_InputPin> uml2withid_inputpins;




    private UML2WithID_CallTrigger uml2withid_calltrigger;


    public UML2WithID_ReplyAction(
    ) {
        super(
        );
        this.uml2withid_inputpins = new ArrayList<>();
    }

    public UML2WithID_ReplyAction(
        ArrayList<UML2WithID_InputPin> uml2withid_inputpins    ) {
        this.uml2withid_inputpins = uml2withid_inputpins;
    }


    public UML2WithID_InputPin getUml2withid_inputpin() {
        return uml2withid_inputpin;
    }

    public void setUml2withid_inputpin(UML2WithID_InputPin uml2withid_inputpin) {
        this.uml2withid_inputpin = uml2withid_inputpin;
    }
    public List<UML2WithID_InputPin> getUml2withid_inputpins() {
        return uml2withid_inputpins;
    }

    public void addUml2withid_inputpin(Uml2withid_inputpin uml2withid_inputpin) {
        this.uml2withid_inputpins.add(uml2withid_inputpin);
    }
    public UML2WithID_CallTrigger getUml2withid_calltrigger() {
        return uml2withid_calltrigger;
    }

    public void setUml2withid_calltrigger(UML2WithID_CallTrigger uml2withid_calltrigger) {
        this.uml2withid_calltrigger = uml2withid_calltrigger;
    }

}