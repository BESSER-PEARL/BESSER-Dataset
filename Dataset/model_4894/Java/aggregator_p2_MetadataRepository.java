





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_MetadataRepository extends IMetadataRepository {






    private List<InstallableUnit> installableunits;


    public aggregator_p2_MetadataRepository(
    ) {
        super(
        );
        this.installableunits = new ArrayList<>();
    }

    public aggregator_p2_MetadataRepository(
        ArrayList<InstallableUnit> installableunits    ) {
        this.installableunits = installableunits;
    }


    public List<InstallableUnit> getInstallableunits() {
        return installableunits;
    }

    public void addInstallableunit(Installableunit installableunit) {
        this.installableunits.add(installableunit);
    }

}