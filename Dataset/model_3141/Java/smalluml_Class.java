





import java.util.List;
import java.util.ArrayList;

public class smalluml_Class extends NamedElement {






    private List<smalluml_Class> smalluml_classs;




    private List<smalluml_Attribute> smalluml_attributes;




    private List<smalluml_Method> smalluml_methods;


    public smalluml_Class(
    ) {
        super(
        );
        this.smalluml_classs = new ArrayList<>();
        this.smalluml_attributes = new ArrayList<>();
        this.smalluml_methods = new ArrayList<>();
    }

    public smalluml_Class(
        ArrayList<smalluml_Class> smalluml_classs,        ArrayList<smalluml_Attribute> smalluml_attributes,        ArrayList<smalluml_Method> smalluml_methods    ) {
        this.smalluml_classs = smalluml_classs;
        this.smalluml_attributes = smalluml_attributes;
        this.smalluml_methods = smalluml_methods;
    }


    public List<smalluml_Class> getSmalluml_classs() {
        return smalluml_classs;
    }

    public void addSmalluml_class(Smalluml_class smalluml_class) {
        this.smalluml_classs.add(smalluml_class);
    }
    public List<smalluml_Attribute> getSmalluml_attributes() {
        return smalluml_attributes;
    }

    public void addSmalluml_attribute(Smalluml_attribute smalluml_attribute) {
        this.smalluml_attributes.add(smalluml_attribute);
    }
    public List<smalluml_Method> getSmalluml_methods() {
        return smalluml_methods;
    }

    public void addSmalluml_method(Smalluml_method smalluml_method) {
        this.smalluml_methods.add(smalluml_method);
    }

}