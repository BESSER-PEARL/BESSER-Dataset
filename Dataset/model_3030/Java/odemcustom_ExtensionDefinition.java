





import java.util.List;
import java.util.ArrayList;

public class odemcustom_ExtensionDefinition extends NamedElement {






    private odemcustom_Module odemcustom_module;




    private List<odemcustom_Classifier> odemcustom_classifiers;


    public odemcustom_ExtensionDefinition(
    ) {
        super(
        );
        this.odemcustom_classifiers = new ArrayList<>();
    }

    public odemcustom_ExtensionDefinition(
        ArrayList<odemcustom_Classifier> odemcustom_classifiers    ) {
        this.odemcustom_classifiers = odemcustom_classifiers;
    }


    public odemcustom_Module getOdemcustom_module() {
        return odemcustom_module;
    }

    public void setOdemcustom_module(odemcustom_Module odemcustom_module) {
        this.odemcustom_module = odemcustom_module;
    }
    public List<odemcustom_Classifier> getOdemcustom_classifiers() {
        return odemcustom_classifiers;
    }

    public void addOdemcustom_classifier(Odemcustom_classifier odemcustom_classifier) {
        this.odemcustom_classifiers.add(odemcustom_classifier);
    }

}