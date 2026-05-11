





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_InstallableUnitFragment extends p2_IInstallableUnitFragment, p2_InstallableUnit {






    private List<RequiredCapability> requiredcapabilitys;


    public aggregator_p2_InstallableUnitFragment(
    ) {
        super(
        );
        this.requiredcapabilitys = new ArrayList<>();
    }

    public aggregator_p2_InstallableUnitFragment(
        ArrayList<RequiredCapability> requiredcapabilitys    ) {
        this.requiredcapabilitys = requiredcapabilitys;
    }


    public List<RequiredCapability> getRequiredcapabilitys() {
        return requiredcapabilitys;
    }

    public void addRequiredcapability(Requiredcapability requiredcapability) {
        this.requiredcapabilitys.add(requiredcapability);
    }

}