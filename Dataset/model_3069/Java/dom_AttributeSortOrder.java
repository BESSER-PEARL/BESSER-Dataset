





import java.util.List;
import java.util.ArrayList;

public class dom_AttributeSortOrder  {

    private boolean asc;
    private boolean desc;





    private dom_AttributeGroup dom_attributegroup;




    private dom_Attribute dom_attribute;


    public dom_AttributeSortOrder(
        boolean asc,        boolean desc    ) {
        this.asc = asc;
        this.desc = desc;
    }


    public boolean getAsc() {
        return asc;
    }

    public void setAsc(boolean asc) {
        this.asc = asc;
    }
    public boolean getDesc() {
        return desc;
    }

    public void setDesc(boolean desc) {
        this.desc = desc;
    }

    public dom_AttributeGroup getDom_attributegroup() {
        return dom_attributegroup;
    }

    public void setDom_attributegroup(dom_AttributeGroup dom_attributegroup) {
        this.dom_attributegroup = dom_attributegroup;
    }
    public dom_Attribute getDom_attribute() {
        return dom_attribute;
    }

    public void setDom_attribute(dom_Attribute dom_attribute) {
        this.dom_attribute = dom_attribute;
    }

}