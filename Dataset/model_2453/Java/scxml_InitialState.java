





import java.util.List;
import java.util.ArrayList;

public class scxml_InitialState extends NamedElement {






    private scxml_State scxml_state;




    private scxml_ServiceTemplate scxml_servicetemplate;


    public scxml_InitialState(
    ) {
        super(
        );
    }



    public scxml_State getScxml_state() {
        return scxml_state;
    }

    public void setScxml_state(scxml_State scxml_state) {
        this.scxml_state = scxml_state;
    }
    public scxml_ServiceTemplate getScxml_servicetemplate() {
        return scxml_servicetemplate;
    }

    public void setScxml_servicetemplate(scxml_ServiceTemplate scxml_servicetemplate) {
        this.scxml_servicetemplate = scxml_servicetemplate;
    }

}