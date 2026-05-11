





import java.util.List;
import java.util.ArrayList;

public class dom_ComplexType extends Type, ModelElement {






    private List<dom_Attribute> dom_attributes;




    private dom_Mapper dom_mapper;




    private dom_Mapper dom_mapper;




    private List<dom_Attribute> dom_attributes;


    public dom_ComplexType(
    ) {
        super(
        );
        this.dom_attributes = new ArrayList<>();
        this.dom_attributes = new ArrayList<>();
    }

    public dom_ComplexType(
        ArrayList<dom_Attribute> dom_attributes,        ArrayList<dom_Attribute> dom_attributes    ) {
        this.dom_attributes = dom_attributes;
        this.dom_attributes = dom_attributes;
    }


    public List<dom_Attribute> getDom_attributes() {
        return dom_attributes;
    }

    public void addDom_attribute(Dom_attribute dom_attribute) {
        this.dom_attributes.add(dom_attribute);
    }
    public dom_Mapper getDom_mapper() {
        return dom_mapper;
    }

    public void setDom_mapper(dom_Mapper dom_mapper) {
        this.dom_mapper = dom_mapper;
    }
    public dom_Mapper getDom_mapper() {
        return dom_mapper;
    }

    public void setDom_mapper(dom_Mapper dom_mapper) {
        this.dom_mapper = dom_mapper;
    }
    public List<dom_Attribute> getDom_attributes() {
        return dom_attributes;
    }

    public void addDom_attribute(Dom_attribute dom_attribute) {
        this.dom_attributes.add(dom_attribute);
    }

}