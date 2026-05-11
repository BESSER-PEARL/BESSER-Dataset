





import java.util.List;
import java.util.ArrayList;

public class build_UnitConcernContext extends IRequiredCapabilityContainer, BuildConcernContext {

    private String outputLocation;
    private String sourceLocation;



    public build_UnitConcernContext(
        String outputLocation,        String sourceLocation    ) {
        super(
        );
        this.outputLocation = outputLocation;
        this.sourceLocation = sourceLocation;
    }


    public String getOutputlocation() {
        return outputLocation;
    }

    public void setOutputlocation(String outputLocation) {
        this.outputLocation = outputLocation;
    }
    public String getSourcelocation() {
        return sourceLocation;
    }

    public void setSourcelocation(String sourceLocation) {
        this.sourceLocation = sourceLocation;
    }


}