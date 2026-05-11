





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Transaction extends SubProcess {

    private String protocol;
    private String method;





    private bpmn2_DocumentRoot bpmn2_documentroot;


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

    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}