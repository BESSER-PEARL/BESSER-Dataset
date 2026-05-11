





import java.util.List;
import java.util.ArrayList;

public class jpdl31_ScriptType  {

    private String mixed;
    private String any;
    private String acceptPropagatedEvents;
    private String name;



    public jpdl31_ScriptType(
        String mixed,        String any,        String acceptPropagatedEvents,        String name    ) {
        this.mixed = mixed;
        this.any = any;
        this.acceptPropagatedEvents = acceptPropagatedEvents;
        this.name = name;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}