





import java.util.List;
import java.util.ArrayList;

public class setup_Eclipse extends ConfigurableItem {

    private String version;





    private setup_Configuration setup_configuration;




    private setup_Project setup_project;




    private setup_Branch setup_branch;




    private setup_Configuration setup_configuration;


    public setup_Eclipse(
        String version    ) {
        super(
        );
        this.version = version;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public setup_Configuration getSetup_configuration() {
        return setup_configuration;
    }

    public void setSetup_configuration(setup_Configuration setup_configuration) {
        this.setup_configuration = setup_configuration;
    }
    public setup_Project getSetup_project() {
        return setup_project;
    }

    public void setSetup_project(setup_Project setup_project) {
        this.setup_project = setup_project;
    }
    public setup_Branch getSetup_branch() {
        return setup_branch;
    }

    public void setSetup_branch(setup_Branch setup_branch) {
        this.setup_branch = setup_branch;
    }
    public setup_Configuration getSetup_configuration() {
        return setup_configuration;
    }

    public void setSetup_configuration(setup_Configuration setup_configuration) {
        this.setup_configuration = setup_configuration;
    }

}