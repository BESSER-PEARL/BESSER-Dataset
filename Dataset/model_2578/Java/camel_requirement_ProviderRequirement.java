





import java.util.List;
import java.util.ArrayList;

public class camel_requirement_ProviderRequirement extends HardRequirement {






    private List<CloudProvider> cloudproviders;


    public camel_requirement_ProviderRequirement(
    ) {
        super(
        );
        this.cloudproviders = new ArrayList<>();
    }

    public camel_requirement_ProviderRequirement(
        ArrayList<CloudProvider> cloudproviders    ) {
        this.cloudproviders = cloudproviders;
    }


    public List<CloudProvider> getCloudproviders() {
        return cloudproviders;
    }

    public void addCloudprovider(Cloudprovider cloudprovider) {
        this.cloudproviders.add(cloudprovider);
    }

}