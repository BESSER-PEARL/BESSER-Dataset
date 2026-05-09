





import java.util.List;
import java.util.ArrayList;

public class UML2_ConditionalNode extends StructuredActivityNode {

    private boolean isAssured;
    private boolean isDeterminate;





    private List<UML2_OutputPin> uml2_outputpins;


    public UML2_ConditionalNode(
        boolean isAssured,        boolean isDeterminate    ) {
        super(
        );
        this.isAssured = isAssured;
        this.isDeterminate = isDeterminate;
        this.uml2_outputpins = new ArrayList<>();
    }

    public UML2_ConditionalNode(
        boolean isAssured,        boolean isDeterminate        ArrayList<UML2_OutputPin> uml2_outputpins    ) {
        this.isAssured = isAssured;
        this.isDeterminate = isDeterminate;
        this.uml2_outputpins = uml2_outputpins;
    }

    public boolean getIsassured() {
        return isAssured;
    }

    public void setIsassured(boolean isAssured) {
        this.isAssured = isAssured;
    }
    public boolean getIsdeterminate() {
        return isDeterminate;
    }

    public void setIsdeterminate(boolean isDeterminate) {
        this.isDeterminate = isDeterminate;
    }

    public List<UML2_OutputPin> getUml2_outputpins() {
        return uml2_outputpins;
    }

    public void addUml2_outputpin(Uml2_outputpin uml2_outputpin) {
        this.uml2_outputpins.add(uml2_outputpin);
    }

}