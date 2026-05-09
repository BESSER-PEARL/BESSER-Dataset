





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_CallAction extends InvocationAction {

    private boolean isSynchronous;





    private List<UML2WithID_OutputPin> uml2withid_outputpins;


    public UML2WithID_CallAction(
        boolean isSynchronous    ) {
        super(
        );
        this.isSynchronous = isSynchronous;
        this.uml2withid_outputpins = new ArrayList<>();
    }

    public UML2WithID_CallAction(
        boolean isSynchronous        ArrayList<UML2WithID_OutputPin> uml2withid_outputpins    ) {
        this.isSynchronous = isSynchronous;
        this.uml2withid_outputpins = uml2withid_outputpins;
    }

    public boolean getIssynchronous() {
        return isSynchronous;
    }

    public void setIssynchronous(boolean isSynchronous) {
        this.isSynchronous = isSynchronous;
    }

    public List<UML2WithID_OutputPin> getUml2withid_outputpins() {
        return uml2withid_outputpins;
    }

    public void addUml2withid_outputpin(Uml2withid_outputpin uml2withid_outputpin) {
        this.uml2withid_outputpins.add(uml2withid_outputpin);
    }

}