





import java.util.List;
import java.util.ArrayList;

public class service_architecture_ServiceDirectory  {






    private List<InterfaceDescription> interfacedescriptions;




    private ServiceProfile serviceprofile;




    private List<Endpoint> endpoints;


    public service_architecture_ServiceDirectory(
    ) {
        this.interfacedescriptions = new ArrayList<>();
        this.endpoints = new ArrayList<>();
    }

    public service_architecture_ServiceDirectory(
        ArrayList<InterfaceDescription> interfacedescriptions,        ArrayList<Endpoint> endpoints    ) {
        this.interfacedescriptions = interfacedescriptions;
        this.endpoints = endpoints;
    }


    public List<InterfaceDescription> getInterfacedescriptions() {
        return interfacedescriptions;
    }

    public void addInterfacedescription(Interfacedescription interfacedescription) {
        this.interfacedescriptions.add(interfacedescription);
    }
    public ServiceProfile getServiceprofile() {
        return serviceprofile;
    }

    public void setServiceprofile(ServiceProfile serviceprofile) {
        this.serviceprofile = serviceprofile;
    }
    public List<Endpoint> getEndpoints() {
        return endpoints;
    }

    public void addEndpoint(Endpoint endpoint) {
        this.endpoints.add(endpoint);
    }

}