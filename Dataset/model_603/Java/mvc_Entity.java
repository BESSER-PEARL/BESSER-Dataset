





import java.util.List;
import java.util.ArrayList;

public class mvc_Entity extends Annotable {

    private String name;





    private mvc_Model mvc_model;




    private List<mvc_Entity> mvc_entitys;




    private List<mvc_Attribute> mvc_attributes;


    public mvc_Entity(
        String name    ) {
        super(
        );
        this.name = name;
        this.mvc_entitys = new ArrayList<>();
        this.mvc_attributes = new ArrayList<>();
    }

    public mvc_Entity(
        String name        ArrayList<mvc_Entity> mvc_entitys,        ArrayList<mvc_Attribute> mvc_attributes    ) {
        this.name = name;
        this.mvc_entitys = mvc_entitys;
        this.mvc_attributes = mvc_attributes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mvc_Model getMvc_model() {
        return mvc_model;
    }

    public void setMvc_model(mvc_Model mvc_model) {
        this.mvc_model = mvc_model;
    }
    public List<mvc_Entity> getMvc_entitys() {
        return mvc_entitys;
    }

    public void addMvc_entity(Mvc_entity mvc_entity) {
        this.mvc_entitys.add(mvc_entity);
    }
    public List<mvc_Attribute> getMvc_attributes() {
        return mvc_attributes;
    }

    public void addMvc_attribute(Mvc_attribute mvc_attribute) {
        this.mvc_attributes.add(mvc_attribute);
    }

}