





import java.util.List;
import java.util.ArrayList;

public class UMLModel_InterfaceRealization extends Realization {

    private String realizingClassifier;
    private String contract;





    private UMLModel_BehavioredClassifier umlmodel_behavioredclassifier;


    public UMLModel_InterfaceRealization(
        String realizingClassifier,        String contract    ) {
        super(
        );
        this.realizingClassifier = realizingClassifier;
        this.contract = contract;
    }


    public String getRealizingclassifier() {
        return realizingClassifier;
    }

    public void setRealizingclassifier(String realizingClassifier) {
        this.realizingClassifier = realizingClassifier;
    }
    public String getContract() {
        return contract;
    }

    public void setContract(String contract) {
        this.contract = contract;
    }

    public UMLModel_BehavioredClassifier getUmlmodel_behavioredclassifier() {
        return umlmodel_behavioredclassifier;
    }

    public void setUmlmodel_behavioredclassifier(UMLModel_BehavioredClassifier umlmodel_behavioredclassifier) {
        this.umlmodel_behavioredclassifier = umlmodel_behavioredclassifier;
    }

}