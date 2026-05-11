





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDXPathDefinition extends XSDComponent {

    private String value;
    private String variety;





    private XSDAnnotation xsdannotation;


    public model_xsd_XSDXPathDefinition(
        String value,        String variety    ) {
        super(
        );
        this.value = value;
        this.variety = variety;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getVariety() {
        return variety;
    }

    public void setVariety(String variety) {
        this.variety = variety;
    }

    public XSDAnnotation getXsdannotation() {
        return xsdannotation;
    }

    public void setXsdannotation(XSDAnnotation xsdannotation) {
        this.xsdannotation = xsdannotation;
    }

}