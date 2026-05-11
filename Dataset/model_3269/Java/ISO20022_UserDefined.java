





import java.util.List;
import java.util.ArrayList;

public class ISO20022_UserDefined extends MessageComponentType {

    private String _;
    private String processContents;
    private String namespaceList;



    public ISO20022_UserDefined(
        String _,        String processContents,        String namespaceList    ) {
        super(
        );
        this._ = _;
        this.processContents = processContents;
        this.namespaceList = namespaceList;
    }


    public String get_() {
        return _;
    }

    public void set_(String _) {
        this._ = _;
    }
    public String getProcesscontents() {
        return processContents;
    }

    public void setProcesscontents(String processContents) {
        this.processContents = processContents;
    }
    public String getNamespacelist() {
        return namespaceList;
    }

    public void setNamespacelist(String namespaceList) {
        this.namespaceList = namespaceList;
    }


}