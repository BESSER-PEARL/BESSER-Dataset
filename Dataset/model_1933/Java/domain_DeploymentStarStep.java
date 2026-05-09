





import java.util.List;
import java.util.ArrayList;

public class domain_DeploymentStarStep  {

    private String name;
    private String uid;





    private domain_DeploymentComponent domain_deploymentcomponent;




    private domain_DeploymentComponents domain_deploymentcomponents;


    public domain_DeploymentStarStep(
        String name,        String uid    ) {
        this.name = name;
        this.uid = uid;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_DeploymentComponent getDomain_deploymentcomponent() {
        return domain_deploymentcomponent;
    }

    public void setDomain_deploymentcomponent(domain_DeploymentComponent domain_deploymentcomponent) {
        this.domain_deploymentcomponent = domain_deploymentcomponent;
    }
    public domain_DeploymentComponents getDomain_deploymentcomponents() {
        return domain_deploymentcomponents;
    }

    public void setDomain_deploymentcomponents(domain_DeploymentComponents domain_deploymentcomponents) {
        this.domain_deploymentcomponents = domain_deploymentcomponents;
    }

}