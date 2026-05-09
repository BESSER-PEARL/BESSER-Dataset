





import java.util.List;
import java.util.ArrayList;

public class domain_ModelMapper extends ArtifactRef {

    private String artifactExecutionString;
    private String artifactRoot;
    private String name;





    private domain_Component domain_component;




    private domain_DeploymentComponent domain_deploymentcomponent;




    private domain_Component domain_component;


    public domain_ModelMapper(
        String artifactExecutionString,        String artifactRoot,        String name    ) {
        super(
        );
        this.artifactExecutionString = artifactExecutionString;
        this.artifactRoot = artifactRoot;
        this.name = name;
    }


    public String getArtifactexecutionstring() {
        return artifactExecutionString;
    }

    public void setArtifactexecutionstring(String artifactExecutionString) {
        this.artifactExecutionString = artifactExecutionString;
    }
    public String getArtifactroot() {
        return artifactRoot;
    }

    public void setArtifactroot(String artifactRoot) {
        this.artifactRoot = artifactRoot;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public domain_Component getDomain_component() {
        return domain_component;
    }

    public void setDomain_component(domain_Component domain_component) {
        this.domain_component = domain_component;
    }
    public domain_DeploymentComponent getDomain_deploymentcomponent() {
        return domain_deploymentcomponent;
    }

    public void setDomain_deploymentcomponent(domain_DeploymentComponent domain_deploymentcomponent) {
        this.domain_deploymentcomponent = domain_deploymentcomponent;
    }
    public domain_Component getDomain_component() {
        return domain_component;
    }

    public void setDomain_component(domain_Component domain_component) {
        this.domain_component = domain_component;
    }

}