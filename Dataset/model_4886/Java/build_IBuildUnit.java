





import java.util.List;
import java.util.ArrayList;

public class build_IBuildUnit extends IGenericUnit, ICapability, PropertyScope {

    private boolean circularityAllowed;
    private String filter;
    private String instanceLocation;





    private build_IBuildUnit build_ibuildunit;


    public build_IBuildUnit(
        boolean circularityAllowed,        String filter,        String instanceLocation    ) {
        super(
        );
        this.circularityAllowed = circularityAllowed;
        this.filter = filter;
        this.instanceLocation = instanceLocation;
    }


    public boolean getCircularityallowed() {
        return circularityAllowed;
    }

    public void setCircularityallowed(boolean circularityAllowed) {
        this.circularityAllowed = circularityAllowed;
    }
    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
    }
    public String getInstancelocation() {
        return instanceLocation;
    }

    public void setInstancelocation(String instanceLocation) {
        this.instanceLocation = instanceLocation;
    }

    public build_IBuildUnit getBuild_ibuildunit() {
        return build_ibuildunit;
    }

    public void setBuild_ibuildunit(build_IBuildUnit build_ibuildunit) {
        this.build_ibuildunit = build_ibuildunit;
    }

}