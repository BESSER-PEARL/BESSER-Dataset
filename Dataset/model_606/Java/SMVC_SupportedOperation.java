





import java.util.List;
import java.util.ArrayList;

public class SMVC_SupportedOperation  {

    private String operationKind;
    private String url;





    private SMVC_List smvc_list;


    public SMVC_SupportedOperation(
        String operationKind,        String url    ) {
        this.operationKind = operationKind;
        this.url = url;
    }


    public String getOperationkind() {
        return operationKind;
    }

    public void setOperationkind(String operationKind) {
        this.operationKind = operationKind;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public SMVC_List getSmvc_list() {
        return smvc_list;
    }

    public void setSmvc_list(SMVC_List smvc_list) {
        this.smvc_list = smvc_list;
    }

}