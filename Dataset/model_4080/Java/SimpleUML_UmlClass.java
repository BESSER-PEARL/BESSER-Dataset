





import java.util.List;
import java.util.ArrayList;

public class SimpleUML_UmlClass extends UmlClassifier {






    private List<SimpleUML_UmlAssociation> simpleuml_umlassociations;




    private List<SimpleUML_UmlAssociation> simpleuml_umlassociations;




    private List<SimpleUML_UmlAttribute> simpleuml_umlattributes;




    private List<SimpleUML_UmlClass> simpleuml_umlclasss;




    private SimpleUML_UmlAssociation simpleuml_umlassociation;




    private SimpleUML_UmlAttribute simpleuml_umlattribute;




    private SimpleUML_UmlClass simpleuml_umlclass;




    private SimpleUML_UmlAssociation simpleuml_umlassociation;


    public SimpleUML_UmlClass(
    ) {
        super(
        );
        this.simpleuml_umlassociations = new ArrayList<>();
        this.simpleuml_umlassociations = new ArrayList<>();
        this.simpleuml_umlattributes = new ArrayList<>();
        this.simpleuml_umlclasss = new ArrayList<>();
    }

    public SimpleUML_UmlClass(
        ArrayList<SimpleUML_UmlAssociation> simpleuml_umlassociations,        ArrayList<SimpleUML_UmlAssociation> simpleuml_umlassociations,        ArrayList<SimpleUML_UmlAttribute> simpleuml_umlattributes,        ArrayList<SimpleUML_UmlClass> simpleuml_umlclasss    ) {
        this.simpleuml_umlassociations = simpleuml_umlassociations;
        this.simpleuml_umlassociations = simpleuml_umlassociations;
        this.simpleuml_umlattributes = simpleuml_umlattributes;
        this.simpleuml_umlclasss = simpleuml_umlclasss;
    }


    public List<SimpleUML_UmlAssociation> getSimpleuml_umlassociations() {
        return simpleuml_umlassociations;
    }

    public void addSimpleuml_umlassociation(Simpleuml_umlassociation simpleuml_umlassociation) {
        this.simpleuml_umlassociations.add(simpleuml_umlassociation);
    }
    public List<SimpleUML_UmlAssociation> getSimpleuml_umlassociations() {
        return simpleuml_umlassociations;
    }

    public void addSimpleuml_umlassociation(Simpleuml_umlassociation simpleuml_umlassociation) {
        this.simpleuml_umlassociations.add(simpleuml_umlassociation);
    }
    public List<SimpleUML_UmlAttribute> getSimpleuml_umlattributes() {
        return simpleuml_umlattributes;
    }

    public void addSimpleuml_umlattribute(Simpleuml_umlattribute simpleuml_umlattribute) {
        this.simpleuml_umlattributes.add(simpleuml_umlattribute);
    }
    public List<SimpleUML_UmlClass> getSimpleuml_umlclasss() {
        return simpleuml_umlclasss;
    }

    public void addSimpleuml_umlclass(Simpleuml_umlclass simpleuml_umlclass) {
        this.simpleuml_umlclasss.add(simpleuml_umlclass);
    }
    public SimpleUML_UmlAssociation getSimpleuml_umlassociation() {
        return simpleuml_umlassociation;
    }

    public void setSimpleuml_umlassociation(SimpleUML_UmlAssociation simpleuml_umlassociation) {
        this.simpleuml_umlassociation = simpleuml_umlassociation;
    }
    public SimpleUML_UmlAttribute getSimpleuml_umlattribute() {
        return simpleuml_umlattribute;
    }

    public void setSimpleuml_umlattribute(SimpleUML_UmlAttribute simpleuml_umlattribute) {
        this.simpleuml_umlattribute = simpleuml_umlattribute;
    }
    public SimpleUML_UmlClass getSimpleuml_umlclass() {
        return simpleuml_umlclass;
    }

    public void setSimpleuml_umlclass(SimpleUML_UmlClass simpleuml_umlclass) {
        this.simpleuml_umlclass = simpleuml_umlclass;
    }
    public SimpleUML_UmlAssociation getSimpleuml_umlassociation() {
        return simpleuml_umlassociation;
    }

    public void setSimpleuml_umlassociation(SimpleUML_UmlAssociation simpleuml_umlassociation) {
        this.simpleuml_umlassociation = simpleuml_umlassociation;
    }

}