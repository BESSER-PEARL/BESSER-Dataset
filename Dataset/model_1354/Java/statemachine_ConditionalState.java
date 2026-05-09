





import java.util.List;
import java.util.ArrayList;

public class statemachine_ConditionalState extends AbstractState {

    private boolean andExpression;
    private String conditionsOrganization;



    public statemachine_ConditionalState(
        boolean andExpression,        String conditionsOrganization    ) {
        super(
        );
        this.andExpression = andExpression;
        this.conditionsOrganization = conditionsOrganization;
    }


    public boolean getAndexpression() {
        return andExpression;
    }

    public void setAndexpression(boolean andExpression) {
        this.andExpression = andExpression;
    }
    public String getConditionsorganization() {
        return conditionsOrganization;
    }

    public void setConditionsorganization(String conditionsOrganization) {
        this.conditionsOrganization = conditionsOrganization;
    }


}