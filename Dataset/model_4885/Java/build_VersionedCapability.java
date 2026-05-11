





import java.util.List;
import java.util.ArrayList;

public class build_VersionedCapability extends Capability {

    private String version;



    public build_VersionedCapability(
        String version    ) {
        super(
        );
        this.version = version;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }


}