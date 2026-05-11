





import java.util.List;
import java.util.ArrayList;

public class iso20022_UserDefined extends MessageComponentType {

    private String processContents;
    private String namespaceList;
    private String namespace;



    public iso20022_UserDefined(
        String processContents,        String namespaceList,        String namespace    ) {
        super(
        );
        this.processContents = processContents;
        this.namespaceList = namespaceList;
        this.namespace = namespace;
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
    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }


}