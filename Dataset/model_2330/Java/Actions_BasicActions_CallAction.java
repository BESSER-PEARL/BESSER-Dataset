





import java.util.List;
import java.util.ArrayList;

public class Actions_BasicActions_CallAction extends InvocationAction {

    private boolean isSynchronous;





    private List<OutputPin> outputpins;


    public Actions_BasicActions_CallAction(
        boolean isSynchronous    ) {
        super(
        );
        this.isSynchronous = isSynchronous;
        this.outputpins = new ArrayList<>();
    }

    public Actions_BasicActions_CallAction(
        boolean isSynchronous        ArrayList<OutputPin> outputpins    ) {
        this.isSynchronous = isSynchronous;
        this.outputpins = outputpins;
    }

    public boolean getIssynchronous() {
        return isSynchronous;
    }

    public void setIssynchronous(boolean isSynchronous) {
        this.isSynchronous = isSynchronous;
    }

    public List<OutputPin> getOutputpins() {
        return outputpins;
    }

    public void addOutputpin(Outputpin outputpin) {
        this.outputpins.add(outputpin);
    }

}