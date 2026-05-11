





import java.util.List;
import java.util.ArrayList;

public class model_wsdl_WSDLElement  {

    private String documentationElement;
    private String element;



    public model_wsdl_WSDLElement(
        String documentationElement,        String element    ) {
        this.documentationElement = documentationElement;
        this.element = element;
    }


    public String getDocumentationelement() {
        return documentationElement;
    }

    public void setDocumentationelement(String documentationElement) {
        this.documentationElement = documentationElement;
    }
    public String getElement() {
        return element;
    }

    public void setElement(String element) {
        this.element = element;
    }


}