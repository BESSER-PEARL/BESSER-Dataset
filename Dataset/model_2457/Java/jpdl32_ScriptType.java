





import java.util.List;
import java.util.ArrayList;

public class jpdl32_ScriptType  {

    private String any;
    private String acceptPropagatedEvents;
    private String mixed;
    private String name;





    private jpdl32_CreateTimerType jpdl32_createtimertype;


    public jpdl32_ScriptType(
        String any,        String acceptPropagatedEvents,        String mixed,        String name    ) {
        this.any = any;
        this.acceptPropagatedEvents = acceptPropagatedEvents;
        this.mixed = mixed;
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

    public jpdl32_CreateTimerType getJpdl32_createtimertype() {
        return jpdl32_createtimertype;
    }

    public void setJpdl32_createtimertype(jpdl32_CreateTimerType jpdl32_createtimertype) {
        this.jpdl32_createtimertype = jpdl32_createtimertype;
    }

}