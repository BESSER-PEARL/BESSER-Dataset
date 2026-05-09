





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ReadLinkObjectEndQualifierAction extends Action {

    private String qualifier;





    private UMLModel_OutputPin umlmodel_outputpin;


    public UMLModel_ReadLinkObjectEndQualifierAction(
        String qualifier    ) {
        super(
        );
        this.qualifier = qualifier;
    }


    public String getQualifier() {
        return qualifier;
    }

    public void setQualifier(String qualifier) {
        this.qualifier = qualifier;
    }

    public UMLModel_OutputPin getUmlmodel_outputpin() {
        return umlmodel_outputpin;
    }

    public void setUmlmodel_outputpin(UMLModel_OutputPin umlmodel_outputpin) {
        this.umlmodel_outputpin = umlmodel_outputpin;
    }

}