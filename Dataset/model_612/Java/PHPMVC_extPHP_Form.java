





import java.util.List;
import java.util.ArrayList;

public class PHPMVC_extPHP_Form extends HTMLElement {

    private String target;
    private String method;
    private String action;



    public PHPMVC_extPHP_Form(
        String target,        String method,        String action    ) {
        super(
        );
        this.target = target;
        this.method = method;
        this.action = action;
    }


    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }
    public String getMethod() {
        return method;
    }

    public void setMethod(String method) {
        this.method = method;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }


}