





import java.util.List;
import java.util.ArrayList;

public class core_COREStrategy extends CORENamedElement {






    private List<core_COREConfiguration> core_coreconfigurations;


    public core_COREStrategy(
    ) {
        super(
        );
        this.core_coreconfigurations = new ArrayList<>();
    }

    public core_COREStrategy(
        ArrayList<core_COREConfiguration> core_coreconfigurations    ) {
        this.core_coreconfigurations = core_coreconfigurations;
    }


    public List<core_COREConfiguration> getCore_coreconfigurations() {
        return core_coreconfigurations;
    }

    public void addCore_coreconfiguration(Core_coreconfiguration core_coreconfiguration) {
        this.core_coreconfigurations.add(core_coreconfiguration);
    }

}