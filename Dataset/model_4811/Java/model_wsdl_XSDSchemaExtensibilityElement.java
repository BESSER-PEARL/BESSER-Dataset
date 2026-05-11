





import java.util.List;
import java.util.ArrayList;

public class model_wsdl_XSDSchemaExtensibilityElement extends wsdl_ISchema, wsdl_ExtensibilityElement {

    private String documentBaseURI;





    private XSDSchema xsdschema;


    public model_wsdl_XSDSchemaExtensibilityElement(
        String documentBaseURI    ) {
        super(
        );
        this.documentBaseURI = documentBaseURI;
    }


    public String getDocumentbaseuri() {
        return documentBaseURI;
    }

    public void setDocumentbaseuri(String documentBaseURI) {
        this.documentBaseURI = documentBaseURI;
    }

    public XSDSchema getXsdschema() {
        return xsdschema;
    }

    public void setXsdschema(XSDSchema xsdschema) {
        this.xsdschema = xsdschema;
    }

}