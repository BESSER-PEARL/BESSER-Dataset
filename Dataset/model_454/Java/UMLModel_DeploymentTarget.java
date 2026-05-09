





import java.util.List;
import java.util.ArrayList;

public class UMLModel_DeploymentTarget extends NamedElement {

    private String deployedElement;



    public UMLModel_DeploymentTarget(
        String deployedElement    ) {
        super(
        );
        this.deployedElement = deployedElement;
    }


    public String getDeployedelement() {
        return deployedElement;
    }

    public void setDeployedelement(String deployedElement) {
        this.deployedElement = deployedElement;
    }


}