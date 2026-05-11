





import java.util.List;
import java.util.ArrayList;

public class build_BuilderCallFacade  {

    private String aliases;





    private build_BuilderCall build_buildercall;




    private build_RequiredCapability build_requiredcapability;


    public build_BuilderCallFacade(
        String aliases    ) {
        this.aliases = aliases;
    }


    public String getAliases() {
        return aliases;
    }

    public void setAliases(String aliases) {
        this.aliases = aliases;
    }

    public build_BuilderCall getBuild_buildercall() {
        return build_buildercall;
    }

    public void setBuild_buildercall(build_BuilderCall build_buildercall) {
        this.build_buildercall = build_buildercall;
    }
    public build_RequiredCapability getBuild_requiredcapability() {
        return build_requiredcapability;
    }

    public void setBuild_requiredcapability(build_RequiredCapability build_requiredcapability) {
        this.build_requiredcapability = build_requiredcapability;
    }

}