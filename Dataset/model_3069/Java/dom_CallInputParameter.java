





import java.util.List;
import java.util.ArrayList;

public class dom_CallInputParameter  {

    private String name;





    private dom_QueryParameter dom_queryparameter;




    private dom_CallableStatement dom_callablestatement;




    private dom_Attribute dom_attribute;


    public dom_CallInputParameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dom_QueryParameter getDom_queryparameter() {
        return dom_queryparameter;
    }

    public void setDom_queryparameter(dom_QueryParameter dom_queryparameter) {
        this.dom_queryparameter = dom_queryparameter;
    }
    public dom_CallableStatement getDom_callablestatement() {
        return dom_callablestatement;
    }

    public void setDom_callablestatement(dom_CallableStatement dom_callablestatement) {
        this.dom_callablestatement = dom_callablestatement;
    }
    public dom_Attribute getDom_attribute() {
        return dom_attribute;
    }

    public void setDom_attribute(dom_Attribute dom_attribute) {
        this.dom_attribute = dom_attribute;
    }

}