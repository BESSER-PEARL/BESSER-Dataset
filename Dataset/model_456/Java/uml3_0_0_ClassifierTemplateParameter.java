





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_ClassifierTemplateParameter extends TemplateParameter {

    private String allowSubstitutable;





    private List<uml3_0_0_Classifier> uml3_0_0_classifiers;


    public uml3_0_0_ClassifierTemplateParameter(
        String allowSubstitutable    ) {
        super(
        );
        this.allowSubstitutable = allowSubstitutable;
        this.uml3_0_0_classifiers = new ArrayList<>();
    }

    public uml3_0_0_ClassifierTemplateParameter(
        String allowSubstitutable        ArrayList<uml3_0_0_Classifier> uml3_0_0_classifiers    ) {
        this.allowSubstitutable = allowSubstitutable;
        this.uml3_0_0_classifiers = uml3_0_0_classifiers;
    }

    public String getAllowsubstitutable() {
        return allowSubstitutable;
    }

    public void setAllowsubstitutable(String allowSubstitutable) {
        this.allowSubstitutable = allowSubstitutable;
    }

    public List<uml3_0_0_Classifier> getUml3_0_0_classifiers() {
        return uml3_0_0_classifiers;
    }

    public void addUml3_0_0_classifier(Uml3_0_0_classifier uml3_0_0_classifier) {
        this.uml3_0_0_classifiers.add(uml3_0_0_classifier);
    }

}