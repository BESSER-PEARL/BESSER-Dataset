





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ClassifierTemplateParameter extends TemplateParameter {

    private String allowSubstitutable;
    private String defaultClassifier;
    private String constrainingClassifier;



    public UMLModel_ClassifierTemplateParameter(
        String allowSubstitutable,        String defaultClassifier,        String constrainingClassifier    ) {
        super(
        );
        this.allowSubstitutable = allowSubstitutable;
        this.defaultClassifier = defaultClassifier;
        this.constrainingClassifier = constrainingClassifier;
    }


    public String getAllowsubstitutable() {
        return allowSubstitutable;
    }

    public void setAllowsubstitutable(String allowSubstitutable) {
        this.allowSubstitutable = allowSubstitutable;
    }
    public String getDefaultclassifier() {
        return defaultClassifier;
    }

    public void setDefaultclassifier(String defaultClassifier) {
        this.defaultClassifier = defaultClassifier;
    }
    public String getConstrainingclassifier() {
        return constrainingClassifier;
    }

    public void setConstrainingclassifier(String constrainingClassifier) {
        this.constrainingClassifier = constrainingClassifier;
    }


}