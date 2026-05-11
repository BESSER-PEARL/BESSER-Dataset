





import java.util.List;
import java.util.ArrayList;

public class jpdl32_ScriptType  {

    private String mixed;
    private String name;
    private String any;
    private String acceptPropagatedEvents;



    public jpdl32_ScriptType(
        String mixed,        String name,        String any,        String acceptPropagatedEvents    ) {
        this.mixed = mixed;
        this.name = name;
        this.any = any;
        this.acceptPropagatedEvents = acceptPropagatedEvents;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getAcceptpropagatedevents() {
        return acceptPropagatedEvents;
    }

    public void setAcceptpropagatedevents(String acceptPropagatedEvents) {
        this.acceptPropagatedEvents = acceptPropagatedEvents;
    }


}