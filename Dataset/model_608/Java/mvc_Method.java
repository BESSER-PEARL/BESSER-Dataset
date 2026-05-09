





import java.util.List;
import java.util.ArrayList;

public class mvc_Method  {

    private String type;
    private String namemethod;





    private List<mvc_Attribute> mvc_attributes;


    public mvc_Method(
        String type,        String namemethod    ) {
        this.type = type;
        this.namemethod = namemethod;
        this.mvc_attributes = new ArrayList<>();
    }

    public mvc_Method(
        String type,        String namemethod        ArrayList<mvc_Attribute> mvc_attributes    ) {
        this.type = type;
        this.namemethod = namemethod;
        this.mvc_attributes = mvc_attributes;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getNamemethod() {
        return namemethod;
    }

    public void setNamemethod(String namemethod) {
        this.namemethod = namemethod;
    }

    public List<mvc_Attribute> getMvc_attributes() {
        return mvc_attributes;
    }

    public void addMvc_attribute(Mvc_attribute mvc_attribute) {
        this.mvc_attributes.add(mvc_attribute);
    }

}