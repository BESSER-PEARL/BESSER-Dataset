





import java.util.List;
import java.util.ArrayList;

public class Actions_IntermediateActions_ValueSpecificationAction extends Action {






    private ValueSpecification valuespecification;




    private OutputPin outputpin;


    public Actions_IntermediateActions_ValueSpecificationAction(
    ) {
        super(
        );
    }



    public ValueSpecification getValuespecification() {
        return valuespecification;
    }

    public void setValuespecification(ValueSpecification valuespecification) {
        this.valuespecification = valuespecification;
    }
    public OutputPin getOutputpin() {
        return outputpin;
    }

    public void setOutputpin(OutputPin outputpin) {
        this.outputpin = outputpin;
    }

}