





import java.util.List;
import java.util.ArrayList;

public class build_UnitConcernContext extends BuildConcernContext, IRequiredCapabilityContainer {

    private String sourceLocation;
    private String outputLocation;





    private List<build_BuilderConcernContext> build_builderconcerncontexts;




    private List<build_CapabilityPredicate> build_capabilitypredicates;




    private List<build_ProvidesPredicate> build_providespredicates;




    private List<build_RequiresPredicate> build_requirespredicates;


    public build_UnitConcernContext(
        String sourceLocation,        String outputLocation    ) {
        super(
        );
        this.sourceLocation = sourceLocation;
        this.outputLocation = outputLocation;
        this.build_builderconcerncontexts = new ArrayList<>();
        this.build_capabilitypredicates = new ArrayList<>();
        this.build_providespredicates = new ArrayList<>();
        this.build_requirespredicates = new ArrayList<>();
    }

    public build_UnitConcernContext(
        String sourceLocation,        String outputLocation        ArrayList<build_BuilderConcernContext> build_builderconcerncontexts,        ArrayList<build_CapabilityPredicate> build_capabilitypredicates,        ArrayList<build_ProvidesPredicate> build_providespredicates,        ArrayList<build_RequiresPredicate> build_requirespredicates    ) {
        this.sourceLocation = sourceLocation;
        this.outputLocation = outputLocation;
        this.build_builderconcerncontexts = build_builderconcerncontexts;
        this.build_capabilitypredicates = build_capabilitypredicates;
        this.build_providespredicates = build_providespredicates;
        this.build_requirespredicates = build_requirespredicates;
    }

    public String getSourcelocation() {
        return sourceLocation;
    }

    public void setSourcelocation(String sourceLocation) {
        this.sourceLocation = sourceLocation;
    }
    public String getOutputlocation() {
        return outputLocation;
    }

    public void setOutputlocation(String outputLocation) {
        this.outputLocation = outputLocation;
    }

    public List<build_BuilderConcernContext> getBuild_builderconcerncontexts() {
        return build_builderconcerncontexts;
    }

    public void addBuild_builderconcerncontext(Build_builderconcerncontext build_builderconcerncontext) {
        this.build_builderconcerncontexts.add(build_builderconcerncontext);
    }
    public List<build_CapabilityPredicate> getBuild_capabilitypredicates() {
        return build_capabilitypredicates;
    }

    public void addBuild_capabilitypredicate(Build_capabilitypredicate build_capabilitypredicate) {
        this.build_capabilitypredicates.add(build_capabilitypredicate);
    }
    public List<build_ProvidesPredicate> getBuild_providespredicates() {
        return build_providespredicates;
    }

    public void addBuild_providespredicate(Build_providespredicate build_providespredicate) {
        this.build_providespredicates.add(build_providespredicate);
    }
    public List<build_RequiresPredicate> getBuild_requirespredicates() {
        return build_requirespredicates;
    }

    public void addBuild_requirespredicate(Build_requirespredicate build_requirespredicate) {
        this.build_requirespredicates.add(build_requirespredicate);
    }

}