





import java.util.List;
import java.util.ArrayList;

public class ecore_State  {

    private String name;





    private ecore_FSM ecore_fsm;




    private ecore_FSM ecore_fsm;




    private ecore_FSM ecore_fsm;




    private ecore_FSM ecore_fsm;




    private List<ecore_EClass> ecore_eclasss;


    public ecore_State(
        String name    ) {
        this.name = name;
        this.ecore_eclasss = new ArrayList<>();
    }

    public ecore_State(
        String name        ArrayList<ecore_EClass> ecore_eclasss    ) {
        this.name = name;
        this.ecore_eclasss = ecore_eclasss;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ecore_FSM getEcore_fsm() {
        return ecore_fsm;
    }

    public void setEcore_fsm(ecore_FSM ecore_fsm) {
        this.ecore_fsm = ecore_fsm;
    }
    public ecore_FSM getEcore_fsm() {
        return ecore_fsm;
    }

    public void setEcore_fsm(ecore_FSM ecore_fsm) {
        this.ecore_fsm = ecore_fsm;
    }
    public ecore_FSM getEcore_fsm() {
        return ecore_fsm;
    }

    public void setEcore_fsm(ecore_FSM ecore_fsm) {
        this.ecore_fsm = ecore_fsm;
    }
    public ecore_FSM getEcore_fsm() {
        return ecore_fsm;
    }

    public void setEcore_fsm(ecore_FSM ecore_fsm) {
        this.ecore_fsm = ecore_fsm;
    }
    public List<ecore_EClass> getEcore_eclasss() {
        return ecore_eclasss;
    }

    public void addEcore_eclass(Ecore_eclass ecore_eclass) {
        this.ecore_eclasss.add(ecore_eclass);
    }

}