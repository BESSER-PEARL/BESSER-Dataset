





import java.util.List;
import java.util.ArrayList;

public class wsmodel3_System  {

    private String name;





    private List<wsmodel3_MessageBroker> wsmodel3_messagebrokers;




    private List<wsmodel3_Server> wsmodel3_servers;




    private List<wsmodel3_AccesPoint> wsmodel3_accespoints;




    private List<wsmodel3_IoTNode> wsmodel3_iotnodes;




    private List<wsmodel3_IntegrationPattern> wsmodel3_integrationpatterns;




    private List<wsmodel3_ExternalAPI> wsmodel3_externalapis;


    public wsmodel3_System(
        String name    ) {
        this.name = name;
        this.wsmodel3_messagebrokers = new ArrayList<>();
        this.wsmodel3_servers = new ArrayList<>();
        this.wsmodel3_accespoints = new ArrayList<>();
        this.wsmodel3_iotnodes = new ArrayList<>();
        this.wsmodel3_integrationpatterns = new ArrayList<>();
        this.wsmodel3_externalapis = new ArrayList<>();
    }

    public wsmodel3_System(
        String name        ArrayList<wsmodel3_MessageBroker> wsmodel3_messagebrokers,        ArrayList<wsmodel3_Server> wsmodel3_servers,        ArrayList<wsmodel3_AccesPoint> wsmodel3_accespoints,        ArrayList<wsmodel3_IoTNode> wsmodel3_iotnodes,        ArrayList<wsmodel3_IntegrationPattern> wsmodel3_integrationpatterns,        ArrayList<wsmodel3_ExternalAPI> wsmodel3_externalapis    ) {
        this.name = name;
        this.wsmodel3_messagebrokers = wsmodel3_messagebrokers;
        this.wsmodel3_servers = wsmodel3_servers;
        this.wsmodel3_accespoints = wsmodel3_accespoints;
        this.wsmodel3_iotnodes = wsmodel3_iotnodes;
        this.wsmodel3_integrationpatterns = wsmodel3_integrationpatterns;
        this.wsmodel3_externalapis = wsmodel3_externalapis;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<wsmodel3_MessageBroker> getWsmodel3_messagebrokers() {
        return wsmodel3_messagebrokers;
    }

    public void addWsmodel3_messagebroker(Wsmodel3_messagebroker wsmodel3_messagebroker) {
        this.wsmodel3_messagebrokers.add(wsmodel3_messagebroker);
    }
    public List<wsmodel3_Server> getWsmodel3_servers() {
        return wsmodel3_servers;
    }

    public void addWsmodel3_server(Wsmodel3_server wsmodel3_server) {
        this.wsmodel3_servers.add(wsmodel3_server);
    }
    public List<wsmodel3_AccesPoint> getWsmodel3_accespoints() {
        return wsmodel3_accespoints;
    }

    public void addWsmodel3_accespoint(Wsmodel3_accespoint wsmodel3_accespoint) {
        this.wsmodel3_accespoints.add(wsmodel3_accespoint);
    }
    public List<wsmodel3_IoTNode> getWsmodel3_iotnodes() {
        return wsmodel3_iotnodes;
    }

    public void addWsmodel3_iotnode(Wsmodel3_iotnode wsmodel3_iotnode) {
        this.wsmodel3_iotnodes.add(wsmodel3_iotnode);
    }
    public List<wsmodel3_IntegrationPattern> getWsmodel3_integrationpatterns() {
        return wsmodel3_integrationpatterns;
    }

    public void addWsmodel3_integrationpattern(Wsmodel3_integrationpattern wsmodel3_integrationpattern) {
        this.wsmodel3_integrationpatterns.add(wsmodel3_integrationpattern);
    }
    public List<wsmodel3_ExternalAPI> getWsmodel3_externalapis() {
        return wsmodel3_externalapis;
    }

    public void addWsmodel3_externalapi(Wsmodel3_externalapi wsmodel3_externalapi) {
        this.wsmodel3_externalapis.add(wsmodel3_externalapi);
    }

}