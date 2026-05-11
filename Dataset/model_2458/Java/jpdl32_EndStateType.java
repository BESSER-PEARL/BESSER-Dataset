





import java.util.List;
import java.util.ArrayList;

public class jpdl32_EndStateType  {

    private String group;
    private String name;
    private String endCompleteProcess;
    private String description;





    private jpdl32_DocumentRoot jpdl32_documentroot;




    private List<jpdl32_ExceptionHandlerType> jpdl32_exceptionhandlertypes;




    private List<jpdl32_EventType> jpdl32_eventtypes;


    public jpdl32_EndStateType(
        String group,        String name,        String endCompleteProcess,        String description    ) {
        this.group = group;
        this.name = name;
        this.endCompleteProcess = endCompleteProcess;
        this.description = description;
        this.jpdl32_exceptionhandlertypes = new ArrayList<>();
        this.jpdl32_eventtypes = new ArrayList<>();
    }

    public jpdl32_EndStateType(
        String group,        String name,        String endCompleteProcess,        String description        ArrayList<jpdl32_ExceptionHandlerType> jpdl32_exceptionhandlertypes,        ArrayList<jpdl32_EventType> jpdl32_eventtypes    ) {
        this.group = group;
        this.name = name;
        this.endCompleteProcess = endCompleteProcess;
        this.description = description;
        this.jpdl32_exceptionhandlertypes = jpdl32_exceptionhandlertypes;
        this.jpdl32_eventtypes = jpdl32_eventtypes;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEndcompleteprocess() {
        return endCompleteProcess;
    }

    public void setEndcompleteprocess(String endCompleteProcess) {
        this.endCompleteProcess = endCompleteProcess;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public jpdl32_DocumentRoot getJpdl32_documentroot() {
        return jpdl32_documentroot;
    }

    public void setJpdl32_documentroot(jpdl32_DocumentRoot jpdl32_documentroot) {
        this.jpdl32_documentroot = jpdl32_documentroot;
    }
    public List<jpdl32_ExceptionHandlerType> getJpdl32_exceptionhandlertypes() {
        return jpdl32_exceptionhandlertypes;
    }

    public void addJpdl32_exceptionhandlertype(Jpdl32_exceptionhandlertype jpdl32_exceptionhandlertype) {
        this.jpdl32_exceptionhandlertypes.add(jpdl32_exceptionhandlertype);
    }
    public List<jpdl32_EventType> getJpdl32_eventtypes() {
        return jpdl32_eventtypes;
    }

    public void addJpdl32_eventtype(Jpdl32_eventtype jpdl32_eventtype) {
        this.jpdl32_eventtypes.add(jpdl32_eventtype);
    }

}