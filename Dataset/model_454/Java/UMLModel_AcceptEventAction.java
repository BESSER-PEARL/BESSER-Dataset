





import java.util.List;
import java.util.ArrayList;

public class UMLModel_AcceptEventAction extends Action {

    private String isUnmarshall;





    private List<UMLModel_OutputPin> umlmodel_outputpins;


    public UMLModel_AcceptEventAction(
        String isUnmarshall    ) {
        super(
        );
        this.isUnmarshall = isUnmarshall;
        this.umlmodel_outputpins = new ArrayList<>();
    }

    public UMLModel_AcceptEventAction(
        String isUnmarshall        ArrayList<UMLModel_OutputPin> umlmodel_outputpins    ) {
        this.isUnmarshall = isUnmarshall;
        this.umlmodel_outputpins = umlmodel_outputpins;
    }

    public String getIsunmarshall() {
        return isUnmarshall;
    }

    public void setIsunmarshall(String isUnmarshall) {
        this.isUnmarshall = isUnmarshall;
    }

    public List<UMLModel_OutputPin> getUmlmodel_outputpins() {
        return umlmodel_outputpins;
    }

    public void addUmlmodel_outputpin(Umlmodel_outputpin umlmodel_outputpin) {
        this.umlmodel_outputpins.add(umlmodel_outputpin);
    }

}