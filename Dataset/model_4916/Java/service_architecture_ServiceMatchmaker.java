





import java.util.List;
import java.util.ArrayList;

public class service_architecture_ServiceMatchmaker  {






    private List<ServiceDirectory> servicedirectorys;


    public service_architecture_ServiceMatchmaker(
    ) {
        this.servicedirectorys = new ArrayList<>();
    }

    public service_architecture_ServiceMatchmaker(
        ArrayList<ServiceDirectory> servicedirectorys    ) {
        this.servicedirectorys = servicedirectorys;
    }


    public List<ServiceDirectory> getServicedirectorys() {
        return servicedirectorys;
    }

    public void addServicedirectory(Servicedirectory servicedirectory) {
        this.servicedirectorys.add(servicedirectory);
    }

}