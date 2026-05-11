





import java.util.List;
import java.util.ArrayList;

public class cloudml_Artefact extends WithProperties {






    private List<cloudml_ClientPort> cloudml_clientports;




    private cloudml_DeploymentModel cloudml_deploymentmodel;




    private cloudml_ArtefactPort cloudml_artefactport;




    private cloudml_Resource cloudml_resource;




    private cloudml_ArtefactInstance cloudml_artefactinstance;


    public cloudml_Artefact(
    ) {
        super(
        );
        this.cloudml_clientports = new ArrayList<>();
    }

    public cloudml_Artefact(
        ArrayList<cloudml_ClientPort> cloudml_clientports    ) {
        this.cloudml_clientports = cloudml_clientports;
    }


    public List<cloudml_ClientPort> getCloudml_clientports() {
        return cloudml_clientports;
    }

    public void addCloudml_clientport(Cloudml_clientport cloudml_clientport) {
        this.cloudml_clientports.add(cloudml_clientport);
    }
    public cloudml_DeploymentModel getCloudml_deploymentmodel() {
        return cloudml_deploymentmodel;
    }

    public void setCloudml_deploymentmodel(cloudml_DeploymentModel cloudml_deploymentmodel) {
        this.cloudml_deploymentmodel = cloudml_deploymentmodel;
    }
    public cloudml_ArtefactPort getCloudml_artefactport() {
        return cloudml_artefactport;
    }

    public void setCloudml_artefactport(cloudml_ArtefactPort cloudml_artefactport) {
        this.cloudml_artefactport = cloudml_artefactport;
    }
    public cloudml_Resource getCloudml_resource() {
        return cloudml_resource;
    }

    public void setCloudml_resource(cloudml_Resource cloudml_resource) {
        this.cloudml_resource = cloudml_resource;
    }
    public cloudml_ArtefactInstance getCloudml_artefactinstance() {
        return cloudml_artefactinstance;
    }

    public void setCloudml_artefactinstance(cloudml_ArtefactInstance cloudml_artefactinstance) {
        this.cloudml_artefactinstance = cloudml_artefactinstance;
    }

}