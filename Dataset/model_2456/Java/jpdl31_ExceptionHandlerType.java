





import java.util.List;
import java.util.ArrayList;

public class jpdl31_ExceptionHandlerType  {

    private String exceptionClass;
    private String group;





    private jpdl31_DecisionType jpdl31_decisiontype;




    private List<jpdl31_ActionType> jpdl31_actiontypes;




    private List<jpdl31_ScriptType> jpdl31_scripttypes;


    public jpdl31_ExceptionHandlerType(
        String exceptionClass,        String group    ) {
        this.exceptionClass = exceptionClass;
        this.group = group;
        this.jpdl31_actiontypes = new ArrayList<>();
        this.jpdl31_scripttypes = new ArrayList<>();
    }

    public jpdl31_ExceptionHandlerType(
        String exceptionClass,        String group        ArrayList<jpdl31_ActionType> jpdl31_actiontypes,        ArrayList<jpdl31_ScriptType> jpdl31_scripttypes    ) {
        this.exceptionClass = exceptionClass;
        this.group = group;
        this.jpdl31_actiontypes = jpdl31_actiontypes;
        this.jpdl31_scripttypes = jpdl31_scripttypes;
    }

    public String getExceptionclass() {
        return exceptionClass;
    }

    public void setExceptionclass(String exceptionClass) {
        this.exceptionClass = exceptionClass;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public jpdl31_DecisionType getJpdl31_decisiontype() {
        return jpdl31_decisiontype;
    }

    public void setJpdl31_decisiontype(jpdl31_DecisionType jpdl31_decisiontype) {
        this.jpdl31_decisiontype = jpdl31_decisiontype;
    }
    public List<jpdl31_ActionType> getJpdl31_actiontypes() {
        return jpdl31_actiontypes;
    }

    public void addJpdl31_actiontype(Jpdl31_actiontype jpdl31_actiontype) {
        this.jpdl31_actiontypes.add(jpdl31_actiontype);
    }
    public List<jpdl31_ScriptType> getJpdl31_scripttypes() {
        return jpdl31_scripttypes;
    }

    public void addJpdl31_scripttype(Jpdl31_scripttype jpdl31_scripttype) {
        this.jpdl31_scripttypes.add(jpdl31_scripttype);
    }

}