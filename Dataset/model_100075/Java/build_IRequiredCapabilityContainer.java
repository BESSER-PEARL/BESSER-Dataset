





import java.util.List;
import java.util.ArrayList;

public class build_IRequiredCapabilityContainer  {






    private List<build_CapabilityPredicate> build_capabilitypredicates;


    public build_IRequiredCapabilityContainer(
    ) {
        this.build_capabilitypredicates = new ArrayList<>();
    }

    public build_IRequiredCapabilityContainer(
        ArrayList<build_CapabilityPredicate> build_capabilitypredicates    ) {
        this.build_capabilitypredicates = build_capabilitypredicates;
    }


    public List<build_CapabilityPredicate> getBuild_capabilitypredicates() {
        return build_capabilitypredicates;
    }

    public void addBuild_capabilitypredicate(Build_capabilitypredicate build_capabilitypredicate) {
        this.build_capabilitypredicates.add(build_capabilitypredicate);
    }

}