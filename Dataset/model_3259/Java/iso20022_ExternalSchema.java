





import java.util.List;
import java.util.ArrayList;

public class iso20022_ExternalSchema extends MessageComponentType {

    private String processContent;
    private String namespaceList;



    public iso20022_ExternalSchema(
        String processContent,        String namespaceList    ) {
        super(
        );
        this.processContent = processContent;
        this.namespaceList = namespaceList;
    }


    public String getProcesscontent() {
        return processContent;
    }

    public void setProcesscontent(String processContent) {
        this.processContent = processContent;
    }
    public String getNamespacelist() {
        return namespaceList;
    }

    public void setNamespacelist(String namespaceList) {
        this.namespaceList = namespaceList;
    }


}