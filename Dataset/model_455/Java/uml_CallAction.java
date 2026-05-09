





import java.util.List;
import java.util.ArrayList;

public class uml_CallAction extends InvocationAction {

    private String isSynchronous;





    private List<uml_OutputPin> uml_outputpins;


    public uml_CallAction(
        String isSynchronous    ) {
        super(
        );
        this.isSynchronous = isSynchronous;
        this.uml_outputpins = new ArrayList<>();
    }

    public uml_CallAction(
        String isSynchronous        ArrayList<uml_OutputPin> uml_outputpins    ) {
        this.isSynchronous = isSynchronous;
        this.uml_outputpins = uml_outputpins;
    }

    public String getIssynchronous() {
        return isSynchronous;
    }

    public void setIssynchronous(String isSynchronous) {
        this.isSynchronous = isSynchronous;
    }

    public List<uml_OutputPin> getUml_outputpins() {
        return uml_outputpins;
    }

    public void addUml_outputpin(Uml_outputpin uml_outputpin) {
        this.uml_outputpins.add(uml_outputpin);
    }

}