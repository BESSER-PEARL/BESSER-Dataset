





import java.util.List;
import java.util.ArrayList;

public class xmof_BasicActions_Action extends ExecutableNode {

    private boolean locallyReentrant;





    private List<BasicActions_InputPin> basicactions_inputpins;




    private List<BasicActions_OutputPin> basicactions_outputpins;


    public xmof_BasicActions_Action(
        boolean locallyReentrant    ) {
        super(
        );
        this.locallyReentrant = locallyReentrant;
        this.basicactions_inputpins = new ArrayList<>();
        this.basicactions_outputpins = new ArrayList<>();
    }

    public xmof_BasicActions_Action(
        boolean locallyReentrant        ArrayList<BasicActions_InputPin> basicactions_inputpins,        ArrayList<BasicActions_OutputPin> basicactions_outputpins    ) {
        this.locallyReentrant = locallyReentrant;
        this.basicactions_inputpins = basicactions_inputpins;
        this.basicactions_outputpins = basicactions_outputpins;
    }

    public boolean getLocallyreentrant() {
        return locallyReentrant;
    }

    public void setLocallyreentrant(boolean locallyReentrant) {
        this.locallyReentrant = locallyReentrant;
    }

    public List<BasicActions_InputPin> getBasicactions_inputpins() {
        return basicactions_inputpins;
    }

    public void addBasicactions_inputpin(Basicactions_inputpin basicactions_inputpin) {
        this.basicactions_inputpins.add(basicactions_inputpin);
    }
    public List<BasicActions_OutputPin> getBasicactions_outputpins() {
        return basicactions_outputpins;
    }

    public void addBasicactions_outputpin(Basicactions_outputpin basicactions_outputpin) {
        this.basicactions_outputpins.add(basicactions_outputpin);
    }

}