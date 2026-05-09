





import java.util.List;
import java.util.ArrayList;

public class UMLModel_RedefinableTemplateSignature extends RedefinableElement, TemplateSignature {

    private String extendedSignature;
    private String classifier;
    private String inheritedParameter;



    public UMLModel_RedefinableTemplateSignature(
        String extendedSignature,        String classifier,        String inheritedParameter    ) {
        super(
        );
        this.extendedSignature = extendedSignature;
        this.classifier = classifier;
        this.inheritedParameter = inheritedParameter;
    }


    public String getExtendedsignature() {
        return extendedSignature;
    }

    public void setExtendedsignature(String extendedSignature) {
        this.extendedSignature = extendedSignature;
    }
    public String getClassifier() {
        return classifier;
    }

    public void setClassifier(String classifier) {
        this.classifier = classifier;
    }
    public String getInheritedparameter() {
        return inheritedParameter;
    }

    public void setInheritedparameter(String inheritedParameter) {
        this.inheritedParameter = inheritedParameter;
    }


}