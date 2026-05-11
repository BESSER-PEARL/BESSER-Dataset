





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDConcreteComponent  {

    private String element;





    private XSDSchema xsdschema;


    public model_xsd_XSDConcreteComponent(
        String element    ) {
        this.element = element;
    }


    public String getElement() {
        return element;
    }

    public void setElement(String element) {
        this.element = element;
    }

    public XSDSchema getXsdschema() {
        return xsdschema;
    }

    public void setXsdschema(XSDSchema xsdschema) {
        this.xsdschema = xsdschema;
    }

}