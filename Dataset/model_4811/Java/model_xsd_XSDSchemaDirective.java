





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDSchemaDirective extends XSDSchemaContent {

    private String schemaLocation;





    private XSDSchema xsdschema;


    public model_xsd_XSDSchemaDirective(
        String schemaLocation    ) {
        super(
        );
        this.schemaLocation = schemaLocation;
    }


    public String getSchemalocation() {
        return schemaLocation;
    }

    public void setSchemalocation(String schemaLocation) {
        this.schemaLocation = schemaLocation;
    }

    public XSDSchema getXsdschema() {
        return xsdschema;
    }

    public void setXsdschema(XSDSchema xsdschema) {
        this.xsdschema = xsdschema;
    }

}