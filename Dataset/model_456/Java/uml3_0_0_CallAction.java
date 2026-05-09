





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_CallAction extends InvocationAction {

    private String isSynchronous;





    private List<uml3_0_0_OutputPin> uml3_0_0_outputpins;


    public uml3_0_0_CallAction(
        String isSynchronous    ) {
        super(
        );
        this.isSynchronous = isSynchronous;
        this.uml3_0_0_outputpins = new ArrayList<>();
    }

    public uml3_0_0_CallAction(
        String isSynchronous        ArrayList<uml3_0_0_OutputPin> uml3_0_0_outputpins    ) {
        this.isSynchronous = isSynchronous;
        this.uml3_0_0_outputpins = uml3_0_0_outputpins;
    }

    public String getIssynchronous() {
        return isSynchronous;
    }

    public void setIssynchronous(String isSynchronous) {
        this.isSynchronous = isSynchronous;
    }

    public List<uml3_0_0_OutputPin> getUml3_0_0_outputpins() {
        return uml3_0_0_outputpins;
    }

    public void addUml3_0_0_outputpin(Uml3_0_0_outputpin uml3_0_0_outputpin) {
        this.uml3_0_0_outputpins.add(uml3_0_0_outputpin);
    }

}