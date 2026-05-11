





import java.util.List;
import java.util.ArrayList;

public class defaultname_FORM  {

    private String action;
    private String method;



    public defaultname_FORM(
        String action,        String method    ) {
        this.action = action;
        this.method = method;
    }


    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }
    public String getMethod() {
        return method;
    }

    public void setMethod(String method) {
        this.method = method;
    }


}