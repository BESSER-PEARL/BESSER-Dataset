





import java.util.List;
import java.util.ArrayList;

public class build_BuildUnit extends VersionedCapability, BFunctionContainer, IRequiredCapabilityContainer, IVarName, IProvidedCapabilityContainer {

    private String outputLocation;
    private String platformFilter;
    private String executionMode;
    private String sourceLocation;
    private String documentation;



    public build_BuildUnit(
        String outputLocation,        String platformFilter,        String executionMode,        String sourceLocation,        String documentation    ) {
        super(
        );
        this.outputLocation = outputLocation;
        this.platformFilter = platformFilter;
        this.executionMode = executionMode;
        this.sourceLocation = sourceLocation;
        this.documentation = documentation;
    }


    public String getOutputlocation() {
        return outputLocation;
    }

    public void setOutputlocation(String outputLocation) {
        this.outputLocation = outputLocation;
    }
    public String getPlatformfilter() {
        return platformFilter;
    }

    public void setPlatformfilter(String platformFilter) {
        this.platformFilter = platformFilter;
    }
    public String getExecutionmode() {
        return executionMode;
    }

    public void setExecutionmode(String executionMode) {
        this.executionMode = executionMode;
    }
    public String getSourcelocation() {
        return sourceLocation;
    }

    public void setSourcelocation(String sourceLocation) {
        this.sourceLocation = sourceLocation;
    }
    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }


}