





import java.util.List;
import java.util.ArrayList;

public class mvc_Entity extends Annotable {

    private String name;





    private List<mvc_Attribute> mvc_attributes;




    private mvc_Entity mvc_entity;




    private mvc_Association mvc_association;




    private mvc_Association mvc_association;




    private mvc_Model mvc_model;


    public mvc_Entity(
        String name    ) {
        super(
        );
        this.name = name;
        this.mvc_attributes = new ArrayList<>();
    }

    public mvc_Entity(
        String name        ArrayList<mvc_Attribute> mvc_attributes    ) {
        this.name = name;
        this.mvc_attributes = mvc_attributes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<mvc_Attribute> getMvc_attributes() {
        return mvc_attributes;
    }

    public void addMvc_attribute(Mvc_attribute mvc_attribute) {
        this.mvc_attributes.add(mvc_attribute);
    }
    public mvc_Entity getMvc_entity() {
        return mvc_entity;
    }

    public void setMvc_entity(mvc_Entity mvc_entity) {
        this.mvc_entity = mvc_entity;
    }
    public mvc_Association getMvc_association() {
        return mvc_association;
    }

    public void setMvc_association(mvc_Association mvc_association) {
        this.mvc_association = mvc_association;
    }
    public mvc_Association getMvc_association() {
        return mvc_association;
    }

    public void setMvc_association(mvc_Association mvc_association) {
        this.mvc_association = mvc_association;
    }
    public mvc_Model getMvc_model() {
        return mvc_model;
    }

    public void setMvc_model(mvc_Model mvc_model) {
        this.mvc_model = mvc_model;
    }

}