





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Substitution extends Realization {

    private String substitutingClassifier;
    private String contract;





    private UMLModel_Classifier umlmodel_classifier;


    public UMLModel_Substitution(
        String substitutingClassifier,        String contract    ) {
        super(
        );
        this.substitutingClassifier = substitutingClassifier;
        this.contract = contract;
    }


    public String getSubstitutingclassifier() {
        return substitutingClassifier;
    }

    public void setSubstitutingclassifier(String substitutingClassifier) {
        this.substitutingClassifier = substitutingClassifier;
    }
    public String getContract() {
        return contract;
    }

    public void setContract(String contract) {
        this.contract = contract;
    }

    public UMLModel_Classifier getUmlmodel_classifier() {
        return umlmodel_classifier;
    }

    public void setUmlmodel_classifier(UMLModel_Classifier umlmodel_classifier) {
        this.umlmodel_classifier = umlmodel_classifier;
    }

}