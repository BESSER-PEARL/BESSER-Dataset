





import java.util.List;
import java.util.ArrayList;

public class oaam_functions_Input extends common_OaamBaseElementA, scenario_VariantDependentElementA, scenario_ModeDependentElementA {

    private int queueLength;



    public oaam_functions_Input(
        int queueLength    ) {
        super(
        );
        this.queueLength = queueLength;
    }


    public int getQueuelength() {
        return queueLength;
    }

    public void setQueuelength(int queueLength) {
        this.queueLength = queueLength;
    }


}