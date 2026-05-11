





import java.util.List;
import java.util.ArrayList;

public class build_EffectiveCapabilityFacade extends EffectiveFacade {






    private build_EffectiveUnitFacade build_effectiveunitfacade;




    private build_Capability build_capability;


    public build_EffectiveCapabilityFacade(
    ) {
        super(
        );
    }



    public build_EffectiveUnitFacade getBuild_effectiveunitfacade() {
        return build_effectiveunitfacade;
    }

    public void setBuild_effectiveunitfacade(build_EffectiveUnitFacade build_effectiveunitfacade) {
        this.build_effectiveunitfacade = build_effectiveunitfacade;
    }
    public build_Capability getBuild_capability() {
        return build_capability;
    }

    public void setBuild_capability(build_Capability build_capability) {
        this.build_capability = build_capability;
    }

}