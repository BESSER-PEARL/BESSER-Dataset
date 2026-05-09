





import java.util.List;
import java.util.ArrayList;

public class oaam_functions_OutputIntegrityState extends common_OaamBaseElementA, scenario_ModeDependentElementA, scenario_VariantDependentElementA, common_BoolA {

    private String state;



    public oaam_functions_OutputIntegrityState(
        String state    ) {
        super(
        );
        this.state = state;
    }


    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }


}