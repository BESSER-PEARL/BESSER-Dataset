





import java.util.List;
import java.util.ArrayList;

public class jpdl31_ScriptType  {

    private String mixed;
    private String name;
    private String any;
    private String acceptPropagatedEvents;





    private jpdl31_CreateTimerType jpdl31_createtimertype;


    public jpdl31_ScriptType(
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

    public jpdl31_CreateTimerType getJpdl31_createtimertype() {
        return jpdl31_createtimertype;
    }

    public void setJpdl31_createtimertype(jpdl31_CreateTimerType jpdl31_createtimertype) {
        this.jpdl31_createtimertype = jpdl31_createtimertype;
    }

}