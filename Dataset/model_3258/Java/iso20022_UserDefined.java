





import java.util.List;
import java.util.ArrayList;

public class iso20022_UserDefined extends MessageComponentType {

    private String namespaceList;
    private String processContents;
    private String namespace;



    public iso20022_UserDefined(
        String namespaceList,        String processContents,        String namespace    ) {
        super(
        );
        this.namespaceList = namespaceList;
        this.processContents = processContents;
        this.namespace = namespace;
    }


    public String getNamespacelist() {
        return namespaceList;
    }

    public void setNamespacelist(String namespaceList) {
        this.namespaceList = namespaceList;
    }
    public String getProcesscontents() {
        return processContents;
    }

    public void setProcesscontents(String processContents) {
        this.processContents = processContents;
    }
    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }


}