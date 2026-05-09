





import java.util.List;
import java.util.ArrayList;

public class UMLModel_UnmarshallAction extends Action {

    private String unmarshallType;





    private List<UMLModel_OutputPin> umlmodel_outputpins;


    public UMLModel_UnmarshallAction(
        String unmarshallType    ) {
        super(
        );
        this.unmarshallType = unmarshallType;
        this.umlmodel_outputpins = new ArrayList<>();
    }

    public UMLModel_UnmarshallAction(
        String unmarshallType        ArrayList<UMLModel_OutputPin> umlmodel_outputpins    ) {
        this.unmarshallType = unmarshallType;
        this.umlmodel_outputpins = umlmodel_outputpins;
    }

    public String getUnmarshalltype() {
        return unmarshallType;
    }

    public void setUnmarshalltype(String unmarshallType) {
        this.unmarshallType = unmarshallType;
    }

    public List<UMLModel_OutputPin> getUmlmodel_outputpins() {
        return umlmodel_outputpins;
    }

    public void addUmlmodel_outputpin(Umlmodel_outputpin umlmodel_outputpin) {
        this.umlmodel_outputpins.add(umlmodel_outputpin);
    }

}