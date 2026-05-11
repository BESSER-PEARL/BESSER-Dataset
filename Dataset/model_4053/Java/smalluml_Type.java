





import java.util.List;
import java.util.ArrayList;

public class smalluml_Type extends NamedElement {






    private smalluml_Method smalluml_method;




    private smalluml_Attribute smalluml_attribute;


    public smalluml_Type(
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
    public smalluml_Attribute getSmalluml_attribute() {
        return smalluml_attribute;
    }

    public void setSmalluml_attribute(smalluml_Attribute smalluml_attribute) {
        this.smalluml_attribute = smalluml_attribute;
    }

}