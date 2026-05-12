





import java.util.List;
import java.util.ArrayList;

public class urml_service_Service extends Asset {






    private Service service;




    private List<Requirement> requirements;




    private List<Service> services;


    public urml_service_Service(
    ) {
        super(
        );
        this.requirements = new ArrayList<>();
        this.services = new ArrayList<>();
    }

    public urml_service_Service(
        ArrayList<Requirement> requirements,        ArrayList<Service> services    ) {
        this.requirements = requirements;
        this.services = services;
    }


    public Service getService() {
        return service;
    }

    public void setService(Service service) {
        this.service = service;
    }
    public List<Requirement> getRequirements() {
        return requirements;
    }

    public void addRequirement(Requirement requirement) {
        this.requirements.add(requirement);
    }
    public List<Service> getServices() {
        return services;
    }

    public void addService(Service service) {
        this.services.add(service);
    }

}