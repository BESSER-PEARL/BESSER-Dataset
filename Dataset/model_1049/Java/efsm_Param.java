





import java.util.List;
import java.util.ArrayList;

public class efsm_Param  {

    private String argName;
    private String argType;





    private efsm_Event efsm_event;


    public efsm_Param(
        String argName,        String argType    ) {
        this.argName = argName;
        this.argType = argType;
    }


    public String getArgname() {
        return argName;
    }

    public void setArgname(String argName) {
        this.argName = argName;
    }
    public String getArgtype() {
        return argType;
    }

    public void setArgtype(String argType) {
        this.argType = argType;
    }

    public efsm_Event getEfsm_event() {
        return efsm_event;
    }

    public void setEfsm_event(efsm_Event efsm_event) {
        this.efsm_event = efsm_event;
    }

}