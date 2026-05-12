





import java.util.List;
import java.util.ArrayList;

public class UML2_InvocationAction extends Action {






    private UML2_Port uml2_port;




    private List<UML2_InputPin> uml2_inputpins;


    public UML2_InvocationAction(
    ) {
        super(
        );
        this.uml2_inputpins = new ArrayList<>();
    }

    public UML2_InvocationAction(
        ArrayList<UML2_InputPin> uml2_inputpins    ) {
        this.uml2_inputpins = uml2_inputpins;
    }


    public UML2_Port getUml2_port() {
        return uml2_port;
    }

    public void setUml2_port(UML2_Port uml2_port) {
        this.uml2_port = uml2_port;
    }
    public List<UML2_InputPin> getUml2_inputpins() {
        return uml2_inputpins;
    }

    public void addUml2_inputpin(Uml2_inputpin uml2_inputpin) {
        this.uml2_inputpins.add(uml2_inputpin);
    }

}