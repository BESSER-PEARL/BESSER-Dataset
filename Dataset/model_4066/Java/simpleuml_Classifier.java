





import java.util.List;
import java.util.ArrayList;

public class simpleuml_Classifier extends PackageElement {






    private simpleuml_Attribute simpleuml_attribute;




    private List<simpleuml_Attribute> simpleuml_attributes;


    public simpleuml_Classifier(
    ) {
        super(
        );
        this.simpleuml_attributes = new ArrayList<>();
    }

    public simpleuml_Classifier(
        ArrayList<simpleuml_Attribute> simpleuml_attributes    ) {
        this.simpleuml_attributes = simpleuml_attributes;
    }


    public simpleuml_Attribute getSimpleuml_attribute() {
        return simpleuml_attribute;
    }

    public void setSimpleuml_attribute(simpleuml_Attribute simpleuml_attribute) {
        this.simpleuml_attribute = simpleuml_attribute;
    }
    public List<simpleuml_Attribute> getSimpleuml_attributes() {
        return simpleuml_attributes;
    }

    public void addSimpleuml_attribute(Simpleuml_attribute simpleuml_attribute) {
        this.simpleuml_attributes.add(simpleuml_attribute);
    }

}