





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_pc_repository_pc_pc_BasicComponent extends ImplementationComponentType {






    private List<PassiveResource> passiveresources;




    private List<ServiceEffectSpecification> serviceeffectspecifications;


    public pcm_pc_pc_repository_pc_pc_BasicComponent(
    ) {
        super(
        );
        this.passiveresources = new ArrayList<>();
        this.serviceeffectspecifications = new ArrayList<>();
    }

    public pcm_pc_pc_repository_pc_pc_BasicComponent(
        ArrayList<PassiveResource> passiveresources,        ArrayList<ServiceEffectSpecification> serviceeffectspecifications    ) {
        this.passiveresources = passiveresources;
        this.serviceeffectspecifications = serviceeffectspecifications;
    }


    public List<PassiveResource> getPassiveresources() {
        return passiveresources;
    }

    public void addPassiveresource(Passiveresource passiveresource) {
        this.passiveresources.add(passiveresource);
    }
    public List<ServiceEffectSpecification> getServiceeffectspecifications() {
        return serviceeffectspecifications;
    }

    public void addServiceeffectspecification(Serviceeffectspecification serviceeffectspecification) {
        this.serviceeffectspecifications.add(serviceeffectspecification);
    }

}