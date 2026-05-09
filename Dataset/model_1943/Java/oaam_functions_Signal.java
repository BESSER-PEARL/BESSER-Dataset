





import java.util.List;
import java.util.ArrayList;

public class oaam_functions_Signal extends common_OaamBaseElementA, scenario_VariantDependentElementA, scenario_ModeDependentElementA {

    private int inIndex;
    private int outIndex;



    public oaam_functions_Signal(
        int inIndex,        int outIndex    ) {
        super(
        );
        this.inIndex = inIndex;
        this.outIndex = outIndex;
    }


    public int getInindex() {
        return inIndex;
    }

    public void setInindex(int inIndex) {
        this.inIndex = inIndex;
    }
    public int getOutindex() {
        return outIndex;
    }

    public void setOutindex(int outIndex) {
        this.outIndex = outIndex;
    }


}