





import java.util.List;
import java.util.ArrayList;

public class SimpleUML_UmlClassifier extends UmlPackageElement {






    private List<SimpleUML_UmlAttribute> simpleuml_umlattributes;




    private SimpleUML_UmlAttribute simpleuml_umlattribute;


    public SimpleUML_UmlClassifier(
    ) {
        super(
        );
        this.simpleuml_umlattributes = new ArrayList<>();
    }

    public SimpleUML_UmlClassifier(
        ArrayList<SimpleUML_UmlAttribute> simpleuml_umlattributes    ) {
        this.simpleuml_umlattributes = simpleuml_umlattributes;
    }


    public List<SimpleUML_UmlAttribute> getSimpleuml_umlattributes() {
        return simpleuml_umlattributes;
    }

    public void addSimpleuml_umlattribute(Simpleuml_umlattribute simpleuml_umlattribute) {
        this.simpleuml_umlattributes.add(simpleuml_umlattribute);
    }
    public SimpleUML_UmlAttribute getSimpleuml_umlattribute() {
        return simpleuml_umlattribute;
    }

    public void setSimpleuml_umlattribute(SimpleUML_UmlAttribute simpleuml_umlattribute) {
        this.simpleuml_umlattribute = simpleuml_umlattribute;
    }

}