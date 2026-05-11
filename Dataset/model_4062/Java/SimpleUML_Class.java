





import java.util.List;
import java.util.ArrayList;

public class SimpleUML_Class extends Classifier {






    private List<SimpleUML_Attribute> simpleuml_attributes;




    private SimpleUML_Association simpleuml_association;




    private List<SimpleUML_Class> simpleuml_classs;




    private List<SimpleUML_Association> simpleuml_associations;




    private SimpleUML_Association simpleuml_association;




    private List<SimpleUML_Association> simpleuml_associations;




    private SimpleUML_Attribute simpleuml_attribute;


    public SimpleUML_Class(
    ) {
        super(
        );
        this.simpleuml_attributes = new ArrayList<>();
        this.simpleuml_classs = new ArrayList<>();
        this.simpleuml_associations = new ArrayList<>();
        this.simpleuml_associations = new ArrayList<>();
    }

    public SimpleUML_Class(
        ArrayList<SimpleUML_Attribute> simpleuml_attributes,        ArrayList<SimpleUML_Class> simpleuml_classs,        ArrayList<SimpleUML_Association> simpleuml_associations,        ArrayList<SimpleUML_Association> simpleuml_associations    ) {
        this.simpleuml_attributes = simpleuml_attributes;
        this.simpleuml_classs = simpleuml_classs;
        this.simpleuml_associations = simpleuml_associations;
        this.simpleuml_associations = simpleuml_associations;
    }


    public List<SimpleUML_Attribute> getSimpleuml_attributes() {
        return simpleuml_attributes;
    }

    public void addSimpleuml_attribute(Simpleuml_attribute simpleuml_attribute) {
        this.simpleuml_attributes.add(simpleuml_attribute);
    }
    public SimpleUML_Association getSimpleuml_association() {
        return simpleuml_association;
    }

    public void setSimpleuml_association(SimpleUML_Association simpleuml_association) {
        this.simpleuml_association = simpleuml_association;
    }
    public List<SimpleUML_Class> getSimpleuml_classs() {
        return simpleuml_classs;
    }

    public void addSimpleuml_class(Simpleuml_class simpleuml_class) {
        this.simpleuml_classs.add(simpleuml_class);
    }
    public List<SimpleUML_Association> getSimpleuml_associations() {
        return simpleuml_associations;
    }

    public void addSimpleuml_association(Simpleuml_association simpleuml_association) {
        this.simpleuml_associations.add(simpleuml_association);
    }
    public SimpleUML_Association getSimpleuml_association() {
        return simpleuml_association;
    }

    public void setSimpleuml_association(SimpleUML_Association simpleuml_association) {
        this.simpleuml_association = simpleuml_association;
    }
    public List<SimpleUML_Association> getSimpleuml_associations() {
        return simpleuml_associations;
    }

    public void addSimpleuml_association(Simpleuml_association simpleuml_association) {
        this.simpleuml_associations.add(simpleuml_association);
    }
    public SimpleUML_Attribute getSimpleuml_attribute() {
        return simpleuml_attribute;
    }

    public void setSimpleuml_attribute(SimpleUML_Attribute simpleuml_attribute) {
        this.simpleuml_attribute = simpleuml_attribute;
    }

}