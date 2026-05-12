





import java.util.List;
import java.util.ArrayList;

public class build_BuildUnit extends BFunctionContainer, VersionedCapability, IVarName, IProvidedCapabilityContainer, IRequiredCapabilityContainer {

    private String documentation;
    private String executionMode;
    private String outputLocation;
    private String sourceLocation;
    private String platformFilter;





    private build_UnitResolutionInfo build_unitresolutioninfo;




    private List<build_FirstFoundUnitProvider> build_firstfoundunitproviders;




    private build_EffectiveUnitFacade build_effectiveunitfacade;




    private List<build_Repository> build_repositorys;


    public build_BuildUnit(
        String documentation,        String executionMode,        String outputLocation,        String sourceLocation,        String platformFilter    ) {
        super(
        );
        this.documentation = documentation;
        this.executionMode = executionMode;
        this.outputLocation = outputLocation;
        this.sourceLocation = sourceLocation;
        this.platformFilter = platformFilter;
        this.build_firstfoundunitproviders = new ArrayList<>();
        this.build_repositorys = new ArrayList<>();
    }

    public build_BuildUnit(
        String documentation,        String executionMode,        String outputLocation,        String sourceLocation,        String platformFilter        ArrayList<build_FirstFoundUnitProvider> build_firstfoundunitproviders,        ArrayList<build_Repository> build_repositorys    ) {
        this.documentation = documentation;
        this.executionMode = executionMode;
        this.outputLocation = outputLocation;
        this.sourceLocation = sourceLocation;
        this.platformFilter = platformFilter;
        this.build_firstfoundunitproviders = build_firstfoundunitproviders;
        this.build_repositorys = build_repositorys;
    }

    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }
    public String getExecutionmode() {
        return executionMode;
    }

    public void setExecutionmode(String executionMode) {
        this.executionMode = executionMode;
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
    public String getPlatformfilter() {
        return platformFilter;
    }

    public void setPlatformfilter(String platformFilter) {
        this.platformFilter = platformFilter;
    }

    public build_UnitResolutionInfo getBuild_unitresolutioninfo() {
        return build_unitresolutioninfo;
    }

    public void setBuild_unitresolutioninfo(build_UnitResolutionInfo build_unitresolutioninfo) {
        this.build_unitresolutioninfo = build_unitresolutioninfo;
    }
    public List<build_FirstFoundUnitProvider> getBuild_firstfoundunitproviders() {
        return build_firstfoundunitproviders;
    }

    public void addBuild_firstfoundunitprovider(Build_firstfoundunitprovider build_firstfoundunitprovider) {
        this.build_firstfoundunitproviders.add(build_firstfoundunitprovider);
    }
    public build_EffectiveUnitFacade getBuild_effectiveunitfacade() {
        return build_effectiveunitfacade;
    }

    public void setBuild_effectiveunitfacade(build_EffectiveUnitFacade build_effectiveunitfacade) {
        this.build_effectiveunitfacade = build_effectiveunitfacade;
    }
    public List<build_Repository> getBuild_repositorys() {
        return build_repositorys;
    }

    public void addBuild_repository(Build_repository build_repository) {
        this.build_repositorys.add(build_repository);
    }

}