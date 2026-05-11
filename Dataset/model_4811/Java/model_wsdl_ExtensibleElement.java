





import java.util.List;
import java.util.ArrayList;

public class model_wsdl_ExtensibleElement extends wsdl_WSDLElement, wsdl_IElementExtensible, wsdl_IAttributeExtensible {






    private List<ExtensibilityElement> extensibilityelements;


    public model_wsdl_ExtensibleElement(
    ) {
        super(
        );
        this.extensibilityelements = new ArrayList<>();
    }

    public model_wsdl_ExtensibleElement(
        ArrayList<ExtensibilityElement> extensibilityelements    ) {
        this.extensibilityelements = extensibilityelements;
    }


    public List<ExtensibilityElement> getExtensibilityelements() {
        return extensibilityelements;
    }

    public void addExtensibilityelement(Extensibilityelement extensibilityelement) {
        this.extensibilityelements.add(extensibilityelement);
    }

}