





import java.util.List;
import java.util.ArrayList;

public class classes_Attribute extends NamedElement {

    private boolean isMany;





    private classes_Classifier classes_classifier;


    public classes_Attribute(
        boolean isMany    ) {
        super(
        );
        this.isMany = isMany;
    }


    public boolean getIsmany() {
        return isMany;
    }

    public void setIsmany(boolean isMany) {
        this.isMany = isMany;
    }

    public classes_Classifier getClasses_classifier() {
        return classes_classifier;
    }

    public void setClasses_classifier(classes_Classifier classes_classifier) {
        this.classes_classifier = classes_classifier;
    }

}