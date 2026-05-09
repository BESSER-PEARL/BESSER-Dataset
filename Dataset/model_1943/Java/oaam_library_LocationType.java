





import java.util.List;
import java.util.ArrayList;

public class oaam_library_LocationType extends library_ResourceProviderA, common_OaamBaseElementA {

    private boolean isJoint;



    public oaam_library_LocationType(
        boolean isJoint    ) {
        super(
        );
        this.isJoint = isJoint;
    }


    public boolean getIsjoint() {
        return isJoint;
    }

    public void setIsjoint(boolean isJoint) {
        this.isJoint = isJoint;
    }


}