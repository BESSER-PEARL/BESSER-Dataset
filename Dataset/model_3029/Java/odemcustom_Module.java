





import java.util.List;
import java.util.ArrayList;

public class odemcustom_Module extends EmbeddableExtensionsContainer, NamedElement {






    private List<odemcustom_Classifier> odemcustom_classifiers;




    private List<odemcustom_ExtensionDefinition> odemcustom_extensiondefinitions;




    private List<odemcustom_Procedure> odemcustom_procedures;




    private List<odemcustom_Annotation> odemcustom_annotations;


    public odemcustom_Module(
    ) {
        super(
        );
        this.odemcustom_classifiers = new ArrayList<>();
        this.odemcustom_extensiondefinitions = new ArrayList<>();
        this.odemcustom_procedures = new ArrayList<>();
        this.odemcustom_annotations = new ArrayList<>();
    }

    public odemcustom_Module(
        ArrayList<odemcustom_Classifier> odemcustom_classifiers,        ArrayList<odemcustom_ExtensionDefinition> odemcustom_extensiondefinitions,        ArrayList<odemcustom_Procedure> odemcustom_procedures,        ArrayList<odemcustom_Annotation> odemcustom_annotations    ) {
        this.odemcustom_classifiers = odemcustom_classifiers;
        this.odemcustom_extensiondefinitions = odemcustom_extensiondefinitions;
        this.odemcustom_procedures = odemcustom_procedures;
        this.odemcustom_annotations = odemcustom_annotations;
    }


    public List<odemcustom_Classifier> getOdemcustom_classifiers() {
        return odemcustom_classifiers;
    }

    public void addOdemcustom_classifier(Odemcustom_classifier odemcustom_classifier) {
        this.odemcustom_classifiers.add(odemcustom_classifier);
    }
    public List<odemcustom_ExtensionDefinition> getOdemcustom_extensiondefinitions() {
        return odemcustom_extensiondefinitions;
    }

    public void addOdemcustom_extensiondefinition(Odemcustom_extensiondefinition odemcustom_extensiondefinition) {
        this.odemcustom_extensiondefinitions.add(odemcustom_extensiondefinition);
    }
    public List<odemcustom_Procedure> getOdemcustom_procedures() {
        return odemcustom_procedures;
    }

    public void addOdemcustom_procedure(Odemcustom_procedure odemcustom_procedure) {
        this.odemcustom_procedures.add(odemcustom_procedure);
    }
    public List<odemcustom_Annotation> getOdemcustom_annotations() {
        return odemcustom_annotations;
    }

    public void addOdemcustom_annotation(Odemcustom_annotation odemcustom_annotation) {
        this.odemcustom_annotations.add(odemcustom_annotation);
    }

}