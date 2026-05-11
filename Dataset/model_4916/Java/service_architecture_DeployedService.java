





import java.util.List;
import java.util.ArrayList;

public class service_architecture_DeployedService  {

    private String artifact;





    private ExecutionFramework executionframework;


    public service_architecture_DeployedService(
        String artifact    ) {
        this.artifact = artifact;
    }


    public String getArtifact() {
        return artifact;
    }

    public void setArtifact(String artifact) {
        this.artifact = artifact;
    }

    public ExecutionFramework getExecutionframework() {
        return executionframework;
    }

    public void setExecutionframework(ExecutionFramework executionframework) {
        this.executionframework = executionframework;
    }

}