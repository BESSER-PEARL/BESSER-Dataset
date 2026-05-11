





import java.util.List;
import java.util.ArrayList;

public class jpdl32_ActionType  {

    private String class_;
    private String configType;
    private String expression;
    private String acceptPropagatedEvents;
    private String name;
    private String refName;
    private String mixed;
    private String async_;
    private String any;





    private jpdl32_TimerType jpdl32_timertype;




    private jpdl32_NodeType jpdl32_nodetype;




    private jpdl32_DocumentRoot jpdl32_documentroot;




    private jpdl32_EventType jpdl32_eventtype;




    private jpdl32_CreateTimerType jpdl32_createtimertype;




    private jpdl32_TransitionType jpdl32_transitiontype;




    private jpdl32_ExceptionHandlerType jpdl32_exceptionhandlertype;




    private jpdl32_ProcessDefinitionType jpdl32_processdefinitiontype;


    public jpdl32_ActionType(
        String class_,        String configType,        String expression,        String acceptPropagatedEvents,        String name,        String refName,        String mixed,        String async_,        String any    ) {
        this.class_ = class_;
        this.configType = configType;
        this.expression = expression;
        this.acceptPropagatedEvents = acceptPropagatedEvents;
        this.name = name;
        this.refName = refName;
        this.mixed = mixed;
        this.async_ = async_;
        this.any = any;
    }


    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getConfigtype() {
        return configType;
    }

    public void setConfigtype(String configType) {
        this.configType = configType;
    }
    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
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
    public String getRefname() {
        return refName;
    }

    public void setRefname(String refName) {
        this.refName = refName;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getAsync_() {
        return async_;
    }

    public void setAsync_(String async_) {
        this.async_ = async_;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }

    public jpdl32_TimerType getJpdl32_timertype() {
        return jpdl32_timertype;
    }

    public void setJpdl32_timertype(jpdl32_TimerType jpdl32_timertype) {
        this.jpdl32_timertype = jpdl32_timertype;
    }
    public jpdl32_NodeType getJpdl32_nodetype() {
        return jpdl32_nodetype;
    }

    public void setJpdl32_nodetype(jpdl32_NodeType jpdl32_nodetype) {
        this.jpdl32_nodetype = jpdl32_nodetype;
    }
    public jpdl32_DocumentRoot getJpdl32_documentroot() {
        return jpdl32_documentroot;
    }

    public void setJpdl32_documentroot(jpdl32_DocumentRoot jpdl32_documentroot) {
        this.jpdl32_documentroot = jpdl32_documentroot;
    }
    public jpdl32_EventType getJpdl32_eventtype() {
        return jpdl32_eventtype;
    }

    public void setJpdl32_eventtype(jpdl32_EventType jpdl32_eventtype) {
        this.jpdl32_eventtype = jpdl32_eventtype;
    }
    public jpdl32_CreateTimerType getJpdl32_createtimertype() {
        return jpdl32_createtimertype;
    }

    public void setJpdl32_createtimertype(jpdl32_CreateTimerType jpdl32_createtimertype) {
        this.jpdl32_createtimertype = jpdl32_createtimertype;
    }
    public jpdl32_TransitionType getJpdl32_transitiontype() {
        return jpdl32_transitiontype;
    }

    public void setJpdl32_transitiontype(jpdl32_TransitionType jpdl32_transitiontype) {
        this.jpdl32_transitiontype = jpdl32_transitiontype;
    }
    public jpdl32_ExceptionHandlerType getJpdl32_exceptionhandlertype() {
        return jpdl32_exceptionhandlertype;
    }

    public void setJpdl32_exceptionhandlertype(jpdl32_ExceptionHandlerType jpdl32_exceptionhandlertype) {
        this.jpdl32_exceptionhandlertype = jpdl32_exceptionhandlertype;
    }
    public jpdl32_ProcessDefinitionType getJpdl32_processdefinitiontype() {
        return jpdl32_processdefinitiontype;
    }

    public void setJpdl32_processdefinitiontype(jpdl32_ProcessDefinitionType jpdl32_processdefinitiontype) {
        this.jpdl32_processdefinitiontype = jpdl32_processdefinitiontype;
    }

}