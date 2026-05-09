





import java.util.List;
import java.util.ArrayList;

public class PSM_DockerContainerLink extends ArtifactElement {

    private String LinksDependsOnField;
    private int DependencyOrder;





    private PSM_DockerContainerDefinition psm_dockercontainerdefinition;


    public PSM_DockerContainerLink(
        String LinksDependsOnField,        int DependencyOrder    ) {
        super(
        );
        this.LinksDependsOnField = LinksDependsOnField;
        this.DependencyOrder = DependencyOrder;
    }


    public String getLinksdependsonfield() {
        return LinksDependsOnField;
    }

    public void setLinksdependsonfield(String LinksDependsOnField) {
        this.LinksDependsOnField = LinksDependsOnField;
    }
    public int getDependencyorder() {
        return DependencyOrder;
    }

    public void setDependencyorder(int DependencyOrder) {
        this.DependencyOrder = DependencyOrder;
    }

    public PSM_DockerContainerDefinition getPsm_dockercontainerdefinition() {
        return psm_dockercontainerdefinition;
    }

    public void setPsm_dockercontainerdefinition(PSM_DockerContainerDefinition psm_dockercontainerdefinition) {
        this.psm_dockercontainerdefinition = psm_dockercontainerdefinition;
    }

}