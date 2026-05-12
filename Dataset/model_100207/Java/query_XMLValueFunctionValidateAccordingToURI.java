





import java.util.List;
import java.util.ArrayList;

public class query_XMLValueFunctionValidateAccordingToURI extends XMLValueFunctionValidateAccordingTo {

    private String targetNamespaceURI;
    private boolean noNamespace;
    private String schemaLocationURI;



    public query_XMLValueFunctionValidateAccordingToURI(
        String targetNamespaceURI,        boolean noNamespace,        String schemaLocationURI    ) {
        super(
        );
        this.targetNamespaceURI = targetNamespaceURI;
        this.noNamespace = noNamespace;
        this.schemaLocationURI = schemaLocationURI;
    }


    public String getTargetnamespaceuri() {
        return targetNamespaceURI;
    }

    public void setTargetnamespaceuri(String targetNamespaceURI) {
        this.targetNamespaceURI = targetNamespaceURI;
    }
    public boolean getNonamespace() {
        return noNamespace;
    }

    public void setNonamespace(boolean noNamespace) {
        this.noNamespace = noNamespace;
    }
    public String getSchemalocationuri() {
        return schemaLocationURI;
    }

    public void setSchemalocationuri(String schemaLocationURI) {
        this.schemaLocationURI = schemaLocationURI;
    }


}