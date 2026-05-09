





import java.util.List;
import java.util.ArrayList;

public class oclinEcoreCST_ClassifierCS extends NamedElementCS {

    private String qualifiers;
    private String instanceClassName;





    private oclinEcoreCST_ClassifierCSRef oclinecorecst_classifiercsref;


    public oclinEcoreCST_ClassifierCS(
        String qualifiers,        String instanceClassName    ) {
        super(
        );
        this.qualifiers = qualifiers;
        this.instanceClassName = instanceClassName;
    }


    public String getQualifiers() {
        return qualifiers;
    }

    public void setQualifiers(String qualifiers) {
        this.qualifiers = qualifiers;
    }
    public String getInstanceclassname() {
        return instanceClassName;
    }

    public void setInstanceclassname(String instanceClassName) {
        this.instanceClassName = instanceClassName;
    }

    public oclinEcoreCST_ClassifierCSRef getOclinecorecst_classifiercsref() {
        return oclinecorecst_classifiercsref;
    }

    public void setOclinecorecst_classifiercsref(oclinEcoreCST_ClassifierCSRef oclinecorecst_classifiercsref) {
        this.oclinecorecst_classifiercsref = oclinecorecst_classifiercsref;
    }

}