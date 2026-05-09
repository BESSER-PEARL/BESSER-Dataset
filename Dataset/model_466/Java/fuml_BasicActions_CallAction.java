





import java.util.List;
import java.util.ArrayList;

public class fuml_BasicActions_CallAction extends InvocationAction {

    private boolean synchronous;





    private List<BasicActions_OutputPin> basicactions_outputpins;


    public fuml_BasicActions_CallAction(
        boolean synchronous    ) {
        super(
        );
        this.synchronous = synchronous;
        this.basicactions_outputpins = new ArrayList<>();
    }

    public fuml_BasicActions_CallAction(
        boolean synchronous        ArrayList<BasicActions_OutputPin> basicactions_outputpins    ) {
        this.synchronous = synchronous;
        this.basicactions_outputpins = basicactions_outputpins;
    }

    public boolean getSynchronous() {
        return synchronous;
    }

    public void setSynchronous(boolean synchronous) {
        this.synchronous = synchronous;
    }

    public List<BasicActions_OutputPin> getBasicactions_outputpins() {
        return basicactions_outputpins;
    }

    public void addBasicactions_outputpin(Basicactions_outputpin basicactions_outputpin) {
        this.basicactions_outputpins.add(basicactions_outputpin);
    }

}