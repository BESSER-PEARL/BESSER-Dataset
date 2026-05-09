





import java.util.List;
import java.util.ArrayList;

public class oaam_scenario_ScenarioParameterNumeric extends common_OaamBaseElementA, scenario_ScenarioParameterA {

    private float value;



    public oaam_scenario_ScenarioParameterNumeric(
        float value    ) {
        super(
        );
        this.value = value;
    }


    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }


}