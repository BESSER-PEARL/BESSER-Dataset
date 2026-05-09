





import java.util.List;
import java.util.ArrayList;

public class fSM_EnumerationLiteral  {

    private String name;





    private fSM_EnumerationType fsm_enumerationtype;




    private fSM_State fsm_state;


    public fSM_EnumerationLiteral(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fSM_EnumerationType getFsm_enumerationtype() {
        return fsm_enumerationtype;
    }

    public void setFsm_enumerationtype(fSM_EnumerationType fsm_enumerationtype) {
        this.fsm_enumerationtype = fsm_enumerationtype;
    }
    public fSM_State getFsm_state() {
        return fsm_state;
    }

    public void setFsm_state(fSM_State fsm_state) {
        this.fsm_state = fsm_state;
    }

}