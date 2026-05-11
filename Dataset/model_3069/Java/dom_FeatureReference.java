





import java.util.List;
import java.util.ArrayList;

public class dom_FeatureReference extends IDocumentable, PresentableFeature {

    private boolean all;





    private List<dom_AttributeProperty> dom_attributepropertys;




    private dom_Attribute dom_attribute;




    private dom_Entity dom_entity;




    private dom_DataView dom_dataview;




    private dom_Attribute dom_attribute;




    private dom_DataView dom_dataview;


    public dom_FeatureReference(
        boolean all    ) {
        super(
        );
        this.all = all;
        this.dom_attributepropertys = new ArrayList<>();
    }

    public dom_FeatureReference(
        boolean all        ArrayList<dom_AttributeProperty> dom_attributepropertys    ) {
        this.all = all;
        this.dom_attributepropertys = dom_attributepropertys;
    }

    public boolean getAll() {
        return all;
    }

    public void setAll(boolean all) {
        this.all = all;
    }

    public List<dom_AttributeProperty> getDom_attributepropertys() {
        return dom_attributepropertys;
    }

    public void addDom_attributeproperty(Dom_attributeproperty dom_attributeproperty) {
        this.dom_attributepropertys.add(dom_attributeproperty);
    }
    public dom_Attribute getDom_attribute() {
        return dom_attribute;
    }

    public void setDom_attribute(dom_Attribute dom_attribute) {
        this.dom_attribute = dom_attribute;
    }
    public dom_Entity getDom_entity() {
        return dom_entity;
    }

    public void setDom_entity(dom_Entity dom_entity) {
        this.dom_entity = dom_entity;
    }
    public dom_DataView getDom_dataview() {
        return dom_dataview;
    }

    public void setDom_dataview(dom_DataView dom_dataview) {
        this.dom_dataview = dom_dataview;
    }
    public dom_Attribute getDom_attribute() {
        return dom_attribute;
    }

    public void setDom_attribute(dom_Attribute dom_attribute) {
        this.dom_attribute = dom_attribute;
    }
    public dom_DataView getDom_dataview() {
        return dom_dataview;
    }

    public void setDom_dataview(dom_DataView dom_dataview) {
        this.dom_dataview = dom_dataview;
    }

}