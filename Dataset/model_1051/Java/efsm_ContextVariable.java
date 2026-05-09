





import java.util.List;
import java.util.ArrayList;

public class efsm_ContextVariable  {

    private String type;
    private String name;





    private efsm_EFSM efsm_efsm;


    public efsm_ContextVariable(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public efsm_EFSM getEfsm_efsm() {
        return efsm_efsm;
    }

    public void setEfsm_efsm(efsm_EFSM efsm_efsm) {
        this.efsm_efsm = efsm_efsm;
    }

}