





import java.util.List;
import java.util.ArrayList;

public class umlClass_Property extends StructuralFeature {






    private umlClass_Property umlclass_property;




    private List<umlClass_Property> umlclass_propertys;




    private umlClass_Classifier umlclass_classifier;




    private umlClass_Property umlclass_property;




    private umlClass_Classifier umlclass_classifier;


    public umlClass_Property(
    ) {
        super(
        );
        this.umlclass_propertys = new ArrayList<>();
    }

    public umlClass_Property(
        ArrayList<umlClass_Property> umlclass_propertys    ) {
        this.umlclass_propertys = umlclass_propertys;
    }


    public umlClass_Property getUmlclass_property() {
        return umlclass_property;
    }

    public void setUmlclass_property(umlClass_Property umlclass_property) {
        this.umlclass_property = umlclass_property;
    }
    public List<umlClass_Property> getUmlclass_propertys() {
        return umlclass_propertys;
    }

    public void addUmlclass_property(Umlclass_property umlclass_property) {
        this.umlclass_propertys.add(umlclass_property);
    }
    public umlClass_Classifier getUmlclass_classifier() {
        return umlclass_classifier;
    }

    public void setUmlclass_classifier(umlClass_Classifier umlclass_classifier) {
        this.umlclass_classifier = umlclass_classifier;
    }
    public umlClass_Property getUmlclass_property() {
        return umlclass_property;
    }

    public void setUmlclass_property(umlClass_Property umlclass_property) {
        this.umlclass_property = umlclass_property;
    }
    public umlClass_Classifier getUmlclass_classifier() {
        return umlclass_classifier;
    }

    public void setUmlclass_classifier(umlClass_Classifier umlclass_classifier) {
        this.umlclass_classifier = umlclass_classifier;
    }

}