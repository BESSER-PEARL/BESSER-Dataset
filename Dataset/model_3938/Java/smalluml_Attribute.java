





import java.util.List;
import java.util.ArrayList;

public class smalluml_Attribute  {

    private String type;
    private String name;





    private smalluml_SmallClass smalluml_smallclass;




    private smalluml_Association smalluml_association;


    public smalluml_Attribute(
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

    public smalluml_SmallClass getSmalluml_smallclass() {
        return smalluml_smallclass;
    }

    public void setSmalluml_smallclass(smalluml_SmallClass smalluml_smallclass) {
        this.smalluml_smallclass = smalluml_smallclass;
    }
    public smalluml_Association getSmalluml_association() {
        return smalluml_association;
    }

    public void setSmalluml_association(smalluml_Association smalluml_association) {
        this.smalluml_association = smalluml_association;
    }

}