





import java.util.List;
import java.util.ArrayList;

public class tfsm_TimedSystem extends NamedElement {






    private List<tfsm_TFSM> tfsm_tfsms;


    public tfsm_TimedSystem(
    ) {
        super(
        );
        this.tfsm_tfsms = new ArrayList<>();
    }

    public tfsm_TimedSystem(
        ArrayList<tfsm_TFSM> tfsm_tfsms    ) {
        this.tfsm_tfsms = tfsm_tfsms;
    }


    public List<tfsm_TFSM> getTfsm_tfsms() {
        return tfsm_tfsms;
    }

    public void addTfsm_tfsm(Tfsm_tfsm tfsm_tfsm) {
        this.tfsm_tfsms.add(tfsm_tfsm);
    }

}