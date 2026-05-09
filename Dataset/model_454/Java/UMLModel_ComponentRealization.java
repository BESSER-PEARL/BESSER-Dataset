





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ComponentRealization extends Realization {

    private String realizingClassifier;
    private String abstraction;





    private UMLModel_Component umlmodel_component;


    public UMLModel_ComponentRealization(
        String realizingClassifier,        String abstraction    ) {
        super(
        );
        this.realizingClassifier = realizingClassifier;
        this.abstraction = abstraction;
    }


    public String getRealizingclassifier() {
        return realizingClassifier;
    }

    public void setRealizingclassifier(String realizingClassifier) {
        this.realizingClassifier = realizingClassifier;
    }
    public String getAbstraction() {
        return abstraction;
    }

    public void setAbstraction(String abstraction) {
        this.abstraction = abstraction;
    }

    public UMLModel_Component getUmlmodel_component() {
        return umlmodel_component;
    }

    public void setUmlmodel_component(UMLModel_Component umlmodel_component) {
        this.umlmodel_component = umlmodel_component;
    }

}