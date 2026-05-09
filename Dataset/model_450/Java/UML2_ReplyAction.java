





import java.util.List;
import java.util.ArrayList;

public class UML2_ReplyAction extends Action {






    private UML2_InputPin uml2_inputpin;




    private UML2_CallTrigger uml2_calltrigger;




    private List<UML2_InputPin> uml2_inputpins;


    public UML2_ReplyAction(
    ) {
        super(
        );
        this.uml2_inputpins = new ArrayList<>();
    }

    public UML2_ReplyAction(
        ArrayList<UML2_InputPin> uml2_inputpins    ) {
        this.uml2_inputpins = uml2_inputpins;
    }


    public UML2_InputPin getUml2_inputpin() {
        return uml2_inputpin;
    }

    public void setUml2_inputpin(UML2_InputPin uml2_inputpin) {
        this.uml2_inputpin = uml2_inputpin;
    }
    public UML2_CallTrigger getUml2_calltrigger() {
        return uml2_calltrigger;
    }

    public void setUml2_calltrigger(UML2_CallTrigger uml2_calltrigger) {
        this.uml2_calltrigger = uml2_calltrigger;
    }
    public List<UML2_InputPin> getUml2_inputpins() {
        return uml2_inputpins;
    }

    public void addUml2_inputpin(Uml2_inputpin uml2_inputpin) {
        this.uml2_inputpins.add(uml2_inputpin);
    }

}