





import java.util.List;
import java.util.ArrayList;

public class build_RequiredCapability extends Capability {

    private int min;
    private int max;
    private boolean greedy;
    private String versionRange;





    private build_BuildUnit build_buildunit;




    private build_IRequiredCapabilityContainer build_irequiredcapabilitycontainer;




    private build_BuilderCallFacade build_buildercallfacade;




    private build_BuildCallOnDeclaredRequirement build_buildcallondeclaredrequirement;




    private build_BuildCallSingle build_buildcallsingle;




    private build_BuildCallOnReferencedRequirement build_buildcallonreferencedrequirement;




    private build_EffectiveRequirementFacade build_effectiverequirementfacade;


    public build_RequiredCapability(
        int min,        int max,        boolean greedy,        String versionRange    ) {
        super(
        );
        this.min = min;
        this.max = max;
        this.greedy = greedy;
        this.versionRange = versionRange;
    }


    public int getMin() {
        return min;
    }

    public void setMin(int min) {
        this.min = min;
    }
    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }
    public boolean getGreedy() {
        return greedy;
    }

    public void setGreedy(boolean greedy) {
        this.greedy = greedy;
    }
    public String getVersionrange() {
        return versionRange;
    }

    public void setVersionrange(String versionRange) {
        this.versionRange = versionRange;
    }

    public build_BuildUnit getBuild_buildunit() {
        return build_buildunit;
    }

    public void setBuild_buildunit(build_BuildUnit build_buildunit) {
        this.build_buildunit = build_buildunit;
    }
    public build_IRequiredCapabilityContainer getBuild_irequiredcapabilitycontainer() {
        return build_irequiredcapabilitycontainer;
    }

    public void setBuild_irequiredcapabilitycontainer(build_IRequiredCapabilityContainer build_irequiredcapabilitycontainer) {
        this.build_irequiredcapabilitycontainer = build_irequiredcapabilitycontainer;
    }
    public build_BuilderCallFacade getBuild_buildercallfacade() {
        return build_buildercallfacade;
    }

    public void setBuild_buildercallfacade(build_BuilderCallFacade build_buildercallfacade) {
        this.build_buildercallfacade = build_buildercallfacade;
    }
    public build_BuildCallOnDeclaredRequirement getBuild_buildcallondeclaredrequirement() {
        return build_buildcallondeclaredrequirement;
    }

    public void setBuild_buildcallondeclaredrequirement(build_BuildCallOnDeclaredRequirement build_buildcallondeclaredrequirement) {
        this.build_buildcallondeclaredrequirement = build_buildcallondeclaredrequirement;
    }
    public build_BuildCallSingle getBuild_buildcallsingle() {
        return build_buildcallsingle;
    }

    public void setBuild_buildcallsingle(build_BuildCallSingle build_buildcallsingle) {
        this.build_buildcallsingle = build_buildcallsingle;
    }
    public build_BuildCallOnReferencedRequirement getBuild_buildcallonreferencedrequirement() {
        return build_buildcallonreferencedrequirement;
    }

    public void setBuild_buildcallonreferencedrequirement(build_BuildCallOnReferencedRequirement build_buildcallonreferencedrequirement) {
        this.build_buildcallonreferencedrequirement = build_buildcallonreferencedrequirement;
    }
    public build_EffectiveRequirementFacade getBuild_effectiverequirementfacade() {
        return build_effectiverequirementfacade;
    }

    public void setBuild_effectiverequirementfacade(build_EffectiveRequirementFacade build_effectiverequirementfacade) {
        this.build_effectiverequirementfacade = build_effectiverequirementfacade;
    }

}