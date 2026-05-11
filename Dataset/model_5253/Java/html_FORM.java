





import java.util.List;
import java.util.ArrayList;

public class html_FORM  {

    private String method;
    private String action;



    public html_FORM(
        String method,        String action    ) {
        this.method = method;
        this.action = action;
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