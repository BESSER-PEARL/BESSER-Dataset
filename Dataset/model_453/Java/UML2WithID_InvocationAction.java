





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_InvocationAction extends Action {






    private UML2WithID_Port uml2withid_port;




    private List<UML2WithID_InputPin> uml2withid_inputpins;


    public UML2WithID_InvocationAction(
    ) {
        super(
        );
        this.uml2withid_inputpins = new ArrayList<>();
    }

    public UML2WithID_InvocationAction(
        ArrayList<UML2WithID_InputPin> uml2withid_inputpins    ) {
        this.uml2withid_inputpins = uml2withid_inputpins;
    }


    public UML2WithID_Port getUml2withid_port() {
        return uml2withid_port;
    }

    public void setUml2withid_port(UML2WithID_Port uml2withid_port) {
        this.uml2withid_port = uml2withid_port;
    }
    public List<UML2WithID_InputPin> getUml2withid_inputpins() {
        return uml2withid_inputpins;
    }

    public void addUml2withid_inputpin(Uml2withid_inputpin uml2withid_inputpin) {
        this.uml2withid_inputpins.add(uml2withid_inputpin);
    }

}