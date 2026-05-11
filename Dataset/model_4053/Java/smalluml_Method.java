





import java.util.List;
import java.util.ArrayList;

public class smalluml_Method extends NamedElement {






    private List<smalluml_Attribute> smalluml_attributes;




    private smalluml_Class smalluml_class;


    public smalluml_Method(
    ) {
        super(
        );
        this.smalluml_attributes = new ArrayList<>();
    }

    public smalluml_Method(
        ArrayList<smalluml_Attribute> smalluml_attributes    ) {
        this.smalluml_attributes = smalluml_attributes;
    }


    public List<smalluml_Attribute> getSmalluml_attributes() {
        return smalluml_attributes;
    }

    public void addSmalluml_attribute(Smalluml_attribute smalluml_attribute) {
        this.smalluml_attributes.add(smalluml_attribute);
    }
    public smalluml_Class getSmalluml_class() {
        return smalluml_class;
    }

    public void setSmalluml_class(smalluml_Class smalluml_class) {
        this.smalluml_class = smalluml_class;
    }

}