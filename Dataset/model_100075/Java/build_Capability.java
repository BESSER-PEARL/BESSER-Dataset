





import java.util.List;
import java.util.ArrayList;

public class build_Capability extends INamedValue {

    private String nameSpace;





    private build_IProvidedCapabilityContainer build_iprovidedcapabilitycontainer;




    private build_BExpression build_bexpression;




    private build_EffectiveCapabilityFacade build_effectivecapabilityfacade;


    public build_Capability(
        String nameSpace    ) {
        super(
        );
        this.nameSpace = nameSpace;
    }


    public String getNamespace() {
        return nameSpace;
    }

    public void setNamespace(String nameSpace) {
        this.nameSpace = nameSpace;
    }

    public build_IProvidedCapabilityContainer getBuild_iprovidedcapabilitycontainer() {
        return build_iprovidedcapabilitycontainer;
    }

    public void setBuild_iprovidedcapabilitycontainer(build_IProvidedCapabilityContainer build_iprovidedcapabilitycontainer) {
        this.build_iprovidedcapabilitycontainer = build_iprovidedcapabilitycontainer;
    }
    public build_BExpression getBuild_bexpression() {
        return build_bexpression;
    }

    public void setBuild_bexpression(build_BExpression build_bexpression) {
        this.build_bexpression = build_bexpression;
    }
    public build_EffectiveCapabilityFacade getBuild_effectivecapabilityfacade() {
        return build_effectivecapabilityfacade;
    }

    public void setBuild_effectivecapabilityfacade(build_EffectiveCapabilityFacade build_effectivecapabilityfacade) {
        this.build_effectivecapabilityfacade = build_effectivecapabilityfacade;
    }

}