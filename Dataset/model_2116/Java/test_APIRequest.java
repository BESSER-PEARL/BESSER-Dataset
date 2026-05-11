





import java.util.List;
import java.util.ArrayList;

public class test_APIRequest extends TestStep {

    private String scheme;
    private String accept;
    private String contentType;
    private String operationId;



    public test_APIRequest(
        String scheme,        String accept,        String contentType,        String operationId    ) {
        super(
        );
        this.scheme = scheme;
        this.accept = accept;
        this.contentType = contentType;
        this.operationId = operationId;
    }


    public String getScheme() {
        return scheme;
    }

    public void setScheme(String scheme) {
        this.scheme = scheme;
    }
    public String getAccept() {
        return accept;
    }

    public void setAccept(String accept) {
        this.accept = accept;
    }
    public String getContenttype() {
        return contentType;
    }

    public void setContenttype(String contentType) {
        this.contentType = contentType;
    }
    public String getOperationid() {
        return operationId;
    }

    public void setOperationid(String operationId) {
        this.operationId = operationId;
    }


}