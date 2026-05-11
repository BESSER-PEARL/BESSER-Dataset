





import java.util.List;
import java.util.ArrayList;

public class iso20022_UserDefined extends MessageComponentType {

    private String namespace;
    private String processContents;
    private String namespaceList;



    public iso20022_UserDefined(
        String namespace,        String processContents,        String namespaceList    ) {
        super(
        );
        this.namespace = namespace;
        this.processContents = processContents;
        this.namespaceList = namespaceList;
    }


    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
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


}