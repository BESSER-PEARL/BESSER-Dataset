





import java.util.List;
import java.util.ArrayList;

public class oaam_library_BusType extends library_ResourceProviderA, common_OaamBaseElementA {

    private boolean isSelfManaging;
    private float mtbf;
    private boolean requiresMaster;



    public oaam_library_BusType(
        boolean isSelfManaging,        float mtbf,        boolean requiresMaster    ) {
        super(
        );
        this.isSelfManaging = isSelfManaging;
        this.mtbf = mtbf;
        this.requiresMaster = requiresMaster;
    }


    public boolean getIsselfmanaging() {
        return isSelfManaging;
    }

    public void setIsselfmanaging(boolean isSelfManaging) {
        this.isSelfManaging = isSelfManaging;
    }
    public float getMtbf() {
        return mtbf;
    }

    public void setMtbf(float mtbf) {
        this.mtbf = mtbf;
    }
    public boolean getRequiresmaster() {
        return requiresMaster;
    }

    public void setRequiresmaster(boolean requiresMaster) {
        this.requiresMaster = requiresMaster;
    }


}