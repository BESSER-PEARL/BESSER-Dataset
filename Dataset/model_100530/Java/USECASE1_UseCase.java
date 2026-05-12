





import java.util.List;
import java.util.ArrayList;

public class USECASE1_UseCase  {






    private List<Service> services;


    public USECASE1_UseCase(
    ) {
        this.services = new ArrayList<>();
    }

    public USECASE1_UseCase(
        ArrayList<Service> services    ) {
        this.services = services;
    }


    public List<Service> getServices() {
        return services;
    }

    public void addService(Service service) {
        this.services.add(service);
    }

}