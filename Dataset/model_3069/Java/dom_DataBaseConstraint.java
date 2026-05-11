





import java.util.List;
import java.util.ArrayList;

public class dom_DataBaseConstraint  {

    private String type;
    private String name;





    private dom_Dao dom_dao;




    private List<dom_Attribute> dom_attributes;




    private dom_Dao dom_dao;




    private List<dom_Attribute> dom_attributes;




    private dom_Dao dom_dao;


    public dom_DataBaseConstraint(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
        this.dom_attributes = new ArrayList<>();
        this.dom_attributes = new ArrayList<>();
    }

    public dom_DataBaseConstraint(
        String type,        String name        ArrayList<dom_Attribute> dom_attributes,        ArrayList<dom_Attribute> dom_attributes    ) {
        this.type = type;
        this.name = name;
        this.dom_attributes = dom_attributes;
        this.dom_attributes = dom_attributes;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dom_Dao getDom_dao() {
        return dom_dao;
    }

    public void setDom_dao(dom_Dao dom_dao) {
        this.dom_dao = dom_dao;
    }
    public List<dom_Attribute> getDom_attributes() {
        return dom_attributes;
    }

    public void addDom_attribute(Dom_attribute dom_attribute) {
        this.dom_attributes.add(dom_attribute);
    }
    public dom_Dao getDom_dao() {
        return dom_dao;
    }

    public void setDom_dao(dom_Dao dom_dao) {
        this.dom_dao = dom_dao;
    }
    public List<dom_Attribute> getDom_attributes() {
        return dom_attributes;
    }

    public void addDom_attribute(Dom_attribute dom_attribute) {
        this.dom_attributes.add(dom_attribute);
    }
    public dom_Dao getDom_dao() {
        return dom_dao;
    }

    public void setDom_dao(dom_Dao dom_dao) {
        this.dom_dao = dom_dao;
    }

}