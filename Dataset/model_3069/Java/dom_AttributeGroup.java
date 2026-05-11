





import java.util.List;
import java.util.ArrayList;

public class dom_AttributeGroup extends IDocumentable {

    private String name;
    private boolean key;
    private boolean unique;
    private boolean filter;
    private boolean sortorder;





    private List<dom_Attribute> dom_attributes;




    private dom_Entity dom_entity;




    private dom_Entity dom_entity;




    private dom_Entity dom_entity;




    private dom_Attribute dom_attribute;


    public dom_AttributeGroup(
        String name,        boolean key,        boolean unique,        boolean filter,        boolean sortorder    ) {
        super(
        );
        this.name = name;
        this.key = key;
        this.unique = unique;
        this.filter = filter;
        this.sortorder = sortorder;
        this.dom_attributes = new ArrayList<>();
    }

    public dom_AttributeGroup(
        String name,        boolean key,        boolean unique,        boolean filter,        boolean sortorder        ArrayList<dom_Attribute> dom_attributes    ) {
        this.name = name;
        this.key = key;
        this.unique = unique;
        this.filter = filter;
        this.sortorder = sortorder;
        this.dom_attributes = dom_attributes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getKey() {
        return key;
    }

    public void setKey(boolean key) {
        this.key = key;
    }
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public boolean getFilter() {
        return filter;
    }

    public void setFilter(boolean filter) {
        this.filter = filter;
    }
    public boolean getSortorder() {
        return sortorder;
    }

    public void setSortorder(boolean sortorder) {
        this.sortorder = sortorder;
    }

    public List<dom_Attribute> getDom_attributes() {
        return dom_attributes;
    }

    public void addDom_attribute(Dom_attribute dom_attribute) {
        this.dom_attributes.add(dom_attribute);
    }
    public dom_Entity getDom_entity() {
        return dom_entity;
    }

    public void setDom_entity(dom_Entity dom_entity) {
        this.dom_entity = dom_entity;
    }
    public dom_Entity getDom_entity() {
        return dom_entity;
    }

    public void setDom_entity(dom_Entity dom_entity) {
        this.dom_entity = dom_entity;
    }
    public dom_Entity getDom_entity() {
        return dom_entity;
    }

    public void setDom_entity(dom_Entity dom_entity) {
        this.dom_entity = dom_entity;
    }
    public dom_Attribute getDom_attribute() {
        return dom_attribute;
    }

    public void setDom_attribute(dom_Attribute dom_attribute) {
        this.dom_attribute = dom_attribute;
    }

}