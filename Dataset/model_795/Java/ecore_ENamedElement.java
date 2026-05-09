





import java.util.List;
import java.util.ArrayList;

public class ecore_ENamedElement  {






    private List<ecore_FSM> ecore_fsms;


    public ecore_ENamedElement(
    ) {
        this.ecore_fsms = new ArrayList<>();
    }

    public ecore_ENamedElement(
        ArrayList<ecore_FSM> ecore_fsms    ) {
        this.ecore_fsms = ecore_fsms;
    }


    public List<ecore_FSM> getEcore_fsms() {
        return ecore_fsms;
    }

    public void addEcore_fsm(Ecore_fsm ecore_fsm) {
        this.ecore_fsms.add(ecore_fsm);
    }

}