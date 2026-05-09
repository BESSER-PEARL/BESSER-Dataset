





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ReduceAction extends Action {

    private String isOrdered;
    private String reducer;





    private UMLModel_OutputPin umlmodel_outputpin;


    public UMLModel_ReduceAction(
        String isOrdered,        String reducer    ) {
        super(
        );
        this.isOrdered = isOrdered;
        this.reducer = reducer;
    }


    public String getIsordered() {
        return isOrdered;
    }

    public void setIsordered(String isOrdered) {
        this.isOrdered = isOrdered;
    }
    public String getReducer() {
        return reducer;
    }

    public void setReducer(String reducer) {
        this.reducer = reducer;
    }

    public UMLModel_OutputPin getUmlmodel_outputpin() {
        return umlmodel_outputpin;
    }

    public void setUmlmodel_outputpin(UMLModel_OutputPin umlmodel_outputpin) {
        this.umlmodel_outputpin = umlmodel_outputpin;
    }

}