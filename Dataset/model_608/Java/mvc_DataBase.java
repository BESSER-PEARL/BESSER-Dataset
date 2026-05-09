





import java.util.List;
import java.util.ArrayList;

public class mvc_DataBase extends Model {






    private List<mvc_Attribute> mvc_attributes;


    public mvc_DataBase(
    ) {
        super(
        );
        this.mvc_attributes = new ArrayList<>();
    }

    public mvc_DataBase(
        ArrayList<mvc_Attribute> mvc_attributes    ) {
        this.mvc_attributes = mvc_attributes;
    }


    public List<mvc_Attribute> getMvc_attributes() {
        return mvc_attributes;
    }

    public void addMvc_attribute(Mvc_attribute mvc_attribute) {
        this.mvc_attributes.add(mvc_attribute);
    }

}