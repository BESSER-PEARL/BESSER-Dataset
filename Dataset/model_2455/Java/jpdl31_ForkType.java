





import java.util.List;
import java.util.ArrayList;

public class jpdl31_ForkType  {

    private String group;
    private String name;
    private String async_;





    private jpdl31_DocumentRoot jpdl31_documentroot;




    private List<jpdl31_EventType> jpdl31_eventtypes;




    private List<jpdl31_ExceptionHandlerType> jpdl31_exceptionhandlertypes;




    private List<jpdl31_ScriptType> jpdl31_scripttypes;


    public jpdl31_ForkType(
        String group,        String name,        String async_    ) {
        this.group = group;
        this.name = name;
        this.async_ = async_;
        this.jpdl31_eventtypes = new ArrayList<>();
        this.jpdl31_exceptionhandlertypes = new ArrayList<>();
        this.jpdl31_scripttypes = new ArrayList<>();
    }

    public jpdl31_ForkType(
        String group,        String name,        String async_        ArrayList<jpdl31_EventType> jpdl31_eventtypes,        ArrayList<jpdl31_ExceptionHandlerType> jpdl31_exceptionhandlertypes,        ArrayList<jpdl31_ScriptType> jpdl31_scripttypes    ) {
        this.group = group;
        this.name = name;
        this.async_ = async_;
        this.jpdl31_eventtypes = jpdl31_eventtypes;
        this.jpdl31_exceptionhandlertypes = jpdl31_exceptionhandlertypes;
        this.jpdl31_scripttypes = jpdl31_scripttypes;
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
    public String getAsync_() {
        return async_;
    }

    public void setAsync_(String async_) {
        this.async_ = async_;
    }

    public jpdl31_DocumentRoot getJpdl31_documentroot() {
        return jpdl31_documentroot;
    }

    public void setJpdl31_documentroot(jpdl31_DocumentRoot jpdl31_documentroot) {
        this.jpdl31_documentroot = jpdl31_documentroot;
    }
    public List<jpdl31_EventType> getJpdl31_eventtypes() {
        return jpdl31_eventtypes;
    }

    public void addJpdl31_eventtype(Jpdl31_eventtype jpdl31_eventtype) {
        this.jpdl31_eventtypes.add(jpdl31_eventtype);
    }
    public List<jpdl31_ExceptionHandlerType> getJpdl31_exceptionhandlertypes() {
        return jpdl31_exceptionhandlertypes;
    }

    public void addJpdl31_exceptionhandlertype(Jpdl31_exceptionhandlertype jpdl31_exceptionhandlertype) {
        this.jpdl31_exceptionhandlertypes.add(jpdl31_exceptionhandlertype);
    }
    public List<jpdl31_ScriptType> getJpdl31_scripttypes() {
        return jpdl31_scripttypes;
    }

    public void addJpdl31_scripttype(Jpdl31_scripttype jpdl31_scripttype) {
        this.jpdl31_scripttypes.add(jpdl31_scripttype);
    }

}