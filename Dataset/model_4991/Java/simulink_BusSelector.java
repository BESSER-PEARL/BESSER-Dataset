





import java.util.List;
import java.util.ArrayList;

public class simulink_BusSelector extends BusSpecification {

    private boolean outputAsBus;



    public simulink_BusSelector(
        boolean outputAsBus    ) {
        super(
        );
        this.outputAsBus = outputAsBus;
    }


    public boolean getOutputasbus() {
        return outputAsBus;
    }

    public void setOutputasbus(boolean outputAsBus) {
        this.outputAsBus = outputAsBus;
    }


}