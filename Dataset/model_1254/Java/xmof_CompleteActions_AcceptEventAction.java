





import java.util.List;
import java.util.ArrayList;

public class xmof_CompleteActions_AcceptEventAction extends Action {

    private boolean unmarshall;





    private List<BasicActions_OutputPin> basicactions_outputpins;


    public xmof_CompleteActions_AcceptEventAction(
        boolean unmarshall    ) {
        super(
        );
        this.unmarshall = unmarshall;
        this.basicactions_outputpins = new ArrayList<>();
    }

    public xmof_CompleteActions_AcceptEventAction(
        boolean unmarshall        ArrayList<BasicActions_OutputPin> basicactions_outputpins    ) {
        this.unmarshall = unmarshall;
        this.basicactions_outputpins = basicactions_outputpins;
    }

    public boolean getUnmarshall() {
        return unmarshall;
    }

    public void setUnmarshall(boolean unmarshall) {
        this.unmarshall = unmarshall;
    }

    public List<BasicActions_OutputPin> getBasicactions_outputpins() {
        return basicactions_outputpins;
    }

    public void addBasicactions_outputpin(Basicactions_outputpin basicactions_outputpin) {
        this.basicactions_outputpins.add(basicactions_outputpin);
    }

}