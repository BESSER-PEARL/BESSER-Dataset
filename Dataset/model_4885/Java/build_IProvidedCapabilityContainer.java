





import java.util.List;
import java.util.ArrayList;

public class build_IProvidedCapabilityContainer  {






    private List<build_Capability> build_capabilitys;


    public build_IProvidedCapabilityContainer(
    ) {
        this.build_capabilitys = new ArrayList<>();
    }

    public build_IProvidedCapabilityContainer(
        ArrayList<build_Capability> build_capabilitys    ) {
        this.build_capabilitys = build_capabilitys;
    }


    public List<build_Capability> getBuild_capabilitys() {
        return build_capabilitys;
    }

    public void addBuild_capability(Build_capability build_capability) {
        this.build_capabilitys.add(build_capability);
    }

}