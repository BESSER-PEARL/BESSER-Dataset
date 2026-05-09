





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Feature extends RedefinableElement {

    private String featuringClassifier;
    private String isStatic;



    public UMLModel_Feature(
        String featuringClassifier,        String isStatic    ) {
        super(
        );
        this.featuringClassifier = featuringClassifier;
        this.isStatic = isStatic;
    }


    public String getFeaturingclassifier() {
        return featuringClassifier;
    }

    public void setFeaturingclassifier(String featuringClassifier) {
        this.featuringClassifier = featuringClassifier;
    }
    public String getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(String isStatic) {
        this.isStatic = isStatic;
    }


}