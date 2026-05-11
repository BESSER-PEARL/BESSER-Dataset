





import java.util.List;
import java.util.ArrayList;

public class aggregator_InstallableUnitRequest extends StatusProvider, DescriptionProvider, InfosProvider {

    private String versionRange;
    private String name;



    public aggregator_InstallableUnitRequest(
        String versionRange,        String name    ) {
        super(
        );
        this.versionRange = versionRange;
        this.name = name;
    }


    public String getVersionrange() {
        return versionRange;
    }

    public void setVersionrange(String versionRange) {
        this.versionRange = versionRange;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}