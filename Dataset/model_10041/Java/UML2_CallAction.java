





import java.util.List;
import java.util.ArrayList;

public class UML2_CallAction extends InvocationAction {

    private boolean isSynchronous;





    private List<UML2_OutputPin> uml2_outputpins;


    public UML2_CallAction(
        boolean isSynchronous    ) {
        super(
        );
        this.isSynchronous = isSynchronous;
        this.uml2_outputpins = new ArrayList<>();
    }

    public UML2_CallAction(
        boolean isSynchronous        ArrayList<UML2_OutputPin> uml2_outputpins    ) {
        this.isSynchronous = isSynchronous;
        this.uml2_outputpins = uml2_outputpins;
    }

    public boolean getIssynchronous() {
        return isSynchronous;
    }

    public void setIssynchronous(boolean isSynchronous) {
        this.isSynchronous = isSynchronous;
    }

    public List<UML2_OutputPin> getUml2_outputpins() {
        return uml2_outputpins;
    }

    public void addUml2_outputpin(Uml2_outputpin uml2_outputpin) {
        this.uml2_outputpins.add(uml2_outputpin);
    }

}