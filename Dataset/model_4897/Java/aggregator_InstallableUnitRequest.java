





import java.util.List;
import java.util.ArrayList;

public class aggregator_InstallableUnitRequest extends StatusProvider, DescriptionProvider, InfosProvider {

    private String name;
    private String versionRange;



    public aggregator_InstallableUnitRequest(
        String name,        String versionRange    ) {
        super(
        );
        this.name = name;
        this.versionRange = versionRange;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVersionrange() {
        return versionRange;
    }

    public void setVersionrange(String versionRange) {
        this.versionRange = versionRange;
    }


}