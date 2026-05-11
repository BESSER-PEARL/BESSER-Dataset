





import java.util.List;
import java.util.ArrayList;

public class sWML_Attribute  {

    private String type;
    private String name;





    private sWML_Class swml_class;


    public sWML_Attribute(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
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

    public sWML_Class getSwml_class() {
        return swml_class;
    }

    public void setSwml_class(sWML_Class swml_class) {
        this.swml_class = swml_class;
    }

}