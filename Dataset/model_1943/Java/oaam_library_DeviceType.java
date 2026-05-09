





import java.util.List;
import java.util.ArrayList;

public class oaam_library_DeviceType extends library_ResourceProviderA, common_OaamBaseElementA, library_ResourceConsumerA {

    private boolean isSelfManaging;
    private boolean canHaveSubdevices;
    private float mtbf;
    private boolean isSubdevice;
    private float cost;
    private float weight;



    public oaam_library_DeviceType(
        boolean isSelfManaging,        boolean canHaveSubdevices,        float mtbf,        boolean isSubdevice,        float cost,        float weight    ) {
        super(
        );
        this.isSelfManaging = isSelfManaging;
        this.canHaveSubdevices = canHaveSubdevices;
        this.mtbf = mtbf;
        this.isSubdevice = isSubdevice;
        this.cost = cost;
        this.weight = weight;
    }


    public boolean getIsselfmanaging() {
        return isSelfManaging;
    }

    public void setIsselfmanaging(boolean isSelfManaging) {
        this.isSelfManaging = isSelfManaging;
    }
    public boolean getCanhavesubdevices() {
        return canHaveSubdevices;
    }

    public void setCanhavesubdevices(boolean canHaveSubdevices) {
        this.canHaveSubdevices = canHaveSubdevices;
    }
    public float getMtbf() {
        return mtbf;
    }

    public void setMtbf(float mtbf) {
        this.mtbf = mtbf;
    }
    public boolean getIssubdevice() {
        return isSubdevice;
    }

    public void setIssubdevice(boolean isSubdevice) {
        this.isSubdevice = isSubdevice;
    }
    public float getCost() {
        return cost;
    }

    public void setCost(float cost) {
        this.cost = cost;
    }
    public float getWeight() {
        return weight;
    }

    public void setWeight(float weight) {
        this.weight = weight;
    }


}