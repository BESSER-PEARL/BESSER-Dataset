





import java.util.List;
import java.util.ArrayList;

public class wsmodel3_Orchestrator  {

    private String port;
    private String name;





    private List<wsmodel3_InputOrchestrator> wsmodel3_inputorchestrators;




    private List<wsmodel3_REST> wsmodel3_rests;




    private wsmodel3_IntegrationPattern wsmodel3_integrationpattern;




    private List<wsmodel3_ExternalAPI> wsmodel3_externalapis;


    public wsmodel3_Orchestrator(
        String port,        String name    ) {
        this.port = port;
        this.name = name;
        this.wsmodel3_inputorchestrators = new ArrayList<>();
        this.wsmodel3_rests = new ArrayList<>();
        this.wsmodel3_externalapis = new ArrayList<>();
    }

    public wsmodel3_Orchestrator(
        String port,        String name        ArrayList<wsmodel3_InputOrchestrator> wsmodel3_inputorchestrators,        ArrayList<wsmodel3_REST> wsmodel3_rests,        ArrayList<wsmodel3_ExternalAPI> wsmodel3_externalapis    ) {
        this.port = port;
        this.name = name;
        this.wsmodel3_inputorchestrators = wsmodel3_inputorchestrators;
        this.wsmodel3_rests = wsmodel3_rests;
        this.wsmodel3_externalapis = wsmodel3_externalapis;
    }

    public String getPort() {
        return port;
    }

    public void setPort(String port) {
        this.port = port;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<wsmodel3_InputOrchestrator> getWsmodel3_inputorchestrators() {
        return wsmodel3_inputorchestrators;
    }

    public void addWsmodel3_inputorchestrator(Wsmodel3_inputorchestrator wsmodel3_inputorchestrator) {
        this.wsmodel3_inputorchestrators.add(wsmodel3_inputorchestrator);
    }
    public List<wsmodel3_REST> getWsmodel3_rests() {
        return wsmodel3_rests;
    }

    public void addWsmodel3_rest(Wsmodel3_rest wsmodel3_rest) {
        this.wsmodel3_rests.add(wsmodel3_rest);
    }
    public wsmodel3_IntegrationPattern getWsmodel3_integrationpattern() {
        return wsmodel3_integrationpattern;
    }

    public void setWsmodel3_integrationpattern(wsmodel3_IntegrationPattern wsmodel3_integrationpattern) {
        this.wsmodel3_integrationpattern = wsmodel3_integrationpattern;
    }
    public List<wsmodel3_ExternalAPI> getWsmodel3_externalapis() {
        return wsmodel3_externalapis;
    }

    public void addWsmodel3_externalapi(Wsmodel3_externalapi wsmodel3_externalapi) {
        this.wsmodel3_externalapis.add(wsmodel3_externalapi);
    }

}