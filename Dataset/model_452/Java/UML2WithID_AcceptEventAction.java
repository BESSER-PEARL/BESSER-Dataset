





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_AcceptEventAction extends Action {






    private List<UML2WithID_Trigger> uml2withid_triggers;


    public UML2WithID_AcceptEventAction(
    ) {
        super(
        );
        this.uml2withid_triggers = new ArrayList<>();
    }

    public UML2WithID_AcceptEventAction(
        ArrayList<UML2WithID_Trigger> uml2withid_triggers    ) {
        this.uml2withid_triggers = uml2withid_triggers;
    }


    public List<UML2WithID_Trigger> getUml2withid_triggers() {
        return uml2withid_triggers;
    }

    public void addUml2withid_trigger(Uml2withid_trigger uml2withid_trigger) {
        this.uml2withid_triggers.add(uml2withid_trigger);
    }

}