





import java.util.List;
import java.util.ArrayList;

public class smalluml_Attribute  {

    private String name;





    private smalluml_Class smalluml_class;




    private smalluml_Type smalluml_type;


    public smalluml_Attribute(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public smalluml_Class getSmalluml_class() {
        return smalluml_class;
    }

    public void setSmalluml_class(smalluml_Class smalluml_class) {
        this.smalluml_class = smalluml_class;
    }
    public smalluml_Type getSmalluml_type() {
        return smalluml_type;
    }

    public void setSmalluml_type(smalluml_Type smalluml_type) {
        this.smalluml_type = smalluml_type;
    }

}