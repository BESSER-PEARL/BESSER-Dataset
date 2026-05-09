





import java.util.List;
import java.util.ArrayList;

public class tfsmextended_TimedSystem extends NamedElement {






    private List<tfsmextended_TFSM> tfsmextended_tfsms;


    public tfsmextended_TimedSystem(
    ) {
        super(
        );
        this.tfsmextended_tfsms = new ArrayList<>();
    }

    public tfsmextended_TimedSystem(
        ArrayList<tfsmextended_TFSM> tfsmextended_tfsms    ) {
        this.tfsmextended_tfsms = tfsmextended_tfsms;
    }


    public List<tfsmextended_TFSM> getTfsmextended_tfsms() {
        return tfsmextended_tfsms;
    }

    public void addTfsmextended_tfsm(Tfsmextended_tfsm tfsmextended_tfsm) {
        this.tfsmextended_tfsms.add(tfsmextended_tfsm);
    }

}