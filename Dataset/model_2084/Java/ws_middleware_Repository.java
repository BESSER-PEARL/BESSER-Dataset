





import java.util.List;
import java.util.ArrayList;

public class ws_middleware_Repository  {






    private List<ServiceDescription> servicedescriptions;


    public ws_middleware_Repository(
    ) {
        this.servicedescriptions = new ArrayList<>();
    }

    public ws_middleware_Repository(
        ArrayList<ServiceDescription> servicedescriptions    ) {
        this.servicedescriptions = servicedescriptions;
    }


    public List<ServiceDescription> getServicedescriptions() {
        return servicedescriptions;
    }

    public void addServicedescription(Servicedescription servicedescription) {
        this.servicedescriptions.add(servicedescription);
    }

}