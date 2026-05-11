





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Transaction extends SubProcess {

    private String method;
    private String protocol;



    public bpmn2_Transaction(
        String method,        String protocol    ) {
        super(
        );
        this.method = method;
        this.protocol = protocol;
    }


    public String getMethod() {
        return method;
    }

    public void setMethod(String method) {
        this.method = method;
    }
    public String getProtocol() {
        return protocol;
    }

    public void setProtocol(String protocol) {
        this.protocol = protocol;
    }


}