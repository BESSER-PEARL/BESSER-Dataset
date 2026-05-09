





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ReadLinkObjectEndAction extends Action {

    private String end;





    private UMLModel_OutputPin umlmodel_outputpin;


    public UMLModel_ReadLinkObjectEndAction(
        String end    ) {
        super(
        );
        this.end = end;
    }


    public String getEnd() {
        return end;
    }

    public void setEnd(String end) {
        this.end = end;
    }

    public UMLModel_OutputPin getUmlmodel_outputpin() {
        return umlmodel_outputpin;
    }

    public void setUmlmodel_outputpin(UMLModel_OutputPin umlmodel_outputpin) {
        this.umlmodel_outputpin = umlmodel_outputpin;
    }

}