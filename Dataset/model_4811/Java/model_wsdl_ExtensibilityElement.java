





import java.util.List;
import java.util.ArrayList;

public class model_wsdl_ExtensibilityElement extends wsdl_WSDLElement, wsdl_IExtensibilityElement {

    private boolean required;
    private String elementType;



    public model_wsdl_ExtensibilityElement(
        boolean required,        String elementType    ) {
        super(
        );
        this.required = required;
        this.elementType = elementType;
    }


    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }
    public String getElementtype() {
        return elementType;
    }

    public void setElementtype(String elementType) {
        this.elementType = elementType;
    }


}