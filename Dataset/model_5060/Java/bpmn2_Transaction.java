





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Transaction extends SubProcess {

    private String protocol;
    private String method;



    public bpmn2_Transaction(
        String protocol,        String method    ) {
        super(
        );
        this.protocol = protocol;
        this.method = method;
    }


    public String getProtocol() {
        return protocol;
    }

    public void setProtocol(String protocol) {
        this.protocol = protocol;
    }
    public String getMethod() {
        return method;
    }

    public void setMethod(String method) {
        this.method = method;
    }


}