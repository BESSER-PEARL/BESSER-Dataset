





import java.util.List;
import java.util.ArrayList;

public class ISO20022_ExternalSchema extends MessageComponentType {

    private String namespaceList;
    private String processContent;



    public ISO20022_ExternalSchema(
        String namespaceList,        String processContent    ) {
        super(
        );
        this.namespaceList = namespaceList;
        this.processContent = processContent;
    }


    public String getNamespacelist() {
        return namespaceList;
    }

    public void setNamespacelist(String namespaceList) {
        this.namespaceList = namespaceList;
    }
    public String getProcesscontent() {
        return processContent;
    }

    public void setProcesscontent(String processContent) {
        this.processContent = processContent;
    }


}