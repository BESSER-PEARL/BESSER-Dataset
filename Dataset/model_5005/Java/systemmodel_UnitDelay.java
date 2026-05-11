





import java.util.List;
import java.util.ArrayList;

public class systemmodel_UnitDelay extends Block {

    private String initialCondition;



    public systemmodel_UnitDelay(
        String initialCondition    ) {
        super(
        );
        this.initialCondition = initialCondition;
    }


    public String getInitialcondition() {
        return initialCondition;
    }

    public void setInitialcondition(String initialCondition) {
        this.initialCondition = initialCondition;
    }


}