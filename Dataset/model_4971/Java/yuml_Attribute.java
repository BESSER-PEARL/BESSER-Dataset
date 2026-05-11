





import java.util.List;
import java.util.ArrayList;

public class yuml_Attribute extends ClassMember {

    private String stereotype;
    private String type;





    private yuml_Class yuml_class;


    public yuml_Attribute(
        String stereotype,        String type    ) {
        super(
        );
        this.stereotype = stereotype;
        this.type = type;
    }


    public String getStereotype() {
        return stereotype;
    }

    public void setStereotype(String stereotype) {
        this.stereotype = stereotype;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public yuml_Class getYuml_class() {
        return yuml_class;
    }

    public void setYuml_class(yuml_Class yuml_class) {
        this.yuml_class = yuml_class;
    }

}