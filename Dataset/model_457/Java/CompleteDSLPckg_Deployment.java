





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Deployment extends Dependency {






    private CompleteDSLPckg_DeploymentTarget completedslpckg_deploymenttarget;




    private CompleteDSLPckg_DeploymentTarget completedslpckg_deploymenttarget;




    private List<CompleteDSLPckg_DeployedArtifact> completedslpckg_deployedartifacts;


    public CompleteDSLPckg_Deployment(
    ) {
        super(
        );
        this.completedslpckg_deployedartifacts = new ArrayList<>();
    }

    public CompleteDSLPckg_Deployment(
        ArrayList<CompleteDSLPckg_DeployedArtifact> completedslpckg_deployedartifacts    ) {
        this.completedslpckg_deployedartifacts = completedslpckg_deployedartifacts;
    }


    public CompleteDSLPckg_DeploymentTarget getCompletedslpckg_deploymenttarget() {
        return completedslpckg_deploymenttarget;
    }

    public void setCompletedslpckg_deploymenttarget(CompleteDSLPckg_DeploymentTarget completedslpckg_deploymenttarget) {
        this.completedslpckg_deploymenttarget = completedslpckg_deploymenttarget;
    }
    public CompleteDSLPckg_DeploymentTarget getCompletedslpckg_deploymenttarget() {
        return completedslpckg_deploymenttarget;
    }

    public void setCompletedslpckg_deploymenttarget(CompleteDSLPckg_DeploymentTarget completedslpckg_deploymenttarget) {
        this.completedslpckg_deploymenttarget = completedslpckg_deploymenttarget;
    }
    public List<CompleteDSLPckg_DeployedArtifact> getCompletedslpckg_deployedartifacts() {
        return completedslpckg_deployedartifacts;
    }

    public void addCompletedslpckg_deployedartifact(Completedslpckg_deployedartifact completedslpckg_deployedartifact) {
        this.completedslpckg_deployedartifacts.add(completedslpckg_deployedartifact);
    }

}