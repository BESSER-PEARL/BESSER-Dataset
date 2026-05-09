





import java.util.List;
import java.util.ArrayList;

public class oaam_allocations_MessageA extends common_OaamBaseElementA, scenario_VariantDependentElementA, scenario_ModeDependentElementA {

    private boolean isPersistent;
    private int length;



    public oaam_allocations_MessageA(
        boolean isPersistent,        int length    ) {
        super(
        );
        this.isPersistent = isPersistent;
        this.length = length;
    }


    public boolean getIspersistent() {
        return isPersistent;
    }

    public void setIspersistent(boolean isPersistent) {
        this.isPersistent = isPersistent;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }


}