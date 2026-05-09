





import java.util.List;
import java.util.ArrayList;

public class oaam_scenario_ScenarioParameterBool extends common_OaamBaseElementA, scenario_ScenarioParameterA {

    private boolean value;



    public oaam_scenario_ScenarioParameterBool(
        boolean value    ) {
        super(
        );
        this.value = value;
    }


    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }


}