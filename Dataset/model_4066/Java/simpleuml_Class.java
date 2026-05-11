





import java.util.List;
import java.util.ArrayList;

public class simpleuml_Class extends Classifier {






    private List<simpleuml_Class> simpleuml_classs;




    private List<simpleuml_Attribute> simpleuml_attributes;




    private simpleuml_Attribute simpleuml_attribute;




    private List<simpleuml_Class> simpleuml_classs;


    public simpleuml_Class(
    ) {
        super(
        );
        this.simpleuml_classs = new ArrayList<>();
        this.simpleuml_attributes = new ArrayList<>();
        this.simpleuml_classs = new ArrayList<>();
    }

    public simpleuml_Class(
        ArrayList<simpleuml_Class> simpleuml_classs,        ArrayList<simpleuml_Attribute> simpleuml_attributes,        ArrayList<simpleuml_Class> simpleuml_classs    ) {
        this.simpleuml_classs = simpleuml_classs;
        this.simpleuml_attributes = simpleuml_attributes;
        this.simpleuml_classs = simpleuml_classs;
    }


    public List<simpleuml_Class> getSimpleuml_classs() {
        return simpleuml_classs;
    }

    public void addSimpleuml_class(Simpleuml_class simpleuml_class) {
        this.simpleuml_classs.add(simpleuml_class);
    }
    public List<simpleuml_Attribute> getSimpleuml_attributes() {
        return simpleuml_attributes;
    }

    public void addSimpleuml_attribute(Simpleuml_attribute simpleuml_attribute) {
        this.simpleuml_attributes.add(simpleuml_attribute);
    }
    public simpleuml_Attribute getSimpleuml_attribute() {
        return simpleuml_attribute;
    }

    public void setSimpleuml_attribute(simpleuml_Attribute simpleuml_attribute) {
        this.simpleuml_attribute = simpleuml_attribute;
    }
    public List<simpleuml_Class> getSimpleuml_classs() {
        return simpleuml_classs;
    }

    public void addSimpleuml_class(Simpleuml_class simpleuml_class) {
        this.simpleuml_classs.add(simpleuml_class);
    }

}