





import java.util.List;
import java.util.ArrayList;

public class jpdl32_ExceptionHandlerType  {

    private String group;
    private String exceptionClass;





    private jpdl32_DecisionType jpdl32_decisiontype;




    private List<jpdl32_ScriptType> jpdl32_scripttypes;




    private List<jpdl32_ActionType> jpdl32_actiontypes;


    public jpdl32_ExceptionHandlerType(
        String group,        String exceptionClass    ) {
        this.group = group;
        this.exceptionClass = exceptionClass;
        this.jpdl32_scripttypes = new ArrayList<>();
        this.jpdl32_actiontypes = new ArrayList<>();
    }

    public jpdl32_ExceptionHandlerType(
        String group,        String exceptionClass        ArrayList<jpdl32_ScriptType> jpdl32_scripttypes,        ArrayList<jpdl32_ActionType> jpdl32_actiontypes    ) {
        this.group = group;
        this.exceptionClass = exceptionClass;
        this.jpdl32_scripttypes = jpdl32_scripttypes;
        this.jpdl32_actiontypes = jpdl32_actiontypes;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getExceptionclass() {
        return exceptionClass;
    }

    public void setExceptionclass(String exceptionClass) {
        this.exceptionClass = exceptionClass;
    }

    public jpdl32_DecisionType getJpdl32_decisiontype() {
        return jpdl32_decisiontype;
    }

    public void setJpdl32_decisiontype(jpdl32_DecisionType jpdl32_decisiontype) {
        this.jpdl32_decisiontype = jpdl32_decisiontype;
    }
    public List<jpdl32_ScriptType> getJpdl32_scripttypes() {
        return jpdl32_scripttypes;
    }

    public void addJpdl32_scripttype(Jpdl32_scripttype jpdl32_scripttype) {
        this.jpdl32_scripttypes.add(jpdl32_scripttype);
    }
    public List<jpdl32_ActionType> getJpdl32_actiontypes() {
        return jpdl32_actiontypes;
    }

    public void addJpdl32_actiontype(Jpdl32_actiontype jpdl32_actiontype) {
        this.jpdl32_actiontypes.add(jpdl32_actiontype);
    }

}