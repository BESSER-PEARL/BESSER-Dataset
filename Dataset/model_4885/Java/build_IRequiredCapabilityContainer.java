





import java.util.List;
import java.util.ArrayList;

public class build_IRequiredCapabilityContainer  {






    private List<build_CapabilityPredicate> build_capabilitypredicates;




    private List<build_RequiredCapability> build_requiredcapabilitys;


    public build_IRequiredCapabilityContainer(
    ) {
        this.build_capabilitypredicates = new ArrayList<>();
        this.build_requiredcapabilitys = new ArrayList<>();
    }

    public build_IRequiredCapabilityContainer(
        ArrayList<build_CapabilityPredicate> build_capabilitypredicates,        ArrayList<build_RequiredCapability> build_requiredcapabilitys    ) {
        this.build_capabilitypredicates = build_capabilitypredicates;
        this.build_requiredcapabilitys = build_requiredcapabilitys;
    }


    public List<build_CapabilityPredicate> getBuild_capabilitypredicates() {
        return build_capabilitypredicates;
    }

    public void addBuild_capabilitypredicate(Build_capabilitypredicate build_capabilitypredicate) {
        this.build_capabilitypredicates.add(build_capabilitypredicate);
    }
    public List<build_RequiredCapability> getBuild_requiredcapabilitys() {
        return build_requiredcapabilitys;
    }

    public void addBuild_requiredcapability(Build_requiredcapability build_requiredcapability) {
        this.build_requiredcapabilitys.add(build_requiredcapability);
    }

}