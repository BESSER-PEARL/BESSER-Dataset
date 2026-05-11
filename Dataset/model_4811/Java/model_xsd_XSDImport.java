





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDImport extends XSDSchemaDirective {

    private String namespace;





    private XSDAnnotation xsdannotation;


    public model_xsd_XSDImport(
        String namespace    ) {
        super(
        );
        this.namespace = namespace;
    }


    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }

    public XSDAnnotation getXsdannotation() {
        return xsdannotation;
    }

    public void setXsdannotation(XSDAnnotation xsdannotation) {
        this.xsdannotation = xsdannotation;
    }

}