





import java.util.List;
import java.util.ArrayList;

public class service_architecture_ExecutionFramework  {

    private String container;





    private List<DeployedService> deployedservices;


    public service_architecture_ExecutionFramework(
        String container    ) {
        this.container = container;
        this.deployedservices = new ArrayList<>();
    }

    public service_architecture_ExecutionFramework(
        String container        ArrayList<DeployedService> deployedservices    ) {
        this.container = container;
        this.deployedservices = deployedservices;
    }

    public String getContainer() {
        return container;
    }

    public void setContainer(String container) {
        this.container = container;
    }

    public List<DeployedService> getDeployedservices() {
        return deployedservices;
    }

    public void addDeployedservice(Deployedservice deployedservice) {
        this.deployedservices.add(deployedservice);
    }

}