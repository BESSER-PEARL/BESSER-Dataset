





import java.util.List;
import java.util.ArrayList;

public class jpdl32_ActionType  {

    private String async_;
    private String any;
    private String acceptPropagatedEvents;
    private String mixed;
    private String expression;
    private String configType;
    private String name;
    private String class_;
    private String refName;



    public jpdl32_ActionType(
        String async_,        String any,        String acceptPropagatedEvents,        String mixed,        String expression,        String configType,        String name,        String class_,        String refName    ) {
        this.async_ = async_;
        this.any = any;
        this.acceptPropagatedEvents = acceptPropagatedEvents;
        this.mixed = mixed;
        this.expression = expression;
        this.configType = configType;
        this.name = name;
        this.class_ = class_;
        this.refName = refName;
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
    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }
    public String getConfigtype() {
        return configType;
    }

    public void setConfigtype(String configType) {
        this.configType = configType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getRefname() {
        return refName;
    }

    public void setRefname(String refName) {
        this.refName = refName;
    }


}