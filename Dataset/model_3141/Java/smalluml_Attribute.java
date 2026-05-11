





import java.util.List;
import java.util.ArrayList;

public class smalluml_Attribute extends NamedElement {






    private smalluml_Method smalluml_method;




    private smalluml_Type smalluml_type;


    public smalluml_Attribute(
    ) {
        super(
        );
    }



    public smalluml_Method getSmalluml_method() {
        return smalluml_method;
    }

    public void setSmalluml_method(smalluml_Method smalluml_method) {
        this.smalluml_method = smalluml_method;
    }
    public smalluml_Type getSmalluml_type() {
        return smalluml_type;
    }

    public void setSmalluml_type(smalluml_Type smalluml_type) {
        this.smalluml_type = smalluml_type;
    }

}