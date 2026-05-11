





import java.util.List;
import java.util.ArrayList;

public class jpdl31_ActionType  {

    private String mixed;
    private String any;
    private String refName;
    private String class_;
    private String configType;
    private String acceptPropagatedEvents;
    private String name;
    private String expression;
    private String async_;



    public jpdl31_ActionType(
        String mixed,        String any,        String refName,        String class_,        String configType,        String acceptPropagatedEvents,        String name,        String expression,        String async_    ) {
        this.mixed = mixed;
        this.any = any;
        this.refName = refName;
        this.class_ = class_;
        this.configType = configType;
        this.acceptPropagatedEvents = acceptPropagatedEvents;
        this.name = name;
        this.expression = expression;
        this.async_ = async_;
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
    public String getRefname() {
        return refName;
    }

    public void setRefname(String refName) {
        this.refName = refName;
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
    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }
    public String getAsync_() {
        return async_;
    }

    public void setAsync_(String async_) {
        this.async_ = async_;
    }


}