





import java.util.List;
import java.util.ArrayList;

public class UMLModel_CallAction extends InvocationAction {

    private String isSynchronous;





    private List<UMLModel_OutputPin> umlmodel_outputpins;


    public UMLModel_CallAction(
        String isSynchronous    ) {
        super(
        );
        this.isSynchronous = isSynchronous;
        this.umlmodel_outputpins = new ArrayList<>();
    }

    public UMLModel_CallAction(
        String isSynchronous        ArrayList<UMLModel_OutputPin> umlmodel_outputpins    ) {
        this.isSynchronous = isSynchronous;
        this.umlmodel_outputpins = umlmodel_outputpins;
    }

    public String getIssynchronous() {
        return isSynchronous;
    }

    public void setIssynchronous(String isSynchronous) {
        this.isSynchronous = isSynchronous;
    }

    public List<UMLModel_OutputPin> getUmlmodel_outputpins() {
        return umlmodel_outputpins;
    }

    public void addUmlmodel_outputpin(Umlmodel_outputpin umlmodel_outputpin) {
        this.umlmodel_outputpins.add(umlmodel_outputpin);
    }

}