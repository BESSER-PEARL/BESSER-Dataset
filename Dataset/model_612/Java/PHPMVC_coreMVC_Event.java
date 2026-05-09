





import java.util.List;
import java.util.ArrayList;

public class PHPMVC_coreMVC_Event  {

    private String type;
    private String handler;



    public PHPMVC_coreMVC_Event(
        String type,        String handler    ) {
        this.type = type;
        this.handler = handler;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getHandler() {
        return handler;
    }

    public void setHandler(String handler) {
        this.handler = handler;
    }


}