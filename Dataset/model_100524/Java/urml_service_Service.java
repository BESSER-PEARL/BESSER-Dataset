





import java.util.List;
import java.util.ArrayList;

public class urml_service_Service extends Asset {






    private Service service;




    private List<Service> services;




    private List<Requirement> requirements;


    public urml_service_Service(
    ) {
        super(
        );
        this.services = new ArrayList<>();
        this.requirements = new ArrayList<>();
    }

    public urml_service_Service(
        ArrayList<Service> services,        ArrayList<Requirement> requirements    ) {
        this.services = services;
        this.requirements = requirements;
    }


    public Service getService() {
        return service;
    }

    public void setService(Service service) {
        this.service = service;
    }
    public List<Service> getServices() {
        return services;
    }

    public void addService(Service service) {
        this.services.add(service);
    }
    public List<Requirement> getRequirements() {
        return requirements;
    }

    public void addRequirement(Requirement requirement) {
        this.requirements.add(requirement);
    }

}