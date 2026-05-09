





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ReadExtentAction extends Action {

    private String classifier;





    private UMLModel_OutputPin umlmodel_outputpin;


    public UMLModel_ReadExtentAction(
        String classifier    ) {
        super(
        );
        this.classifier = classifier;
    }


    public String getClassifier() {
        return classifier;
    }

    public void setClassifier(String classifier) {
        this.classifier = classifier;
    }

    public UMLModel_OutputPin getUmlmodel_outputpin() {
        return umlmodel_outputpin;
    }

    public void setUmlmodel_outputpin(UMLModel_OutputPin umlmodel_outputpin) {
        this.umlmodel_outputpin = umlmodel_outputpin;
    }

}