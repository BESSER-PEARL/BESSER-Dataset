





import java.util.List;
import java.util.ArrayList;

public class uml_ClassifierTemplateParameter extends TemplateParameter {

    private String allowSubstitutable;





    private List<uml_Classifier> uml_classifiers;


    public uml_ClassifierTemplateParameter(
        String allowSubstitutable    ) {
        super(
        );
        this.allowSubstitutable = allowSubstitutable;
        this.uml_classifiers = new ArrayList<>();
    }

    public uml_ClassifierTemplateParameter(
        String allowSubstitutable        ArrayList<uml_Classifier> uml_classifiers    ) {
        this.allowSubstitutable = allowSubstitutable;
        this.uml_classifiers = uml_classifiers;
    }

    public String getAllowsubstitutable() {
        return allowSubstitutable;
    }

    public void setAllowsubstitutable(String allowSubstitutable) {
        this.allowSubstitutable = allowSubstitutable;
    }

    public List<uml_Classifier> getUml_classifiers() {
        return uml_classifiers;
    }

    public void addUml_classifier(Uml_classifier uml_classifier) {
        this.uml_classifiers.add(uml_classifier);
    }

}