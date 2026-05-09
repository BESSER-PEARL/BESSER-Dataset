





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ReadIsClassifiedObjectAction extends Action {

    private String classifier;
    private String isDirect;





    private UMLModel_OutputPin umlmodel_outputpin;


    public UMLModel_ReadIsClassifiedObjectAction(
        String classifier,        String isDirect    ) {
        super(
        );
        this.classifier = classifier;
        this.isDirect = isDirect;
    }


    public String getClassifier() {
        return classifier;
    }

    public void setClassifier(String classifier) {
        this.classifier = classifier;
    }
    public String getIsdirect() {
        return isDirect;
    }

    public void setIsdirect(String isDirect) {
        this.isDirect = isDirect;
    }

    public UMLModel_OutputPin getUmlmodel_outputpin() {
        return umlmodel_outputpin;
    }

    public void setUmlmodel_outputpin(UMLModel_OutputPin umlmodel_outputpin) {
        this.umlmodel_outputpin = umlmodel_outputpin;
    }

}