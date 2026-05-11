





import java.util.List;
import java.util.ArrayList;

public class jpdl31_ActionType  {

    private String expression;
    private String class_;
    private String acceptPropagatedEvents;
    private String name;
    private String refName;
    private String mixed;
    private String configType;
    private String async_;
    private String any;



    public jpdl31_ActionType(
        String expression,        String class_,        String acceptPropagatedEvents,        String name,        String refName,        String mixed,        String configType,        String async_,        String any    ) {
        this.expression = expression;
        this.class_ = class_;
        this.acceptPropagatedEvents = acceptPropagatedEvents;
        this.name = name;
        this.refName = refName;
        this.mixed = mixed;
        this.configType = configType;
        this.async_ = async_;
        this.any = any;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
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
    public String getConfigtype() {
        return configType;
    }

    public void setConfigtype(String configType) {
        this.configType = configType;
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


}